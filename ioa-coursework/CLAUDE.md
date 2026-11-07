# CLAUDE.md — Session Rules for ioa-coursework

## Voice

Graduate-level, precise, no hype. Write for a reader who ships distributed systems.
Assume familiarity with public-key cryptography, hash functions, HTTP, and JSON.
Do not anthropomorphize protocols. Do not use "revolutionary", "cutting-edge",
"game-changing", or similar. State what a thing does, then show it working.

## Hard Rules

1. **Public sources only.** Every claim must be traceable to a public spec, RFC, paper, repo, or docs page. No insider knowledge, no "it is known."
2. **Every example must run.** If it is in a `*.py` file under `examples/`, it must execute cleanly with Python 3.11+ and exit 0.
3. **No hallucinated APIs.** Only reference functions, classes, and endpoints that exist in the linked library version. When in doubt, read the source.
4. **stdlib + requests only.** Examples use only the Python standard library and `requests`. Module-specific dependencies (e.g., `sm-arp`) are declared per-module.
5. **Each module stands alone.** A reader can start at any module. Forward references are allowed; forward *dependencies* are not.
6. **Glossary terms link to shared/glossary.md.** First use of a glossary term in each module README links to the shared glossary.
7. **Journal entry every session.** At least one entry in `journal/` per build session, written before push.
8. **Verify before push.** Run `scripts/check_links.py` and `scripts/run_examples.sh` before every push. Both must exit 0.

## Module Acceptance Checklist

A module is complete when **all** of the following hold:

- [ ] README.md has all 7 sections (see template below)
- [ ] All internal markdown links resolve (`scripts/check_links.py` exits 0)
- [ ] All `examples/*.py` files run cleanly (`scripts/run_examples.sh` exits 0)
- [ ] Every entry in `reading-list.md` has a working URL
- [ ] Every exercise in `exercises.md` has clear success criteria
- [ ] At least one journal entry documents the build session

## Module README Template

```markdown
# Module NN — Title

## Learning Objectives

- Objective 1
- Objective 2
- Objective 3

## Conceptual Overview

Prose explaining the core ideas. Link glossary terms on first use.

## Architecture and Data Flow

Diagrams (Mermaid or inline SVG) and prose describing how components interact.

## Worked Examples

Step-by-step walkthroughs with code. Reference files in `examples/`.

## Exercises

Pointers to `exercises.md` with brief descriptions.

## Key Takeaways

3–5 bullet points summarizing what the reader should retain.

## Further Reading

Pointers to `reading-list.md` and external resources.
```
