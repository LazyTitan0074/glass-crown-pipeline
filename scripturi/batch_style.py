import re, sys
sys.stdout.reconfigure(encoding="utf-8")
P = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_%d.md"

def sub(n, old, new, count=1):
    p = P % n
    t = open(p, encoding="utf-8").read()
    assert t.count(old) >= 1, (n, old[:70])
    t = t.replace(old, new, count)
    open(p, "w", encoding="utf-8").write(t)
    print("ch%d: %s" % (n, new[:70]))

# --- m9 US standard ---
sub(1, "painted the colour of dried blood", "painted the color of dried blood")
sub(10, "sky went the colour of iron", "sky went the color of iron")
sub(10, "dawn, or its rumour", "dawn, or its rumor")
sub(2, "harbour", "harbor")
sub(9, "harbour", "harbor")
sub(10, "harbour", "harbor")
# remaining harbour instances
for n in (2, 9, 10):
    p = P % n
    t = open(p, encoding="utf-8").read()
    if "harbour" in t:
        t = t.replace("harbour", "harbor")
        open(p, "w", encoding="utf-8").write(t)
        print("ch%d: harbour sweep done" % n)
# travelling/traveling + realise/organise sweep
for n in range(1, 11):
    p = P % n
    t = open(p, encoding="utf-8").read()
    t2 = t.replace("travelling", "traveling").replace("realise", "realize").replace("organise", "organize").replace("behaviour", "behavior")
    if t2 != t:
        open(p, "w", encoding="utf-8").write(t2)
        print("ch%d: -ise/-elling sweep" % n)

# --- m6 sandalwood (keep ch4s1 + ch10 only) ---
sub(3, "a faint trace of sandalwood oil that clung to the carved headboard", "a faint trace of lavender oil that clung to the carved headboard")
sub(3, "the faint, lingering scent of sandalwood", "the faint, lingering scent of warm linen")
sub(3, "smelled of sandalwood and stale wine", "smelled of sour wine and lamp oil")
sub(3, "smelled faintly of sandalwood", "smelled faintly of leather and road dust")
sub(4, "smelled of sandalwood and aged wine", "smelled of beeswax and aged wine")
sub(4, "the scent of wine and sandalwood filling her lungs", "the scent of wine and warm skin filling her lungs")
sub(4, "scent of sandalwood and warm wax lingered", "scent of warm wax and smoke lingered")
sub(7, "heavy with sandalwood and something sharper", "heavy with wine and something sharper")
# --- m6 amber candles (keep Elowen eyes) ---
for n, olds in ((4, ["casting amber light", "amber light stretching", "casting amber light"]),):
    pass
sub(4, "casting amber light across the silk-draped walls", "casting low golden light across the silk-draped walls")
sub(4, "their amber light stretching long shadows", "their firelight stretching long shadows")
print("batch done")
