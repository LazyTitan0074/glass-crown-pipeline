import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_4.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("########## tracing line ##########")
i = t.find("tracing the line of Leah")
print(t[max(0, i-400):i+800])
print("########## reveal: army/host ##########")
for m in re.finditer(r".{300}(army|host|soldiers|conquer|throne).{300}", t, re.I | re.S):
    print(m.group(0)); print("----")
