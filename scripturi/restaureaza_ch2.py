from pathlib import Path
from libriscribe.knowledge_base import ProjectKnowledgeBase, Chapter, Scene

PROJ = Path(r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara")
k = ProjectKnowledgeBase.load_from_file(str(PROJ / "project_data.json"))
ch = Chapter(
    chapter_number=2, title="The Lower City",
    summary=("Flight, fear, hunger. Leah reaches the Red Velvet Inn, the costliest brothel in the "
             "capital, where information is worth more than flesh. Its mistress Elowen recognizes her "
             "in the first second, and takes her in out of interest: a virgin princess is a fortune. "
             "Leah accepts: for the first time, her body is her own."))
sc = [
    ("Elowen tells her she knows who she is and offers the contract: young clients only, discretion, her cut.",
     ["Leah", "Elowen"], "Elowen's study", "The contract", "Suspicion"),
    ("The first young client, hasty and clumsy; Leah frightened, but her body is hers for the first time.",
     ["Leah"], "Inn suite", "First autonomy", "Shame and curiosity"),
    ("Second day: the girls teach her to listen and remember; nobles' secrets are worth gold.",
     ["Leah", "Elowen"], "Inn salon", "The lesson of information", "Adaptation"),
    ("A drunken officer talks of the host in the east; Elowen listens carefully.",
     ["Leah", "Elowen"], "Inn salon", "Foreshadowing", "Unease"),
]
for i, (s, cc, st, g, b) in enumerate(sc, 1):
    ch.scenes.append(Scene(scene_number=i, summary=s, characters=cc, setting=st, goal=g, emotional_beat=b))
k.chapters[2] = ch
k.save_to_file(str(PROJ / "project_data.json"))
print("restored:", k.chapters[2].title, len(k.chapters[2].scenes))
