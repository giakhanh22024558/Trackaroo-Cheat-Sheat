"""Slim down roadmap-milestones.md per user request:
- Remove intro block, A3, B1, B2, B5, B6, B7, Assumptions
- Keep A1, A2, B4
- Move B3 content → confluence-export/02-product/03-modules/_index.md
"""

from pathlib import Path
import re

ROOT = Path(r"C:\Users\Admin\Desktop\Trackagroo local management")
ROADMAP = ROOT / "confluence-export" / "01-about" / "02-roadmap-milestones.md"
MODULES_INDEX = ROOT / "confluence-export" / "02-product" / "03-modules" / "_index.md"

content = ROADMAP.read_text(encoding='utf-8')

# ----- Extract B3 content for relocation -----
b3_match = re.search(
    r'## B3\. Consolidated Feature Backlog.*?(?=^## B\d|\Z)',
    content, flags=re.MULTILINE | re.DOTALL
)
assert b3_match, "B3 section not found"
b3_body = b3_match.group(0).rstrip()

# Strip the leading "## B3. ..." heading line — we'll use our own heading in new file
b3_lines = b3_body.split('\n', 1)
b3_inner = b3_lines[1] if len(b3_lines) > 1 else ''

# ----- Remove sections -----

# 1. Strip intro block (h1 to first `---\n---`)
# Original starts with: # Roadmap... + intro blockquote + Document map + Sprint 0 note + ---\n---
# We want: keep only "# Roadmap..." h1, then jump to "# PART A"
new_content = re.sub(
    r'^# Roadmap & Milestones[^\n]*\n.*?^---\n---\n',
    '# Roadmap & Milestones — Trackaroo® Phase 1 Delivery Plan\n\n---\n---\n',
    content, count=1, flags=re.MULTILINE | re.DOTALL
)

# 2. Remove A3
new_content = re.sub(
    r'\n## A3\. Coverage check.*?(?=^---|^## )',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 3. Remove B1
new_content = re.sub(
    r'\n## B1\. Scope rule.*?(?=^## )',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 4. Remove B2 (and B2.1 / B2.2 nested)
new_content = re.sub(
    r'\n## B2\. Sprint 0 Foundation Register.*?(?=^## )',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 5. Remove B3 (moved)
new_content = re.sub(
    r'\n## B3\. Consolidated Feature Backlog.*?(?=^## )',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 6. Remove B5
new_content = re.sub(
    r'\n## B5\. Discovery Gate Deliverable Register.*?(?=^## )',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 7. Remove B6
new_content = re.sub(
    r'\n## B6\. Feature → Governing Spec.*?(?=^## )',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 8. Remove B7
new_content = re.sub(
    r'\n## B7\. Cross-cutting standards reserved for AC.*?(?=^## |\Z)',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 9. Remove "Assumptions, risks & next step" (at end of file)
new_content = re.sub(
    r'\n## Assumptions, risks & next step.*\Z',
    '\n',
    new_content, flags=re.MULTILINE | re.DOTALL
)

# 10. Collapse multiple --- separators that may remain from B7/Assumptions removal
new_content = re.sub(r'(\n---\n){2,}', '\n---\n', new_content)

# 11. Strip trailing whitespace, ensure ending newline
new_content = new_content.rstrip() + '\n'

ROADMAP.write_text(new_content, encoding='utf-8')
print(f"Slimmed roadmap-milestones.md: {len(content):,} → {len(new_content):,} chars")
print(f"  Removed: ~{len(content) - len(new_content):,} chars · ~{content.count(chr(10)) - new_content.count(chr(10))} lines")

# ----- Write modules/_index.md with B3 content -----

NEW_MODULES_INDEX = """# 2.3 Modules — Feature Backlog (canonical)

> **The full Phase 1 product backlog.** 11 Epics · 51 Features. Each Epic = one product module (page below). Each Feature lives under exactly one Epic.

## Why this is the master backlog

The 9-column MasterMind canonical layout. Stories (col E–I) deferred to the Story-pass (planned post-Discovery). Priority is gate-driven — see [Roadmap & Milestones §B4](../../01-about/02-roadmap-milestones.md#b4-delivery-gate--priority).

## Per-module pages

| # | Module | Epic | Gate | Page |
|---|---|---|---|---|
| 1 | Navigation | EPIC-001 | Alpha | [01-navigation.md](./01-navigation.md) |
| 2 | SOS | EPIC-002 | Alpha | [02-sos.md](./02-sos.md) |
| 3 | BackTrack™ | EPIC-003 | Alpha | [03-backtrack.md](./03-backtrack.md) |
| 4 | HazTrack™ | EPIC-004 | Alpha | [04-haztrack.md](./04-haztrack.md) |
| 5 | First Aid Reference | EPIC-005 | Alpha | [05-first-aid.md](./05-first-aid.md) |
| 6 | App Experience | EPIC-006 | Alpha | [06-app-experience.md](./06-app-experience.md) |
| 7 | Operations Console | EPIC-007 | Alpha + Beta | [07-operations-console.md](./07-operations-console.md) |
| 8 | TrackIQ™ | EPIC-008 | Beta-Ready | [08-trackiq.md](./08-trackiq.md) |
| 9 | PCR (Point Condition Reports) | EPIC-009 | Beta-Ready | [09-pcr.md](./09-pcr.md) |
| 10 | TrackMate™ | EPIC-010 | Beta-Ready | [10-trackmate.md](./10-trackmate.md) |
| 11 | POI | EPIC-011 | Beta-Ready | [11-poi.md](./11-poi.md) |

Each module page contains: purpose · feature list with 1-line description · wireframe states · Phase 1 prohibitions · cross-module dependencies · open clarifications (CLR-TRK).

---

## Consolidated Feature Backlog (9-column canonical)

""" + b3_inner.replace('[B4](#b4-delivery-gate--priority)', '[Roadmap & Milestones §B4](../../01-about/02-roadmap-milestones.md#b4-delivery-gate--priority)') \
            .replace('[A1](#a1-master-delivery-timeline)', '[Roadmap & Milestones §A1](../../01-about/02-roadmap-milestones.md#a1-master-delivery-timeline)') \
            .replace('[B2](#b2-sprint-0-foundation-register)', "Sprint 0 register — see [`docs/sprint-0-foundation-criteria.md`](../../../docs/sprint-0-foundation-criteria.md)")
NEW_MODULES_INDEX = NEW_MODULES_INDEX.rstrip() + '\n'

MODULES_INDEX.write_text(NEW_MODULES_INDEX, encoding='utf-8')
print(f"Wrote {MODULES_INDEX.relative_to(ROOT)} ({len(NEW_MODULES_INDEX):,} chars)")
