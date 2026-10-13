import sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"
cache = {}

def rep(n, old, new):
    p = P % n
    t = cache.get(n)
    if t is None:
        t = open(p, encoding="utf-8").read()
    cands = [old, old.replace("'", "\u2019"), old.replace("\u2019", "'")]
    for c in cands:
        if t.count(c) == 1:
            t = t.replace(c, new, 1)
            cache[n] = t
            open(p, "w", encoding="utf-8").write(t)
            print("ch%d OK: %s" % (n, new[:60]))
            return
    print("ch%d MISS/SKIP: %s (counts=%s)" % (n, old[:60], [t.count(c) for c in cands]))

EDITS = [
 (5, "Leah's breath hitched. \"You're not waiting.\"", "Leah's stomach dropped. \"You're not waiting.\""),
 (6, "Leah's breath hitched.\n\n*\"Two hundred and seventy-three thousand,\"*", "Leah went very still.\n\n*\"Two hundred and seventy-three thousand,\"*"),
 (6, "Her breath hitched. She pressed a hand to her chest", "Her breathing went shallow. She pressed a hand to her chest"),
 (7, "Leah's breath hitched. *\"What does that mean?\"*", "Leah's chest tightened. *\"What does that mean?\"*"),
 (7, "Leah's breath hitched. *\"That is not what I\u2014\"*", "Leah flinched. *\"That is not what I\u2014\"*"),
 (7, "Leah's breath hitched. She had never been told what to do like this before.", "Something cold settled in her stomach. She had never been told what to do like this before."),
 (8, "Leah's breath hitched. *Vestalia's mark.*", "Leah's fingers closed around it. *Vestalia's mark.*"),
 (8, "It was *fear*. |  | Leah's breath hitched.", "It was *fear*. |  | Something in her chest cracked."),
 (8, "*\"Good,\"* Lara said. |  | Leah's breath hitched.", "*\"Good,\"* Lara said. |  | Leah's shoulders dropped."),
 (9, "Leah's breath hitched. She had been called worse.", "It landed harder than any insult. She had been called worse."),
 (9, "Leah's breath hitched. \"I\u2014\"", "Leah swallowed. \"I\u2014\""),
 (9, "Her breath hitched. *\"I understand.\"*", "Cold spread through her fingers. *\"I understand.\"*"),
 (9, "Leah's breath hitched. *\"What if I'm not strong enough?\"*", "Her eyes burned. *\"What if I'm not strong enough?\"*"),
 (5, "Leah's breath caught. \"You\u2014\"", "Leah's mind blanked. \"You\u2014\""),
 (7, "Her heart stuttered. She had not expected that. She had expected *no*, or *why*", "DUP-PLACEHOLDER"),
]
for n, o, w in EDITS:
    if w != "DUP-PLACEHOLDER":
        rep(n, o, w)

EDITS2 = [
 (7, "Leah's breath caught. She had not expected that. She had expected *no*, or *why*, or the slow dismantling", "Her heart stuttered. She had not expected that. She had expected *no*, or *why*, or the slow dismantling"),
 (7, "Leah's breath caught. She had not expected that. She had expected *yes*", "The truth of it winded her. She had not expected that. She had expected *yes*"),
 (7, "Leah's breath caught. *\"Why not?\"*", "The question came out small. *\"Why not?\"*"),
 (7, "Leah's breath caught. *\"Understand what?\"*", "Her hands went still. *\"Understand what?\"*"),
 (8, "Leah's breath caught. |  | She had not thought this far.", "Her stomach turned over. |  | She had not thought this far."),
 (5, "Leah's fingers tightened around the goblet.", "Leah's knuckles whitened around the goblet."),
 (6, "Leah's fingers tightened around the ledger in her lap.", "Leah pressed the ledger flat against her knees."),
 (6, "Leah's fingers tightened around the ledger.", "Leah's hold on the ledger hardened."),
 (7, "Leah's fingers tightened around the paper.", "The paper creased in her grip."),
 (8, "Leah's fingers tightened around the coin.", "Leah's hand closed around the coin."),
 (8, "Leah's fingers tightened around the fabric of her gown.", "Leah twisted a fold of her gown."),
 (5, "Leah's throat burned. \"But\u2014\"", "Leah's voice frayed. \"But\u2014\""),
 (5, "Leah's throat tightened. She thought of the ledgers", "Her chest ached. She thought of the ledgers"),
 (7, "Leah's throat tightened. \"I\u2014\"", "The words stuck. \"I\u2014\""),
 (9, "Leah's voice was steady, but her throat burned.", "Leah's voice was steady, but thinning."),
 (9, "Leah's throat tightened. *\"I\u2014\"*", "The words came out frayed. *\"I\u2014\"*"),
 (6, "Leah's pulse hammered in her throat.", "Her heart knocked against her ribs."),
 (6, "Her voice was steady, but her pulse roared in her ears.", "Her voice was steady, but blood beat in her ears."),
 (6, "Leah's pulse roared in her ears. She had her first crack.", "Her pulse quickened. She had her first crack."),
 (8, "Leah's pulse hammered in her throat.", "Dread pooled low in her belly."),
 (4, "The suite smelled of beeswax and aged wine", "The suite smelled of honeyed wax and aged wine"),
]
for n, o, w in EDITS2:
    rep(n, o, w)
print("trim batch done")
