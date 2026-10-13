import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_2.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-")
for kw in ["Azara", "Vohra", "Two Faces", "Daughters of Flame", "name will be spoken", "Tomas"]:
    print("##########", kw)
    for m in re.finditer(r".{350}" + re.escape(kw) + r".{350}", t, re.I | re.S):
        print(m.group(0)); print("----")
