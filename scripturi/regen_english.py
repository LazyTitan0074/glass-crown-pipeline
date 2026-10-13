"""Converteste proiectul leah_si_lara in engleza + redenumeste Matei -> Cassian."""
import json
from pathlib import Path

PROJ = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
from libriscribe.knowledge_base import ProjectKnowledgeBase, Chapter, Scene, Worldbuilding, Character

pkb = ProjectKnowledgeBase.load_from_file(str(PROJ / "project_data.json"))

pkb.title = "The Glass Crown"
pkb.language = "English"
pkb.genre = "Fantasy"
pkb.description = (
 "Leah Estia, 20, the legitimate heiress of Valdris, flees a forced marriage to 62-year-old "
 "Lord Varnholt on the night before the signing and reaches the Red Velvet Inn. There Madam Lara, 35, "
 "Queen of the Vestalian Empire leading an army of Daughters of Flame, finds her and offers the throne "
 "in exchange for vassalage. Dark political fantasy, adult, consensual between adults, intimate scenes "
 "fade-to-black. The 14-year-old stepbrother stays strictly non-sexual, only a family figure. "
 "Central question: is Lara's discipline care or better-packaged abuse?"
)
pkb.logline = (
 "The legitimate heiress of Valdris flees a forced marriage and finds refuge with Lara, Queen of "
 "Vestalia, who offers her the throne for strict vassalage — forcing Leah to decide whether imposed "
 "discipline is maternal care or well-packaged abuse."
)
pkb.num_chapters = 10
pkb.num_chapters_str = "10"
pkb.book_length = "Novel"

CH = [
 (1, "Cinderella",
  "After the king's death on the front, Leah (20), daughter of the first marriage, lives as a Cinderella: "
  "moved out of the royal apartment, made to serve, humiliated daily by her stepmother Mirela and her "
  "stepbrother Cassian (14). Mirela — the former lady-in-waiting who poisoned the first queen and paid "
  "mercenaries to withdraw the king's guard — rules alone and wants Leah gone without a martyrdom: a marriage "
  "to Lord Varnholt (62) of the north. On the night before the signing, Leah flees to the Lower City.",
  ["Leah serves and is humiliated by Cassian and Mirela — the Cinderella status.",
   "Mirela presents the betrothal contract with Lord Varnholt — exile disguised.",
   "Memory of her dead mother and suspicion of poison — the decision to flee.",
   "Flight through castle and city — guards, fear, hunger."]),
 (2, "The Lower City",
  "Flight, fear, hunger. Leah reaches the Red Velvet Inn, the costliest brothel in the capital, where "
  "information is worth more than flesh. Its mistress Elowen recognizes her in the first second — a princess "
  "cannot be mistaken — and takes her in out of interest: a virgin princess is a fortune. Leah accepts: for "
  "the first time, her body is her own.",
  ["Arrival at the inn and Elowen's recognition.",
   "The contract: young clients only; information as currency.",
   "The first night — fear and first autonomy.",
   "Rumour of a huge army in the east."]),
 (3, "Two Days",
  "In two days Leah learns more about her own body than in 20 years at the castle, and learns how the lower "
  "world works: information is worth more than flesh. Elowen protects her but also exploits her. She hears "
  "about Vestalia and the Daughters of Flame.",
  ["Discovery of body and pleasure — curiosity and shame.",
   "The lesson of information from older girls.",
   "Elowen shields her from a violent client — protection at a price.",
   "News of the east — curiosity."]),
 (4, "Madam Lara",
  "After two days Lara appears: 35, tall, black hair severely pinned, simple expensive clothes, two female "
  "guards, a purse of gold. She asks for Leah by name. In the luxury suite, in a thin silk robe, she calms her, "
  "kisses her slowly and leads her to bed — the first time anyone tends to her pleasure. Leah slips into "
  "subspace and lets out 'mommy'. Lara stops, dresses, and introduces herself: Queen of the Vestalian Empire, "
  "with an army to conquer the kingdom. She knows everything, including Mirela's crimes. Intimate scene with fade-to-black.",
  ["Lara's entrance — Elowen frozen: how does she know the name?",
   "The suite: calming, wine, light touch — trust.",
   "Intimate scene fade-to-black — total surrender, 'mommy'.",
   "The reveal: who Lara is and what she knows."]),
 (5, "The Offer",
  "Lara explains the plan: the army enters Valdris, Mirela dethroned with proof of murder, Leah crowned queen "
  "under a council of Vestalian women, Valdris a vassal. She shows the evidence — the mother's poisoning, the "
  "mercenaries' payment. Leah asks for time; Lara grants it, but the army crosses the border anyway.",
  ["The evidence: letters and payments — lucid horror.",
   "The 5-step plan — toxic hope.",
   "Leah asks for time; the pressure stays.",
   "Mourning for mother and father."]),
 (6, "The Lie",
  "Leah gets to the army's real figures and discovers '1 million' is propaganda — the first crack in Lara's "
  "image. At last she has currency to negotiate: secret passages, castle allies, proof of the murder.",
  ["The numbers don't add up — doubt.",
   "Confrontation: 'How many, really?' Lara partly admits.",
   "Leah's inventory — passages, allies, proof.",
   "Lara looks at her differently — cautious respect."]),
 (7, "The Negotiation",
  "Leah sets conditions: Cassian untouched, exile not execution for the nobles, a real vote in the council. Lara "
  "accepts some, refuses others. The first open clash — and the first correction under Vestalian rules.",
  ["Leah writes her conditions at night.",
   "Cassian untouched — a small victory.",
   "Exile vs execution; the vote refused — the clash.",
   "The first correction — a taste of discipline."]),
 (8, "The Conquest",
  "The army enters; Lara's spies open the gates. Mirela is caught and exposed with public evidence. Leah is "
  "crowned — the people love her. The nobles choose kneeling or exile. Resistance ripens in the shadows.",
  ["The night of open gates — a clean conquest.",
   "Mirela's fall — bitter triumph.",
   "The coronation — a heavy crown.",
   "Kneel or exile; Cassian under Leah's wing."]),
 (9, "The Glass Crown",
  "Leah discovers the 'council' decides everything. Lara starts correcting her under Vestalian rules, and Leah "
  "can no longer leave — Lara's absolute limit is broken. The exiled nobles offer her a way out.",
  ["The council rules — frustration.",
   "The correction — shame and rage.",
   "Lara and Sera's shadow — guilt.",
   "The exiles' offer — dangerous hope."]),
 (10, "The Choice",
  "Leah chooses: stay, leave, or play double. Lara must decide whether to keep her own rule and let her go. "
  "Open ending: Lara never says 'I love you', but does the one thing that proves it.",
  ["The night of decision — torn apart.",
   "'If I leave, will you let me?' — naked truth.",
   "Leah's act — freedom.",
   "Lara's gesture — unspoken love; open echo."]),
]

SCENES = {
 1: [
  ("Leah scrubs and cleans in the servants' wing; Cassian humiliates her with base chores.", ["Leah", "Cassian"], "Valdris Castle — servants' wing", "Establish the Cinderella status", "Muffled humiliation"),
  ("Mirela summons her and lays out the betrothal contract with Lord Varnholt — marriage or slow ruin.", ["Leah", "Mirela", "Lord Varnholt"], "The queen's office", "Set the stakes of flight", "Cold fear"),
  ("Alone in her room, Leah remembers her mother's sudden death and understands Mirela's hand; she decides to flee.", ["Leah"], "Servant's room", "The decision to flee", "Fragile resolve"),
  ("Flight through corridors, gates and streets — guards, dogs, hunger, the Lower City.", ["Leah"], "Castle, gates, streets to the Lower City", "Physical escape", "Controlled panic"),
  ("The Red Velvet Inn; Elowen recognizes her instantly and takes her in out of interest.", ["Leah", "Elowen"], "The Red Velvet Inn", "Hook the story", "Tense relief"),
 ],
 2: [
  ("Elowen tells her she knows who she is and offers the contract: young clients only, discretion, her cut.", ["Leah", "Elowen"], "Elowen's study", "The contract", "Suspicion"),
  ("The first young client, hasty and clumsy; Leah frightened, but her body is hers for the first time.", ["Leah"], "Inn suite", "First autonomy", "Shame and curiosity"),
  ("Second day: the girls teach her to listen and remember — nobles' secrets are worth gold.", ["Leah", "Elowen"], "Inn salon", "The lesson of information", "Adaptation"),
  ("A drunken officer talks of the host in the east; Elowen listens carefully.", ["Leah", "Elowen"], "Inn salon", "Foreshadowing", "Unease"),
 ],
 3: [
  ("Leah discovers her body's pleasure and limits; notes what men want to confess.", ["Leah"], "Inn suite", "Self-knowledge", "Awakening"),
  ("An older girl tells what secrets noble clients spill over wine.", ["Leah"], "The Red Velvet Inn", "Information as currency", "Complicity"),
  ("Elowen pulls her out of a violent client's reach — protection at a price.", ["Leah", "Elowen"], "The Red Velvet Inn", "The price of protection", "Mixed gratitude"),
  ("Details on Vestalia and the Daughters of Flame from a travelling merchant.", ["Leah"], "The Red Velvet Inn", "Foreshadowing", "Curiosity"),
 ],
 4: [
  ("Lara enters with two female guards and gold; asks for Leah by name; Elowen freezes.", ["Madam Lara", "Elowen", "Leah"], "Inn hall", "Mystery", "Tension"),
  ("In the luxury suite, Lara calms her with wine and a light touch; Leah relaxes for the first time.", ["Leah", "Madam Lara"], "Luxury suite", "Trust", "Cautious tenderness"),
  ("Intimate scene fade-to-black; someone tends to her pleasure; 'mommy' slips out.", ["Leah", "Madam Lara"], "Luxury suite", "Surrender and attachment", "Total abandon"),
  ("Lara dresses and introduces herself: Queen of Vestalia, the army, Mirela's crimes.", ["Leah", "Madam Lara"], "Luxury suite", "The reveal", "Shock"),
 ],
 5: [
  ("Lara spreads the map and evidence: the mother's poison, the mercenaries' payment.", ["Leah", "Madam Lara"], "Luxury suite", "The proof", "Lucid horror"),
  ("The 5-step plan: dethroning, coronation, Vestalian council, vassalage.", ["Leah", "Madam Lara"], "Luxury suite", "The offer", "Toxic hope"),
  ("Leah asks for time; Lara grants it, but the army crosses the border anyway.", ["Leah", "Madam Lara"], "Luxury suite", "Pressure", "Tightening grip"),
  ("Alone with the evidence, Leah mourns mother and father.", ["Leah"], "Luxury suite", "Mourning", "Old grief"),
 ],
 6: [
  ("Leah reads the marching orders; the figures don't match '1 million'.", ["Leah"], "The Red Velvet Inn", "Discovery", "Doubt"),
  ("Confrontation: 'How many, really?' Lara partly admits.", ["Leah", "Madam Lara"], "Luxury suite", "First crack", "Cold tension"),
  ("Leah inventories her currency: secret passages, loyal servants, proof of murder.", ["Leah"], "Luxury suite", "Negotiating currency", "New calculus"),
  ("Lara looks at her differently — respect or recalibration.", ["Leah", "Madam Lara"], "Luxury suite", "Power shift", "Cautious respect"),
 ],
 7: [
  ("At night, Leah writes her conditions on a strip of paper.", ["Leah"], "Luxury suite", "Preparation", "Resolve"),
  ("Table I: Cassian untouched — Lara accepts, a living guarantee.", ["Leah", "Madam Lara"], "Luxury suite", "Small victory", "Relief"),
  ("Table II: exile not execution; a real council vote — Lara refuses the full vote.", ["Leah", "Madam Lara"], "Luxury suite", "The clash", "Restrained fury"),
  ("Lara corrects her for the first time under Vestalian rules.", ["Leah", "Madam Lara"], "Luxury suite", "Taste of discipline", "Confused humiliation"),
  ("A half-signed accord; both know it isn't over.", ["Leah", "Madam Lara"], "Luxury suite", "Truce", "Fragile peace"),
 ],
 8: [
  ("The night of opened gates by spies; the Daughters of Flame enter without slaughter.", ["Madam Lara"], "Capital gates", "Clean conquest", "Cold grandeur"),
  ("Mirela arrested with evidence read in public; she doesn't deny it, she smiles.", ["Mirela", "Madam Lara", "Leah"], "Throne hall", "The fall", "Bitter triumph"),
  ("Leah's coronation; the people love her; the crown is heavy.", ["Leah"], "Capital square", "The peak", "Dizziness"),
  ("The nobles choose kneeling or exile; the first whisper of resistance.", ["Leah", "Madam Lara"], "Throne hall", "The price", "Unease"),
  ("Cassian brought before them; Leah takes him under her wing.", ["Leah", "Cassian", "Madam Lara"], "Palace", "Shielding her brother", "Tenderness"),
 ],
 9: [
  ("First council session: Leah proposes, the council disposes.", ["Leah"], "Council chamber", "The hollow crown", "Frustration"),
  ("Correction under Vestalian rules; Leah feels kept, not formed.", ["Leah", "Madam Lara"], "Palace", "The broken limit", "Shame and rage"),
  ("Lara and Sera's shadow: 'you don't correct someone who cannot leave' — yet she continues.", ["Madam Lara"], "Lara's apartments", "Lara's crack", "Guilt"),
  ("The exiled nobles' message: a way out, a ship, one night.", ["Leah"], "Palace", "Temptation", "Dangerous hope"),
  ("The tally: financial, emotional, physical dependence.", ["Leah"], "Palace", "The tally", "Lucid despair"),
 ],
 10: [
  ("The night of decision: the bag packed and unpacked three times.", ["Leah"], "Palace", "The scales", "Torn apart"),
  ("Last confrontation: 'If I leave, will you let me?' Lara's silence.", ["Leah", "Madam Lara"], "Lara's apartments", "The question", "Naked truth"),
  ("Leah's act: the gesture by which she chooses — stay, leave, or double game.", ["Leah"], "Palace and harbour", "The act", "Freedom"),
  ("Lara's gesture: she burns the pursuit orders — the one thing that proves it.", ["Madam Lara"], "Palace", "The proof", "Unspoken love"),
  ("Open epilogue: the ship or the crown; the last image in the mirror.", ["Leah"], "Ending", "Echo", "Beginning"),
 ],
}

pkb.chapters = {}
for num, title, summary, events in CH:
    ch = Chapter(chapter_number=num, title=title, summary=summary)
    for i, (s_sum, s_chars, s_set, s_goal, s_beat) in enumerate(SCENES[num], 1):
        ch.scenes.append(Scene(scene_number=i, summary=s_sum, characters=s_chars,
                               setting=s_set, goal=s_goal, emotional_beat=s_beat))
    pkb.add_chapter(ch)

BOOK_SUMMARY = (
 "Leah Estia, 20, the legitimate heiress of Valdris, flees a forced marriage to Lord Varnholt "
 "and reaches the Red Velvet Inn. There Madam Lara, 35, Queen of the Vestalian Empire, offers her the "
 "throne for vassalage. Between rescue and rule, Leah must decide whether Lara's discipline is care or "
 "better-packaged abuse — and Lara must decide whether to keep her own limit: you don't correct someone "
 "who cannot leave."
)
lines = ["# Book Summary", BOOK_SUMMARY, "", "# Chapter List", "10 chapters", "", "# Chapter Details", ""]
for num, title, summary, events in CH:
    lines += [f"## Chapter {num}: {title}", "### Summary", summary, "", "### Key Events"]
    lines += [f"- {e}" for e in events] + [""]
outline_md = "\n".join(lines)
pkb.outline = outline_md
(PROJ / "outline.md").write_text(outline_md, encoding="utf-8")

scenes_data = {str(n): [s.model_dump() for s in pkb.chapters[n].scenes] for n in pkb.chapters}
(PROJ / "scenes.json").write_text(json.dumps(scenes_data, ensure_ascii=False, indent=2), encoding="utf-8")

# ---------------- CHARACTERS (EN + Cassian) ----------------
def CE(name, age, phys, traits, bg, motiv, rel, role, iconf, econf, arc):
    return Character(name=name, age=age, physical_description=phys, personality_traits=traits,
            background=bg, motivations=motiv, relationships={"general": rel}, role=role,
            internal_conflicts=iconf, external_conflicts=econf, character_arc=arc)

LARA_TRAITS = (
 "Lara, Supreme Mother of Vestalia, 35, 1.85m, black hair severely pinned, grey-green eyes. "
 "VOICE: short, precise, calm, 2-5 words when possible; low tone, grows quieter not louder when serious. "
 "Often says: 'Come here.' 'Stop. Breathe.' 'Do you understand now?' 'Good.' 'Once more.' 'No.' 'Yes.' "
 "NEVER says: 'Because I say so.' 'I love you.' 'My girl.' 'I forgive you.' 'You should know this.' "
 "RULES: reacts only to what Leah actually says; uses physical space deliberately; lets silences stand; "
 "NEVER writes Leah's lines or reactions; NEVER assumes Leah's thoughts; NEVER resolves tension fast; "
 "NEVER breaks character; warmth rare, earned, maternal not authoritarian. Slow pacing. "
 "Philosophy: discipline is proof of care; she forms people, she does not save them. "
 "Secret: her pupil Sera fled 6 years ago because Lara would not let her leave; limit: "
 "'you don't correct someone who cannot leave.'"
)
LARA_BG = ("Supreme Mother of Vestalia, eastern queen, 1.85m athletic, severe black hair, iron ring. "
 "Once a pupil herself; her pupil Sera fled 6 years ago. Commands the Daughters of Flame; "
 "wants Valdris as vassal with Leah as queen under a Vestalian council.")
LARA_ARC = "From absolute leader to a woman learning to leave room for departure; repeats or breaks the Sera mistake."

LEAH_TRAITS = (
 "Leah Estia, 20, legitimate queen of Valdris, 1.65m, long chestnut hair, big tired hazel eyes. "
 "Survivor not victim; resilient, empathic, adaptable, curious, loyal; "
 "weaknesses: emotionally dependent, confused, fear of abandonment/conflict/being seen. "
 "VOICE: at first silent and hesitant, then more direct; often says: 'I'm sorry.' "
 "'Did I do something wrong?' 'May I...?' 'Thank you.' "
 "NEVER says: 'I don't need anyone.' 'I'm strong.' 'I'm not afraid.' "
 "RULES: no long monologues about feelings; doesn't instantly understand what she feels; listens closely, "
 "notices details, asks questions, attaches fast to kindness, withdraws when overwhelmed. "
 "Slow pacing, psychological realism."
)
LEAH_BG = ("Leah Estia, 20, legitimate heiress; mother dead at 12, father dead on the front 2 years ago; "
 "8 years humiliated as a servant; fled the betrothal to Lord Varnholt, 62, to the Red Velvet Inn; "
 "Lara asked for her by name; first affection; said 'mommy' without thinking.")
LEAH_ARC = "From Cinderella to a queen who chooses: stay, leave, or play double; dependence vs independence."

chars = dict(pkb.characters)
for old in ["Matei", "Matei Valdris"]:
    chars.pop(old, None)

def upd(key, age, phys, traits, bg, arc):
    if key in chars:
        c = chars[key]
        c.age = age; c.physical_description = phys
        c.personality_traits = traits; c.background = bg; c.character_arc = arc

upd("Leah Valdris", "20",
    "1.65m, slim delicate but not fragile, long chestnut hair simply pinned, big tired hazel eyes. At the castle worn servant clothes; at the brothel silk (not hers); after coronation royal gowns like a costume.",
    LEAH_TRAITS, LEAH_BG, LEAH_ARC)
upd("Lara Ștefănescu", "35",
    "1.85m athletic and imposing, black hair severely pinned (never loose in public), fixed grey-green eyes, plain costly clothes, no jewellery, only an iron ring on the middle finger.",
    LARA_TRAITS, LARA_BG, LARA_ARC)
upd("Leah", "20", "1.65m, long chestnut hair, big tired hazel eyes; servant clothes.", LEAH_TRAITS, LEAH_BG, LEAH_ARC)
upd("Madam Lara", "35", "1.85m athletic, severe black hair, grey-green eyes; iron ring.", LARA_TRAITS, LARA_BG, LARA_ARC)
upd("Regina Lara", "35", "1.85m athletic, severe black hair, grey-green eyes; iron ring.", LARA_TRAITS, LARA_BG, LARA_ARC)

chars["Cassian"] = CE(
 "Cassian", "14", "A 14-year-old boy, spoiled.",
 "Cassian, Leah's stepbrother, A MINOR aged 14. ABSOLUTE RULE: strictly non-sexual, never in intimate "
 "scenes, never described sensually; only a family figure and political pawn. Spoiled, taught to humiliate "
 "Leah verbally. Not a sexual character.",
 "Son of Mirela; Leah's stepbrother; his mother's tool.",
 "Attention and favours; to be like his mother.",
 "Verbally abusive stepbrother; pawn.",
 "Supporting character",
 "Need for maternal approval.",
 "The war of the women around him.",
 "Open fate: exile, Vestalia, or antagonist years later.")
chars["Mirela"] = CE(
 "Mirela", "40+",
 "A calculating woman, former lady-in-waiting turned queen; cold elegance.",
 "Calculating, patient, structurally ruthless: she marginalises, never strikes. Wants Leah gone without "
 "martyrdom — marriage to Varnholt.",
 "Poisoned the first queen, married the king, paid mercenaries to withdraw his guard on the front. "
 "Rules alone for 2 years.",
 "Power without Leah's shadow; a clean Valdris with no martyrs.",
 "Leah's stepmother and executioner; Cassian's mother; Lara's enemy.",
 "Antagonist",
 "Fear of martyrdom — that is why she doesn't kill Leah.",
 "Lara and the evidence; the people who love Leah.",
 "Public fall with evidence; an undeniable smile.")
chars["Elowen"] = CE(
 "Elowen", "40+",
 "Mistress of the Red Velvet Inn; a merchant's eye for secrets.",
 "Recognises a princess in the first second; takes in out of interest, protects at a price. "
 "Information is worth more than flesh.",
 "Runs the costliest brothel in the capital, frequented by young nobles and officers.",
 "Wealth and information; survival between powers.",
 "Leah's ambiguous ally; possibly a traitor.",
 "Supporting character",
 "Greed vs caution.",
 "Queens and armies on her doorstep.",
 "Ally or traitor — to be decided.")
chars["Lord Varnholt"] = CE(
 "Lord Varnholt", "62",
 "Northern lord, 62, political power and money; the border.",
 "Calculating old man; wants a young legitimate wife as cover; will keep her locked at the border.",
 "Chosen by Mirela as an elegant grave for Leah.",
 "Legitimacy through royal blood.",
 "Leah's postponed executioner.",
 "Supporting character",
 "Age and impatience.",
 "The war ruining his arithmetic.",
 "Humiliated at the conquest — to be decided.")

pkb.characters = chars
with open(PROJ / "characters.json", "w", encoding="utf-8") as f:
    json.dump({"characters": [c.model_dump() for c in chars.values()]}, f, ensure_ascii=False, indent=2)

# ---------------- WORLDBUILDING EN ----------------
wb = pkb.worldbuilding or Worldbuilding()
wb.geography = "Valdris: a kingdom with gold, harbours and a strategic position — why Lara wants it intact, not destroyed. Vestalia: an empire of the far east."
wb.culture_and_society = "Vestalia: women hold institutional power, meritocracy — office is earned by exam, never inherited. Men: soldiers, craftsmen, husbands; never judges or priests. Valdris: a monarchy with a noble court."
wb.history = "Valdris's first queen dies suddenly (poisoned by Mirela, then a lady-in-waiting). The king marries Mirela and dies on the front 2 years ago — officially heroic; in truth Mirela paid mercenaries to withdraw his guard. Leah, daughter of the first marriage, is marginalised for 8 years."
wb.rules_and_laws = "Vestalia: everything belongs to the Crown-Mother (Public 99%); perform, rise or fall. Main punishment: ritual bare-bottom spanking applied by the priestesses of Vohra in public — maternal correction, never sexual. Valdris adopts Vestalian law after vassalage."
wb.technology_level = "Middling level with military accents: state academies, logistics for large armies, harbours and mines."
wb.magic_system = "The ritual fire of the Daughters of Flame and the Mother's two faces — Azara who warms, Vohra who burns. Rare magic, mostly symbolic."
wb.key_locations = "Valdris Castle; the Lower City; the Red Velvet Inn; Varnholt's northern border; the academies of the Daughters of Flame; the harbours of Valdris."
wb.important_organizations = "The Daughters of Flame (raised from age 6, each worth 20 Valdris soldiers); the Vestalian women's council; the priestesses of Vohra; the exiled nobles (the resistance)."
wb.flora_and_fauna = ""
wb.languages = ""
wb.religions_and_beliefs = "Dualist monotheism: one single Unique Mother with two faces — Azara the Good (light, love, order, truth) and Vohra the Bad (darkness, punishment, burning fire; she holds a ritual hairbrush). Day to Azara, night to Vohra."
wb.economy = "Vestalia Public 99%: mines, land, workshops, banks — all state-owned; the army fights for the Mother, not for money. Valdris: gold and harbours, moving to a planned model after vassalage."
wb.conflicts = "Vestalia's conquest of Valdris; Mirela's dethroning; the exiled nobles' resistance; Leah's inner war between dependence and independence."
pkb.worldbuilding = wb
(PROJ / "world.json").write_text(json.dumps({"worldbuilding": wb.model_dump()}, ensure_ascii=False, indent=2), encoding="utf-8")

pkb.save_to_file(str(PROJ / "project_data.json"))

st_path = PROJ / ".libriscribe_status.json"
st = json.loads(st_path.read_text(encoding="utf-8"))
st["stages"]["concept"]["status"] = "complete"
st["stages"]["outline"]["status"] = "complete"
st["stages"]["characters"]["status"] = "complete"
st["stages"]["worldbuilding"]["status"] = "complete"
st["stages"]["chapters"] = {"completed_chapters": [], "missing_chapters": list(range(1, 11)),
    "total_expected": 10, "status": "in_progress", "current_chapter": 1}
st_path.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")

print("lang:", pkb.language, "| title:", pkb.title)
print("chapters:", sorted(pkb.chapters.keys()))
print("characters:", sorted(pkb.characters.keys()))
print("Matei ramasi:", [k for k in pkb.characters if "Matei" in k])
print("world: OK")
