import json, sys, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
env = dict(l.strip().split("=", 1) for l in open(r"C:\Users\bizoi\libriscribe-roman\.env", encoding="utf-8") if "=" in l.strip() and not l.strip().startswith("#"))
KEY = env["OPENROUTER_API_KEY"].strip().strip("'").strip('"')

PROMPT = """You are writing one scene of the dark-fantasy novel "The Glass Crown" (English, adult audience, consensual-adult themes only).

Context: Leah Estia, 20, legitimate heiress of Valdris, fled a forced marriage and hides in the Red Velvet Inn, the capital's costliest brothel. Its mistress Elowen (mahogany hair, amber eyes) shelters her for a price: young clients only, plus Leah must listen and report secrets. This is day 3.

Leah's voice: hesitant, quiet, then direct. Often says "I'm sorry." / "May I...?" / "Thank you." Survivor, not victim. Third person limited on Leah, PAST tense. Sensory, lean prose, no purple metaphors.

SCENE (aim ~1000-1200 words): A travelling merchant in the inn's salon tells distant travellers' tales over wine: a far-eastern empire called "Vestalia" and its army of women called the "Daughters of Flame" — foreign words only, half-believed gossip. Leah listens, curious, and practices remembering details the way the older girls taught her.

HARD RULES (violating any = failure):
- NEVER name any goddess, no "Azara", no "Vohra", no "Mother of Two Faces", no sacred fire, no temples.
- NEVER mention anyone named Lara/Isolde, Mira, Vela, Sera. No envoys, no letters, no proof of anything.
- Keep it tavern gossip: vague, contradictory, half-drunk. Nobody in the room treats it as certain.
- No new named characters except the merchant (give him NO surname from this list: Varnholt, Cassian, Mirela, Elara, Elowen).

Write ONLY the scene prose with a short scene heading."""

def run(model):
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": PROMPT}], "max_tokens": 2000, "temperature": 0.7}).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + KEY, "HTTP-Referer": "local", "X-Title": "canon-test"})
    r = urllib.request.urlopen(req, timeout=120)
    j = json.load(r)
    return j["choices"][0]["message"]["content"], j.get("usage", {})

for m in ["google/gemma-4-31b-it:free", "nvidia/nemotron-3-super-120b-a12b:free"]:
    try:
        text, usage = run(m)
        print("MODEL:", m, "USAGE:", usage)
        open(r"C:\Users\bizoi\roman\test_scene_or.md", "w", encoding="utf-8").write("# TEST " + m + "\n\n" + text)
        print("chars:", len(text))
        break
    except Exception as e:
        print("MODEL:", m, "DOWN:", str(e)[:200])
