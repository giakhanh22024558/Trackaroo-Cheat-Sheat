# Drive Docs — Trackaroo® Phase 1 Workspace

Project workspace pages structured for **upload to Google Drive** (manual upload — you handle the actual upload). The folder hierarchy here mirrors the intended Drive folder tree.

## Folder structure (= intended Drive folder tree)

```
drive-docs/
├── README.md                       ← this file (do not upload)
├── 00-home.md                      ← workspace home / landing
├── 01-about/                       ← 📘 1. ABOUT — Project & Team
│   ├── _index.md                   ← section landing page
│   ├── 01-overview.md
│   ├── 02-roadmap-milestones.md    ⭐ live delivery plan + backlog
│   ├── 03-team-contacts.md          ⭐ filled from CMP-5026 + Squad §1.3
│   ├── 04-ways-of-working.md
│   ├── 05-story-ac-conventions.md
│   ├── 06-change-request-process.md
│   ├── 07-tool-stack.md
│   ├── 08-onboarding.md
│   └── 09-glossary.md
├── 02-product/                     ← 📗 2. PRODUCT
│   ├── _index.md
│   ├── 01-system-overview.md
│   ├── 02-user-roles.md
│   ├── 03-modules/                 ← Per-module pages + canonical backlog
│   │   ├── _index.md               ⭐ full 51-feature backlog (9-column)
│   │   └── 01-navigation.md … 11-poi.md
│   └── 04-shared-features.md
├── 03-rules/                       ← 📕 3. RULES
│   ├── _index.md
│   ├── 01-business-rules.md
│   ├── 02-permission-matrix.md
│   ├── 03-data-dictionary.md
│   └── 04-ux-guidelines.md
└── 04-tech/                        ← 📙 4. TECH
    ├── _index.md
    ├── 01-architecture-overview.md
    ├── 02-erd.md
    ├── 03-api-integration.md
    ├── 04-infrastructure-environments.md
    ├── 05-security-auth.md
    ├── 06-adr-decision-records.md
    └── 07-tech-standards.md
```

## How to upload to Drive (manual)

### Option A — Drag-and-drop entire folder (fastest)

1. Open Drive in browser → navigate to target parent folder (e.g. *TRACKAROO 2026 RFT Phase 1*).
2. Drag the `drive-docs/` folder from Windows Explorer → Drive. Drive uploads the full hierarchy preserving sub-folders.
3. Files upload as `.md` (raw markdown). They remain editable as text but Drive's preview won't render markdown formatting.

### Option B — Convert to Google Docs on upload (richer view)

1. Drive Settings → **Convert uploads** → toggle ON.
2. Drag the folder. Each `.md` becomes a native **Google Doc** — tables, headings, links render properly.
3. Caveat: **Mermaid `gantt` / diagram code blocks lose rendering** — they appear as monospace text. For 02-roadmap-milestones.md you'll want to either (a) keep as `.md`, (b) export gantt to image and paste in, or (c) edit out the gantt code blocks after upload.

### Option C — `gdrive` CLI (scriptable)

```bash
gdrive upload --recursive --parent <PARENT_FOLDER_ID> drive-docs
```

Add `--convert` to auto-convert to Google Docs.

## Recommended upload strategy

| Folder / file | Recommendation | Why |
|---|---|---|
| `00-home.md` | **Convert to Google Doc** | Pure text, links work, easier landing page |
| `01-about/02-roadmap-milestones.md` | **Keep as `.md`** | Heavy Mermaid gantt content — loses rendering in Docs |
| `01-about/03-team-contacts.md` | **Convert to Google Doc** | All tables, no diagrams — tables render fine in Docs |
| `02-product/03-modules/_index.md` | Convert to Google Doc | Big backlog table — Docs handles tables well |
| Skeleton detail pages (most others) | Either | Light content, draft state — pick your preference |
| `_index.md` section landings | Convert to Google Doc | Navigation tables |

## After upload

- Drive lets you organize via drag/drop in the UI.
- Edit pages in Google Docs (if converted) or via local editor + re-upload (`.md`).
- If you re-edit locally, the canonical content is in this repo — re-upload to refresh Drive.

## Content conventions

- **Language:** English (per project deliverable rule in `CLAUDE.md`).
- **Trademark terms** preserved: SOS, BackTrack™, TrackMate™, TrackIQ™, HazTrack™, PCR, CAL.
- **Cross-references** within this workspace use relative paths (`./01-overview.md`). They become file-name references in Drive; user clicks the linked file in Drive UI.
- **Tables** preferred over long bullet lists.
- **Diagrams** referenced (`../../diagrams/...drawio`) live in the repo, not in Drive — embed via screenshot in Docs if needed.

## Source of truth

| Artefact | Source of truth | Location |
|---|---|---|
| **Delivery plan + backlog** | **This folder** (`01-about/02-roadmap-milestones.md` + `02-product/03-modules/_index.md`) | Edits here, re-upload to refresh Drive copy |
| Sprint 0 Foundation criteria (45 ACs) | Repo (`docs/sprint-0-foundation-criteria.md`) | — |
| Open clarification register (CLR-TRK) | Repo (`docs/gap-clarifications.md`) | — |
| Spec extracts (20 docs) | Repo (`research/spec-docs/*.md`) | — |
| Architecture diagrams | Repo (`diagrams/`) | — |

## NOT included in this folder (do not upload)

- `MasterMind/` — read-only skill library, not project documentation
- Internal vendor proposals — referenced but not duplicated
- Day-to-day sprint backlog (Jira will own this when set up)
- `docs/gap-clarifications.md` — operational tool, kept in repo
