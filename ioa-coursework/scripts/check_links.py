#!/usr/bin/env python3
"""Validate internal markdown links across the coursework."""

import os
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
HEADING_RE = re.compile(r'^#{1,6}\s+(.+)$', re.MULTILINE)

def slugify(heading: str) -> str:
    slug = heading.strip().lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    return slug

def collect_headings(text: str) -> set[str]:
    return {slugify(m.group(1)) for m in HEADING_RE.finditer(text)}

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    md_files = sorted(root.rglob('*.md'))
    broken = []

    file_headings: dict[Path, set[str]] = {}
    for md in md_files:
        file_headings[md] = collect_headings(md.read_text(encoding='utf-8'))

    for md in md_files:
        text = md.read_text(encoding='utf-8')
        for m in LINK_RE.finditer(text):
            target = m.group(2)
            if target.startswith(('http://', 'https://', 'mailto:')):
                continue

            anchor = None
            if '#' in target:
                path_part, anchor = target.rsplit('#', 1)
            else:
                path_part = target

            if path_part:
                resolved = (md.parent / path_part).resolve()
                if not resolved.exists():
                    broken.append(f"  {md.relative_to(root)}: broken link -> {target}")
                    continue
                if anchor and resolved.is_file() and resolved in file_headings:
                    if anchor not in file_headings[resolved]:
                        broken.append(f"  {md.relative_to(root)}: broken anchor -> {target}")
            elif anchor:
                if anchor not in file_headings[md]:
                    broken.append(f"  {md.relative_to(root)}: broken anchor -> #{anchor}")

    if broken:
        print(f"Found {len(broken)} broken link(s):")
        for b in broken:
            print(b)
        return 1
    else:
        print(f"All links OK across {len(md_files)} markdown files.")
        return 0

if __name__ == '__main__':
    sys.exit(main())
