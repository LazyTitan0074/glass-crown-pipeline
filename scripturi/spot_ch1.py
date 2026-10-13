import sys, re
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_1.md", encoding="utf-8").read()
print("len:", len(t))
for p in ["sixteen", "seventeen", "eighteen", "nineteen", "thirteen", "fifteen",
          "Lara", "Isolde", "Vestal", "Daughters of Flame", "Mira", "Vela", "Sera",
          "Unique Mother", "Crown-Mother", "Queen-Mother", "their mother",
          "she did this", "realization", "knew", "poison"]:
    print(p, "->", len(re.findall(p, t, re.I)))
print("########## fourteen ctx ##########")
for m in re.finditer(r".{200}fourteen.{200}", t, re.I | re.S):
    print(m.group(0)); print("----")
print("########## poison/knew ctx ##########")
for m in re.finditer(r".{250}poison.{250}", t, re.I | re.S):
    print(m.group(0)); print("----")
