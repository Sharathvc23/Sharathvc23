#!/usr/bin/env python3
"""Scaffold a new journal entry."""

import sys
from datetime import date
from pathlib import Path

TEMPLATE = """# {title}

**Date:** {date}

## Context

_What prompted this session._

## Built

_What was created or changed._

## Broke / Surprised

_What went wrong or was unexpected._

## Decisions

_Key choices made and why._

## Open

_Unresolved questions._

## Next

_What the next session should tackle._
"""

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: new_journal_entry.py <slug> [title]")
        print("  e.g.: new_journal_entry.py phase-1-glossary 'Phase 1: Glossary and Module 1'")
        return 1

    slug = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else slug.replace('-', ' ').title()
    today = date.today().isoformat()
    filename = f"{today}-{slug}.md"

    journal_dir = Path(__file__).resolve().parent.parent / "journal"
    journal_dir.mkdir(parents=True, exist_ok=True)
    target = journal_dir / filename

    if target.exists():
        print(f"Already exists: {target}")
        return 1

    target.write_text(TEMPLATE.format(title=title, date=today), encoding='utf-8')
    print(f"Created: {target}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
