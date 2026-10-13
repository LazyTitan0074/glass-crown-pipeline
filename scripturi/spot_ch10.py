import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_10.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
def wb(pat):
    return len(re.findall(r"\b" + pat + r"\b", t, re.I))
for p in ["Sera", "Mira", "Vela", "Sorina", "Cassian", "Mirela", "Elowen",
          "Elara", "Varnholt", "betrothal", "You are mine", "I love you",
          "mommy", "burn", "orders", "ship", "crown", "mirror", "leave",
          "Azara", "Vohra", "Unique Mother", "Crown-Mother", "Supreme Mother",
          "Key Refinements", "Revised Chapter"]:
    print(p, "->", wb(p))
print("########## leave-let-go ctx ##########")
for m in re.finditer(r".{350}\b(if I leave|will you let me|let you go|let her go)\b.{350}", t, re.I | re.S):
    print(m.group(0)); print("----")
