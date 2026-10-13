import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
sc["2"][1]["summary"] = "The first client, UNNAMED (young, fumbling, clumsy; finishes fast, pays, leaves): rushed and graceless; he NEVER asks what she feels and NEVER tends to her pleasure — she performs, observes, endures; autonomy only. (aim ~1200 words)"
sc["2"][3]["summary"] = "A drunken officer talks of nothing but 'a host in the east' (big numbers, a woman leads them, they say — NO goddess names, NO 'Mother of Two Faces', NO 'Daughters', NO Vestalia, NO Lara); Elowen listens carefully. (aim ~1200 words)"
sc["3"][3]["summary"] = "Distant travellers' tales from a merchant: the far-eastern empire 'Vestalia' and its women-army 'Daughters of Flame' as foreign words only — NO goddess names, NO theology, NO Lara, NO envoys. (aim ~1200 words)"
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
print("ch2-3 doctrine guards pinned")
