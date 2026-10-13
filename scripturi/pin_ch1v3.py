import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")
P = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
sc = json.loads((A / "scenes.json").read_text(encoding="utf-8"))
sc["1"][0]["summary"] = "Leah scrubs and cleans in the servants' wing; Cassian (EXACTLY 14, a BOY — verbal cruelty ONLY; he NEVER touches/shoves/grabs her, NEVER any physical contact at all; no sexualized words like whore/slut; NEVER describe his gaze, fingers or closeness on her body, nothing sensual) humiliates her with base chores."
sc["1"][2]["summary"] = "Alone in her room, Leah remembers her mother's sudden death in sensory fragments (a sweet brew, trembling hands) and begins to SUSPECT Mirela's hand (dread, questions — she does NOT know; NEVER write 'she knew/had known' about any murder; NO ledger, NO letters, NO written proof of anything — evidence appears ONLY in ch5 via Lara; NO Vestalian religion: NEVER name Azara, Vohra, Unique Mother or sacred fire; confirmation comes only in ch4). She decides to flee."
(A / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "scenes.json").write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
print("scenes pinned v3")
