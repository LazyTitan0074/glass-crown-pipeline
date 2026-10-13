import sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"

def rep(n, old, new):
    p = P % n
    t = open(p, encoding="utf-8").read()
    cands = [old]
    for a, b in [("'", "\u2019"), ('"', "\u201c"), ('"', "\u201d")]:
        cands.append(cands[-1].replace(a, b) if a == "'" else cands[0].replace('"', "\u201c").replace('"', "\u201d"))
    seen = []
    for c in dict.fromkeys(cands):
        k = t.count(c)
        seen.append(k)
        if k == 1:
            open(p, "w", encoding="utf-8").write(t.replace(c, new, 1))
            print("ch%d OK: %s" % (n, new[:60]))
            return
    print("ch%d MISS: %s counts=%s" % (n, old[:60], seen))

ED = [
 (5, "Leah's breath hitched. \"You're not waiting.\"", "Leah's stomach dropped. \"You're not waiting.\""),
 (8, "It was *fear*. |  | Leah's breath hitched.", "It was *fear*. |  | Something in her chest cracked."),
 (8, "*\"Good,\"* Lara said. |  | Leah's breath hitched.", "*\"Good,\"* Lara said. |  | Leah's shoulders dropped."),
 (9, "Leah's breath hitched. \"I\u2014\"", "Leah swallowed. \"I\u2014\""),
 (5, "Leah's breath caught. \"You\u2014\"", "Leah's mind blanked. \"You\u2014\""),
 (8, "Leah's breath caught. |  | She had not thought this far.", "Her stomach turned over. |  | She had not thought this far."),
 (5, "Leah's throat burned. \"But\u2014\"", "Leah's voice frayed. \"But\u2014\""),
 (7, "Leah's throat tightened. \"I\u2014\"", "The words stuck. \"I\u2014\""),
]
# normalize the pipe separators: dump used " |  | " for paragraph breaks (\n\n)
ED2 = []
for n, o, w in ED:
    ED2.append((n, o.replace(" |  | ", "\n\n"), w.replace(" |  | ", "\n\n")))
for n, o, w in ED2:
    rep(n, o, w)
print("retry done")
