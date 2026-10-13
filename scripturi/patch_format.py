import re
p = r"C:\Users\bizoi\AppData\Roaming\Python\Python314\site-packages\libriscribe\agents\formatting_optimized.py"
t = open(p, encoding="utf-8").read()
old1 = "for i, chapter_file in enumerate(sorted(chapter_files), 1):"
old2 = "for chapter_file in sorted(chapter_files):"
assert t.count(old1) == 1 and t.count(old2) == 1, (t.count(old1), t.count(old2))
t = t.replace(old1, "for i, chapter_file in enumerate(sorted(chapter_files, key=_chapter_key), 1):")
t = t.replace(old2, "for chapter_file in sorted(chapter_files, key=_chapter_key):")
helper = "console = Console()\n"
assert helper in t
t = t.replace(helper, helper + '\ndef _chapter_key(path):\n    m = re.search(r"chapter_(\\d+)\\.md$", str(path))\n    return int(m.group(1)) if m else 0\n', 1)
open(p, "w", encoding="utf-8").write(t)
print("patched OK")
