import sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_7.md"
t = open(p, encoding="utf-8").read()
o = '"Good." Lara refilled the cup. "And the figures?"'
print("count:", t.count(o))
t = t.replace(o, '"Good girl." Lara refilled the cup. "And the figures?"', 1)
open(p, "w", encoding="utf-8").write(t)
print("done")
