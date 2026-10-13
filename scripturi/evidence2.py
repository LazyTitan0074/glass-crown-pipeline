import re, sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"
ch = {n: open(P % n, encoding="utf-8").read() for n in range(1, 11)}
print("### shutter contexts")
for n in range(1, 11):
    for m in re.finditer(r".{100}shutters?.{100}", ch[n], re.I | re.S):
        print("ch%d:" % n, m.group(0).replace("\n", " | ")[:320])
print("### sandalwood")
for n in range(1, 11):
    for m in re.finditer(r".{60}sandalwood.{60}", ch[n], re.I | re.S):
        print("ch%d:" % n, m.group(0).replace("\n", " | ")[:220])
print("### amber non-eye")
for n in range(1, 11):
    for m in re.finditer(r".{50}amber.{50}", ch[n], re.I | re.S):
        s = m.group(0).replace("\n", " | ")
        if "eye" not in s.lower():
            print("ch%d:" % n, s[:200])
print("### weight of crown/words")
for n in range(1, 11):
    for m in re.finditer(r".{40}weight of (the )?(crown|words).{40}", ch[n], re.I | re.S):
        print("ch%d:" % n, m.group(0).replace("\n", " | ")[:220])
print("### air smelled of")
for n in range(1, 11):
    for m in re.finditer(r".{30}air smelled of.{60}", ch[n], re.I | re.S):
        print("ch%d:" % n, m.group(0).replace("\n", " | ")[:200])
print("### US variants")
for n in range(1, 11):
    for m in re.finditer(r"\b\w*(our|ise|yse|ogue)\b", ch[n]):
        w = m.group(0)
        if w.lower() not in ("your", "our", "their", "hour", "vogue", "rogue", "togue"):
            print("ch%d:" % n, w)
