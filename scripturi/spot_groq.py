import sys, re
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_1.md", encoding="utf-8").read()
print("len:", len(t))
for p in ["sixteen", "seventeen", "eighteen", "nineteen", "thirteen", "fifteen", "fourteen",
          "Isolde", "Vestal", "Daughters of Flame", "Mira", "Vela", "Sera",
          "Unique Mother", "Crown-Mother", "Crown Mother", "Queen-Mother", "Azara", "Vohra",
          "their mother", "she did this", "ledger", "letter", "note", "poison"]:
    print(p, "->", len(re.findall(p, t, re.I)))
print("########## ctx: flame/crown/azara ##########")
for m in re.finditer(r".{250}(daughters of flame|crown.mother|azara|vohra).{250}", t, re.I | re.S):
    print(m.group(0)); print("----")
