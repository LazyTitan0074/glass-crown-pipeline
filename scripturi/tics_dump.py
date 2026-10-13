import re, sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"
C = {n: open(P % n, encoding="utf-8").read() for n in range(1, 11)}
pats = [r"breath hitched", r"breath caught", r"suite smelled", r"smelled of",
        r"fingers tightened", r"throat (tightened|closed|burned)",
        r"pulse (hammered|roared)"]
out = []
for n in range(1, 11):
    for pat in pats:
        for m in re.finditer(pat, C[n], re.I):
            out.append("ch%d @%d :: %s || %s" % (n, m.start(), pat, C[n][max(0, m.start()-140):m.end()+140].replace("\n", " | ")))
open(r"C:\Users\bizoi\roman\tics_dump.txt", "w", encoding="utf-8").write("\n\n".join(out))
print("dumped", len(out), "occurrences")
