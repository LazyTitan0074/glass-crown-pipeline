import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
print("before:", {k: len(v) for k, v in sc.items()})

# ch7: merge s4+s5 (correction + truce)
s7 = sc["7"]
s7[3]["summary"] = "Lara corrects her for the first time under Vestalian rules (maternal correction, consensual personal level; political disagreement never punished by personal withdrawal) — then a half-signed accord both know isn't over. (aim ~1200 words)"
s7[3]["goal"] = "Taste of discipline + truce"
s7[3]["emotional_beat"] = "Fragile peace"
del s7[4]

# ch8: merge s4+s5 (price: nobles + Cassian)
s8 = sc["8"]
s8[3]["summary"] = "The price: nobles choose kneeling or exile (first whisper of resistance), and Cassian is brought before them — Leah takes him under her wing in one unguarded child moment (fear, not cruelty; no redemption). (aim ~1200 words)"
s8[3]["characters"] = ["Leah", "Madam Lara", "Cassian"]
s8[3]["goal"] = "The price + shielding her brother"
s8[3]["emotional_beat"] = "Unease + tenderness"
del s8[4]

# ch9: merge s4+s5 (offer forces tally)
s9 = sc["9"]
s9[3]["summary"] = "The exiled nobles' message (a way out, a ship, one night) forces the tally: financial, emotional, physical dependence itemized. (aim ~1200 words)"
s9[3]["goal"] = "Temptation + the tally"
s9[3]["emotional_beat"] = "Dangerous hope + lucid despair"
del s9[4]

# ch10: merge s4+s5 (gesture + echo)
s10 = sc["10"]
s10[3]["summary"] = "Lara's gesture: she burns the pursuit orders — the one thing that proves it — then the open epilogue: ship or crown, last image in the mirror. (aim ~1200 words)"
s10[3]["characters"] = ["Madam Lara", "Leah"]
s10[3]["goal"] = "The proof + echo"
s10[3]["emotional_beat"] = "Unspoken love + beginning"
del s10[4]

# renumber + word budget on every future scene (ch2-10; ch1 finished, untouched)
for ch, scenes in sc.items():
    if ch == "1":
        continue
    for i, s in enumerate(scenes, 1):
        s["scene_number"] = i
        if "(aim ~1200 words)" not in s["summary"]:
            s["summary"] = s["summary"].rstrip() + " (aim ~1200 words)"

print("after:", {k: len(v) for k, v in sc.items()})
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
print("scenes standardized 4x1200")
