"""Aplica deciziile: Cassian fiul regelui + succesiune, Mira & Vela, Elara, 18+ explicit."""
import json
from pathlib import Path

PROJ = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
from libriscribe.knowledge_base import ProjectKnowledgeBase, Character

pkb = ProjectKnowledgeBase.load_from_file(str(PROJ / "project_data.json"))

pkb.description = (
 "Leah Estia, 20, the legitimate heiress of Valdris, flees a forced marriage to 62-year-old "
 "Lord Varnholt on the night before the signing and reaches the Red Velvet Inn. There Madam Lara, 35, "
 "Queen of the Vestalian Empire leading an army of Daughters of Flame, finds her and offers the throne "
 "in exchange for vassalage. Dark political fantasy, adult, consensual between adults; explicit adult "
 "content allowed including light BDSM, always consensual. The 14-year-old stepbrother Cassian — also the "
 "king's son, second after Leah — stays strictly non-sexual, only a family figure. Succession is firstborn; "
 "Mirela pushes male-first. Central question: is Lara's discipline care or better-packaged abuse?"
)

# Cassian: king's son + succession
c = pkb.characters["Cassian"]
c.background = ("Son of Mirela AND of the king (second marriage). Both Leah and Cassian know this. "
 "Second in line after Leah under firstborn succession; Mirela pushes to change the law to male-first.")
c.motivations = ("Attention and favour; to be like his mother — and the throne Mirela promises him. "
 "A living spare heir.")
c.character_arc = ("Spare heir weaponised by Mirela; protected by Leah's negotiation. "
 "Open fate: exile, Vestalia, or antagonist years later.")

# Mira & Vela
def CE(name, phys, traits, bg, motiv, rel, role, iconf, econf, arc):
    return Character(name=name, age="30+", physical_description=phys, personality_traits=traits,
            background=bg, motivations=motiv, relationships={"general": rel}, role=role,
            internal_conflicts=iconf, external_conflicts=econf, character_arc=arc)

pkb.characters["Mira"] = CE(
 "Mira", "Vestalian woman, sharp-eyed, plain costly dress.",
 "Competent, loyal to Lara, economical with words. Speaks only when it matters.",
 "One of the two women of Lara's proposed future council; first appears in ch5 as envoy and living proof.",
 "A loyal Valdris under Vestalian order; her own seat on the council.",
 "Lara's envoy alongside Vela; measured toward Leah.",
 "Supporting character", "Duty vs doubt about Leah.",
 "Valdris nobles who despise Vestalia.",
 "From envoy to councillor — if Leah accepts.")
pkb.characters["Vela"] = CE(
 "Vela", "Vestalian woman, younger, watchful, soldier's bearing.",
 "Direct, dry, observant. Notices everything, comments little.",
 "One of the two women of Lara's proposed future council; first appears in ch5 as envoy and living proof.",
 "To prove a Valdris queen can be formed; order through strength.",
 "Lara's envoy alongside Mira; tests Leah with silence.",
 "Supporting character", "Contempt for weakness vs Lara's orders.",
 "Anyone threatening the mission.",
 "From envoy to councillor — if Leah accepts.")

# ch5 scenes: add envoys; ch4 scene3: explicit (no fade requirement)
ch5 = pkb.chapters[5]
ch5.scenes[0].characters = ["Leah", "Madam Lara", "Mira", "Vela"]
ch5.scenes[0].summary = ("Lara spreads the map and evidence: Queen Elara's poison, the mercenaries' payment. "
 "Two Vestalian women, Mira and Vela of the proposed future council, attend as living proof.")
ch5.scenes[1].characters = ["Leah", "Madam Lara", "Mira", "Vela"]
ch4 = pkb.chapters[4]
ch4.scenes[2].summary = ("Consensual intimate scene between adults (explicit allowed, always consensual); "
 "someone tends to her pleasure for the first time; 'mommy' slips out.")

pkb.save_to_file(str(PROJ / "project_data.json"))

# mirror files
with open(PROJ / "characters.json", "w", encoding="utf-8") as f:
    json.dump({"characters": [x.model_dump() for x in pkb.characters.values()]}, f, ensure_ascii=False, indent=2)
scenes_data = {str(n): [s.model_dump() for s in pkb.chapters[n].scenes] for n in pkb.chapters}
(PROJ / "scenes.json").write_text(json.dumps(scenes_data, ensure_ascii=False, indent=2), encoding="utf-8")

# outline.md targeted updates
om = (PROJ / "outline.md").read_text(encoding="utf-8")
om = om.replace("Intimate scene fade-to-black — total surrender, 'mommy'.",
                "Consensual intimate scene between adults (explicit allowed) — total surrender, 'mommy'.")
om = om.replace("Intimate scene with fade-to-black.",
                "Consensual intimate scene between adults (explicit allowed).")
om = om.replace("She shows the evidence — the mother's poisoning, the mercenaries' payment.",
                "She shows the evidence — Queen Elara's poisoning, the mercenaries' payment. Mira and Vela, two women of the proposed future council, attend as living proof.")
(PROJ / "outline.md").write_text(om, encoding="utf-8")

print("chars:", sorted(pkb.characters.keys()))
print("ch5sc1:", ch5.scenes[0].characters)
print("OK decizii aplicate")
