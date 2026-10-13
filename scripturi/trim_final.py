import sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"
ED = [
 (5, "Leah\u2019s breath hitched. \u201cYou\u2019re not waiting.\u201d", "Leah\u2019s stomach dropped. \u201cYou\u2019re not waiting.\u201d"),
 (5, "Leah\u2019s throat burned. \u201cBut\u2014\u201d", "Leah\u2019s voice frayed. \u201cBut\u2014\u201d"),
 (5, "Leah\u2019s breath caught. \u201cYou\u2014\u201d", "Leah\u2019s mind blanked. \u201cYou\u2014\u201d"),
 (8, "It was *fear*.\n\nLeah\u2019s breath hitched.", "It was *fear*.\n\nSomething in her chest cracked."),
 (8, "*\"Good,\"* Lara said.\n\nLeah\u2019s breath hitched.", "*\"Good,\"* Lara said.\n\nLeah\u2019s shoulders dropped."),
 (8, "Leah\u2019s breath caught.\n\nShe had not thought this far.", "Her stomach turned over.\n\nShe had not thought this far."),
 (9, "Leah\u2019s breath hitched. \u201cI\u2014\u201d", "Leah swallowed. \u201cI\u2014\u201d"),
 (7, "Leah\u2019s throat tightened. \u201cI\u2014\u201d", "The words stuck. \u201cI\u2014\u201d"),
]
for n, o, w in ED:
    p = P % n
    t = open(p, encoding="utf-8").read()
    assert t.count(o) == 1, (n, o[:60], t.count(o))
    open(p, "w", encoding="utf-8").write(t.replace(o, w, 1))
    print("ch%d OK" % n)
print("trim complete: 36/36")
