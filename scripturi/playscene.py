import sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_8.md"
t = open(p, encoding="utf-8").read()

new = """That night, coronation night, Leah did something stupid and small: she skipped the morning arms inspection to sleep an extra hour, and when Mira asked, she lied about why. A nothing. A smudge. It sat in her all day anyway, fizzing, until bedtime, when she understood what she wanted to do with it.

Lara's door was unguarded — a trust, or a trap; with Lara the two were shaped alike. Leah knocked once and entered in her robe, bare underneath, skin prickling at the night air of the room.

Lara lay in bed reading by a single candle, robe tied loose, hair down for once, looking up over the page with no surprise at all. As if she had been expecting exactly this and had decided, beforehand, to allow it.

Leah said nothing. She let the robe fall — heard Lara's breath change, once — and laid herself across Lara's knees, legs parted, face pressed to the coverlet that smelled of her. Her whole body rang like a struck bell.

"Mommy," she said to the dark under the bed's edge. "I've been naughty. Please. I need this."

Lara did not ask a single question. Her hand came down, and it was nothing like the rail, nothing counted, nothing witnessed — this was not correction, whatever shape it borrowed. This was heat. A steady rhythm and a low scolding murmur about inspections and honest queens that Leah stopped hearing after the fourth stroke, because Lara's other hand had slid between her legs, and the world narrowed to that.

She gasped. Clutched the coverlet. "Mommy—" again, moaned this time, helpless and deliberate both, past shame and into something brighter. Lara slowed, then didn't. At some point there was a stillness — a single held breath in which Leah could have ended it with a word, the agreement alive underneath everything like bedrock — and Leah answered it by pressing back, harder, and Lara made a sound low in her throat and went on.

After, when Leah lay wrung out and shaking-laughing into the pillow, Lara gathered her up, naked and all, into her arms the way you carry something precious and asleep already. Held her. Breathed her in.

"Good girl," Lara murmured into her hair.

Leah slept.

Lara lay awake a while longer in the candle dark, holding the warm weight of her, and said it once, to no one, to the room, to the record only she would ever keep.

"Mine."
"""

start = t.find("That night, coronation night,")
endmark = "Tomorrow the grain figures eat us both."
end = t.find(endmark)
assert start > 0 and end > start, (start, end)
t = t[:start] + new + t[end + len(endmark):]
open(p, "w", encoding="utf-8").write(t)
print("ch8 play-scene swapped in")
