import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_9.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
def wb(pat):
    return len(re.findall(r"\b" + pat + r"\b", t, re.I))
for p in ["Sera", "Elowen", "Mira", "Vela", "Sorina", "Cassian", "Mirela",
          "Elara", "spank", "rod", "bare", "kneel", "apolog", "mommy",
          "I love you", "Azara", "Vohra", "Unique Mother", "Crown-Mother",
          "Supreme Mother", "council", "exile", "ship", "Key Refinements", "Revised Chapter"]:
    print(p, "->", wb(p))
print("########## sera ctx ##########")
for m in re.finditer(r".{400}\bsera\b.{400}", t, re.I | re.S):
    print(m.group(0)); print("----")
