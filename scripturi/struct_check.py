"""Structural deterministic check: a second gate that is NOT grep-for-meaning
and NOT a model. Verifies shape without understanding text:

  1. SCENES  - scene-heading count (## ... Scene N) matches scenes.json
  2. WORDS   - word count within tolerance of (n_scenes * words-per-scene)
  3. CAST    - every scenes.json character appears >=1; staging-banned names absent
  4. ENDING  - the chapter lands where the outline says (last-scene keywords
               present in the closing tail)

Usage:
    python scripturi/struct_check.py 4 [--proj DIR] [--tol 0.35] [--words-per-scene 1200]

Chapter source: PROJ/chapter_N.md (default PROJ = repo root; override with
--proj or GLASS_PROJ env). Expectations: scenes.json + outline.md at repo root.

Writes struct_verdict_chN.json at repo root, prints PASS/FAIL lines,
exit 0 = PASS, 1 = FAIL so it can gate the pipeline like canon_check.py.
Stdlib only, UTF-8.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent

# Staging bans derived from CANON.md (C08/C15/C16). Single source of truth for
# "who may be named when" that needs no semantic judgment to enforce.
# name -> chapters where ANY mention is a violation.
BANNED = {
    "lara": {1, 2, 3},        # C08: Lara only from ch4
    "mira": {1, 2, 3, 4},     # C16: Mira first appears ch5
    "vela": {1, 2, 3, 4},     # C16: Vela first appears ch5
    "sera": {1, 2, 3, 4, 5, 6, 7, 8, 10},  # C15: Sera named ONLY ch9
}

ALIAS = {  # scenes.json name -> match tokens (lowercase, word-boundary)
    "madam lara": ["lara"],
    "lord varnholt": ["varnholt"],
}

STOPWORDS = set("""
a an and are as at be but by for from had has have her his him in into is it its
of on or she that the their them they this to was were will with you your
care din este este nu sau pentru care cum Fie ce se si în din un una prin mai
mult fata spre dupa cum deja foarte poate sunt fost avea face luat cînd cind
scene summary goal setting beat aim words chapter herself himself without
""".split())


def norm_name(n):
    n = n.strip().lower()
    return ALIAS.get(n, [n.split()[-1]])  # "Madam Lara" -> lara


def keywords(text, limit=8):
    words = re.findall(r"[a-zA-Z\u00c0-\u024f]{5,}", text.lower())
    freq = {}
    for w in words:
        if w in STOPWORDS:
            continue
        freq[w] = freq.get(w, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda kv: -kv[1])[:limit]]


def load_outline_endings(outline_path):
    """outline.md -> {ch: last Key-Events bullet} for the ENDING anchor."""
    text = outline_path.read_text(encoding="utf-8")
    endings = {}
    for m in re.finditer(r"^## Chapter (\d+):.*?(?=^## Chapter |\Z)",
                         text, re.M | re.S):
        ch = int(m.group(1))
        bullets = re.findall(r"^- (.+)$", m.group(0), re.M)
        if bullets:
            endings[ch] = bullets[-1]
    return endings


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("ch", type=int)
    ap.add_argument("--proj", default=os.getenv("GLASS_PROJ", str(ROOT)),
                    help="dir with chapter_N.md (default: repo root or $GLASS_PROJ)")
    ap.add_argument("--tol", type=float, default=0.35,
                    help="word-count tolerance fraction (default 0.35)")
    ap.add_argument("--words-per-scene", type=int, default=1200,
                    help="expected words per scene (default 1200, per scenes.json aims)")
    args = ap.parse_args()

    ch = args.ch
    proj = Path(args.proj)
    failures = []

    scenes = json.loads((ROOT / "scenes.json").read_text(encoding="utf-8"))
    expected_scenes = scenes.get(str(ch), [])
    if not expected_scenes:
        print(f"no scenes.json entry for ch{ch} -- cannot check", file=sys.stderr)
        return 2
    chap_path = proj / f"chapter_{ch}.md"
    if not chap_path.exists():
        print(f"missing {chap_path} -- cannot check", file=sys.stderr)
        return 2
    text = chap_path.read_text(encoding="utf-8")
    words = len(text.split())

    # 1. SCENES
    found_headings = len(re.findall(r"(?m)^#{1,4} .*Scene \d+", text))
    n_exp = len(expected_scenes)
    ok_scenes = found_headings == n_exp
    print(f"[{'PASS' if ok_scenes else 'FAIL'}] scenes: "
          f"headings={found_headings} expected={n_exp}")
    if not ok_scenes:
        failures.append(f"scene count {found_headings} != {n_exp}")

    # 2. WORDS
    expected_words = n_exp * args.words_per_scene
    lo, hi = expected_words * (1 - args.tol), expected_words * (1 + args.tol)
    ok_words = lo <= words <= hi
    print(f"[{'PASS' if ok_words else 'FAIL'}] words: {words} "
          f"expected~{expected_words} bounds [{int(lo)}-{int(hi)}]")
    if not ok_words:
        failures.append(f"word count {words} outside [{int(lo)}-{int(hi)}]")

    # 3. CAST: expected present, banned absent.
    lowered = text.lower()
    want = set()
    for sc in expected_scenes:
        for c in sc.get("characters", []):
            want.update(norm_name(c))
    missing = [w for w in sorted(want)
               if not re.search(r"\b" + re.escape(w) + r"\b", lowered)]
    ok_cast = not missing
    print(f"[{'PASS' if ok_cast else 'FAIL'}] cast present: "
          f"{sorted(want)}" + (f" MISSING={missing}" if missing else ""))
    if missing:
        failures.append(f"missing characters: {missing}")

    banned_hit = sorted(b for b, chs in BANNED.items()
                        if ch in chs and re.search(r"\b" + b + r"\b", lowered))
    ok_banned = not banned_hit
    print(f"[{'PASS' if ok_banned else 'FAIL'}] cast staging: "
          + ("clean" if ok_banned else f"BANNED mentions={banned_hit}"))
    if banned_hit:
        failures.append(f"banned mentions in ch{ch}: {banned_hit}")

    # 4. ENDING: last-scene keywords (+ outline last bullet) in closing tail.
    tail = " ".join(text.split()[-max(300, words // 10):]).lower()
    anchor_src = expected_scenes[-1].get("summary", "")
    try:
        anchor_src += " " + load_outline_endings(ROOT / "outline.md").get(ch, "")
    except FileNotFoundError:
        pass
    keys = keywords(anchor_src)
    hits = [k for k in keys if re.search(r"\b" + re.escape(k) + r"\b", tail)]
    need = 2 if len(keys) >= 3 else 1
    ok_end = len(hits) >= need
    print(f"[{'PASS' if ok_end else 'FAIL'}] ending: keywords={keys} "
          f"hits={hits} (need>={need} in closing tail)")
    if not ok_end:
        failures.append(f"ending anchor weak: {len(hits)}/{need} keywords {keys}")

    verdict = {"chapter": ch, "pass": not failures, "failures": failures,
               "words": words, "scenes_found": found_headings,
               "scenes_expected": n_exp}
    (ROOT / f"struct_verdict_ch{ch}.json").write_text(
        json.dumps(verdict, ensure_ascii=False, indent=2), encoding="utf-8")
    print("STRUCT " + ("PASS" if verdict["pass"] else "FAIL") + f" ch{ch}")
    for f in failures:
        print(f" - {f}")
    return 0 if verdict["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
