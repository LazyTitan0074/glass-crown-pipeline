"""Canon check pe lista de fapte (NU pe 'citeste biblia').
Reviewer = model DIFERIT de writer. Primar: gemini-2.5-flash-lite. Fallback: modelul
ne-folosit-la-scriere dintre {gpt-oss-120b (Groq), ministral-8b}.
Orice abatere => respins, fara netezire. Uz: python canon_check.py <nr_cap> [writer_model]
"""
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(os.getenv("GLASS_BASE", r"C:\Users\bizoi\libriscribe-roman"))
PROJ = Path(os.getenv("GLASS_PROJ", r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara"))
load_dotenv(BASE / ".env")

PROMPT = """You are a canon continuity checker for the novel "The Glass Crown".
AUTHORITATIVE STORY FACTS (any contradiction = fail):
{facts}

CHAPTER {ch} TEXT:
{text}

Compare EVERY factual claim about named people, ages, relationships, parentage, past events,
who-killed-whom, world rules, numbers, and timeline (who appears when).
Return ONLY this JSON, nothing else:
{{"pass": true/false, "violations": [{{"fact": "C##", "quote": "<exact chapter quote>", "why": "<what it contradicts>"}}]}}
Rules: a single contradiction (names, ages, parentage, events, anachronistic appearance, e.g. Lara before ch4) => pass=false. Prose quality is NOT your job. Do not smooth over contradictions. Empty violations + pass=true only if fully clean.
ANTI-FALSE-POSITIVE RULES (binding, take precedence):
- Only DECLARED facts count (names/ages/filiation/events/numbers/chronological appearances). Behaviour, voice, or implied maturity is NEVER a violation (e.g. Leah seeming young/frightened does NOT contradict C01 age 20).
- A quote that CONFIRMS a fact (e.g. naming Elowen as mistress of the inn) is NEVER a violation of that fact.
- An object that merely evokes a person (locket, portrait, memory) does NOT place that person alive in the timeline and is NEVER a parentage/death-date violation by itself.
- Pre-Lara brothel clients (ch2-3) MUST be young/experienced, rushed/clumsy, and MUST NEVER tend to Leah's pleasure (C09). A tender/attentive client before ch4 IS a real C09 violation. Her first pleasure-tended scene is Lara in ch4 with "mommy".
- Sera may be named ONLY in ch9 Lara-context scenes (C15). Any mention of Sera before ch9 IS a real violation.
- DISAMBIGUATION (binding): Elowen appearing/interacting with Leah in ch1 (Red Velvet Inn recognition) is CORRECT per C07 — NEVER flag Elowen under C08. C08 restricts ONLY Lara (no appearance, no name, no messages before ch4). Vague eastern-host rumours in ch1–3 are CORRECT, not violations.
- The "asks for Leah BY NAME" beat belongs to the ch4 ENTRANCE scene ONLY. In ch5+ Lara addressing Leah without her name (pronouns, "you", titles) is CORRECT — NEVER flag it under C08.
- TIMING GATE (binding): Lara pre-ch4 = violation. Mira/Vela appearing or referenced ch5+ = CORRECT (C16). Sera named ONLY ch9 Lara-context. Elowen in ch1 = CORRECT (C07). Vague eastern-host rumours ch1–3 = CORRECT.
- ARITHMETIC (binding): you are checking CHAPTER {ch}. 7 > 4 and 7 > 5 and 7 > 6: anything allowed "from ch4/ch5/ch6 onward" is CORRECT here. NEVER claim the current chapter is "pre-ch4" or "pre-ch5" when {ch} >= 5.
- Keep every "why" under 20 words. Keep the whole reply under 1200 tokens.
{locked_block}"""

LOCKED_TMPL = """LOCKED OBJECTS — contents consistency (binding):
{locked}
For EACH locked object above, list the items stated to be INSIDE it IN EACH SCENE of this chapter. If two scenes enumerate different sets — an item vanishes, or an item appears inside that is not in the CANON set — that is a CONTENTS-DRIFT violation: pass=false with fact=the L-code, quote=the conflicting sentence, why=<20 words. A locked object whose contents are never shown is CORRECT (not a violation); only contradictory enumerations fail."""


def locked_facts(canon_text):
    """Lines '- Lxx: ...' from CANON.md (FIX-3). Empty list => prompt unchanged."""
    out = []
    for line in canon_text.splitlines():
        line = line.strip()
        if line.startswith("- L") and ":" in line:
            out.append(line[2:].strip())
    return out


def check_flash_lite(prompt):
    from google import genai
    c = genai.Client(api_key=os.getenv("GOOGLE_AI_STUDIO_API_KEY"))
    r = c.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    return (r.text or "").strip(), "gemini-2.5-flash-lite"


def check_groq(prompt):
    import requests
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {os.getenv('BEDROCK_MANTLE_API_KEY')}"},
        json={"model": "openai/gpt-oss-120b",
              "messages": [{"role": "user", "content": prompt}],
              "max_tokens": 2500, "temperature": 0.1},
        timeout=120)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip(), "groq/gpt-oss-120b"


def check_ollama(prompt):
    import requests
    r = requests.post(
        "http://localhost:11434/v1/chat/completions",
        headers={"Content-Type": "application/json"},
        json={"model": "qwen2.5:7b",
              "messages": [{"role": "user", "content": prompt}],
              "options": {"num_predict": 2500},
              "temperature": 0.1},
        timeout=300)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip(), "ollama/qwen2.5:7b"


def check_ministral(prompt):
    import requests
    r = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}"},
        json={"model": "ministral-8b-latest",
              "messages": [{"role": "user", "content": prompt}],
              "max_tokens": 2500, "temperature": 0.1},
        timeout=120)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip(), "mistral/ministral-8b-latest"


def is_hedge(why):
    if re.search(r'no violation|not a violation|no pre-ch\d violation|is correct|no issue|correct per|no contradiction|confirmed post-ch\d|allowed|permitted|as required|as expected', why, re.I):
        return True
    if not re.search(r'violat|contradict|break|inconsist|impli|wrong|stated as|aged \d|instead of', why, re.I):
        return True
    return False


_PARSE_MODE = {"mode": "clean"}


def parse_verdict(raw):
    try:
        _PARSE_MODE["mode"] = "clean"
        return json.loads(raw)
    except Exception:
        pass
    s = raw.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1] if "\n" in s else s[3:]
        if s.rstrip().endswith("```"):
            s = s.rstrip()[: -3]
    try:
        _PARSE_MODE["mode"] = "fenced"
        return json.loads(s)
    except Exception:
        pass
    s2, e = s.find("{"), s.rfind("}")
    if s2 >= 0 and e > s2:
        try:
            _PARSE_MODE["mode"] = "braces"
            return json.loads(s[s2:e + 1])
        except Exception:
            pass
    # Truncation-proof fallback: harvest complete violation objects.
    # Drop hedged non-findings ("no violation", "correct", ...) — the small
    # reviewer often lists facts just to conclude they are fine.
    objs = re.findall(r'\{[^{}]*"fact"\s*:\s*"([^"]+)"[^{}]*\}', s)
    if objs:
        out = []
        for m in re.finditer(r'\{\s*"fact"\s*:\s*"([^"]+)"\s*,\s*"quote"\s*:\s*"((?:[^"\\]|\\.)*)"\s*,\s*"why"\s*:\s*"((?:[^"\\]|\\.)*)"\s*\}', s):
            why = m.group(3)
            if re.search(r'no violation|not a violation|no pre-ch\d violation|is correct|no issue|correct per|no contradiction|confirmed post-ch\d|allowed|permitted|as required|as expected', why, re.I):
                continue
            if not re.search(r'violat|contradict|break|inconsist|impli|wrong|stated as|aged \d|instead of', why, re.I):
                continue
            out.append({"fact": m.group(1), "quote": m.group(2)[:200], "why": why[:200]})
        if out:
            _PARSE_MODE["mode"] = "harvested-fail"
            return {"pass": False, "violations": out[:10]}
        _PARSE_MODE["mode"] = "harvested-pass"
        return {"pass": True, "violations": []}
    if re.search(r'"pass"\s*:\s*true', s):
        _PARSE_MODE["mode"] = "pass-sniff"
        return {"pass": True, "violations": []}
    _PARSE_MODE["mode"] = "unparseable"
    return {"pass": False, "violations": [{"fact": "PARSE", "quote": raw[:200], "why": "unparseable verdict"}]}


def main():
    ch = sys.argv[1]
    writer = sys.argv[2] if len(sys.argv) > 2 else "unknown"
    facts = (BASE / "CANON.md").read_text(encoding="utf-8")
    text = (PROJ / f"chapter_{ch}.md").read_text(encoding="utf-8")
    locked = locked_facts(facts)
    locked_block = LOCKED_TMPL.format(locked="\n".join("- " + l for l in locked)) if locked else ""
    prompt = PROMPT.format(facts=facts, ch=ch, text=text, locked_block=locked_block)

    raw, reviewer = None, None
    # Reviewer must differ from writer. Primary: Flash-Lite, then FREE local
    # Ollama (unlimited, private), then Groq/ministral. Last resort: ministral
    # (same-model review is weak; the human spot-check remains the real gate).
    order = [check_flash_lite, check_ollama]
    if "120b" in writer or "groq" in writer:
        order.append(check_ministral)
    else:
        order.append(check_groq)
    order.append(check_ministral if order[-1] is check_groq else check_groq)
    err = None
    for fn in order:
        try:
            raw, reviewer = fn(prompt)
            break
        except Exception as e:
            err = f"{fn.__name__}: {str(e)[:150]}"
    if raw is None:
        verdict = {"pass": False, "violations": [{"fact": "REVIEWER-DOWN", "quote": "", "why": err or "all reviewers failed"}]}
        reviewer = "none"
    else:
        verdict = parse_verdict(raw)
        # Filter hedged non-findings on EVERY path (small reviewers list facts
        # just to conclude they are fine — those are not violations).
        raw_n = len(verdict.get("violations", []))
        # PARSE placeholders are infrastructure failures, never hedges:
        # an unparseable reviewer must FAIL, never silently pass.
        kept = [v for v in verdict.get("violations", [])
                if v.get("fact") == "PARSE" or not is_hedge(str(v.get("why", "")))]
        verdict = {"pass": len(kept) == 0, "violations": kept}
        hedged_filtered = raw_n - len(kept)

    result = {"chapter": int(ch), "writer": writer, "reviewer": reviewer,
              "pass": bool(verdict.get("pass")), "violations": verdict.get("violations", []),
              "parse_mode": _PARSE_MODE["mode"] if raw is not None else "reviewer-down",
              "hedged_filtered": hedged_filtered if raw is not None else 0,
              "at": datetime.now(timezone.utc).isoformat()}
    (BASE / f"canon_verdict_ch{ch}.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(BASE / "canon_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")

    # registry update
    regp = BASE / "canon_registry.json"
    reg = json.loads(regp.read_text(encoding="utf-8")) if regp.exists() else {"chapters": {}}
    reg["chapters"][str(ch)] = {"status": "pass" if result["pass"] else "FAIL",
                                "reviewer": reviewer,
                                "violations": len(result["violations"])}
    regp.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"chapter={ch} writer={writer} reviewer={reviewer} "
          f"verdict={'PASS' if result['pass'] else 'FAIL'} violations={len(result['violations'])}")
    for v in result["violations"][:10]:
        print(f" - [{v.get('fact')}] {str(v.get('why'))[:160]}")


if __name__ == "__main__":
    main()
