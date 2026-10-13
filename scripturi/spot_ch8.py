import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_8.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
def wb(pat):
    return len(re.findall(r"\b" + pat + r"\b", t, re.I))
for p in ["Elowen", "Mirela", "Cassian", "Mira", "Vela", "Sorina", "Sera",
          "glass", "crystal", "crown", "kneel", "exile", "smile", "evidence",
          "Azara", "Vohra", "Unique Mother", "Crown-Mother", "Supreme Mother",
          "mommy", "I love you", "spank", "rod", "bare", "whore", "slut",
          "Key Refinements", "Revised Chapter", "smile"]:
    print(p, "->", wb(p))
