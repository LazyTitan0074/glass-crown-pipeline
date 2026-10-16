"""Reviewer trust tracker: measure the reviewer's false-negative rate explicitly.

Every time a human spot-check catches something the reviewer PASSED, log it:

    python scripturi/reviewer_trust.py log 4 --spot fail --findings 2 --notes "Sera named ch4, reviewer missed it"

After ten chapters you get a real number:

    python scripturi/reviewer_trust.py summary

Definitions (binding):
  - FALSE NEGATIVE = reviewer PASS + spot FAIL (reviewer waved a bad chapter through).
  - FALSE POSITIVE (suspect) = reviewer FAIL + spot PASS (reviewer may be too strict;
    needs human confirmation, counted separately, never auto-trusted).

Storage: reviewer_trust.jsonl next to canon_log.jsonl, one JSON object per line.
Stdlib only, UTF-8, portable paths (repo root = parent of scripturi/).
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent  # repo root: CANON.md, scenes.json, *.jsonl live here
TRUST_LOG = ROOT / "reviewer_trust.jsonl"


def load_reviewer_verdict(ch, verdict_path=None):
    """Read canon_verdict_chN.json -> (writer, reviewer, reviewer_pass)."""
    p = Path(verdict_path) if verdict_path else (ROOT / f"canon_verdict_ch{ch}.json")
    if not p.exists():
        return "unknown", "unknown", None
    v = json.loads(p.read_text(encoding="utf-8"))
    return (
        str(v.get("writer", "unknown")),
        str(v.get("reviewer", "unknown")),
        bool(v.get("pass", False)),
    )


def cmd_log(args):
    writer, reviewer, reviewer_pass = load_reviewer_verdict(args.ch, args.verdict)
    if reviewer_pass is None:
        print(f"no reviewer verdict found for ch{args.ch} "
              f"(looked for canon_verdict_ch{args.ch}.json) -- "
              f"pass --verdict explicitly or run canon_check.py first.",
              file=sys.stderr)
        return 1
    spot_pass = args.spot == "pass"
    entry = {
        "chapter": int(args.ch),
        "writer": writer,
        "reviewer": reviewer,
        "reviewer_pass": reviewer_pass,
        "spot_pass": spot_pass,
        "spot_findings": int(args.findings),
        "false_negative": bool(reviewer_pass and not spot_pass),
        "false_positive_suspect": bool(not reviewer_pass and spot_pass),
        "notes": args.notes or "",
        "at": datetime.now(timezone.utc).isoformat(),
    }
    with open(TRUST_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    tag = "FALSE-NEGATIVE" if entry["false_negative"] else (
        "FALSE-POSITIVE-SUSPECT" if entry["false_positive_suspect"] else "AGREE")
    print(f"ch{args.ch} logged [{tag}] reviewer={reviewer} "
          f"reviewer_pass={reviewer_pass} spot_pass={spot_pass} -> {TRUST_LOG.name}")
    return 0


def cmd_summary(args):
    if not TRUST_LOG.exists():
        print(f"no {TRUST_LOG.name} yet -- log spot outcomes first, e.g.:\n"
              f"  python scripturi/reviewer_trust.py log 4 --spot fail --findings 2")
        return 1
    rows = [json.loads(line) for line in TRUST_LOG.read_text(encoding="utf-8").splitlines()
            if line.strip()]
    if args.reviewer:
        rows = [r for r in rows if r.get("reviewer") == args.reviewer]
        if not rows:
            print(f"no entries for reviewer={args.reviewer}")
            return 1
    n = len(rows)
    rev_pass = [r for r in rows if r.get("reviewer_pass")]
    fn = [r for r in rows if r.get("false_negative")]
    fp = [r for r in rows if r.get("false_positive_suspect")]
    fn_rate = (len(fn) / len(rev_pass)) if rev_pass else 0.0

    print(f"entries: {n} | reviewer PASS: {len(rev_pass)} | "
          f"spot-caught FALSE NEGATIVES: {len(fn)} | "
          f"false-positive suspects: {len(fp)}")
    if rev_pass:
        print(f"false-negative rate: {len(fn)}/{len(rev_pass)} = {fn_rate:.0%}")
    # Per-reviewer breakdown.
    by_rev = {}
    for r in rows:
        by_rev.setdefault(r.get("reviewer", "?"), []).append(r)
    for rev, rs in sorted(by_rev.items()):
        rp = sum(1 for r in rs if r.get("reviewer_pass"))
        rf = sum(1 for r in rs if r.get("false_negative"))
        print(f"  {rev}: {rf}/{rp} FN" + (f" = {rf / rp:.0%}" if rp else ""))
    # Decision hint. Thresholds are tunable; the rule below matches the
    # case-study scale (10 chapters, 3+ catches = systematic, not bad luck).
    if n >= 10:
        if len(fn) >= 3 or fn_rate >= 0.30:
            print("DECISION: reviewer NOT trusted alone -- expand the spot-check "
                  "(more patterns, tighter struct bounds) or change reviewer.")
        elif len(fn) == 0:
            print("DECISION: reviewer provisionally trusted on this sample -- "
                  "spot-checks STAY mandatory (pipeline rule: a PASS alone ships nothing).")
        else:
            print("DECISION: reviewer partially trusted -- keep full spot-checks, "
                  "re-evaluate after 10 more chapters.")
    else:
        print(f"DECISION: only {n}/10 chapters -- keep full spot-checks, "
              f"re-evaluate at 10.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_log = sub.add_parser("log", help="log one chapter's spot outcome vs reviewer verdict")
    p_log.add_argument("ch", type=int, help="chapter number")
    p_log.add_argument("--spot", required=True, choices=["pass", "fail"],
                       help="human spot-check outcome")
    p_log.add_argument("--findings", type=int, default=0,
                       help="number of spot findings (default 0)")
    p_log.add_argument("--notes", default="",
                       help="what the spot-check caught (or confirmed)")
    p_log.add_argument("--verdict", default=None,
                       help="path to canon_verdict_chN.json (default: repo root)")

    p_sum = sub.add_parser("summary", help="report false-negative rate")
    p_sum.add_argument("--reviewer", default=None,
                       help="filter to one reviewer string")
    args = ap.parse_args()
    if args.cmd == "log":
        return cmd_log(args)
    return cmd_summary(args)


if __name__ == "__main__":
    sys.exit(main())
