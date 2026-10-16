"""Cold-run findings generator (PIPELINE TEST §5 + §8).

Reads the three logs and scores what can be scored mechanically:
  retry_log.jsonl      -> attempts/chapter, seconds/chapter (§4 time, §5 fallback depth)
  canon_log.jsonl      -> violations_by_fact, parse_mode stats, hedged_filtered (§4, §5-D)
  reviewer_trust.jsonl -> chapter-level reviewer recall/precision proxies (§5-B/C)

What it CANNOT score (left as TODO in the template): human minutes (§5-F)
and the aesthetic verdict (§5-G). Those are yours to write.

Usage:
    python scripturi/findings.py [--root DIR] [--out FINDINGS.md]

Stdlib only, UTF-8. Missing logs degrade gracefully to "n/a".
"""

import argparse
import json
import os
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR.parent


def read_jsonl(p):
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def main():
    ap = argparse.ArgumentParser(description="Score a cold run from pipeline logs")
    ap.add_argument("--root", default=os.getenv("GLASS_BASE", str(DEFAULT_ROOT)),
                    help="dir with retry_log/canon_log/reviewer_trust jsonl files")
    ap.add_argument("--out", default=None, help="write markdown here (default: stdout)")
    args = ap.parse_args()
    root = Path(args.root)

    retry = read_jsonl(root / "retry_log.jsonl")
    canon = read_jsonl(root / "canon_log.jsonl")
    trust = read_jsonl(root / "reviewer_trust.jsonl")

    L = []
    L.append("# Cold-run findings (generated — fill the TODOs by hand)\n")

    # Attempts + time (§4, §5-E/F support).
    L.append("## Attempts and time per chapter")
    if not retry:
        L.append("n/a — no retry_log.jsonl\n")
    else:
        by_ch = {}
        for r in retry:
            by_ch.setdefault(r["chapter"], []).append(r)
        for ch in sorted(by_ch):
            rs = by_ch[ch]
            secs = [r.get("seconds") for r in rs if r.get("seconds") is not None]
            t = f"{sum(secs):.0f}s total" if secs else "time n/a (old log format)"
            L.append(f"- ch{ch}: {len(rs)} attempt(s), {t}, "
                     f"writers={[r.get('writer') for r in rs]}")
        L.append("")

    # Violations by fact (§5-A support).
    L.append("## Violations by fact (reviewer flags)")
    if not canon:
        L.append("n/a — no canon_log.jsonl\n")
    else:
        facts = Counter()
        for c in canon:
            for v in c.get("violations", []):
                facts[v.get("fact", "?")] += 1
        if facts:
            for f, n in facts.most_common():
                L.append(f"- {f}: flagged {n}x")
        else:
            L.append("- none flagged across all chapters")
        L.append("")

    # Parse stability (§5-D).
    L.append("## Parse stability (§5-D)")
    if not canon:
        L.append("n/a — no canon_log.jsonl\n")
    else:
        modes = Counter(c.get("parse_mode", "unknown") for c in canon)
        L.append("- parse modes: " + ", ".join(f"{m}={n}" for m, n in modes.most_common()))
        L.append(f"- unparseable (PARSE-fact) verdicts: {modes.get('unparseable', 0)}")
        L.append(f"- hedged non-findings filtered total: "
                 f"{sum(c.get('hedged_filtered', 0) for c in canon)}")
        L.append("")

    # Recall / precision proxies (§5-B/C). Chapter-level: the trust log does not
    # record per-flag ground truth, so these are proxies — say so honestly.
    L.append("## Reviewer recall / precision vs spot-check (§5-B/C, chapter-level proxies)")
    if not trust:
        L.append("n/a — no reviewer_trust.jsonl (run reviewer_trust.py log per chapter)\n")
    else:
        rev_pass = [r for r in trust if r.get("reviewer_pass")]
        fn = [r for r in trust if r.get("false_negative")]
        fp = [r for r in trust if r.get("false_positive_suspect")]
        L.append(f"- chapters checked: {len(trust)}, reviewer PASS: {len(rev_pass)}")
        L.append(f"- proxy recall: reviewer flagged SOMETHING in "
                 f"{len(trust) - len(fn)}/{len(trust)} spot-checked chapters "
                 f"({len(fn)} chapters where spot found what reviewer passed)")
        L.append(f"- false-positive suspects (reviewer FAIL + spot PASS): {len(fp)}")
        L.append("- NOTE: true per-flag recall/precision needs per-flag ground truth; "
                 "extend the trust log with flag-level review for an exact number.")
        L.append("")

    # Fallback depth (§5-E).
    L.append("## Fallback depth (§5-E)")
    models = Counter()
    for src in (retry, canon):
        for r in src:
            models[r.get("writer") or r.get("reviewer") or "?"] += 1
    L.append("- models seen: " + (", ".join(f"{m}={n}" for m, n in models.most_common())
                                  if models else "n/a"))
    L.append("")

    L.append("## TODO (human — §5-F/G, §8)")
    L.append("- [ ] Human minutes end-to-end (F): ...")
    L.append("- [ ] Aesthetic verdict, one honest paragraph (G): ...")
    L.append("- [ ] Top-3 pipeline changes, ranked: 1) ... 2) ... 3) ...")
    L.append("")

    md = "\n".join(L)
    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
