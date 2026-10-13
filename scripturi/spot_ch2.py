import sys, re
sys.stdout.reconfigure(encoding="utf-8")
raw = open(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_2.md", encoding="utf-8").read()
t = raw.replace("\u2011", "-").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
print("len:", len(t), "words~", len(t.split()))
for p in ["Lara", "Isolde", "Vestal", "Daughters of Flame", "Azara", "Vohra",
          "Unique Mother", "Crown-Mother", "Mira", "Vela", "Sera", "Elara",
          "Cassian", "Mirela", "Varnholt", "mommy", "Mama", "Kael", "Liora"]:
    print(p, "->", len(re.findall(p, t, re.I)))
print("########## Elowen look ##########")
for m in re.finditer(r".{200}(mahogany|amber|black hair|grey-green).{200}", t, re.I | re.S):
    print(m.group(0)); print("----")
