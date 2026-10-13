import sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara\chapter_9.md"
t = open(p, encoding="utf-8").read()

new_block = """Something in Lara's face gave way — not softness. A crack, quickly mortared. She turned from the fire and poured wine with a hand that was not quite steady, and set the second cup down in front of Leah.

"Sit," she said. "Please."

Leah sat. The "please" frightened her more than the commands had.

Lara stood a long moment with her back to the room. When she spoke, the precision was gone from her voice, and what was left was something Leah had never heard from her: effort.

"Six years ago I had a pupil. Sera. Brilliant. Quicker than you." A pause. "She wanted to leave. I told her formation isn't finished, the Mother isn't finished with you, all the words. I refused to let her go."

The fire popped. Neither of them looked at it.

"She fled that same night. I never saw her again." Lara's fingers found the iron ring and turned it, once. "Afterward I made myself a rule. You don't correct someone who cannot leave. Power without an exit isn't discipline. It's abuse with better furniture."

Leah's throat worked. "Then let me go."

"No."

The word landed like a stone in a well. Lara met her eyes and did not look away from what she was doing. "The council holds the throne. The exiles hold the harbour. If you walk out that door tonight, Valdris burns, and you with it. So no. I am breaking my own rule, and I know it, and I am doing it anyway."

Silence. The confession sat between them, too heavy to move.

Lara picked up her cup. Set it down. "Stay a while," she said quietly. "Sit with me. Not as your— not as anything. Just sit."

Leah looked at the cup. At the door. At the woman who owned the army outside and could not own this moment. "No," she said.

Lara nodded. Slowly. She did not argue, did not chill, did not take anything away — the refusal simply stood, untouched, hers. "Good," she said softly. "Keep that one."
"""

start = t.find("The door groaned open.")
endmark = "But she had never been taught to *stay*."
end = t.rfind(endmark, 0, t.find("Scene 4"))
assert start > 0 and end > start, (start, end)
t = t[:start] + new_block + t[end + len(endmark):]
open(p, "w", encoding="utf-8").write(t)
print("scene3 rewritten, Sera restored to memory")
