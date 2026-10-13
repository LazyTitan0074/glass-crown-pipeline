import sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"

def pre(n, anchor, insert):
    p = P % n
    t = open(p, encoding="utf-8").read()
    assert t.count(anchor) == 1, (n, anchor[:60], t.count(anchor))
    t = t.replace(anchor, insert + "\n\n" + anchor, 1)
    open(p, "w", encoding="utf-8").write(t)
    print("ch%d bridge: %s" % (n, insert[:60]))

pre(3, "The Red Velvet Inn smelled of smoked cedar",
    "By the second evening she had learned the price of the wine: listen first, drink later.")
pre(3, "The Red Velvet Inn smelled of sour wine and lamp oil",
    "Later that same night, the lesson turned teeth.")
pre(3, "The Red Velvet Inn hummed with low conversation",
    "On the third day, a merchant off the east road drank enough to talk.")
pre(5, "The suite smelled of damp silk and old wine",
    "When the ledgers were put aside, Lara unrolled the map.")
pre(5, "The suite smelled of old silk and something sharper",
    "An hour later, with the wine gone cold between them, Lara refilled both cups anyway.")
pre(5, "The suite was too quiet.\n\nLeah stood in the center",
    "Lara left her with the papers. The drums went on without her.\n\nThe suite was too quiet.\n\nLeah stood in the center")
pre(7, "Lara\u2019s hand rested on the edge of the table",
    "She brought the strip down at first light.")
pre(7, "The suite smelled of dried roses",
    "By midday the easy victory had curdled.")
pre(7, "The suite smelled of old parchment and the faint, metallic tang",
    "Past midnight, the candle nearly dead, they came back to the table.")
print("bridges done")
