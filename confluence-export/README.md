# Confluence Export — Trackaroo® Phase 1

Generated Confluence-ready Markdown pages for **import into a Confluence Cloud space**. Mirrors the canonical workspace structure (Home · ABOUT · PRODUCT · RULES · TECH).

## Folder structure (= Confluence page tree)

```
confluence-export/
├── README.md                       ← this file (NOT imported)
├── 00-home.md                      ← Space Home (landing page)
├── 01-about/                       ← 📘 1. ABOUT — Project & Team
│   ├── _index.md                   ← section landing page
│   ├── 01-overview.md
│   ├── 02-roadmap-milestones.md
│   ├── 03-team-contacts.md
│   ├── 04-ways-of-working.md
│   ├── 05-story-ac-conventions.md
│   ├── 06-change-request-process.md
│   ├── 07-tool-stack.md
│   ├── 08-onboarding.md
│   └── 09-glossary.md
├── 02-product/                     ← 📗 2. PRODUCT — Product spec
│   ├── _index.md
│   ├── 01-system-overview.md
│   ├── 02-user-roles.md
│   ├── 03-modules/
│   │   ├── _index.md
│   │   ├── 01-navigation.md        (EPIC-001)
│   │   ├── 02-sos.md               (EPIC-002)
│   │   ├── 03-backtrack.md         (EPIC-003)
│   │   ├── 04-haztrack.md          (EPIC-004)
│   │   ├── 05-first-aid.md         (EPIC-005)
│   │   ├── 06-app-experience.md    (EPIC-006)
│   │   ├── 07-operations-console.md (EPIC-007)
│   │   ├── 08-trackiq.md           (EPIC-008)
│   │   ├── 09-pcr.md               (EPIC-009)
│   │   ├── 10-trackmate.md         (EPIC-010)
│   │   └── 11-poi.md               (EPIC-011)
│   └── 04-shared-features.md
├── 03-rules/                       ← 📕 3. RULES — Business rules & conventions
│   ├── _index.md
│   ├── 01-business-rules.md
│   ├── 02-permission-matrix.md
│   ├── 03-data-dictionary.md
│   └── 04-ux-guidelines.md
└── 04-tech/                        ← 📙 4. TECH — Architecture & engineering
    ├── _index.md
    ├── 01-architecture-overview.md
    ├── 02-erd.md
    ├── 03-api-integration.md
    ├── 04-infrastructure-environments.md
    ├── 05-security-auth.md
    ├── 06-adr-decision-records.md
    └── 07-tech-standards.md
```

## How to import into Confluence

### Option A — Bulk markdown import (recommended)

1. Install the **"Markdown to Confluence"** or **"Scroll Documents"** app in your Confluence Cloud space.
2. Create a new Confluence Space (e.g., `Trackaroo Phase 1`).
3. Use the importer's bulk-upload feature; point it at this folder.
4. The importer reads each `.md` file = one Confluence page; folder hierarchy = page hierarchy. `_index.md` becomes the parent page for each folder.

### Option B — Manual import (per page)

For each `.md` file:
1. In Confluence, create the page at the correct position in the tree.
2. Use **Insert → Markup → Markdown** and paste the file content.
3. Confluence converts markdown to its native format on save.

### Option C — Confluence REST API (scripted)

Use the [Confluence Cloud REST API](https://developer.atlassian.com/cloud/confluence/rest/v2/) `POST /content` endpoint, iterating over files. Pass `representation: "wiki"` or convert markdown → HTML first.

## Content conventions

- **Language:** English (per project deliverable rule in `CLAUDE.md`).
- **Trademark terms** preserved as-is: SOS, BackTrack™, TrackMate™, TrackIQ™, HazTrack™, PCR, CAL.
- **Cross-references** within the workspace use Confluence-style page mentions where helpful (`See [Module: PCR]`); external project artefacts referenced by repo path (`research/spec-docs/<doc>.md`).
- **Tables** preferred over long bullet lists for matrices (RBAC, BR catalog, data dictionary).
- **Diagrams** referenced (`diagrams/...drawio`) — embed via Confluence's draw.io integration after import.

## Source artefacts (what fed each page)

| Page section | Pulled from |
|---|---|
| Home, ABOUT, Tool stack, Glossary | `docs/planning.md`, `CLAUDE.md`, `MASTERMIND-INTEGRATION.md`, `conventions/features-conventions.md` |
| ABOUT Roadmap, Team, Ways of Working | `docs/planning.md` §A1/A2, `research/spec-docs/Slitigenz-Proposal-RFT5026.md` |
| PRODUCT system overview, modules | `research/spec-docs/PRD-5126.md`, `FSD-5126.md`, per-module spec extracts |
| PRODUCT user roles | `research/spec-docs/TAA-5126.md` (6 archetypes), `OCS-5026.md` (3 console roles) |
| RULES business rules | `research/spec-docs/UXS-5726.md`, `OSM-5026.md`, `BTF-5126.md`, `CDG-5126.md`, `FSD-5126.md` |
| RULES permission matrix | `research/spec-docs/OCS-5026.md` §5.2 RBAC + `CDG-5126.md` |
| RULES data dictionary | `research/spec-docs/CDG-5126.md` §5 schemas + `BTF-5126.md` |
| RULES UX guidelines | `research/spec-docs/UXS-5726.md`, `WFD-5126.md`, `FQH-5026.md` |
| TECH architecture | `diagrams/1-overview/`, `2-subsystems/`, `research/spec-docs/AOD-5026.md` |
| TECH security | `research/spec-docs/CDG-5126.md`, `ESF-5026.md`, `SFD-5026.md` |
| TECH ADR | New — to seed from key Phase 1 architectural decisions |

## Maintenance

When project artefacts change:
- **Source of truth stays in the repo** (`docs/`, `research/spec-docs/`, `diagrams/`).
- Re-run the export to refresh the Confluence pages (or edit the changed `.md` here + re-import).
- Do NOT manually edit pages in Confluence and expect the repo to sync — Confluence is the **read view**, repo is the **source of truth**.

## NOT included in this export

- `MasterMind/` skill library (read-only library, not project documentation)
- Internal vendor proposals (`research/spec-docs/Slitigenz-Proposal-RFT5026.md` referenced but not duplicated)
- Gap-clarification register (`docs/gap-clarifications.md`) — operational tool, may be added later if needed
- Day-to-day sprint backlog (Jira will own this once import to Jira happens)
