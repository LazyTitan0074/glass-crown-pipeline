import sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_9.md"
t = open(p, encoding="utf-8").read()

tally = """She made herself count it out, the way Elowen had taught her: what you have, what you lack, what it costs.

Coin: eleven silver crowns and a fistful of copper in the purse, sewn into the hem where the inn girls hid theirs. Enough to bribe a dockhand. Not enough to buy silence after.

Routes: the back stair to the kitchens, the laundry chute to the yard, the harbour at low tide when the watch drank. All of them ended at guards she did not own. Daughters at the corridor's end, Daughters at the stairs. Someone might look away for silver. Someone would report it for gold.

People: Elowen, paid off and finished with her. Mira, who would do her duty and call it kindness. Lara —

She stopped counting there. That column had no numbers in it, only a hand on her shoulder and a voice saying *stop, breathe*, and the particular pain of being kept by someone who claimed to love keeping.

Things: the locket (hers, unsellable), the glass diadem (recognizable at fifty paces, unpawnable, unwearable in flight), a dress too fine to run in and too plain to hide behind.

That was the tally. Eleven crowns, three doors, no one.

"""
start = t.find("The changes began with the smallest things.")
endmark = 'Leah swallowed. *"No."*'
end = t.find(endmark)
assert start > 0 and end > start, (start, end)
t = t[:start] + tally + t[end:]
open(p, "w", encoding="utf-8").write(t)
print("essay removed, tally inserted; cut chars:", end - start)
