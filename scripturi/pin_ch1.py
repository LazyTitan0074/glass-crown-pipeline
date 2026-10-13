import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
sc["1"][0]["summary"] = "Leah scrubs and cleans in the servants' wing; Cassian (EXACTLY 14 years old, her half-brother by a DIFFERENT mother — Mirela, who is alive) humiliates her with base chores, verbal only."
sc["1"][1]["summary"] = "Mirela (queen only — never 'Crown-Mother', never invokes any 'Unique Mother') summons her and lays out the betrothal contract with Lord Varnholt — marriage or slow ruin."
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
import shutil
shutil.copy(A / "CANON.md", Path(r"C:\Users\bizoi\libriscribe-roman\CANON.md"))
shutil.copy(A / "research_results.md", P / "research_results.md")
print("pinned + mirrored")
