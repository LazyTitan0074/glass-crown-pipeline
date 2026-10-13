import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
sc["8"][0]["summary"] = "Dawn departure from the inn: Elowen's FAREWELL (paid off; brothel becomes Vestalian info asset; one unsentimental parting line; Leah never returns, never forgets) — then the night of opened gates by spies; the Daughters of Flame enter without slaughter. (aim ~1200 words)"
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
# sync embedded too (writer reads project_data, not scenes.json!)
d = json.load(open(P / "project_data.json", encoding="utf-8"))
for ch, scenes in sc.items():
    if ch in d.get("chapters", {}):
        d["chapters"][ch]["scenes"] = [
            {"scene_number": s["scene_number"], "summary": s["summary"],
             "characters": s.get("characters", []), "setting": s.get("setting", ""),
             "goal": s.get("goal", ""), "emotional_beat": s.get("emotional_beat", "")}
            for s in scenes]
json.dump(d, open(P / "project_data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("farewell relocated to ch8s1 + embedded re-synced")
