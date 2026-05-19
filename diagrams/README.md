# Trackaroo® Phase 1 — Diagram Navigation Map

Start here to figure out *which* diagram answers *what* question. The diagrams are organized C4-style into **4 tiers** — each tier zooms in one level deeper.

> **Convention:** numbered folder prefixes (`1-`, `2-`, `3-`, `4-`) force sort order to match C4 reading progression. Open them in order on a first read-through.

---

## Quick decision tree

```
"I want to understand…"
│
├── the whole system at a glance               → 1-overview/trackaroo-phase1-architecture.md
├── how one specific zone works internally     → 2-subsystems/<zone>-*.md
├── how data moves at runtime                  → 3-flows/data-flow/dfd-*.md
├── how state changes over time                → 3-flows/state/state-*.md
├── what's prohibited (and why)                → 4-cross-cutting/compliance-matrix.md
├── what performance numbers I must hit        → 4-cross-cutting/performance-targets.md
└── how a single artifact moves end-to-end     → 4-cross-cutting/tile-lifecycle.md
```

---

## Tier 1 — Master Architecture (`1-overview/`)

**Audience:** Execs, vendors at first contact, RFT readers, anyone onboarding.
**Stays at:** Zone + 1-line component names. No implementation detail.

| File | Purpose |
|---|---|
| `trackaroo-phase1-architecture.md` | Mermaid source for the 6-zone master diagram |
| `trackaroo-phase1-architecture.drawio` | Draw.io twin (symlink → Google Drive · multi-page: **Architecture** (stripped overview) + **Legend** + **CAL Architecture** + per-subsystem tabs as added) |

---

## Tier 2 — Subsystem Deep-Dives (`2-subsystems/`)

**Audience:** Devs, vendor implementers, spec reviewers.
**Zooms into:** One zone at a time, at C4 Level 3 (Component). Includes schemas, internal control flow, design pattern choices.

| File | Covers | Mermaid status | Drawio tab |
|---|---|---|---|
| **`mob-cal-architecture.md`** | **`MOB-1101` CAL** — transport priority · 4 mandatory state flags (satReady · queueEnabled · offlineBeacon · partialSignal) · Survival Core isolation · static analysis evidence · **Discovery Gate Deliverable #4** (spec/mandates) | ✅ filled | ✅ **CAL Architecture** |
| **`mob-cal-architectural-diagram.md`** | **`MOB-1101` CAL — architectural visual** — 5 internal components (SFM · LMON · TR · QMGR · SPUB) + state machine with flag transitions per state + flag transition matrix + component-to-state responsibility map | ✅ filled | — |
| `cbe-trackiq-pipeline.md` | `CBE-5000` TrackIQ Backend Pipeline Worker — 4 stages · schemas · thresholds · governance flow · Pipes & Filters detail | ✅ filled | 🚧 (drawio tab deleted — backing material only) |
| `mob-survival-core.md` | `MOB-2000` Survival Core — NAV · BackTrack · HazTrack · SOS · Bundle Download Manager · perf targets | 🚧 stub | 🚧 TBD |
| `mob-application-layer.md` | `MOB-1000` Application Layer — TrackMate · First Aid · PCR Framework · Multi-Tier Transport (CAL detail moved to dedicated file) | 🚧 stub | 🚧 TBD |
| `ocs-operations-console.md` | `OCS-5026` Operations Console — RBAC matrix · approval workflow · break-glass · audit | 🚧 stub | 🚧 TBD |
| `syn-firestore-sync.md` | `SYN-7000` Firestore — collections breakdown · security rules · offline persistence · prohibited paths | 🚧 stub | 🚧 TBD |

> Each stub will be expanded in subsequent iterations. The stub already declares scope, intended diagram type, and links back to the master.

---

## Tier 3 — Behavioral Views (`3-flows/`)

**Audience:** Devs, QA, integration testers.
**Shows:** How data and state actually move at runtime.

### Data Flow (`3-flows/data-flow/`)
Yourdon-notation DFDs in Mermaid.

| File | Scope |
|---|---|
| `dfd-survival-core.md` + **`dfd-survival-core.drawio`** | All data flowing inside `MOB-2000` — triggers · inputs · outputs · stores · independence map. **Drawio twin uses the full master architecture as canvas** (every layer/component preserved 1:1) with DFD-specific overlays on top — see the `DFD OVERLAY LEGEND` block inside that file for the reusable template convention applied to all DFDs in this folder |
| `dfd-trackiq-pipeline.md` | All data flowing inside `CBE-5000` — raw → enriched → scored → tile → published |

### State (`3-flows/state/`)

| File | Scope |
|---|---|
| `state-trackaroo-transitions.md` | System-wide state transition matrix (6 Survival-Core machines + isolation map + prohibition register) |
| `state-cal.md` | **CAL State Matrix** — 5 reachable states × 4 flag vectors × transport behaviour × UI labels × allowed transitions (consolidates `MOB-1101` runtime behaviour) |

### Sequence (`3-flows/sequence/`)
*(Folder placeholder — add `seq-<scenario>.md` when you need to show timed message exchanges, e.g. `seq-sos-trigger.md`, `seq-grade-approval.md`)*

---

## Tier 3 (cont.) — Cross-Cutting Concerns (`4-cross-cutting/`)

**Audience:** Auditors, compliance, architects.
**Why separate:** These concerns touch >1 zone. Putting them inside each subsystem diagram causes duplication and visual noise. One canonical place per concern.

| File | Aggregates | Status |
|---|---|---|
| `compliance-matrix.md` | All `[X] PROHIBITED` paths system-wide + RT-09 rationale + enforcement point per row | 🚧 stub |
| `performance-targets.md` | All numeric SLAs (≤2s render, max 3 layers, ≤2 tap SOS, 90-day audit, 30-day event log, etc.) in one table | 🟡 partial (NAV filled) |
| **`phase-2-readiness.md`** | **Phase 2 Scaffold Zone catalog** — 3 permitted scaffolds (BT escrow schema · CAL satReady flag · CAL satellite pathway) + 4 placeholder disciplines + 2 RT triggers + static-analysis verification + Alpha/Beta/GA gate exit criteria | ✅ filled |
| `tile-lifecycle.md` | Vector tile journey: Mapbox basemap + raw track data → Ingest → DEM → Score → Bake → CDN → Bundle Manager → NAV cache | 🚧 stub |
| `cross-layer-reads.md` *(planned · trigger-based)* | All known "Application Layer reads from Survival Core" surfaces (CLR-01 Event Log Viewer · etc.) + decision on master-diagram visualisation. **Create when CLR count ≥ 3** confirmed surfaces — see `research/design-decisions.md` V5 + interim tracking in `2-subsystems/mob-application-layer.md` "Cross-layer read surfaces" section | 📅 deferred |

---

## Cross-references outside `diagrams/`

| Folder | Purpose |
|---|---|
| `../CLAUDE.md` | Visual style guide + folder conventions |
| `../research/mapbox-sdk-overview.md` | Mapbox SDK deep-dive (third-party knowledge) |
| `../research/tech-stack-inventory.md` | Inventory of every tech used, mapped to zone + component |

---

## How to add a new diagram

1. **Pick the tier first** — is this overview, subsystem, behavioral, or cross-cutting?
2. **Drop it in the right folder** — follow naming convention from `CLAUDE.md`.
3. **Update this README** — add a row to the relevant table so future readers find it.
4. **Cross-link** — at minimum, add a "See also" section pointing back to the master + sibling diagrams.
5. **If it's structural and complex enough to deserve a `.drawio` twin:** add as new page in the existing `trackaroo-phase1-architecture.drawio` tabbed file. One source file, many pages.

---

## Status legend

- ✅ Complete
- 🚧 Stub / skeleton — scope declared, content TBD
- 🟡 Work in progress
- 🔵 Phase 2 placeholder
