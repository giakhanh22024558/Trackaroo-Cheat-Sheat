# features-conventions.md

Overrides defaults of skill [`document/features`](../MasterMind/models/model_001/document/features/conventions-defaults/).

> Leave empty to use skill defaults. Uncomment + fill the blocks below to override.

## ID formats

```yaml
id_formats:
  epic:  "EPIC-{n:03d}"      # PROJECT OVERRIDE → 3-digit (EPIC-001), per user request
  feature: "FEAT-{n:03d}"    # default (canonical prefix FEAT- kept for tooling compatibility)
  story: "STORY-{n:03d}"     # default
  ac:    "AC-{story_num}-{n:02d}"  # default
```

## ⭐ Priority-ordered ID assignment (PROJECT RULE)

> **Implicit rule for this project:** lower ID number = higher delivery priority.
> `EPIC-001` / `FEAT-001` is the **most prioritized** item.

- **Priority = earliest delivery gate** (Discovery → Alpha → Beta-Ready → GA). See "Delivery Gate & Priority" (§B4) in `docs/planning.md`.
- **Epics** are numbered in priority order → tiers fall into contiguous ID ranges:
  - `EPIC-001 … EPIC-005` = **Very high** (Discovery)
  - `EPIC-006 … EPIC-012` = **High** (Alpha)
  - `EPIC-013 … EPIC-016` = **Medium** (Beta-Ready)
- **Features** are numbered by walking Epics in priority order, then by feature priority **within** each Epic. So `FEAT-001` is the highest-priority feature of the highest-priority Epic. (Mixed Epics may carry a lower-priority feature with a small ID because it sits under a high-priority Epic — the feature-tier table in `docs/planning.md` §B4 shows each feature's exact priority.)
- **Re-derivation vs incremental add:** IDs are assigned in priority order during a *major (re-)derivation pass*. For *incremental* additions between passes, append at the tail (highest number) and fold into priority order at the next major pass — avoids constant renumbering churn while honoring the skill's "sequential, never reused" principle.
- This rule is **project-scoped** (recorded here). It does not change the MasterMind model default (which assigns IDs in discovery order, not priority order).

## ⭐ Backlog scope rule — business features only (PROJECT RULE)

> **Epics/Features = business-functional features only.** Cross-cutting / foundational concerns do NOT belong in the feature backlog.
>
> **Single source:** all planning + backlog now lives in **`docs/planning.md`** (Part A = plan, Part B = registers). The former `backlog.md` and `sprint-0-foundation.md` were merged into it.

- **Feature backlog — `docs/planning.md` §B3 (EPIC-/FEAT-):** end-user / operator **business capabilities** (navigation, SOS, BackTrack, HazTrack, First Aid, TrackIQ, PCR, TrackMate, POI, OCS modules, app experience).
- **Sprint 0 register — `docs/planning.md` §B2:** cross-cutting foundation that serves **every** module — overall architecture, infra/CI-CD, foundational data model, auth, code standards, design system, UX guidelines, RBAC/permission matrix, business-rule/compliance baselines, Phase 2 inert scaffolds, public site. Built first as the foundation (Sprint 0 / run-up to Discovery gate).

### Foundation hierarchy naming (PROJECT RULE)

Sprint 0 separates **the work (tasks)** from **how it is assured (criteria)** (it has no end-user stories):

| Layer | Sprint 0 | ID |
|---|---|---|
| The task list — everything Sprint 0 does (not all are hand-overs) | **Task** | `S0-NN` (analysis · documents · site · Figma · codebase) |
| Analysis grouping (theme) | **Topic** | `TOPIC-NN` |
| Analysis area | **Concern** | "Concern N" (the 10 technical concerns) |
| Done-criteria per concern | **Acceptance Criteria** | `AC-C{concern}-{nn}`, language `en`, confirmed at Discovery gate |

- **Tasks (`S0-`)** — 9 items (see `docs/planning.md` §B2.1): business analysis · build backlog · 4 documents · site · Figma · codebase/CI. A **Customer hand-over?** flag marks which are client deliverables (Discovery artefacts) vs internal foundation work. The former per-task `FND-` IDs are retired.
- **Topic → Concern → Acceptance Criteria** is the assurance layer; each criterion notes which **Task (`S0-`)** it validates + which Discovery artefact (D#) it evidences. **Lives in [`docs/sprint-0-foundation-criteria.md`](../docs/sprint-0-foundation-criteria.md)** (moved out of planning.md so BA can analyse separately without bloating the delivery plan).
- **Sources:** tasks → `docs/planning.md` §B2.1 · criteria → `docs/sprint-0-foundation-criteria.md` · gate deliverable register → `docs/planning.md` §B5. Each criterion `AC-C{concern}-{nn}` is unique — never renumber after issue.
- **Link model:** a business feature builds on the Sprint 0 tasks' outputs and asserts foundation standards (5-Q hierarchy, prohibited mutations, WCAG, RT/RG, thresholds) as **Acceptance Criteria** — the standard itself is never a feature.

## Priority levels

```yaml
# priority_values:
#   - Very high     # default order: highest → lowest
#   - High
#   - Medium
#   - Low
```

## Status / Lifecycle

```yaml
# status_values:
#   - Backlog
#   - Ready
#   - In Progress
#   - In Review
#   - Done

# lifecycle_values:
#   - Active
#   - Done
#   - Archived
#   - Superseded
```

## AC writing format

Pick **one** language per project — never mix within a file.
See [`ac-writing.md`](../../MasterMind/models/model_001/document/features/conventions-defaults/ac-writing.md) for full guidance and examples.

```yaml
ac_writing:
  language: en              # en (default) → "Given/When/Then"
                            # vi           → "Nếu/Khi… thì…"
  # max_per_story: 10       # optional — suggested max ACs per story
```

Reference patterns:
- **EN (GWT):** `Given a missing required field, when clicking Save, then the Save button is disabled`
- **VI:** `Nếu thiếu field bắt buộc, thì nút Lưu disable`

## Sheet layout (when rendering xlsx)

```yaml
# sheet_layout:
#   epic_color:    "7030A0"     # purple (default)
#   feature_color: "BDD7EE"     # light blue (default)
#   story_color:   ""           # white = no fill (default)
#   header_color:  "1F4E79"     # canonical dark blue
```

## Project-extended columns (optional)

The canonical 9 columns at A–I are fixed. If the user has explicitly asked for
extra columns for this project, declare them here and they will be appended at
column J onwards, in the order listed. Scoped to this project only — does not
propagate to other projects. To make an extension a global default, ask the
agent to *"save this to the model"*.

```yaml
# extra_columns:
#   - header: "SRS Feature ID"
#     filled_on: feature          # epic | feature | story
#     type: text                  # text | dropdown | checkbox | date | number | formula
#     notes: "Anchor to SRS section"
#
#   - header: "AC count"
#     filled_on: story
#     type: formula
#     formula: "=COUNTIF('Acceptance Criteria'!A:A, E{row})"
#
#   - header: "Sprint"
#     filled_on: story
#     type: dropdown
#     values: ["MVP-1", "MVP-2", "MVP-3", "Backlog"]
#
#   - header: "Owner"
#     filled_on: story
#     type: text
```
