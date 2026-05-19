# MOB-1000 · Application Layer — Subsystem Deep-Dive

**Status:** 🚧 Stub — scope declared, content TBD
**Tier:** 2 (Subsystem / C4 Component level)
**Zone in master:** `MOB_APP` (Mobile · Application Layer · blue)

## Scope

Experience + Intelligence layer of the mobile app — the *non-survival* features. Degradable when offline (unlike Survival Core which is always-on).

## What this diagram will show (TODO)

- [ ] **`MOB-1001` TrackMate™** — peer-to-peer group comms architecture · zero-signal operation
  - [ ] Inputs: text messages (≤500 chars) · WGS84 location coords + GNSS accuracy · group invitations (QR scan + BLE proximity) · presence (last-known position + elapsed time, fallback ping 120s)
  - [ ] Storage: local Firebase-independent WAL queue in `MOB-3002` SQL (per M0f Comms Queue schema) · AES-256 · message history local · cloud sync optional/deferred (never blocks core ops)
  - [ ] Transport: outbound via CAL/MTT (`MOB-1101`/`MOB-1102`) → BLE/Wi-Fi peer mesh
  - [ ] **⚠️ Architecture gap pending spec clarification — see HWG-01** in "App-side hardware access gaps" section below
- [ ] **`MOB-1002` First Aid Reference** — single component covering **all 3 tiers** (Universal Baseline / Plus / Pro) per FRM-5126. Required content:
  - [ ] Universal Baseline content list (DRSABCD · primary survey · uncontrolled bleeding · shock recognition · burns · fracture/spinal immobilisation · choking sequences)
  - [ ] Storage strategy: **read-only assets bundled in app binary at install** (NOT in MOB-3002/3003 SQLite). Updated only via app version (each version gates through OCS-4302 clinical review)
  - [ ] Tier-based runtime behavior matrix:
    - Free (Baseline): zero writes to any store · CAL connectivity indicator hidden · persistent disclaimer always visible
    - Plus: event log to `MOB-3002` (timestamps + user notes · NO clinical health info)
    - Pro: incident log to `MOB-3003` Professional Incident Log (APP 3 sensitive · AES-256 · explicit informed consent · access controls)
  - [ ] UI invariants (cross-ref `compliance-matrix.md §7 §8 §9`):
    - ≤2-tap access from any screen state (incl active NAV + SOS confirmation)
    - Persistent non-dismissible disclaimer + Triple Zero direction
    - "Visual Calm" copy throughout
    - Deterministic step-by-step format (NO AI/symptom inference/adaptive logic)
    - No paywall / upgrade prompts on Baseline screens (RT-XX named rejection trigger)
  - [ ] Clinical review process via `OCS-4302 First Aid Content Admin` (wilderness paramedic / emergency nurse profile required)
  - [ ] Pro tier: multi-patient triage reference (START protocol) + professional incident log entry forms
  - [ ] TGA Software as a Medical Device (SaMD) classification status — open for legal review (`design-decisions.md` M0a referenced)
- [ ] **`MOB-1003` Six Archetype Presets** — UX presets · Firestore-persisted
- [ ] **`MOB-1004` PCR Framework** — 6 categories · supersession rules · WAL queue · sync-when-online behaviour
  - [ ] Inputs: explicit user-initiation only (NO inference from behavior) · 6 categories (Obstruction · Closure · Infrastructure Damage · Surface Condition · Water Crossing · Localised Hazard) · point location · ≤280 char text · anonymised archetype token
  - [ ] Storage local: PCR Queue in `MOB-3002` SQL (Slitigenz unified · separate schema from CAL Comms Queue per M0f · offline-queue-first · AES-256 + WAL)
  - [ ] Storage cloud: Firestore via FCACHE auto-sync when online · append-only · supersession-archive (per design-decision F3)
  - [ ] Prohibited fields: density metrics · trust scores · photo attachments (Phase 2) · user location history
  - [ ] **⚠️ Gap #2 — PCR read cache location ambiguity** — see design-decisions **M0l** (FCACHE current vs new MOB-3006 PCR Cache analogous to HAZ_CACHE pattern · pending spec clarification)
  - [ ] **⚠️ HWG-02** logged — GNSS access pattern for "User-confirmed coordinates" (see "App-side hardware access gaps" section below)
- [ ] **`MOB-1100` Comms & Transport** sub-zone:
  - [ ] `MOB-1101` CAL (Comms Abstraction Layer) — transport priority logic · state flags
  - [ ] `MOB-1102` MTT (Multi-Tier Transport) — BLE Mesh · Wi-Fi Direct · LoRa selection rules
- [ ] **Degradation model** — what each module does at full / partial / no connectivity
- [ ] **Boundary with Survival Core** — what crosses (read-only) vs what's forbidden (no writes into Core)
- [ ] **Sync paths to/from Firestore** — which collections each module reads/writes

## App-side hardware access gaps (pending spec clarification)

Application Layer features sometimes need on-device hardware (GNSS · camera · accelerometer · etc.) — but the master architecture currently only renders `MOB_HW → MOB_CORE` edges (Core consumers). When an App-side feature has a documented hardware dependency without a matching architecture edge, track as **HWG-XX** entry here until spec resolution determines the access pattern.

Two common resolution patterns for each gap:
- **Pattern α — Direct OS access**: feature uses platform API directly (Flutter plugin, native binding) → master needs edge `HW_X → MOB_APP`
- **Pattern β — Cross-layer read from Core**: feature reads from a Core component's published state (e.g. NAV's position fix) → log as additional **CLR-XX** entry (contributes to V5 trigger count)

### Known gaps

| # | App-side feature | Hardware needed | Current architecture | Resolution options |
|---|---|---|---|---|
| **HWG-01** | **TrackMate location sharing** (MOB-1001) — needs WGS84 lat/lon + GNSS accuracy to share with group peers | `HW_GNSS` (MOB-0001) | Edge `HW_GNSS → MOB_CORE` exists with label "(continuous · NAV/BT/SOS)" — does **not** name-check App Layer. No `HW_GNSS → MOB_APP` edge | **α** Direct OS GNSS (cleanest, App independent of Core, matches Survival-Grade independence mandate) → add edge `HW_GNSS → MOB_APP`<br/>**β** Read from Core NAV's published position → log as CLR-02, contributes to V5 trigger count<br/>**Pending:** spec confirmation which pattern is intended for TM |
| **HWG-02** | **PCR Framework point location** (MOB-1004) — needs initial position to populate "User-confirmed coordinates" submission field | `HW_GNSS` (MOB-0001) | Same as HWG-01 — no `HW_GNSS → MOB_APP` edge currently | **α** Direct OS GNSS propose → user confirms on map (likely UX intent) → consolidates with HWG-01 into single `HW_GNSS → MOB_APP` edge<br/>**β** Read from Core NAV's published position → log as CLR-XX<br/>**γ** Pure map-tap (no GNSS) → user manually selects point on rendered map → no architecture change needed<br/>**Pending:** spec confirmation which pattern is intended for PCR |

> **Consolidation observation:** if HWG-01 and HWG-02 both resolve to Pattern α (direct OS GNSS), they share the same target hardware and would be served by a **single consolidated edge** `HW_GNSS → MOB_APP` rather than per-feature edges. Defer the consolidation decision until spec resolution.

### Candidate gaps to audit (when other App features are spec'd in detail)

These features MAY have similar hardware dependencies — re-audit when their specs land:
- ~~**FA Reference (MOB-1002)** Pro tier — does incident logging capture device position? camera (photo evidence)?~~ → **RESOLVED:** spec confirms NO hardware needs (Free/Plus/Pro all text-only · no GNSS · no camera)
- ~~**PCR Framework (MOB-1004)** — does PCR creation capture location? attachments via camera?~~ → **RESOLVED:** camera prohibited in Phase 1 (per PCR spec · photo attachments deferred to Phase 2) · location elevated to **HWG-02**
- ~~**Six Archetype Presets (MOB-1003)** — likely no hardware needs (UI preference only)~~ → **RESOLVED:** spec confirms no hardware (pure UI customization layer)

**All known App-layer features (TM · FA · PRESETS · PCR) audited.** No more candidate gaps in current MOB-1xxx scope. New candidate entries should be added when Phase 2 features land OR when existing specs are amended to include hardware dependencies.

**Trigger to act:** when each gap's source spec lands, resolve to either Pattern α (add architecture edge) or Pattern β (log as CLR-XX). If multiple gaps resolve to Pattern α with the same hardware (e.g. 2+ App features need GNSS), consider one consolidated `HW_X → MOB_APP` edge instead of per-feature edges.

## Cross-layer read surfaces (Application Layer reading Survival Core data)

Per `compliance-matrix.md §5` Immutable Separation Boundary doctrine: *"Application Layer can read from Core (limited surfaces) but NEVER write."*

These read surfaces are **architecturally meaningful exceptions** to the default Core-isolation visualization (master diagram doesn't render each one to avoid clutter — V4 rule). Track all known cases here. When count reaches **≥3 surfaces**, promote to dedicated cross-cutting doc `4-cross-cutting/cross-layer-reads.md` per planning notes in `research/design-decisions.md`.

### Known surfaces

| # | App-side feature | Reads from Core | Core schema | Permission basis |
|---|---|---|---|---|
| **CLR-01** | **Event Log Viewer** (dedicated read-only utility · per MOB-2005 spec) | `D5 event_log` in MOB-3002 SQL | event_id · component · event_type · ts · payload | compliance §5 limited-surface read |

### Candidate surfaces to audit (not yet confirmed in spec)

These COULD become CLR-XX entries if spec confirms App-side viewer features for them:
- BackTrack reverse-path display (reads D2 breadcrumb_log)
- Anchor catalogue browser (reads D6 anchor_points)
- SOS log review screen (reads D4 sos_log)
- Nav session history (reads D2 nav_session schema)

**Trigger to promote:** if any 2 of the candidates above are spec-confirmed, total CLR surfaces ≥ 3 → create `4-cross-cutting/cross-layer-reads.md` as canonical inventory + decide whether master diagram should add aggregated edge `MOB_CORE → MOB_APP "limited-surface reads (Event Log · Reverse Path · Anchor list · …)"`.

## Data store reference notes

When this doc (and others) reference `MOB-3002`, the **display label in the master diagram** is **"Survival Core Data + Comms Queue"** (data-domain name describing what the schema contains: Survival Core data + App-layer Firebase-independent comms queue). The **spec-original name** is **"Encrypted SQLite + WAL"** (storage tech).

The two names refer to the same component and are interchangeable in prose — diagram uses the data-domain name to disambiguate from the parent `SQLITE_STORE` container (which represents the unified physical file per Slitigenz proposal · M0e). Spec name retained as alias for traceability to FSD/CDG-5126 references. See `design-decisions.md` **M0k** for the full rationale.

| Display label (diagram) | Spec alias | Spec authority |
|---|---|---|
| `MOB-3002 Survival Core Data + Comms Queue` | `MOB-3002 Encrypted SQLite + WAL` | FSD-5126 · CDG-5126 |
| `MOB-3003 Professional Incident Log` | (same) | FRM-5126 |
| `MOB-3005 HazTrack Overlay Cache` | (same) | OSM-5026 · HFG-5026 |

## Diagram type

**Mermaid `graph TB`** zoomed into MOB_APP only, with external touchpoints (Firestore, LoRa peripherals via MTT, and read-only references to MOB_CORE).

## Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md` — see MOB_APP zone
- Survival Core (peer): `./mob-survival-core.md`
- Firestore (data plane): `./syn-firestore-sync.md`
- OCS clinical review gate: `./ocs-operations-console.md` — `OCS-4302 First Aid Content Admin`
- CAL deep-dive (sibling component): `./mob-cal-architecture.md`
- Compliance: `../4-cross-cutting/compliance-matrix.md` — Application → Core isolation · §7 FA tier governance · §8 Visual Calm doctrine · §9 perf invariants
- Performance: `../4-cross-cutting/performance-targets.md` — ≤2-tap FA · cold start · battery
- Design decisions: `../../research/design-decisions.md` — M0a (FA tier model · revised 2026-05-17) · M0d (Pro Incident Log storage) · M0k (MOB-3002 display label rename)
- Spec authority: `../../research/spec-authority-stack.md` — FRM-5126 is sole authority for FA Reference
- Navigation: `../README.md`
