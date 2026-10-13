import sys, re
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_1.md", encoding="utf-8").read()
idx = [m.start() for m in re.finditer(r"poison", t, re.I)]
print("poison count:", len(idx))
for i in idx:
    print("====")
    print(t[max(0, i - 300):i + 300])
