# Trackaroo Phase 1 — Project Conventions

## ⚠️ Working interaction rules (READ FIRST)

**Do NOT auto-apply changes when the user asks for analysis, check, audit, or review.**

User intent signals — distinguish carefully:

| Intent (analyze only — present findings, wait for approval) | Intent (apply changes — execute immediately) |
|---|---|
| "kiểm tra giúp mình…" / "check for me…" | "thực hiện…" / "apply…" / "do it" |
| "phân tích thử…" / "analyze…" | "fix giúp mình…" / "làm giúp mình…" |
| "xem giúp…" / "review…" | "update…" / "thay đổi…" with explicit target |
| "có cần…?" / "should we…?" | "execute…" / "make it so…" |
| "nếu… thì sao?" / "what if…?" | "apply A and B" (explicit list of items to action) |
| Open-ended question about architecture | "save this", "add this", "remove this" with concrete object |

**When user intent is unclear:** present the analysis + plan, then **ask explicit yes/no** before applying any file change. Default to asking, not doing.

**Exceptions where auto-apply IS appropriate:**
- User explicitly enumerates changes in their request ("A + B + C, apply ngay")
- User said "apply ngay" / "execute" in previous turn for the SAME scope
- Trivial follow-up cleanup of an already-approved change (e.g., updating a cross-reference after a rename you just executed)

**If in doubt:** present 1-2 sentences of intent confirmation: *"Bạn muốn mình apply ngay hay chỉ analyze?"*

This rule applies to: file edits, diagram changes, design-decisions rows, compliance matrix entries, drawio cells, Python scripts, ANY change to project artifacts.

---

## Folder structure (C4-style, 4-tier)

```
Trackaroo local management/
├── CLAUDE.md                                  ← this file
├── diagrams/
│   ├── README.md                              ← navigation map (read this first)
│   │
│   ├── 1-overview/                            ← TIER 1 · Master architecture (exec-readable)
│   │   ├── trackaroo-phase1-architecture.md   (Mermaid source · stripped to 1-line components)
│   │   └── trackaroo-phase1-architecture.drawio  (symlink → Google Drive · multi-page)
│   │
│   ├── 2-subsystems/                          ← TIER 2 · Per-zone component deep-dives
│   │   ├── cbe-trackiq-pipeline.md            (CBE-5000 detail)
│   │   ├── mob-survival-core.md               (MOB-2000 detail)
│   │   ├── mob-application-layer.md           (MOB-1000 detail)
│   │   ├── ocs-operations-console.md          (OCS-5026 detail)
│   │   └── syn-firestore-sync.md              (SYN-7000 detail)
│   │
│   ├── 3-flows/                               ← Behavioral views (how data/state moves)
│   │   ├── data-flow/                         (Yourdon-notation DFDs)
│   │   │   ├── dfd-survival-core.md
│   │   │   └── dfd-trackiq-pipeline.md
│   │   ├── sequence/                          (seq-*.md when created)
│   │   └── state/
│   │       └── state-trackaroo-transitions.md
│   │
│   └── 4-cross-cutting/                       ← TIER 3 · System-wide concerns
│       ├── compliance-matrix.md               (all [X] PROHIBITED + rationale)
│       ├── performance-targets.md             (all numeric SLAs in one place)
│       └── tile-lifecycle.md                  (tile journey across subsystems)
│
├── research/                                  ← External knowledge / synthesis notes
│   ├── mapbox-sdk-overview.md
│   └── tech-stack-inventory.md
│
└── (other project files: spec, epics, etc.)
```

**The 4 tiers — what goes where:**

| Tier | Folder | Purpose | Audience |
|---|---|---|---|
| **1** | `1-overview/` | One bird's-eye picture. Zones + 1-line component names. No implementation detail. | Execs · vendors at first contact · onboarding |
| **2** | `2-subsystems/` | Deep-dive into one zone at a time. Component-level (C4 Level 3). Schemas, internal flows, implementation choices. | Devs · vendor implementers · spec reviewers |
| **3** | `3-flows/` | Behavioral views — how data/state moves at runtime. DFDs · sequence · state. | Devs · QA · integration testers |
| **3** | `4-cross-cutting/` | Concerns spanning multiple zones — compliance prohibitions, performance SLAs, artifact lifecycles. | Auditors · compliance · architects |

**Rule of thumb:** If a piece of info applies to **>1 zone**, it belongs in `4-cross-cutting/`, not bolted onto each subsystem diagram.

**Conventions for adding new diagrams:**
- Adding to a tier: drop into the right folder, follow naming below.
- New tier-2 deep-dive (new zone): create file `<zone-prefix>-<short-name>.md` in `2-subsystems/`.
- New flow type (e.g. sequence): create sub-folder under `3-flows/` with 1+ files.
- New cross-cutting concern: single file in `4-cross-cutting/` named after the concern.
- Always keep `diagrams/README.md` navigation map in sync with new files.

**File naming (kebab-case):**
- Subsystem deep-dives: `<zone>-<descriptor>.md` (e.g. `cbe-trackiq-pipeline.md`)
- DFDs: `dfd-<scope>.md` (e.g. `dfd-survival-core.md`)
- Sequence: `seq-<scenario>.md`
- State: `state-<entity>.md`
- ERD: `erd-<domain>.md`
- Cross-cutting: descriptive noun (`compliance-matrix.md`, `tile-lifecycle.md`)

## Google Drive sync

The main architecture `.drawio` is a symlink to Google Drive:
- Local: `diagrams/1-overview/trackaroo-phase1-architecture.drawio`
- Drive target: `G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\trackaroo-phase1-architecture.drawio`

Edits via the local symlink path auto-sync to Google Drive (and team members with access see updates within seconds). When editing the symlink target, use the resolved G:\ path directly — Edit tool refuses to write through symlinks.

# Diagram Visual Style Guide

When generating Mermaid architecture diagrams in this project, follow this visual style.
This captures *how* to render, not *what* to render — the content varies per request.

## Mermaid Header

```
---
config:
  layout: elk
  theme: base
  themeVariables:
    fontFamily: Arial
    fontSize: 13px
---
graph LR        # or TB depending on whether columns or rows dominate
```

- Always use `layout: elk` for clean orthogonal routing.
- Use `graph LR` when the diagram has 2–3 major zones side-by-side.
- Use `graph TB` when the hierarchy is strictly top-down.

## Macro Layout

- **Multi-zone composition:** wrap the diagram in 2–4 large outer subgraphs that act as colored "zones" or "columns."
- Inside each zone, place **white inner boxes** (the individual components).
- Zones may contain nested subgraphs (e.g., Platform → Core Zone + Experience Zone, separated by a boundary marker).
- Use a dashed marker node (e.g., `{{"- - - - - BOUNDARY - - - - -"}}`) to visualize architectural separations between nested zones.

## Color Palette (zone backgrounds)

| Zone purpose | Fill | Stroke |
|---|---|---|
| Device / hardware / input matrix | `#e3f2fd` (light blue) | `#1976d2` |
| Survival / safety-critical / offline core | `#c8e6c9` or `#e8f5e9` (green) | `#2e7d32` |
| Mobile app / Experience layer (outer container) | `#bbdefb` (light blue) | `#0277bd` |
| Mobile app — Application sub-layer | `#e3f2fd` (lighter blue) | `#1976d2` |
| Mobile app — Local data persistence | `#f3e5f5` (lavender) | `#6a1b9a` |
| Cloud backend (compute + database) | `#d1c4e9` (light purple) | `#5e35b2` |
| Cloud backend nested sub-groups | `#ede7f6` (lighter purple) | `#5e35b2` |
| Web app / Operations Console | `#b2dfdb` (teal) | `#00695c` |
| Web app nested sub-groups | `#e0f2f1` (lighter teal) | `#00695c` |
| Sync engine (Firebase Firestore) | `#fff9c4` (light yellow) | `#f9a825` |
| External network / providers | `#ffe0b2` or `#fff3e0` (peach) | `#e65100` |
| Companion website / public-facing CMS | `#f5f5dc` (beige) | `#827717` |
| Data persistence — app data (Firestore) | `#e1f5ff` | `#0277bd` |
| Data persistence — core data (local/WAL) | `#f3e5f5` (purple, dashed border) | `#6a1b9a` |

## Tech Stack Notes (mandatory per zone)

Each zone subgraph title MUST include a one-line tech stack note in italics on a second line, format:
```
<b>ZONE NAME</b><br/><i>Tech: stack details · constraints</i>
```

Examples:
- `<b>MOBILE APPLICATION</b><br/><i>Tech: Flutter · Dart · iOS 15+ / Android 13+ · Dual-Layer Architecture</i>`
- `<b>OPERATIONS CONSOLE (OCS-5026)</b><br/><i>Tech: React · Firebase Auth · RBAC · TLS 1.3</i>`
- `<b>CLOUD BACKEND</b><br/><i>Tech: AWS / GCP · self-hosted servers</i>`
- `<b>FIREBASE FIRESTORE — Cloud Sync Engine</b><br/><i>Tech: Firestore real-time DB · auto offline persistence</i>`
- `<b>COMPANION WEBSITE</b><br/><i>Tech: WordPress / Headless CMS</i>`

For individual leaf components with notable tech (databases, encrypted stores), include the tech inline in the description (e.g. `Tech: SQLite + WAL · AES-256 at rest`).

## Component Boxes (inner nodes)

- **Default style:** white fill `#ffffff`, grey stroke `#555`, 1px width, black text `#000`.
- **Bold header** on the first line via `<b>...</b>`, then bulleted body lines with `<br/>- item` separators.
- Keep boxes **text-only** — no emoji icons inside the inner boxes (icons live in zone titles only if useful).
- Multi-line content is preferred over single labels — pack 3–6 bullets per box.

### Special node variants

| Variant | Style |
|---|---|
| Constraint / warning banner | `fill:#ffebee, stroke:#c62828, color:#b71c1c` (red box, red text) |
| Compliance / prohibition callout | `fill:#fff5f5, stroke:#c62828, color:#b71c1c` (red text on near-white) |
| Inert scaffold / Phase-2 placeholder | `fill:#fafafa, stroke:#9e9e9e, stroke-dasharray:5 5, color:#616161` (greyed, dashed) |
| Separation boundary marker | hexagon shape `{{...}}`, `stroke-dasharray:6 4, color:#000` |
| Database / datastore | cylindrical `[(...)]` shape, purple fill if core/local, blue if cloud |

## Edges

- **Solid arrow** `-->` = active hardware/runtime dependency or operational/control relationship.
- **Dashed arrow** `-.->` = optional / conditional / metrics / surfacing.
- **Dotted purple arrow** `-.->` with `stroke-dasharray:2 3` = data payload / data-flow relationship. Style via `linkStyle <idx> stroke:#6a1b9a,stroke-width:2px,stroke-dasharray:2 3` so the tight dot pattern + purple color distinguishes it from the longer-dashed `-.->` optional/surfacing arrows.
- **Red dashed prohibited edge:** use `linkStyle <idx> stroke:#c62828,stroke-width:2px,stroke-dasharray:5 5` and label it `<b>[X] PROHIBITED</b><br/>(reason)`.
- **Always label edges** with the protocol, payload, or semantic (`scrape`, `HTTP load NodePort 30080`, `cache / session`, `persistence writes`).
- Use `<br/>` for multi-line edge labels.

### Edge label phrasing (mandatory)

- **Operational / control edge labels MUST be in verb form** (solid `-->` and dashed `-.->` arrows), describing the action one component performs on the other. Never use bare nouns.
- The verb is conjugated for the source node ("Surfaces …", "Enables …", "Writes …", "Scrapes …").
- Bad: `Operational Visibility` · `Intervention and Control` · `Cache & Sessions` · `DB queries`
- Good: `Surfaces scoring pipeline` · `Enables break-glass intervention` · `Writes cache / session` · `Queries database`
- If the relationship is bidirectional or symmetric, phrase from the arrow's source side; or use two separate edges with one verb each.
- Parenthetical detail after the verb phrase is fine for context (e.g. `Surfaces scoring pipeline (Ingest · DEM Enrichment · Scoring · Tile Publish)`).
- **Exception — data-payload edges** (dotted purple `-.->` arrows with `stroke-dasharray:2 3`): label with the data noun itself (e.g. `TrackIQ Scoring Data`, `User profile`, `Breadcrumb stream`). The arrow style + color already conveys "this is a data flow", so the label names the payload rather than describing an action.

### Edge labels referencing design decisions / spec IDs (mandatory format)

When an edge label needs to point to an authoritative source — design-decision row (`M0a`–`M0X`, `F3`, etc.), compliance matrix section (`§X`), spec authority (`BTF-5126`, `FRM-5126`, etc.), or named rejection trigger (`RT-02`, `RT-05`) — use this format for balance between **compactness** and **self-explanation**:

**Format:** `(<reference-ID> · <1-word characterization>)`

Or chained: `(<owner/context> · <reference-ID> <characterization>)`

**Why this pattern:**
- Pure references (`per M0f`) are compact but force vendors to open `design-decisions.md` to understand the semantic — friction
- Pure characterizations (`Firebase-independent peer mesh queue`) are self-explanatory but lose audit trail to the decision rationale
- Combined form keeps the reference ID for traceability AND gives an immediate one-word semantic clue

**Good examples (apply this format to new edges):**
- `(CAL Comms · M0f Firebase-independent)` — App-layer queue edge
- `(consent-gated · M0h opt-in)` — PRO_LOG sync edge
- `(M0i unified-store)` — SQLITE_STORE container note
- `(F3 write-once)` — PCR Firestore collection edge
- `(§7 cache-only)` — HazTrack Firebase ingress edge (also red font per exception flag)
- `(RT-02 no auto-reroute)` — NAV prohibited route-recalc edge
- `(RT-05 no cloud sync)` — BT breadcrumb prohibited edge
- `(BTF-5126 forensic-immutable)` — SOS log immutability edge note

**Bad — pure reference (forces lookup, no semantic):**
- ❌ `(per M0f)` — vendor must consult docs to understand what M0f says
- ❌ `(§7 exception)` — exception of what?
- ❌ `(BTF-5126)` — what does this mandate?

**Bad — pure characterization (loses traceability):**
- ❌ `(Firebase-independent peer mesh queue per Slitigenz proposal)` — verbose · no decision-row pointer
- ❌ `(cache-only with TTL refresh)` — which mandate authorizes this exception?

**The 1-word characterization should be:**
- A **distinguishing semantic** (what makes this relationship distinct from others) — not a generic descriptor
- Hyphenated if multi-word (`Firebase-independent`, `consent-gated`, `auto-reroute`, `write-once`) — reads as a single concept
- Short enough that label stays scannable at one glance (≤2 hyphenated words ideal)

## Subgraph Titles

- All caps + bold for top-level zones: `<b>SURVIVAL CORE EXECUTION ZONE (100% OFFLINE)</b>`.
- Add a tagline as a second line if there's a defining constraint: `<br/>Deterministic | Non-adaptive | No network dependency`.
- Title case + bold for nested subgraphs.

## Mandatory Inclusions

- **Legend node** in the right/external zone explaining arrow semantics and prohibited markers.
- **Standards / spec references** in box headers when applicable (e.g., `BPS-5126 §4`, `UXS-5726 §4.2`, `RT-09`).
- **Performance / compliance callouts** as red-styled boxes adjacent to the relevant zone, not embedded inside it.

## Same-Level Visual Consistency (mandatory)

- **Components at the same hierarchy level MUST share identical styling** (fill, stroke color, stroke width, stroke-dasharray, shape, font weight).
- If one sibling at a given level is rendered as a subgraph container (e.g. because it has nested children), every other sibling at that same level should also be wrapped as a subgraph with the same border treatment — even if it only contains a single descriptive node. Do not mix bare nodes with container subgraphs at the same level.
- Example: if `APL-1301` is a subgraph (white fill, blue stroke), `APL-1306` at the same level inside `APL-1300` must also be a subgraph with the same white fill and blue stroke, not a plain whiteBox node.
- This rule trumps content-density differences. Visual peer recognition matters more than minimizing nesting depth.

## Anti-patterns (avoid)

- Smooth bezier curves — always force `curve: linear` or use ELK layout.
- Colorful inner boxes — keep the inner components white; let the zone color do the work.
- Single-word labels — every box should have a bold title plus context bullets.
- Crossing edges through unrelated zones when a side-route exists.
- Emoji-heavy inner nodes (reference style is text-first; emojis only as light accents on zone headers when needed).

---

# DFD authoring convention (Tier-3 data-flow diagrams)

When building any DFD in `diagrams/3-flows/data-flow/<name>.drawio`, follow this template so all DFDs share one visual language and vendors can cross-map them 1:1 against the master architecture.

## Core principle — "Architecture as canvas, DFD as overlay"

Every DFD `.drawio` file is built on top of a **full copy of the master architecture canvas** (`trackaroo-phase1-architecture.drawio`). Do NOT redraw a stripped-down subsystem view. Reasons:

- Same component IDs, same colors, same positions → vendor maps DFD ↔ architecture by sight, no mental translation
- Stays in sync when architecture evolves (re-copy canvas, re-apply overlays)
- Out-of-scope components remain visible as architectural context, not deleted

## The 5-step recipe for a new DFD

1. **Copy canvas** — duplicate the full architecture file to `diagrams/3-flows/data-flow/dfd-<scope>.drawio`. Preserve every layer, component, zone, and existing edge.
2. **Copy DFD_LEGEND cell** — copy the legend block from `dfd-survival-core.drawio` (the reference template). Update the `► SCOPE OF THIS FILE` line to name the subsystem in scope.
3. **Grey out non-scope cells** — run a per-DFD grey-out script modeled on `.scripts/grey-out-non-survival-core.py`:
   - Define `KEEP_IDS` set = the in-scope subsystem cells + direct touchpoints + the legend
   - Everything else becomes light grey (`fillColor=#f5f5f5`, `strokeColor=#bdbdbd`, `fontColor=#bdbdbd`, `strokeWidth=1`) with `value=""` (text cleared)
   - Script must preserve structural style attrs (`shape`, `container=1`, `dashed`, `rounded`, `arcSize`, etc.) — only swap color properties
4. **Add process-number prefix** to in-scope component labels (Yourdon style — `1.0`, `2.0`, etc.) prepended to the existing `MOB-2xxx` / `CBE-5xxx` label.
5. **Overlay DFD edges** — purple dotted for data flow (`strokeColor=#6a1b9a`, `dashPattern=2 3`, noun labels) · red dashed for prohibited paths (`strokeColor=#c62828`, `dashPattern=5 5`, label `[X] PROHIBITED` + named RT) · `TRIGGER:` prefix on labels of edges that initiate process execution.

## What counts as "in scope" for KEEP_IDS

- The subsystem container itself
- All subsystem components (e.g. all MOB-2xxx for Survival Core DFD)
- **Direct touchpoints** the subsystem reads/writes:
  - Data stores it accesses (e.g. SQL/HAZ_CACHE/MAP_CACHE for Survival Core)
  - External entities it consumes from (e.g. EXT-9001a Mapbox, CBE-7001 CDN, HW_GNSS for Survival Core)
  - External entities it produces to (rare — most Core outputs are local-only)
  - Background-sync sources that legitimately feed in-scope stores (e.g. SYN-7001 → HAZ_CACHE per compliance §7 exception)
- Architecture barriers / boundaries that frame the subsystem (e.g. CORE_BARRIER for Survival Core)
- The DFD_LEGEND cell

Everything else (other subsystems, irrelevant peripherals, App Layer components if doing Core DFD, etc.) → grey + empty.

## Reusable script pattern

Each DFD gets its own grey-out script at `.scripts/grey-out-non-<scope>.py`. Use `grey-out-non-survival-core.py` as the template. The script:

- Reads the target `.drawio`
- Defines `KEEP_IDS` set (numeric cell IDs as strings + named IDs like `DFD_LEGEND`)
- Iterates `ALL_CELL_IDS` (numeric range covering the architecture cells)
- For each non-KEEP cell: rewrites style via `restyle_to_grey()` helper (parses `style="k=v;k=v;..."`, swaps color properties, preserves structural attrs) and clears `value=""`
- Prints `GREYED OUT / KEPT` counts for verification

## Reference template

The canonical reference DFD demonstrating this convention is `diagrams/3-flows/data-flow/dfd-survival-core.drawio` + its narrative companion `dfd-survival-core.md`. Future DFDs (e.g. `dfd-trackiq-pipeline.drawio`, `dfd-ocs-pipeline.drawio`) follow the same pattern with a different scope.

## Why this convention exists

- **Cross-mapping**: vendors open the master architecture in one window and the DFD in another — same cell positions = trivial side-by-side comparison
- **Overlay readability**: greyed-out out-of-scope cells provide architectural context without competing visually with DFD overlays
- **Maintainability**: re-runs of grey-out scripts handle architecture changes idempotently
- **Separation of concerns**: structural changes happen in master architecture; behavioral views (data flow, state) live in their own files but stay visually anchored to the master
