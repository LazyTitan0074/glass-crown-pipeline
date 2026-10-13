import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_7.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
def wb(pat):
    return len(re.findall(r"\b" + pat + r"\b", t, re.I))
for p in ["Mira", "Vela", "Sorina", "Sera", "Cassian", "Elowen", "Elara",
          "exile", "execution", "vote", "council", "untouched", "mommy",
          "I love you", "spank", "rod", "bare", "Key Refinements", "Revised Chapter",
          "Azara", "Vohra", "Unique Mother", "Crown-Mother", "Supreme Mother"]:
    print(p, "->", wb(p))
print("########## correction ctx ##########")
for m in re.finditer(r".{350}\b(rod|spank|bare|correction|discipline)\b.{350}", t, re.I | re.S):
    print(m.group(0)); print("----")
