import sys, re
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_1.md", encoding="utf-8").read()
for m in re.finditer(r"lara", t, re.I):
    print("----")
    print(t[max(0, m.start() - 120):m.end() + 120])
