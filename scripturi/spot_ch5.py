import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_5.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
def wb(pat):
    return len(re.findall(r"\b" + pat + r"\b", t, re.I))
for p in ["Mira", "Vela", "Sorina", "Sera", "Lara", "Leah", "Elowen",
          "Azara", "Vohra", "Unique Mother", "Crown-Mother", "Supreme Mother",
          "Cassian", "Elara", "poison", "mercenar", "million", "Daughters of Flame",
          "council", "vassal", "exile", "execution", "vote", "mommy", "I love you",
          "Key Refinements", "Revised Chapter"]:
    print(p, "->", wb(p))
