"""Minimal EPUB builder for the Lantern Room cold run (stdlib only).

Reads chapter_1..4.md from GLASS_PROJ (or --proj), writes The_Lantern_Room.epub
next to them, then verifies every source paragraph (>120 chars, non-heading)
is present in the EPUB.

Usage: python build_epub.py [--proj DIR]
Exit 0 = all paragraphs verified, 1 = gaps found.
"""

import argparse
import html as H
import os
import re
import sys
import zipfile
from pathlib import Path

TITLES = {1: "First Night", 2: "Names", 3: "Doubt", 4: "The Lantern Room"}


def md_to_xhtml(title, text):
    paras = []
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block:
            continue
        m = re.match(r"^#{1,4}\s*(.+)$", block)
        if m:
            paras.append(f"<h2>{H.escape(m.group(1))}</h2>")
        else:
            paras.append(f"<p>{H.escape(block).replace(chr(10), ' ')}</p>")
    return ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
            "<!DOCTYPE html>\n<html xmlns=\"http://www.w3.org/1999/xhtml\">\n"
            f"<head><title>{H.escape(title)}</title></head>\n<body>\n"
            f"<h1>{H.escape(title)}</h1>\n" + "\n".join(paras) + "\n</body>\n</html>\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proj", default=os.getenv("GLASS_PROJ", "."))
    args = ap.parse_args()
    proj = Path(args.proj)
    chaps = {}
    for n in range(1, 5):
        p = proj / f"chapter_{n}.md"
        if not p.exists():
            print(f"missing {p}", file=sys.stderr)
            return 2
        chaps[n] = p.read_text(encoding="utf-8")

    epub = proj / "The_Lantern_Room.epub"
    if epub.exists():
        epub.unlink()
    with zipfile.ZipFile(epub, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0"?>\n<container version="1.0" '
                   'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles></container>\n')
        items = "".join(
            f'<item id="ch{n:02d}" href="ch{n:02d}.xhtml" media-type="application/xhtml+xml"/>\n'
            for n in chaps)
        refs = "".join(f'<itemref idref="ch{n:02d}"/>\n' for n in chaps)
        z.writestr("OEBPS/content.opf",
                   '<?xml version="1.0" encoding="utf-8"?>\n<package version="3.0" '
                   'xmlns="http://www.idpf.org/2007/opf" unique-identifier="id">\n'
                   '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
                   '<dc:title>The Lantern Room</dc:title><dc:language>en</dc:language>\n'
                   '<dc:identifier id="id">lantern-room-cold-run</dc:identifier>\n</metadata>\n'
                   f"<manifest>\n{items}</manifest>\n<span>\n{refs}</span>\n</package>\n")
        for n, text in chaps.items():
            z.writestr(f"OEBPS/ch{n:02d}.xhtml", md_to_xhtml(TITLES[n], text))
    print(f"wrote {epub} ({epub.stat().st_size} bytes)")

    # Verify: every long source paragraph must exist in the EPUB text.
    def norm(t):
        t = re.sub(r"<[^>]+>", " ", t)
        t = H.unescape(t)
        return re.sub(r"\s+", " ", t)
    epn = ""
    with zipfile.ZipFile(epub) as z:
        for n in chaps:
            epn += z.read(f"OEBPS/ch{n:02d}.xhtml").decode("utf-8")
    epn = norm(epn)
    ok, total = True, 0
    for n, text in chaps.items():
        paras = [p.strip() for p in re.split(r"\n\s*\n", text)
                 if len(p.strip()) > 120 and not re.match(r"^#{1,4}\s", p.strip())]
        bad = [p for p in paras if norm(p)[:80] not in epn]
        total += len(paras)
        print(f"ch{n}: {len(paras) - len(bad)}/{len(paras)} paras verified"
              + (f" MISS {len(bad)}" if bad else ""))
        ok &= not bad
    print(f"total words: {sum(len(t.split()) for t in chaps.values())}")
    print("EPUB OK" if ok else "EPUB GAPS FOUND")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
