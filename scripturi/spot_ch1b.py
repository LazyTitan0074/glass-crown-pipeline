import sys, re
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_1.md", encoding="utf-8").read()
print("########## cassian ctx ##########")
for m in re.finditer(r".{300}cassian.{300}", t, re.I | re.S):
    print(m.group(0)); print("----")
print("########## knew ctx ##########")
for m in re.finditer(r".{200}knew.{200}", t, re.I | re.S):
    print(m.group(0)); print("----")
print("########## lara ctx ##########")
for m in re.finditer(r".{120}lara.{120}", t, re.I | re.S):
    print(m.group(0)); print("----")
