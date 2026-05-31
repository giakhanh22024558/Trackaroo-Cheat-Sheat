"""Finish the slim job: extract B3 from git HEAD (before slim) and write to modules/_index.md."""
from pathlib import Path
import subprocess, re, io, sys

# Force stdout to UTF-8 to avoid cp1252 print errors
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(r"C:\Users\Admin\Desktop\Trackagroo local management")
MODULES_INDEX = ROOT / "confluence-export" / "02-product" / "03-modules" / "_index.md"

# Get the pre-slim version of the roadmap from git HEAD
result = subprocess.run(
    ['git', 'show', 'HEAD:confluence-export/01-about/02-roadmap-milestones.md'],
    cwd=ROOT, capture_output=True, text=True, encoding='utf-8'
)
content = result.stdout

# Extract B3 section
m = re.search(
    r'## B3\. Consolidated Feature Backlog.*?(?=^## B\d|\Z)',
    content, flags=re.MULTILINE | re.DOTALL
)
if not m:
    print('B3 not found in HEAD')
    sys.exit(1)
b3_body = m.group(0).rstrip()
b3_lines = b3_body.split('\n', 1)
b3_inner = b3_lines[1] if len(b3_lines) > 1 else ''

# Rewrite cross-refs in b3_inner
b3_inner = b3_inner.replace(
    '[B4](#b4-delivery-gate--priority)',
    '[Roadmap & Milestones - B4](../../01-about/02-roadmap-milestones.md#b4-delivery-gate--priority)'
).replace(
    '[A1](#a1-master-delivery-timeline)',
    '[Roadmap & Milestones - A1](../../01-about/02-roadmap-milestones.md#a1-master-delivery-timeline)'
).replace(
    '[B2](#b2-sprint-0-foundation-register)',
    "Sprint 0 register - see `docs/sprint-0-foundation-criteria.md`"
)

NEW = f"""# 2.3 Modules - Feature Backlog (canonical)

> **The full Phase 1 product backlog.** 11 Epics, 51 Features. Each Epic = one product module (page below). Each Feature lives under exactly one Epic.

The 9-column MasterMind canonical layout. Stories (col E-I) deferred to the Story-pass (planned post-Discovery). Priority is gate-driven - see [Roadmap & Milestones - B4](../../01-about/02-roadmap-milestones.md#b4-delivery-gate--priority).

## Per-module pages

| # | Module | Epic | Gate | Page |
|---|---|---|---|---|
| 1 | Navigation | EPIC-001 | Alpha | [01-navigation.md](./01-navigation.md) |
| 2 | SOS | EPIC-002 | Alpha | [02-sos.md](./02-sos.md) |
| 3 | BackTrack(TM) | EPIC-003 | Alpha | [03-backtrack.md](./03-backtrack.md) |
| 4 | HazTrack(TM) | EPIC-004 | Alpha | [04-haztrack.md](./04-haztrack.md) |
| 5 | First Aid Reference | EPIC-005 | Alpha | [05-first-aid.md](./05-first-aid.md) |
| 6 | App Experience | EPIC-006 | Alpha | [06-app-experience.md](./06-app-experience.md) |
| 7 | Operations Console | EPIC-007 | Alpha + Beta | [07-operations-console.md](./07-operations-console.md) |
| 8 | TrackIQ(TM) | EPIC-008 | Beta-Ready | [08-trackiq.md](./08-trackiq.md) |
| 9 | PCR (Point Condition Reports) | EPIC-009 | Beta-Ready | [09-pcr.md](./09-pcr.md) |
| 10 | TrackMate(TM) | EPIC-010 | Beta-Ready | [10-trackmate.md](./10-trackmate.md) |
| 11 | POI | EPIC-011 | Beta-Ready | [11-poi.md](./11-poi.md) |

Each module page contains: purpose, feature list with 1-line description, wireframe states, Phase 1 prohibitions, cross-module dependencies, open clarifications (CLR-TRK).

---

## Consolidated Feature Backlog (9-column canonical)

{b3_inner}
"""

# Restore real (TM) trademarks
NEW = NEW.replace('BackTrack(TM)', 'BackTrack™') \
         .replace('HazTrack(TM)', 'HazTrack™') \
         .replace('TrackIQ(TM)', 'TrackIQ™') \
         .replace('TrackMate(TM)', 'TrackMate™')

MODULES_INDEX.write_text(NEW, encoding='utf-8')
print('Wrote', MODULES_INDEX.relative_to(ROOT), '-', len(NEW), 'chars')
