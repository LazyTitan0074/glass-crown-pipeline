import re, sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"
for n in (3, 5, 7):
    t = open(P % n, encoding="utf-8").read()
    print("=== ch%d ===" % n)
    for m in re.finditer(r"Scene \d+:.*\n", t):
        print(repr(t[m.end():m.end() + 220]))
