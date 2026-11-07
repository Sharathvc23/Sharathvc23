# 2026-11-07 — Phase 0 Scaffold Rebuild

## Context

The original Phase 0 scaffold was built in July 2026 but was never successfully pushed to GitHub. The ephemeral cloud container was reclaimed, and the commit existed only locally. The branch `claude/ioa-coursework-build-xgpqu1` now exists on the remote (pointed at main) but contains no coursework files. This session rebuilds the scaffold from the original spec.

## Built

Full repo skeleton under `ioa-coursework/`:
- `CLAUDE.md` — session rules, voice guidelines, 8 hard rules, module acceptance checklist, README template
- `ioa-coursework-readme.md` — course overview (named to avoid overwriting parent repo README.md)
- `syllabus.md` — one-page module map with learning outcomes
- `CONTRIBUTING.md` — contribution guidelines scoped to 8-module boundary
- `LICENSE` — MIT, StellarMinds.ai
- `shared/glossary.md` — placeholder for Phase 1 seeding
- `shared/diagrams/.gitkeep` — placeholder for Mermaid/SVG sources
- `journal/README.md` — journal protocol
- Module stubs: 8 modules × 3 files (README.md, reading-list.md, exercises.md)
- `scripts/check_links.py` — internal link validator (stdlib only)
- `scripts/run_examples.sh` — example runner
- `scripts/new_journal_entry.py` — journal entry scaffolder
- `.github/workflows/ci.yml` — CI pipeline (link check + example runner)

## Broke / Surprised

The original session in July hit persistent 403 errors on GitHub push (Claude GitHub App lacked Contents:write on this repo). A tar.gz was sent to the user but it's unclear if it was ever applied. The branch now exists on the remote but is identical to main — confirming the scaffold was never pushed.

## Decisions

1. **Subdirectory, not separate repo.** The coursework lives at `ioa-coursework/` within the profile repo. This keeps the StellarMinds.ai ecosystem visible in one place. Revisit in Phase 9.
2. **README naming.** `ioa-coursework-readme.md` instead of `README.md` to avoid colliding with the parent repo's README. GitHub won't auto-render it, but the tradeoff is worth avoiding confusion.
3. **stdlib-only scripts.** `check_links.py` and `new_journal_entry.py` use only the Python standard library. `run_examples.sh` is pure bash. No tooling dependencies to install.
4. **Scoped CI triggers.** The CI workflow triggers only on changes to `modules/**`, `shared/**`, `scripts/**`, and `journal/**` — not on README or top-level doc edits.

## Open

- Should the coursework eventually get its own repo? Deferred to Phase 9.
- Glossary seeding (25–35 terms) is Phase 1 work.

## Next

Phase 1: Seed `shared/glossary.md` with canonical terms, then build Module 01 (Why an Internet of Agents) per the CLAUDE.md acceptance checklist.
