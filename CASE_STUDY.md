# Case study: one novella, one day, zero quota budget

Book: *The Glass Crown* — dark political fantasy, 10 chapters, ~24,000 words, 18+ consensual-adult themes. Production date: 13 Oct 2026. Models used: whatever was alive (rotating free tiers) + human author + local Ollama reviewer.

## Pipeline stats

- Chapters: 10/10 delivered, 0 known canon violations in final manuscript.
- Model drafts rejected for REAL violations: 7 (aged-up minor twice, certainty-before-reveal 3×, proof objects too early, Vestalian titles/objects leaking, physical contact by a verbal-only character).
- Reviewer false-negatives caught by human spot-checks: 3+ (PASS on drafts with real violations).
- Reviewer false-positives filtered by checker rules: ~10 (behavior-as-age, confirming quotes, arithmetic failures like "chapter 7 is pre-chapter-4").
- Authorship split: 3 chapters fully human, 1 fully model, 6 hybrid.
- Human spot-checks written: ~30 scripts. Final build verification: 400+ paragraphs traced source → manuscript → EPUB, 100% match.

## Bugs found in the tooling (all fixed, all documented)

1. **Stale embedded roster**: the writer injected character profiles from an embedded copy, ignoring the cleaned `characters.json`. Fix: rebuild embedded data from source files before every run.
2. **Truncated guardrails**: research context cut at 1200 chars dropped half the bans; canon facts cut at 220 chars dropped staging rules. Fix: compact research to fit; front-load every restriction.
3. **Lexicographic chapter sort** in the official formatter (1, 10, 2…). Fix: numeric sort key.
4. **Build-order race**: EPUB assembled from the manuscript file BEFORE the fresh copy landed. Fix: single ordered build script; verify artifacts, never sources.
5. **Checkpoint clobbering**: the runner overwrote `project_data.json` mid-run, erasing a model switch. Rule: never edit project inputs while a run is active.
6. **Reviewer arithmetic blindness**: small models cannot compare chapter numbers. Mitigation: explicit "you are checking chapter N; N > 4" lines help ~50%; the spot-check remains the real gate.

## Decisions that held

- Rejected chapters are REWRITTEN, never patched (except human micro-edits on isolated phrases, re-checked).
- Never trust a PASS alone. Evidence before synthesis, always.
- Refusal/consent architecture built into the canon itself (C17-style two-level rule), not into reminders.
- Reaction-based editing: every external critique verified mechanically first — ~40% turned out stale or false. Fix confirmed items only.

## What didn't work

- Small-model reviewers for timing gates (0% reliability on "before/after chapter X" judgments).
- Free-tier reasoning models on long prompts (empty responses; only short prompts worked).
- Asking models to self-repair rejected drafts (produced new violations; full rewrites scored better).
