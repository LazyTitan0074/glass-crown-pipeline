import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
d = json.loads((A / "characters.json").read_text(encoding="utf-8"))
for c in d["characters"]:
    n = c.get("name", "")
    if n == "Mirela":
        c["physical_description"] = "Late-40s, tall, greying auburn hair coiled tight, pale eyes, rose-and-darker perfume. Cold elegance; marble-old, harder not softer."
        c["personality_traits"] = "Cool, precise, venomous-calm; NEVER raises her voice. Threats sound like paperwork; language of duty/stability. Often: 'You have until dawn.' / \"Don't make me regret this.\" / 'I did what was necessary.' NEVER begs, NEVER explains twice, NEVER invokes any goddess or Mother-title. Private crack at her fall only: the smile that doesn't reach (fear of making a martyr, not remorse)."
        c["character_arc"] = "Public fall with evidence; an undeniable smile; one private crack showing fear, never remorse."
    if n == "Elowen":
        c["personality_traits"] = "Merchant-warm, predatory-polite; everything is a price said kindly. Often: 'Little bird.' / 'At a price, of course.' / \"Don't thank me yet.\" Sees instantly, charges accordingly."
        c["character_arc"] = "Paid off after vassalage (ch7 farewell: unsentimental, one true line); the brothel continues as a Vestalian info asset. Leah never returns, never forgets."
    if n == "Cassian":
        c["physical_description"] = "A 14-year-old boy, spoiled; outdated finery he hasn't grown into. Never described as a man; no grey-green eyes, no pinned black hair."
        c["character_arc"] = "Spare heir weaponised by Mirela; protected by Leah's negotiation (ch7 win); ONE unguarded child moment in ch8 (fear, not cruelty; no redemption, no forgiveness scene) so the exile terms ache."
(A / "characters.json").write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "characters.json").write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print("characters enriched + mirrored")
