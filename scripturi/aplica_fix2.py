"""Fix2: Cassian din aventura + verbal-only, Mirela motiv, Mira->Sorina, dq resync."""
import json
from pathlib import Path

PROJ = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
from libriscribe.knowledge_base import ProjectKnowledgeBase, Character

pkb = ProjectKnowledgeBase.load_from_file(str(PROJ / "project_data.json"))

c = pkb.characters["Cassian"]
c.background = ("Son of the king AND Mirela, born from their affair DURING the first marriage "
 "(Leah was 6) and legitimized after the royal wedding. Both Leah and Cassian know this. "
 "Second in line after Leah under firstborn succession.")
c.motivations = ("Attention and favour; the throne Mirela promises him under a male-first law. "
 "A living spare heir who knows exactly what he is.")
c.personality_traits = (c.personality_traits.rstrip() +
 " Violence VERBAL ONLY, never physical (hard rule).")
c.character_arc = ("Spare heir weaponised by Mirela; protected by Leah's negotiation. "
 "Open fate: exile, Vestalia, or antagonist years later.")

m = pkb.characters["Mirela"]
m.background = ("Former lady-in-waiting; the king's mistress during his first marriage (their son "
 "Cassian was legitimized after the royal wedding). Poisoned Queen Elara, married the king, paid "
 "mercenaries to withdraw his guard on the front. Rules alone for 2 years.")
m.motivations = ("Power without Leah's shadow; a male-first succession law that crowns her son "
 "and buries the stain of his birth; a clean Valdris with no martyrs.")

pkb.characters.pop("Mira", None)
old = None
for k in list(pkb.characters.keys()):
    pass
pkb.characters["Sorina"] = Character(
    name="Sorina", age="30+",
    physical_description="Vestalian woman, sharp-eyed, plain costly dress.",
    personality_traits="Competent, loyal to Lara, economical with words. Speaks only when it matters.",
    background="One of the two women of Lara's proposed future council; first appears in ch5 as envoy and living proof.",
    motivations="A loyal Valdris under Vestalian order; her own seat on the council.",
    relationships={"general": "Lara's envoy alongside Vela; measured toward Leah."},
    role="Supporting character",
    internal_conflicts="Duty vs doubt about Leah.",
    external_conflicts="Valdris nobles who despise Vestalia.",
    character_arc="From envoy to councillor — if Leah accepts.")

for n in pkb.chapters[5].scenes:
    n.characters = ["Sorina" if x == "Mira" else x for x in (n.characters or [])]

pkb.save_to_file(str(PROJ / "project_data.json"))
with open(PROJ / "characters.json", "w", encoding="utf-8") as f:
    json.dump({"characters": [x.model_dump() for x in pkb.characters.values()]}, f, ensure_ascii=False, indent=2)
scenes_data = {str(n): [s.model_dump() for s in pkb.chapters[n].scenes] for n in pkb.chapters}
(PROJ / "scenes.json").write_text(json.dumps(scenes_data, ensure_ascii=False, indent=2), encoding="utf-8")

import capitol_runner as r
r.sync_registry_dq()
print("chars:", sorted(pkb.characters.keys()))
print("ch5sc1:", pkb.chapters[5].scenes[0].characters)
print("OK fix2")
