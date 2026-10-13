import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_4.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
for p in ["mommy", "Mama", "consent", "wine", "robe", "ring", "guards",
          "Vestalia", "Vestalian", "million", "Mirela", "poison", "mercenar",
          "Mira", "Vela", "Sera", "Cassian", "Elowen", "Azara", "Vohra",
          "Supreme Mother", "Daughters of Flame", "I love you"]:
    print(p, "->", len(re.findall(p, t, re.I)))
print("########## TAIL (truncation?) ##########")
print(t[-1200:])
