"""Runner cu retry capat (max 4/capitol), log per model, registru canon -> dq."""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(os.getenv("GLASS_BASE", r"C:\Users\bizoi\libriscribe-roman"))
PROJ = Path(os.getenv("GLASS_PROJ", r"C:\Users\bizoi\AppData\Roaming\Python\Python314\projects\leah_si_lara"))
PROJECT = os.getenv("GLASS_PROJECT", "leah_si_lara")
SCRIPT_DIR = Path(__file__).resolve().parent  # canon_check.py lives next to the runner
MAX_ATTEMPTS = 4


def log_attempt(ch, attempt, writer, verdict, n_viol, seconds=None, struct=None):
    entry = {"chapter": ch, "attempt": attempt, "writer": writer,
             "verdict": verdict, "violations": n_viol,
             "seconds": seconds,
             "at": datetime.now(timezone.utc).isoformat()}
    if struct is not None:
        entry["struct"] = struct
    with open(BASE / "retry_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def sync_registry_dq():
    from libriscribe.knowledge_base import ProjectKnowledgeBase
    facts = {}
    for line in (BASE / "CANON.md").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if (line.startswith("- C") or line.startswith("- L")) and ":" in line:
            fid, ftxt = line[2:].split(":", 1)
            facts["CANON-" + fid.strip()] = "CANON (must respect): " + ftxt.strip()[:320]
    pkb = ProjectKnowledgeBase.load_from_file(str(PROJ / "project_data.json"))
    dq = dict(pkb.dynamic_questions or {})
    dq.update(facts)
    pkb.dynamic_questions = dq
    pkb.save_to_file(str(PROJ / "project_data.json"))
    print("dq synced: %d canon facts injected for next chapters" % len(facts))


def write_chapter(ch):
    import typer
    typer.confirm = lambda *a, **k: True
    import libriscribe.main as m
    m.typer.confirm = lambda *a, **k: True
    from libriscribe.agents.project_manager import ProjectManagerAgent
    pm = ProjectManagerAgent(llm_client=None)
    pm.load_project_data(PROJECT)
    pkb = pm.project_knowledge_base
    pm.initialize_llm_client(pkb.llm_provider, pkb.model)
    writer = pkb.llm_provider + "/" + str(pkb.model)
    pm.write_and_review_chapter(ch)
    pm.checkpoint()
    return writer


def main():
    ch = int(sys.argv[1])
    sync_registry_dq()
    for attempt in range(1, MAX_ATTEMPTS + 1):
        print("--- ch%s attempt %d/%d ---" % (ch, attempt, MAX_ATTEMPTS), flush=True)
        t0 = time.time()
        f = PROJ / ("chapter_" + str(ch) + ".md")
        if f.exists():
            f.unlink()
        writer = write_chapter(ch)
        r = subprocess.run([sys.executable, str(SCRIPT_DIR / "canon_check.py"), str(ch), writer],
                           capture_output=True, text=True, cwd=str(BASE))
        out = r.stdout if r.stdout else r.stderr
        print(out[-1500:])
        v = json.loads((BASE / ("canon_verdict_ch" + str(ch) + ".json")).read_text(encoding="utf-8"))
        secs = round(time.time() - t0, 1)
        if not v["pass"]:
            log_attempt(ch, attempt, writer, "FAIL", len(v["violations"]), secs)
            print("ch%s RESPINS (%d abateri), reincerc..." % (ch, len(v["violations"])))
            continue
        # FIX-1/2/4 structural gate: canon PASS is necessary but not sufficient.
        s = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "struct_check.py"), str(ch),
             "--proj", str(PROJ), "--base", str(BASE)],
            capture_output=True, text=True, cwd=str(BASE))
        sout = s.stdout if s.stdout else s.stderr
        print(sout[-1500:])
        sv = json.loads((BASE / ("struct_verdict_ch" + str(ch) + ".json")).read_text(encoding="utf-8"))
        if not sv["pass"]:
            log_attempt(ch, attempt, writer, "FAIL", len(v["violations"]), secs,
                        struct=sv["failures"])
            print("ch%s RESPINS structural (%d probleme), reincerc..." % (ch, len(sv["failures"])))
            continue
        log_attempt(ch, attempt, writer, "PASS", len(v["violations"]), secs,
                    struct=[])
        print("ch%s PASS din incercarea %d" % (ch, attempt))
        return
    print("ch%s ESUAT dupa %d incercari — interventie umana necesara" % (ch, MAX_ATTEMPTS))


if __name__ == "__main__":
    main()
