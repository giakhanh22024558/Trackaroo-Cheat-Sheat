"""Move planning.md content to confluence-export/01-about/02-roadmap-milestones.md
with path adjustments. Then replace planning.md with a redirect pointer."""

from pathlib import Path
import re

ROOT = Path(r"C:\Users\Admin\Desktop\Trackagroo local management")
SRC = ROOT / "docs" / "planning.md"
DEST = ROOT / "confluence-export" / "01-about" / "02-roadmap-milestones.md"

content = SRC.read_text(encoding='utf-8')

# Header replacement — adapt for Confluence context
old_header = """# Trackaroo® Phase 1 — Delivery Planning (single source)

> **The single source for delivery planning + backlog.** This file consolidates the former `backlog.md` (business features) and `sprint-0-foundation.md` (cross-cutting foundation) so there is **one place to maintain**.
> Backed by MasterMind skill [`document/features`](../MasterMind/models/model_001/document/features/). Conventions: [`conventions/features-conventions.md`](../conventions/features-conventions.md).
> **Cadence:** 2-week sprints · 8-person Lean Senior Squad · 8 parallel tracks · 900 man-days (Slitigenz proposal §10.3).
> **Build rule (proposal §10.1):** Survival Core first — SOS + BackTrack™ lead; Experience Layer after Alpha; no subsystem coding without WFD-5126 wireframe approval.
> **Last updated:** 2026-05-28

**Document map:**
- **Part A — Delivery Plan:** [A1 Master Timeline](#a1-master-delivery-timeline) · [A2 Sprint-by-sprint execution](#a2-sprint-by-sprint-execution) · [A3 Coverage check](#a3-coverage-check)
- **Part B — Registers (the backlog):** [B1 Scope rule](#b1-scope-rule) · [B2 Sprint 0 Foundation register](#b2-sprint-0-foundation-register) · [B3 Consolidated feature backlog](#b3-consolidated-feature-backlog-9-column-canonical) · [B4 Gate & Priority](#b4-delivery-gate--priority) · [B5 Discovery deliverables](#b5-discovery-gate-deliverable-register) · [B6 Traceability](#b6-feature--governing-spec-traceability) · [B7 Reserved for AC](#b7-cross-cutting-standards-reserved-for-ac)
- *(Sprint 0 deliverables, criteria & ACs are all inline in §B2 — single source.)*"""

new_header = """# Roadmap & Milestones — Trackaroo® Phase 1 Delivery Plan

> **Single-source delivery plan + backlog.** Maintained here in the Confluence workspace going forward (previously `docs/planning.md` — relocated 31 May 2026).
> **Owner:** Delivery Lead · **Last updated:** 2026-05-31
> **Cadence:** 2-week sprints · 8-person Lean Senior Squad · 8 parallel tracks · 900 man-days (Slitigenz proposal §10.3).
> **Build rule (proposal §10.1):** Survival Core first — SOS + BackTrack™ lead; Experience Layer after Alpha; no subsystem coding without WFD-5126 wireframe approval.
> **Backed by:** MasterMind skill [`document/features`](../../MasterMind/models/model_001/document/features/) · conventions in [`conventions/features-conventions.md`](../../conventions/features-conventions.md).

**Document map:**
- **Part A — Delivery Plan:** [A1 Master Timeline](#a1-master-delivery-timeline) · [A2 Sprint-by-sprint execution](#a2-sprint-by-sprint-execution) · [A3 Coverage check](#a3-coverage-check)
- **Part B — Registers (the backlog):** [B1 Scope rule](#b1-scope-rule) · [B2 Sprint 0 Foundation register](#b2-sprint-0-foundation-register) · [B3 Consolidated feature backlog](#b3-consolidated-feature-backlog-9-column-canonical) · [B4 Gate & Priority](#b4-delivery-gate--priority) · [B5 Discovery deliverables](#b5-discovery-gate-deliverable-register) · [B6 Traceability](#b6-feature--governing-spec-traceability) · [B7 Reserved for AC](#b7-cross-cutting-standards-reserved-for-ac)
- *(Sprint 0 Topic → Concern → AC detail in [`docs/sprint-0-foundation-criteria.md`](../../docs/sprint-0-foundation-criteria.md).)*"""

assert old_header in content, "Header mismatch — file structure changed?"
content = content.replace(old_header, new_header)

# Path substitutions — file is now 2 levels deep (confluence-export/01-about/)
# so all relative refs need ../../ prefix where they previously had ./ or ../

# 1. ./sprint-0-foundation-criteria.md  →  ../../docs/sprint-0-foundation-criteria.md
content = content.replace("[`sprint-0-foundation-criteria.md`](./sprint-0-foundation-criteria.md)",
                          "[`sprint-0-foundation-criteria.md`](../../docs/sprint-0-foundation-criteria.md)")

# 2. `research/spec-docs/...`  →  `../../research/spec-docs/...`  (in references)
content = re.sub(r'`research/spec-docs/', '`../../research/spec-docs/', content)

# 3. `conventions/features-conventions.md`  →  `../../conventions/features-conventions.md`
content = content.replace('`conventions/features-conventions.md`', '`../../conventions/features-conventions.md`')

# 4. `(this file)` reference in S0-02 row remains valid (now refers to roadmap-milestones)
# No change needed.

DEST.write_text(content, encoding='utf-8')
print(f"Wrote {DEST} ({len(content):,} chars · {content.count(chr(10))} lines)")

# Replace planning.md with a redirect pointer
pointer = """# Trackaroo® Phase 1 — Delivery Planning (RELOCATED)

> ⚠️ **This file has moved.** The delivery plan + backlog is now maintained in the Confluence workspace at:
>
> **➡️ [`confluence-export/01-about/02-roadmap-milestones.md`](../confluence-export/01-about/02-roadmap-milestones.md)**

## Why moved

The Confluence-bound workspace (`confluence-export/`) is now the authoritative home for project planning so the team can read, edit, and import it directly into Confluence Cloud. The file there is the **single source of truth** for delivery planning going forward.

## What's still in this repo (NOT moved)

- **`docs/sprint-0-foundation-criteria.md`** — 45 Sprint 0 Foundation ACs (Topic → Concern → AC). Stays in repo for BA analysis.
- **`docs/gap-clarifications.md`** — Open clarification register (CLR-TRK-NNN). Stays in repo (operational tool).
- **`research/spec-docs/`** — 20 spec doc extracts. Stays in repo.
- **`diagrams/`** — Architecture diagrams. Stays in repo.
- **`conventions/`** — Project conventions (ID rules, AC writing, etc.). Stays in repo.

## Historical content

The full delivery plan content (Sprint timeline, deliverable checklists, 51-feature backlog, traceability, etc.) was last in this file on 2026-05-31 before being moved. Git history preserves prior versions; use `git log -- docs/planning.md` to access them.
"""

SRC.write_text(pointer, encoding='utf-8')
print(f"Replaced {SRC} with redirect pointer ({len(pointer)} chars)")
