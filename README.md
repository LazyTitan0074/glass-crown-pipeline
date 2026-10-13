# Novella Pipeline — write a canon-locked novel with free AI models

A complete, field-tested system for producing long-form fiction with small, unreliable, quota-limited language models — plus a human who refuses to trust them. Used to produce a 10-chapter, ~24,000-word dark-fantasy novella in one day, with a measured 0% canon-violation rate in the final manuscript.

## The problem this solves

Small/free LLMs writing long fiction will, guaranteed: age characters up and down, upgrade suspicion into certainty three chapters early, invent proof objects to force the plot, leak Act III vocabulary into Chapter 1, flatter your mistakes, and — worst — a *reviewer* model will PASS all of it with a straight face. This pipeline exists because "looks good to the model" is worthless. Everything here is built around one rule:

> **A reviewer PASS means nothing until a deterministic check agrees.**

## How it works

```
MASTER BRIEF  →  CANON.md (N hard facts)  →  BEAT_SHEET / VOICE / CHECKLIST
        │
        ▼
capitol_runner.py ──► write scene-by-scene ──► review ──► canon_check.py ──► PASS? ──► human spot-check
        │                                                                              │
        │ FAIL → delete draft, retry (max 4, new facts pinned per failure)              │ FAIL → human rewrite/micro-edit
        ▼                                                                              ▼
build_all.py: format → copy → epub (fixed order) ──► verify_build.py + verify_epub.py (every paragraph traced source→artifact)
```

### 1. Canon, not vibes (`CANON.md`)
19 facts (C01–C19): names, ages, filiation, events, numbers, staging rules (who may appear/know what, and WHEN), intimacy rules, voice bans. Any contradiction = chapter rejected and **rewritten, never patched** — except human micro-edits on isolated phrases, re-checked after.

Write guards FRONT-LOADED: fact-injection truncates each fact (~320 chars), so restrictions go first, lore second. (We learned this after a model wrote a Vestalian seal into Chapter 3 because the staging rule sat past the truncation point.)

### 2. The checker (`scripturi/canon_check.py`)
An LLM continuity checker with:
- **Anti-false-positive rules** (behavior ≠ age violation; confirming quotes ≠ violations; objects evoking people ≠ timeline violations).
- **Timing disambiguation** (which facts activate in which chapter; "asks by name" belongs to the entrance scene only).
- **Truncation-proof verdict parsing** (fence-stripping, balanced-brace recovery, violation-object harvesting, hedge filtering — small reviewers ramble, hedge ("no violation, but…"), and get cut off mid-JSON).
- **Reviewer fallback chain**, ending in a free local model (see below). Different model from the writer, always.

### 3. The human spot-checks (`scripturi/spot_*.py`, `verify_*.py`)
Deterministic grep sweeps per chapter: age words near the minor, banned names per chapter range, goddess terms per staging window, certainty verbs pre-reveal, contact/sensual language near protected characters, trait duplication (grey-green eyes belong to ONE character). Plus a full build verifier: every source paragraph must exist in the manuscript AND the EPUB (`verify_build.py`, `verify_epub.py`).

### 4. Quota strategy (all free tiers)
The pipeline routes around dead models automatically (fallback chains per agent), and was validated against: Mistral Small (dead all day), Groq 120B (daily tokens burned, then 403), Gemini Flash (20/day), OpenRouter free (50/day, empties on long prompts), `ministral-8b` (always open, most error-prone — produced 7 rejected drafts). When everything cloud died, chapters were written by hand to the same canon and checked identically.

Best free move: **local Ollama** (`qwen2.5:7b`, ~4.7 GB, runs fully on an RTX 4070 laptop GPU) wired in with zero code changes — point the `openrouter` provider slot at `http://localhost:11434/v1`. Unlimited, private, good enough for reviewing and editing.

### 5. Deterministic builds
`build_all.py` enforces **format → copy → epub** order (we shipped a stale EPUB twice by building it before copying the fresh manuscript — the verifier catches this class of bug by design). Scene headings are stripped only at publish time; sources keep them for navigation.

## Quick start

1. Install [Ollama](https://ollama.com/download), `ollama pull qwen2.5:7b`.
2. Copy `.env.example` to `.env`, add provider keys (or point everything at localhost).
3. Write your `CANON.md` (facts first, guards front-loaded), `BEAT_SHEET.md`, `VOICE.md`, scene summaries.
4. `python scripturi/capitol_runner.py <N>` per chapter. **Never trust a PASS alone** — run the spot scripts.
5. `python scripturi/build_all.py`, then `verify_epub.py`. Ship only 100% matches.

## What the numbers looked like (case study)

- 7 model drafts rejected for real violations; 3+ reviewer false-negatives caught by spot-checks; ~10 false-positives filtered by checker rules.
- Final split: 3 chapters fully human, 1 fully model, 6 hybrid. Total: ~24k words, 0 known violations.
- Two infrastructure bugs fixed mid-flight: the writer read embedded stale scenes instead of `scenes.json`; the formatter sorted chapters lexicographically (1, 10, 2…).
- Full story, including every mistake: `CASE_STUDY.md` (from the original Romanian log).

## Contents

- `CANON.md`, `BEAT_SHEET.md`, `VOICE.md`, `CHAPTER_CHECKLIST.md` — the doctrine (worked example from a real book).
- `outline.md`, `scenes.json`, `characters.json`, `world.json`, `research_results.md`, `editor.yml`, `expert-roman.yaml` — LibriScribe-compatible project data.
- `scripturi/` — runner, checker, ~30 spot/verify utilities, builders, quota probes, one-shot patches (full history, warts included).
- `publish/platforme.md` — where to publish adult fiction (Romanian).
- `REVIEW_STRICT_v1.md` — the machine-actionable repair-sheet format for editing passes.

## Rules for derivatives

- 18+ content only with honest labeling. Our canon hard rule travels with the system: **minors are never in intimate scenes, never described sensually, never subject to sexualized language** — in any book built with this pipeline.
- The novel text itself is not included here; it remains the author's property.

## License

MIT — see `LICENSE`.
