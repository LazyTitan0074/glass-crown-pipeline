# STRICT REVIEW — The Glass Crown (v1 manuscript)
**Format: machine-actionable repair sheet. Severity tags per line. Fix instructions direct, no hedging.**

---

## 1. BLOCKERS — CANON VIOLATIONS (must fix before next pass)

**B1 | Ch5 S1 | C02 — CHRONOLOGY ERROR**
> "And beneath it, in Mirela's looping script, the date of her death. *Twelve years ago.*"

Leah is 20 (C01). Elara died when Leah was 12 (C01, Ch1 S3 confirms). Difference = **8 years**, not 12.
**FIX:** Replace "Twelve years ago" → "Eight years ago." Run a global grep for "twelve" across all chapters to catch echoes.

**B2 | Ch3 S4 | C12 STAGING VIOLATION**
> "Some say they serve a Mother with two faces, one that warms, one that burns."

Staging rule (JURNAL, C12): "Mother of Two Faces" theology is allowed **only from Ch4 onward**. Ch1–2 restricted to "a host in the east"; Ch3 restricted to distant mentions of "Vestalia"/"Daughters" *without theology*.
**FIX:** Rewrite the merchant's line to omit "Mother with two faces." Keep "Daughters of Flame" and "crimson banners." Cut "one that warms, one that burns" entirely. Reroute the theology to Ch4 S4 (Lara's reveal) or later.

**B3 | Ch8 S3 | C12/UNIVERSE NEW FACT**
> "The words were in Vestalian, but Leah understood the rhythm."
> "You are the daughter of the Mother. You are the heir of the flame."

Two violations:
(a) "Vestalian" as a distinct language is **not declared** in CANON.md. If it exists, add as C20 or remove.
(b) "Heir of the flame" — Leah is heir of **Valdris**, not Vestalia's flame. The ceremony is her coronation over Valdris, not her adoption into the Vestalian line (which happens later per C18).
**FIX:** Either (i) declare Vestalian as a language in CANON and rewrite to "The words were in a tongue she did not know, but the rhythm carried" — OR (ii) cut the language reference entirely. Replace "heir of the flame" → "heir of Valdris, keeper of the glass crown." Rerun canon_check.

**B4 | Ch4 S1 (opening paragraph) | VOICE.md POV VIOLATION**
> "She had seen Leah the moment the princess slipped through the curtained entrance two nights past—a quiet figure with chestnut hair and tired hazel eyes, weary from some unspoken burden. The innkeeper had taken her in, offered shelter in exchange for silence, a debt she would collect in due time."

This is **Elowen's interiority**. VOICE.md: "3rd person LIMITED on Leah, PAST tense, throughout. No head-hopping (Lara's POV never)."
**FIX:** Rewrite the opening paragraph in Leah-lens only. Elowen's thoughts must be inferred from observable behavior (posture, tone, gesture). Suggested rewrite: start with Leah descending the stairs, seeing Elowen behind the bar, noticing Elowen's hands pause, her gaze shift. Cut all access to Elowen's interior state.

**B5 | Ch9 S4 (whole scene) | STRUCTURAL / POV**
The scene titled "The Exiled Nobles' Message" contains two irreconcilable sections:
- Section (a): The message arrives, Leah considers fleeing. One night.
- Section (b): A retrospective essay titled "The changes began with the smallest things" (bedchamber, food, clothes, guards). Written in an essayistic, past-perfect register with no in-scene action.

**FIX:** Split into two scenes OR delete section (b) and fold its content (the changes Lara has imposed) into earlier chapters where they naturally occur. Section (b) breaks scene continuity (Leah is mid-decision about the exiles' ship; the "changes" are implied to have happened over weeks).

---

## 2. MAJOR — CONTINUITY & STRUCTURAL

**M1 | Ch6 S3 | LOCATION CONTRADICTION WITHIN SAME SCENE**
- Opens: "The suite was stifling. Leah sat on the edge of the bed..."
- Mid-paragraph: "She had spent the last hour in the archives, poring over ledgers that had been locked away for decades."
- Then: "She had traced them in the dark... They led to the old queen's chambers, the ones where Elara had died."
- Then: "A knock at the door... 'Supreme Mother sends her regards.'"

Three locations (suite, archives, castle tunnels) in one undifferentiated scene. Thematically strong material, structurally chaotic.
**FIX:** Split into 2–3 scenes with explicit transitions (location header or narrative beat). "Archives" cannot exist at the Red Velvet Inn — if the archives are in the Valdris castle, that transition must be written. If they are Leah's *memory* of the archives from before she fled, mark clearly.

**M2 | Ch5 S1 vs Ch7 S5 | SIGIL INCONSISTENCY**
- Ch5 S1: "two flames, crimson and gold, locked in eternal opposition"
- Ch7 S5: "the two-faced sigil—Azara's light, Vohra's shadow"
- Ch9: "double-faced goddess"

The Vestalian state sigil is described two different ways.
**FIX:** Standardize. Recommend **two-faced** sigil (consistent with C12's monotheistic dual-face theology). Replace Ch5 S1 "two flames" → "a single face split by a vertical line, half-lit, half-shadowed." Register the canonical sigil in CANON.md as a new sub-clause under C12 or C14.

**M3 | Ch8 S3 | CROWN DESCRIPTION INTERNAL CONTRADICTION**
> "She had never worn a crown before. Not even as a child..."
> "The crown was heavier than she imagined, and cold. Not gold — Lara's doing, she understood later: rock crystal, glass-clear, cut so it caught the light and threw it back in pieces."
> "One of the priestesses placed the last jewel into place."

(a) No jewels were previously mentioned on the crown — it's described as crystal/glass. "Placed the last jewel into place" introduces a fact not established.
(b) "she understood later" — this POV retrojection breaks the scene's past-tense present. It's Leah narrating from a future vantage point.
**FIX:** Delete "One of the priestesses placed the last jewel into place." Replace with an action consistent with a plain glass/crystal crown: "One of the priestesses set the circlet on her brow, and the cold spread down her forehead to her temples." Cut "she understood later" — relocate the Lara-caused-glass explanation to Ch9 S2 (where Leah explicitly examines the crown) or to Ch10.

**M4 | Ch9 S2 | INTERNAL CONTRADICTION — CROWN POSITION**
> "The glass diadem resting on the table between them."
> "...leaving Leah standing there, the weight of the crown pressing down on her, the weight of the words echoing in her mind."

Same paragraph: crown is on the table AND pressing down on her (i.e., on her head). Pick one.
**FIX:** If the crown is on the table, cut "the weight of the crown pressing down on her." Replace with: "...leaving Leah standing there, the cold of the table's edge against her thigh, the weight of the words echoing in her mind." If she is wearing the crown, remove "resting on the table" earlier.

**M5 | Ch7 S4 | BEAT SHEET MISMATCH — "First Correction"**
Title of scene: "Lara Corrects Her for the First Time."
BEAT_SHEET Ch7 S4: "First correction under Vestalian rules (personal level; political disagreement NEVER punished personally)."

What actually occurs: Lara tells Leah to sit, Lara commands "rest," Lara gently instructs "you will not argue." No physical discipline. No formalized Vestalian correction.
**FIX:** Either retitle to something like "The First Rule" — OR insert an actual (non-sexual, consensual, canonical) correction moment consistent with C13's ritual framework and BEAT_SHEET's "discipline-context only" intimacy note. Do not preserve a title that promises something the scene does not deliver.

**M6 | Ch10 S4 | TENSE ERROR IN FINAL ACTION**
> "Lara picked up the first sheet. Held it over the candle. Watched it catch, curl, blacken, and drop it into the brazier."

"drop it" — dropped by whom? The subject is Lara "watched it." The final "it" is the parchment; but "watched it... and drop it" mixes intransitive (it drops) with transitive (she drops it). Grammatically broken.
**FIX:** "...Watched it catch, curl, blacken, and fall into the brazier." OR "...Watched it catch, curl, blacken; then she let it drop into the brazier."

---

## 3. MINOR — REPETITION, STYLE, FORMATTING

**m1 | Global | SCENE TITLES IN PUBLISHED PROSE**
Headers like "#### Scene 1: The Servants' Wing" are beat-sheet artifacts, not novel-ready formatting.
**FIX:** Strip all scene titles. Replace each with a simple scene break: a single centered asterisk or a triple blank line.

**m2 | Ch4 S1 | REPETITION WITHIN SAME SCENE**
> "The heavy oak doors at the far end groaned open" appears twice in the same scene with nearly identical phrasing.
**FIX:** Vary the second instance. Change to "The doors swung inward" or similar.

**m3 | Ch6 S4 & Ch7 S4 | REPEATED SENSORY OPENING**
Both scenes open with: "The suite smelled of burnt sugar and old parchment..."
**FIX:** Change one. Ch7 S4 → "The suite held the ghost of last night's wine..." or similar.

**m4 | Ch8 S2 & Ch8 S3 | REPEATED OPENING PHRASE**
Ch8 S2: "The throne hall was too bright."
Ch8 S3: "The square was too bright."
**FIX:** Change Ch8 S3 opening to "The sun hammered the square without mercy..." or similar.

**m5 | Global | PURPLE PROSE (VOICE.md: "no purple, no metaphysics lectures")**
- Ch6 S4: "The ledger's spine creaked like a dying man's breath."
- Ch7 S2: "Lara's voice was a blade unsheathed and then sheathed again."
- Ch8 S3: "a sickly, sickly gold" — duplication.
**FIX:** Replace each with a leaner concrete image. Suggested: Ch6 S4 → "The ledger's spine cracked." Ch7 S2 → "Lara spoke quietly, each word placed." Ch8 S3 → "a sickly gold" (single word).

**m6 | Global | REPEATED KEYWORDS**
Frequency check needed on:
- "sandalwood" (used as atmospheric default in most suite scenes)
- "amber" (correct for Elowen per C07, but check density)
- "the weight of" (used in Ch5 S1, Ch6 S4, Ch9 S2, Ch9 S4, Ch10 S4)
- "the air smelled of"
**FIX:** Reduce "sandalwood" to 2–3 total instances. Replace "the weight of the crown/words" with varied concrete images in 2 of 5 occurrences.

**m7 | Ch8 S4 | PARENTHESES IN FICTION PROSE**
> "his fine (but clearly ill-fitting) valet's coat"
**FIX:** Rewrite without parentheses. E.g., "his fine valet's coat, clearly ill-fitting."

**m8 | Ch3 S4 vs Ch5 S1 | LEDGER DESCRIPTION CONTRADICTION**
Ch5 S1 describes Mirela's ledger as "yellowed, ink smudged as if written in haste" — but elsewhere Mirela's handwriting is characterized as "precise, measured" (Ch1 S2). Hmm — Ch1 S2 in current manuscript is human-written; verify whether "precise, measured" exists there. If yes → contradiction stands.
**FIX:** Change to "yellowed, ink carefully blotted but uneven in places, as if the writer had paused too long between words" — this preserves tension while staying consistent with Mirela's control.

**m9 | Ch10 S4 | MIXED SPELLING**
"colour" (British) appears alongside (throughout the manuscript) American-English defaults (no visible "gray," but "realize" and "color" usage needs checking).
**FIX:** Run a single variant standard. Given genre and reader base, **US English** is recommended. Global replace: colour→color, rumour→rumor, neighbour→neighbor.

**m10 | Ch10 S3 | IMPRECISE REFERENCE**
> "she had once fled uphill in the opposite direction — servant girl running from a wedding"
She fled from a **betrothal contract**, not a wedding. Reframe.
**FIX:** "servant girl running from a betrothal" or "running from a signature."

**m11 | Ch8 S1 | DESCRIPTION ODDITY**
"the Red Velvet Inn's shutters" — the Inn's interior scenes have never established shutters. Also, Ch8 S1 is the farewell scene; Leah has been at the Inn for a while; place consistency matters.
**FIX:** Verify location. If the farewell happens at the Inn, ensure the Inn's actual layout (established Ch1 S5, Ch2 S1) supports a window with shutters onto dawn.

---

## 4. VOICE-LENS RE-AUDIT

Run the following audit programmatically:
For every paragraph, extract the grammatical subject of interior verbs ("thought", "felt", "remembered", "knew", "understood", "wanted").

Every interior verb must have **Leah** as subject.
Permitted exceptions:
- Dialogue attributions with sensory verbs ("Lara said", "Elowen poured").
- Observable behavior ("Lara's hand tightened", "her jaw set").

Known violations (already flagged in §1 B4):
- Ch4 S1 first paragraph — Elowen interiority (BLOCKER).

Suspect paragraphs (verify manually):
- Ch3 S1: "Elowen's gaze flicked to Leah's face, then softened. 'Your body speaks in signals you've never been taught to read.'" — the softening is observable, but the paragraph pivots between Elowen-observable and Leah-interior without clear marking. Acceptable, but tighten.
- Ch6 S2: "Her voice was low, measured. 'You do not ask for what you need.'" — attribution, not interior. Acceptable.

---

## 5. BEAT SHEET COMPLIANCE AUDIT

Ch1 → 5 scenes required, delivered 5. ✓
Ch2 → 4 scenes required, delivered 4. ✓
Ch3 → 4 scenes required, delivered 4. ✓
Ch4 → 4 scenes required, delivered 4. ✓ (Ch4 S3 explicit scene — required by C08/C09, present.)
Ch5 → 4 scenes required, delivered 4. ✓
Ch6 → 4 scenes required, delivered 4. ✓
Ch7 → 5 scenes required (Night conditions list / Table I / Table II / First correction / Half-signed accord + Elowen farewell), delivered 5. ✓ **BUT** Ch7 S4 mismatch (see M5).
Ch8 → 5 scenes required (Gates/Spies / Mirela exposed + private crack / Coronation / Nobles kneel or exile / Cassian humanizing), delivered 4. **MISSING: Mirela's "private crack" beat** (Ch8 S2 does not include her smile-that-doesn't-reach-eyes beat required by BEAT_SHEET Ch8 S2). **Also missing: Cassian's unguarded child moment** (BEAT_SHEET Ch8 S5: "one unguarded child moment (fear, not cruelty; NO redemption, NO forgiveness scene)"). Current Ch8 S4 has Cassian present but not the humanizing beat.
**FIX:** Add Ch8 S2 beat: Mirela's public exposure includes one private smile that doesn't reach her eyes. Add Ch8 S5 (or extend Ch8 S4): a single unguarded Cassian beat — fear, hesitation, not cruelty. Keep brief (1 paragraph max). No redemption scene.

Ch9 → 5 scenes required (Council / Correction while she can't leave / Sera named / Exiles' offer / Dependence tally), delivered 4. **MISSING: explicit dependence tally scene.** Current Ch9 ends at the exiles' offer; the tally (financial, emotional, physical) is not shown.
**FIX:** Add Ch9 S5: brief, concrete tally. Could be Leah physically checking her purse, her escape routes, the guards at the door. Consistent with C17 test.

Ch10 → 5 scenes required (Bag packed/unpacked / "If I leave" question / Choice / Lara burns orders / Open epilogue), delivered 4. **MISSING: explicit epilogue beat** (BEAT_SHEET Ch10 S5: "Open epilogue: ship or crown; mirror image"). Current Ch10 S4 ends the burn but doesn't deliver the mirror image.
**FIX:** Add Ch10 S5: short mirror epilogue — two images: the ship sailing into dark, and Leah returning to the lit window. No explanation. End.

---

## 6. NAME-GUARD VERIFICATION

Forbidden minor-character names (per C16): Mira, Vela, Elara, Lara, Leah, Mirela, Cassian, Varnholt, Elowen.

Full grep required. Known risk points:
- Ch3 S2: "Lord Halvard" — legal (not on list). But is this intentional world-building? Verify against CANON.
- Ch7 S4: "Mira" is not used as a servant/priestess (verified in current manuscript, ✓).
- Ch8 S3: "One of the priestesses" — no name given (✓ — the journal flagged and fixed the earlier "Mira" collision).
- Global check needed for "Sera" — canonical rule (C15): "Name Sera ONLY in ch9, ONLY in Lara-context scenes." Verify no echoes in Ch1–8 or Ch10.

**FIX:** Run a scripted grep for the forbidden name set + Sera across all 10 chapters. Report any hit outside its allowed chapter.

---

## 7. TENSE CONSISTENCY AUDIT

VOICE.md: "3rd person LIMITED on Leah, PAST tense, throughout."

Verify all narrative prose is past tense. Known deviations:
- Ch9 S4 essay-section drifts into retrospection with present-implications ("The changes began", "She had slept here for years").
- Ch8 S3: "she understood later" — past, but with future-retrojection.

**FIX:** Standardize on past tense with strict contemporaneous limitation. Delete "she understood later" constructions. Convert Ch9 S4 essay prose into either (a) an in-scene moment of examination (Leah noticing the room Lara has changed) OR (b) append to Ch10 as part of the tally.

---

## 8. INTIMACY-SCENE AUDIT (C08/C09)

Ch4 S3 must include, per C08: light touch (arm, throat), explicit consent line ("No one touches you here without your consent. Not even me"), slow kiss, leads to bed.

Verify all present in Ch4 S3, and that the "mommy" line occurs unthinkingly (subspace), not performed.

**FIX (if not present):** Insert consent line if missing. The current text has "No one touches you here without your consent. Not even me. Do you understand?" — present ✓. Verify "mommy" line lands unthinkingly (current: "escaped before she could stop it: 'Mommy.'"). ✓.

Ch2 S2 must contain pre-Lara client: young, rushed, clumsy, never tends to her pleasure. ✓ verified.

Ch2 S1 must contain Elowen's rule: "young ones only, no violent, no old" + "Half share minus room/board" + "Your body is yours here." ✓ verified.

---

## 9. FINAL PRODUCTION CHECKLIST

Before submitting to any publication pipeline:

- [ ] Apply all BLOCKERS (§1) — no exceptions.
- [ ] Apply M2, M3, M4, M5, M6 (structural/continuity).
- [ ] Strip scene titles (§m1).
- [ ] Run US-English variant standardization (§m9).
- [ ] Run name-guard grep (§6).
- [ ] Run POV audit (§4).
- [ ] Run tense consistency (§7).
- [ ] Insert missing BEAT_SHEET beats: Ch8 S2 (Mirela crack), Ch8 S5 (Cassian humanizing), Ch9 S5 (dependence tally), Ch10 S5 (open epilogue).
- [ ] Re-run `canon_check.py` against CANON.md v4 (19 facts C01–C19) — target 0 abateri.
- [ ] Rebuild EPUB after edits (do not regenerate from scratch; patch the assembled manuscript to preserve human-written chapters).
- [ ] Update `JURNAL.md` with repair pass summary and new registry hash.

---

## 10. WHAT NOT TO TOUCH

The following are the manuscript's strongest assets and should not be "improved" by the repair system:

- All Lara voice lines. They are canonical and consistent.
- All Elowen amber-eyes/mahogany-hair mentions (C07 compliance).
- Ch1 S1's "He never touched her. He didn't need to." — master-class C05 compliance line.
- Ch4 S3's explicit consent line — load-bearing.
- Ch9 S3 (Lara's Sera confession + "Sit with me." / "No.") — this is the book's thesis scene.
- Ch10 S2 (the "If I leave, will you let me?" exchange) — canonical test of C17.
- The final line: "Let it sail. She had somewhere to be."

---

**End of repair sheet. Estimated repair pass: 6–10 hours of directed editing (mostly §1 and §5). Do not regenerate chapters — patch in place.**
