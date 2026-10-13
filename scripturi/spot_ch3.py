import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_3.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("len:", len(t), "words~", len(t.split()))
for p in ["Lara", "Isolde", "Vestal", "Daughters of Flame", "Azara", "Vohra",
          "Unique Mother", "Crown-Mother", "Mother of", "Mira", "Vela", "Sera",
          "Elara", "Cassian", "mommy", "Mama", "seal", "coin"]:
    print(p, "->", len(re.findall(p, t, re.I)))
print("########## seal/vestalian ctx ##########")
for m in re.finditer(r".{350}(vestalian|seal).{350}", t, re.I | re.S):
    print(m.group(0)); print("----")
