import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_6.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
def wb(pat):
    return len(re.findall(r"\b" + pat + r"\b", t, re.I))
for p in ["Mira", "Vela", "Sorina", "Sera", "million", "thousand", "hundred",
          "Azara", "Vohra", "Unique Mother", "Crown-Mother", "Supreme Mother",
          "Cassian", "Mirela", "Elara", "Elowen", "spy", "mommy", "I love you",
          "Key Refinements", "Revised Chapter", "poison", "Daughters of Flame"]:
    print(p, "->", wb(p))
print("########## spy ctx ##########")
for m in re.finditer(r".{300}\bspy\b.{300}", t, re.I | re.S):
    print(m.group(0)); print("----")
