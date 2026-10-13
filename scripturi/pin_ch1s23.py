import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
sc["1"][1]["summary"] = "Mirela (queen only — never 'Crown-Mother', never invokes any 'Unique Mother') summons her and lays out the betrothal contract with Lord Varnholt — marriage or slow ruin. Leah does NOT accuse Mirela of any murder; Mirela reveals NOTHING about the past; no poison confrontation."
sc["1"][2]["summary"] = "Alone in her room, Leah remembers her mother's sudden death in sensory fragments (a sweet brew, trembling hands) and begins to SUSPECT Mirela's hand (dread, questions, itching blur — NEVER certainty, NEVER 'the poison was in the tea' stated as fact; confirmation comes only in ch4). She decides to flee."
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
print("scenes pinned")
