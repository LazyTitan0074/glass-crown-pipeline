import json
from pathlib import Path
A = Path(r"C:\Users\bizoi\roman")

# ---------- characters.json ----------
cp = A / "characters.json"
d = json.loads(cp.read_text(encoding="utf-8"))
chars = d.get("characters", [])
keep = []
seen = set()
for c in chars:
    n = (c.get("name") or "").strip()
    nl = n.lower().replace("\u0219", "s").replace("\u015f", "s")
    if nl in ("leah valdris", "lara stefanescu", "regina lara"):
        continue
    if nl in seen:
        continue
    seen.add(nl)
    keep.append(c)

out = []
for c in keep:
    s = json.dumps(c, ensure_ascii=False)
    s = s.replace("Matei", "Cassian").replace("Sorina", "Mira")
    c = json.loads(s)
    n = c.get("name", "")
    if "radu" in n.lower():
        continue
    rel = c.get("relationships", {})
    g = json.dumps(rel, ensure_ascii=False)
    if "Radu" in g or "radu" in g.lower():
        rel["general"] = "At the Red Velvet Inn she learns from the older girls; information is worth more than flesh."
        c["relationships"] = rel
    if n == "Elowen":
        c["physical_description"] = "Mistress of the Red Velvet Inn; mahogany hair, amber eyes (locked). A merchant's eye for secrets."
        c["character_arc"] = "Paid off after vassalage; the brothel continues as a Vestalian info asset. Leah never returns, never forgets."
    if n == "Madam Lara":
        c["physical_description"] = "1.85m athletic and imposing, black hair severely pinned (never loose in public), fixed grey-green eyes, plain costly clothes, no jewellery, only an iron ring on the middle finger. Supreme Mother of Vestalia."
        pt = c.get("personality_traits", "")
        if "NEVER says" in pt and "Sera" not in pt:
            c["personality_traits"] = pt + " Limit: 'you don't correct someone who cannot leave' (Sera fled 6 years ago; name Sera ONLY in ch9 Lara-context)."
    if n == "Leah":
        m = c.get("motivations", "")
        if isinstance(m, str) and "Matei" in m:
            c["motivations"] = m.replace("Matei", "Cassian")
    out.append(c)
d["characters"] = out
cp.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print("characters.json:", [c.get("name") for c in out][:20], "n=", len(out))

# ---------- world.json ----------
wp = A / "world.json"
w = json.loads(wp.read_text(encoding="utf-8"))
wb = w.get("worldbuilding", {})
wb["geography"] = "Valdris: gold, harbours, strategic position — kept intact as perfect vassal, keeps its flag. Vestalia: empire of the far EAST."
wb["culture_and_society"] = "Vestalia: women hold institutional power, meritocracy by exam never inherited. Men: soldiers, craftsmen, husbands; never judges or priests. Lara's values: Discipline, Love, Tradition, Maternal Authority. Title: Supreme Mother."
wb["rules_and_laws"] = "Vestalia: everything belongs to the Crown-Mother (Public 99%); perform, rise or fall. Main punishment: ritual spanking applied publicly by priestesses of Vohra — maternal correction, never sexual. After vassalage: available, not mandatory."
wb["religions_and_beliefs"] = "One Unique Mother, two faces: Azara the Good (light, love, order, truth; warming fire) and Vohra the Bad (same goddess, harsh face: darkness, punishment, burning fire; ritual hairbrush in right hand; not a devil). Day to Azara, night to Vohra."
wb["economy"] = "Vestalia Public 99%: mines, land, brothels, workshops, banks — all state-owned; army fights for Mother not money. Valdris moves to planned model after vassalage."
wb["conflicts"] = "Vestalia's conquest of Valdris; Mirela's dethroning with murder evidence; exiled nobles' resistance (old nobility, not commoners); Leah's dependence-vs-independence war; Lara's test: can she let go."
wb["key_locations"] = "Valdris Castle; Lower City; Red Velvet Inn (later Vestalian info asset); Varnholt's NORTHERN border; academies of the Daughters of Flame; harbours of Valdris."
wb["important_organizations"] = "Daughters of Flame (raised from 6, each ~20 Valdris soldiers; '1 million' is propaganda); Vestalian women's council (Mira, Vela envoys ch5); priestesses of Vohra; exiled nobles (resistance)."
wb["relevant_data"] = "Vestalian values: Unitary 64, Autocracy 81, Security 68, Assimilation 61, Pacifist 31, Nationalist 77, Public 99, Planning 57, Globalism 70, Religious 53, Traditionalist 83, Technology 58."
w["worldbuilding"] = wb
wp.write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding="utf-8")
print("world.json patched")

# ---------- scenes.json ----------
sp = A / "scenes.json"
sc = json.loads(sp.read_text(encoding="utf-8"))
# ch2 scene2 harden C09
sc["2"][1]["summary"] = "The first young client, rushed and clumsy, never tending to her pleasure; Leah frightened, but her body is hers for the first time (performs, does not feel)."
# ch3 scene1 harden
sc["3"][0]["summary"] = "Leah learns her body's responses with rushed clients who care nothing for her pleasure; curiosity and shame; nobody tends to her pleasure yet."
# ch4 scene2-3 consent + subspace beats
sc["4"][1]["summary"] = "In the luxury suite, Lara calms her with wine and light touch, states no one touches her without consent; Leah relaxes for the first time."
sc["4"][2]["summary"] = "Consensual intimate scene between adults (explicit allowed, always consensual); first time anyone tends to her pleasure; subspace, 'mommy' slips out unthinking."
# ch5 Mira fix (was 'Mira and Vela' vs Sorina mix)
sc["5"][0]["summary"] = "Lara spreads map and evidence: Queen Elara's poison, the mercenaries' payment. Two Vestalian women, Mira and Vela of the proposed future council, attend as living proof."
for k in ("1", "2"):
    for s in sc["5"]:
        chars = s.get("characters", [])
        chars = ["Mira" if x == "Sorina" else x for x in chars]
        s["characters"] = chars
# ch7-9 discipline + Sera rules
sc["7"][3]["summary"] = "Lara corrects her for the first time under Vestalian rules (maternal correction, consensual personal level; political disagreement never punished by personal withdrawal)."
sc["9"][1]["summary"] = "Correction under Vestalian rules; Leah feels kept, not formed — the two-levels rule breaks (tested here)."
sc["9"][2]["summary"] = "Lara and Sera's shadow (Sera named ONLY here): 'you don't correct someone who cannot leave' — yet she continues."
sp.write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding="utf-8")
print("scenes.json patched")
