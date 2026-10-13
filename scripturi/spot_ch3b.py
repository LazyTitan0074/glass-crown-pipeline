import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_3.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("########## vestal/daughters ctx ##########")
for m in re.finditer(r".{300}(vestal|daughters of flame).{300}", t, re.I | re.S):
    print(m.group(0)); print("----")
