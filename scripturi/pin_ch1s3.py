import json, shutil
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
sc["1"][2]["summary"] = "Alone in her room, Leah remembers her mother's sudden death and begins to SUSPECT Mirela's hand (dread, questions, itching blur — NEVER certainty; confirmation comes only in ch4). She decides to flee."
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
print("scene3 pinned")
