import sys, re, json
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_5.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'")
print("########## sorina/vela ctx ##########")
for m in re.finditer(r".{300}\b(sorina|vela)\b.{300}", t, re.I | re.S):
    print(m.group(0)); print("----")
print("########## evidence/plan ctx ##########")
for m in re.finditer(r".{250}\b(evidence|proof|payment|plan|vassal|council|time|mourn|grief|coronat)\b.{250}", t, re.I | re.S):
    print(m.group(0)); print("----")
pd = json.load(open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\project_data.json", encoding="utf-8"))
print("########## embedded characters ##########")
for c in pd.get("characters", []):
    print("-", c.get("name"))
