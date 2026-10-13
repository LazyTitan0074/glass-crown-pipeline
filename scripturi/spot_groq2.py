import sys, re
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_1.md", encoding="utf-8").read()
print("########## ledger/letter ##########")
for m in re.finditer(r".{300}(ledger|letter).{300}", t, re.I | re.S):
    print(m.group(0)); print("----")
print("########## lara hits ##########")
for m in re.finditer(r".{100}lara.{100}", t, re.I | re.S):
    print(m.group(0)); print("----")
print("########## cassian body/touch ##########")
for m in re.finditer(r".{200}cassian.{300}", t, re.I | re.S):
    s = m.group(0)
    if re.search(r"(touch|grab|hold|shov|finger|linger|eyes|gaze|wrist|bod|brotherly|sister|whore|slut|naked|bed)", s, re.I):
        print(s); print("----")
