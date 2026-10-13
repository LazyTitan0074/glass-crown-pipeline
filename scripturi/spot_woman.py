import sys, re
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_1.md", encoding="utf-8").read()
i = t.find("You're late")
print(t[max(0, i - 1500):i + 500])
