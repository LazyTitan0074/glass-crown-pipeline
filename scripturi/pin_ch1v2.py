import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
sc["1"][0]["summary"] = "Leah scrubs and cleans in the servants' wing; Cassian (EXACTLY 14, a BOY — verbal cruelty ONLY; NEVER describe his gaze on her body, no lingering eyes, nothing 'not brotherly', nothing sensual) humiliates her with base chores."
sc["1"][2]["summary"] = "Alone in her room, Leah remembers her mother's sudden death in sensory fragments (a sweet brew, trembling hands) and begins to SUSPECT Mirela's hand (dread, questions — she does NOT know; NEVER write 'she knew/had known' about any murder; confirmation comes only in ch4). She decides to flee."
sc["1"][3]["summary"] = "Flight through corridors, gates and streets — guards, dogs, hunger, the Lower City. Flight ONLY: Leah meets NO ONE, NO stranger speaks to her, NO tall dark-haired woman, NO one finds or helps her; she reaches the inn alone."
sc["1"][4]["summary"] = "The Red Velvet Inn; Elowen (mahogany hair, AMBER eyes — never black hair, never grey-green eyes) recognizes her instantly and takes her in out of interest."
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
print("scenes pinned v2")
