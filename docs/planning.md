# Trackaroo® Phase 1 — Delivery Planning (single source)

> **The single source for delivery planning + backlog.** This file consolidates the former `backlog.md` (business features) and `sprint-0-foundation.md` (cross-cutting foundation) so there is **one place to maintain**.
> Backed by MasterMind skill [`document/features`](../MasterMind/models/model_001/document/features/). Conventions: [`conventions/features-conventions.md`](../conventions/features-conventions.md).
> **Cadence:** 2-week sprints · 8-person Lean Senior Squad · 8 parallel tracks · 900 man-days (Slitigenz proposal §10.3).
> **Build rule (proposal §10.1):** Survival Core first — SOS + BackTrack™ lead; Experience Layer after Alpha; no subsystem coding without WFD-5126 wireframe approval.
> **Last updated:** 2026-05-28

**Document map:**
- **Part A — Delivery Plan:** [A1 Master Timeline](#a1-master-delivery-timeline) · [A2 Sprint-by-sprint execution](#a2-sprint-by-sprint-execution) · [A3 Coverage check](#a3-coverage-check)
- **Part B — Registers (the backlog):** [B1 Scope rule](#b1-scope-rule) · [B2 Sprint 0 Foundation register](#b2-sprint-0-foundation-register) · [B3 Consolidated feature backlog](#b3-consolidated-feature-backlog-9-column-canonical) · [B4 Gate & Priority](#b4-delivery-gate--priority) · [B5 Discovery deliverables](#b5-discovery-gate-deliverable-register) · [B6 Traceability](#b6-feature--governing-spec-traceability) · [B7 Reserved for AC](#b7-cross-cutting-standards-reserved-for-ac)
- *(Sprint 0 deliverables, criteria & ACs are all inline in §B2 — single source.)*

---
---

# PART A — DELIVERY PLAN

## A1. Master Delivery Timeline

```mermaid
gantt
    title Trackaroo® Phase 1 — Master Timeline (29 May – 13 Nov 2026) · ~15-day pre-gate buffers
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    section Client Gates
    Contract Execution      :milestone, crit, 2026-05-29, 0d
    Discovery Gate          :milestone, crit, 2026-06-15, 0d
    Alpha Gate              :milestone, crit, 2026-08-22, 0d
    Beta-Ready MVP          :milestone, crit, 2026-10-30, 0d
    GA / Public Launch      :milestone, crit, 2026-11-13, 0d
    section Feature freeze
    Foundation freeze        :milestone, active, 2026-06-10, 0d
    Alpha feature freeze     :milestone, active, 2026-08-08, 0d
    Beta feature freeze      :milestone, active, 2026-10-17, 0d
    section Foundation
    Sprint 0 Foundation (work)        :done, 2026-05-29, 2026-06-10
    S0 acceptance buffer (~5d)        :active, 2026-06-11, 2026-06-15
    section Alpha block — Survival Core
    Sprint 1 SOS                       :2026-06-16, 2026-06-27
    Sprint 2 BackTrack + Nav core      :2026-06-30, 2026-07-11
    Sprint 3 Nav + HazTrack + Onboard  :2026-07-14, 2026-07-25
    Sprint 4 HazTrack + First Aid + OCS S1 :2026-07-28, 2026-08-08
    Sprint 5 STABILISATION buffer (~14d) :active, 2026-08-11, 2026-08-22
    section Beta block — Experience Layer
    Sprint 6 TrackIQ                   :2026-08-25, 2026-09-05
    Sprint 7 PCR                       :2026-09-08, 2026-09-19
    Sprint 8 TrackMate + history       :2026-09-22, 2026-10-03
    Sprint 9 OCS full + extras + Low   :2026-10-06, 2026-10-17
    Sprint 10 STABILISATION buffer (~13d) :active, 2026-10-20, 2026-10-30
    section GA block
    Sprint 11 Release + Store Launch (buffer) :active, 2026-10-31, 2026-11-13
```

### Sprint → Delivery goal → Client gate

Each gate block now ends with a **dedicated stabilisation sprint** so feature work freezes ~2 weeks before the gate, leaving a managed risk buffer for validation/hardening/gate prep. Feature sprints are loaded harder (more parallel tracks) to absorb the pulled-forward work.

| Sprint | Dates (2026) | Delivery goal | Feature work? | Client gate |
|---|---|---|---|---|
| **Sprint 0** | 29 May – 10 Jun (+5d buffer→15 Jun) | Foundation platform + **9 Compliance Artefacts (D1–D9)** + companion website | Sprint 0 tasks (S0-) | **★ Discovery — 15 Jun** |
| **Sprint 1** | 16 – 27 Jun | SOS & Emergency Logging (safety-critical lead) | ✅ 5 feat | → Alpha |
| **Sprint 2** | 30 Jun – 11 Jul | BackTrack™ + Navigation core | ✅ 6 feat | → Alpha |
| **Sprint 3** | 14 – 25 Jul | Navigation complete + HazTrack™ start + onboarding | ✅ 6 feat | → Alpha |
| **Sprint 4** | 28 Jul – 8 Aug | HazTrack™ complete + First Aid + OCS Stage 1 — **Alpha feature freeze 8 Aug** | ✅ 8 feat | → Alpha |
| **Sprint 5** | 11 – 22 Aug | 🛡️ **STABILISATION buffer** — Survival Core validation · RT-16/RT-12 legal & clinical close · hardening · Alpha gate prep | ⛔ buffer | **★ Alpha — 22 Aug** |
| **Sprint 6** | 25 Aug – 5 Sep | TrackIQ™ track-difficulty intelligence | ✅ 6 feat | → Beta-Ready |
| **Sprint 7** | 8 – 19 Sep | PCR — Point Condition Reports | ✅ 6 feat | → Beta-Ready |
| **Sprint 8** | 22 Sep – 3 Oct | TrackMate™ peer communication + multi-session history | ✅ 6 feat | → Beta-Ready |
| **Sprint 9** | 6 – 17 Oct | OCS full modules + event-log + POI + Low-tier — **Beta feature freeze 17 Oct** | ✅ 8 feat | → Beta-Ready |
| **Sprint 10** | 20 – 30 Oct | 🛡️ **STABILISATION buffer** — 11 TQP validation domains · WCAG 2.1 AA audit · 22 RT clearance · hardening | ⛔ buffer | **★ Beta-Ready — 30 Oct** |
| **Sprint 11** | 31 Oct – 13 Nov | 🛡️ **RELEASE buffer** — regression on frozen RC · App Store / Play submission · GA go/no-go | ⛔ buffer | **★ GA — 13 Nov** |

> **Gate blocks:** Sprint 0 → Discovery · Sprints 1–5 → Alpha · Sprints 6–10 → Beta-Ready · Sprint 11 → GA.
> Day-level item durations in the per-sprint charts are **indicative** pending Story-level estimates; tracks run in parallel per the 8-workstream model.

### Risk-buffer policy & parallelisation

**Buffer policy — all feature work completes ~15 days before its gate:**

| Gate | Date | Feature freeze | Buffer | Buffer sprint |
|---|---|---|---|---|
| Discovery | 15 Jun | ~10 Jun | ~5 days *(constrained: contract starts 29 May)* | within Sprint 0 |
| Alpha | 22 Aug | **8 Aug** | **14 days** | Sprint 5 |
| Beta-Ready | 30 Oct | **17 Oct** | **13 days** | Sprint 10 |
| GA | 13 Nov | 17 Oct (RC frozen) | RC stable; Sprint 11 = release-only | Sprint 11 |

> ⚠️ **Discovery is the one constrained gate** — contract executes 29 May, gate is 15 Jun (17-day window), so a full 15-day buffer is impossible. We target foundation-complete by **10 Jun** with a **5-day acceptance buffer**. Mitigation: run all 10 foundation concerns **in parallel from day 1** (8 tracks), front-load D8/D9 audits.

**How we absorb the compression — parallel tracks (8 experts / 8 workstreams, proposal §10.3):** the pulled-forward features run concurrently rather than sequentially. Recommended concurrency per sprint:

| Sprint | Parallel tracks running concurrently |
|---|---|
| S1 | Track 1 (SOS) · Track 7 (RT-16 legal kickoff) |
| S2 | Track 1 (BackTrack) ∥ Track 3 (Navigation) ∥ Track 8 (OCS scaffold) |
| S3 | Track 3 (Nav finish) ∥ Track 5 (HazTrack ingestion) ∥ Track 4 (onboarding) |
| S4 | Track 5 (HazTrack finish) ∥ Track 4 (First Aid) ∥ Track 8 (OCS Stage 1) |
| S6 | Track 4 (TrackIQ display) ∥ Track 5 (TrackIQ scoring/intelligence) |
| S7 | Track 4 (PCR) ∥ Track 3 (PCR markers on map) |
| S8 | Track 2 (TrackMate transport+messaging) ∥ Track 1 (history) |
| S9 | Track 8 (OCS full) ∥ Track 4 (POI) ∥ Track 1 (event-log + export) |

> **Capacity check:** peak load is S4 and S9 (8 features each). With 8 senior experts across 8 tracks (≈1 feature/track/sprint) this is within capacity. Hard dependencies still serialise within a track (e.g. OCS HazTrack admin **after** HazTrack feed pipeline; OCS PCR moderation **after** PCR build).

---

## A2. Sprint-by-sprint execution

> 🎨 **Colour convention:** in every per-sprint Gantt, each `section` = one **Epic** (Sprint 0 = one **Topic**), so **all tasks of the same Epic/Topic share the same bar colour** within that chart. Non-feature activities (Legal, QA, Buffer, Release, Gate) keep their own sections. *(Mermaid cycles ~4 section colours per chart, so colours group within a chart; they are not guaranteed identical across different sprint charts.)*

### Sprint 0 — Foundation (29 May – 15 Jun) → Discovery Gate

**Goal:** Stand up the shared platform once and produce the **9 committed Architectural Compliance Artefacts + companion website**. No business features. Full task list: [B2](#b2-sprint-0-foundation-register). Committed artefacts: [B5](#b5-discovery-gate-deliverable-register).
**Buffer:** all 10 concerns run **in parallel from day 1** → foundation-complete **10 Jun**; **11–15 Jun = artefact-acceptance buffer** (~5 days — constrained by the 29 May contract start; see Risk-buffer policy).
**Gate exit:** D1–D9 accepted by Project Director + companion website live. Validation via lab GPS-spoofing + Faraday (CLR-SLZ-001).

```mermaid
gantt
    title Sprint 0 — Foundation (29 May – 10 Jun work) → Discovery 15 Jun
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section Analysis
    S0-01 Business analysis            :2026-05-29, 2026-06-02
    S0-02 Build backlog & plan         :2026-06-01, 2026-06-05
    section Documents
    S0-03 SAD (D1-D7)                  :2026-06-01, 2026-06-10
    S0-04 Compliance & Audit (D8/D9)   :2026-06-03, 2026-06-10
    S0-05 Design System & UX Guide     :2026-06-03, 2026-06-10
    S0-06 Eng & DevOps Handbook        :2026-06-02, 2026-06-09
    section Build & Site
    S0-07 Companion Website            :2026-05-29, 2026-06-09
    S0-08 Design System (Figma)        :2026-05-29, 2026-06-06
    S0-09 Foundation Codebase & CI     :2026-05-29, 2026-06-10
    section Gate buffer
    Foundation freeze                  :milestone, active, 2026-06-10, 0d
    Artefact acceptance buffer (~5d)   :active, 2026-06-11, 2026-06-15
    Discovery acceptance (D1-D9 + site) :milestone, crit, 2026-06-15, 0d
```

### Sprint 1 — SOS & Emergency Logging (16 – 27 Jun) → Alpha
**Goal:** Safety-critical lead — SOS reaches acceptance first (Evidentiary Integrity early).

| Feature | Name |
|---|---|
| FEAT-006 | SOS activation control (persistent · multi-tap confirm) |
| FEAT-007 | 3-stage SOS log sequence (timestamp → GPS pending → coords) |
| FEAT-008 | SOS confirmation screen (feedback elements · non-dispatch copy) |
| FEAT-009 | SOS onboarding acknowledgement (click-through) |
| FEAT-010 | QR fallback handover (offline-generated) |

```mermaid
gantt
    title Sprint 1 — SOS (16 – 27 Jun)
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-002 SOS
    FEAT-006 SOS activation         :2026-06-16, 2026-06-19
    FEAT-007 3-stage log sequence   :2026-06-18, 2026-06-23
    FEAT-008 Confirmation screen    :2026-06-22, 2026-06-25
    FEAT-009 Onboarding ack         :2026-06-24, 2026-06-26
    FEAT-010 QR fallback            :2026-06-24, 2026-06-27
    section Track 7 Legal
    SOS legal-review (RT-16) kickoff :2026-06-16, 2026-06-27
```

### Sprint 2 — BackTrack™ + Navigation core (30 Jun – 11 Jul) → Alpha
| Feature | Name |
|---|---|
| FEAT-011 | Active-session breadcrumb logging (dual-trigger) |
| FEAT-012 | Breadcrumb immutable write (WAL + encryption) |
| FEAT-013 | BackTrack™ reverse retrace |
| FEAT-014 | Distress-mode breadcrumb capture |
| FEAT-001 | Map region download & offline bundle management |
| FEAT-002 | Current location & orientation indicator |

```mermaid
gantt
    title Sprint 2 — BackTrack + Navigation core (30 Jun – 11 Jul)
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-003 BackTrack™
    FEAT-011 Breadcrumb logging     :2026-06-30, 2026-07-03
    FEAT-012 Immutable write        :2026-07-02, 2026-07-07
    FEAT-013 Reverse retrace        :2026-07-06, 2026-07-10
    FEAT-014 Distress-mode capture  :2026-07-08, 2026-07-11
    section EPIC-001 Navigation
    FEAT-001 Region download        :2026-06-30, 2026-07-04
    FEAT-002 Location/orientation   :2026-07-06, 2026-07-11
```

### Sprint 3 — Navigation complete + HazTrack™ start + onboarding (14 – 25 Jul) → Alpha
| Feature | Name |
|---|---|
| FEAT-003 | Route planning & display (deterministic) |
| FEAT-004 | Map interaction controls |
| FEAT-005 | Navigational instrument overlays (route line + breadcrumb trail) |
| FEAT-017 | Hazard feed ingestion & filter pipeline |
| FEAT-018 | Hazard overlay rendering |
| FEAT-025 | First-use onboarding flow *(pulled from S5)* |

```mermaid
gantt
    title Sprint 3 — Navigation + HazTrack start + onboarding (14 – 25 Jul)
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-001 Navigation
    FEAT-003 Route planning         :2026-07-14, 2026-07-18
    FEAT-004 Map controls           :2026-07-17, 2026-07-21
    FEAT-005 Nav instrument overlays :2026-07-21, 2026-07-25
    section EPIC-004 HazTrack™
    FEAT-017 Feed ingestion/filter  :2026-07-14, 2026-07-21
    FEAT-018 Hazard overlay render  :2026-07-21, 2026-07-25
    section EPIC-006 App Experience
    FEAT-025 First-use onboarding   :2026-07-14, 2026-07-19
```

### Sprint 4 — HazTrack™ complete + First Aid + OCS Stage 1 (28 Jul – 8 Aug) → Alpha · **feature freeze 8 Aug**
| Feature | Name |
|---|---|
| FEAT-019 | Hazard freshness / TTL display |
| FEAT-020 | Hazard source attribution |
| FEAT-021 | Hazard cache management (offline) |
| FEAT-022 | First Aid Reference content rendering |
| FEAT-023 | Mandatory persistent disclaimer |
| FEAT-024 | Offline pre-loaded access |
| FEAT-027 | HazTrack™ feed administration module (OCS) *(pulled from S5 — after FEAT-017 feed)* |
| FEAT-028 | Break-glass intervention module (OCS) *(pulled from S5)* |

```mermaid
gantt
    title Sprint 4 — HazTrack + First Aid + OCS Stage 1 (28 Jul – 8 Aug) · Alpha feature freeze
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-004 HazTrack™
    FEAT-019 Freshness/TTL          :2026-07-28, 2026-07-31
    FEAT-020 Source attribution     :2026-07-30, 2026-08-02
    FEAT-021 Cache management       :2026-08-02, 2026-08-05
    section EPIC-005 First Aid
    FEAT-022 Content rendering      :2026-07-28, 2026-08-02
    FEAT-023 Mandatory disclaimer   :2026-08-02, 2026-08-04
    FEAT-024 Offline access         :2026-08-04, 2026-08-06
    section EPIC-007 Operations Console
    FEAT-027 HazTrack feed admin    :2026-07-28, 2026-08-02
    FEAT-028 Break-glass module     :2026-08-02, 2026-08-06
    section Track 7 Legal
    First Aid clinical review (RT-12) :2026-07-28, 2026-08-08
    Alpha feature freeze            :milestone, active, 2026-08-08, 0d
```

### Sprint 5 — 🛡️ STABILISATION buffer (11 – 22 Aug) → Alpha Gate
**No new features** (Alpha freeze was 8 Aug). 14-day risk buffer: end-to-end Survival Core validation, legal/clinical close, hardening, gate evidence.

| Activity | Detail |
|---|---|
| Survival Core validation | Full regression across Nav · SOS · BackTrack™ · HazTrack™ · First Aid · OCS Stage 1 |
| RT-16 SOS legal review close | Qualified-counsel sign-off (started S1) |
| RT-12 First Aid clinical review close | Clinical reviewer sign-off (started S4) |
| Prohibited-capability scan | Confirm clean (no AI/satellite/Phase-2 triggers) |
| Defect burn-down + gate evidence | Alpha evidence package |

```mermaid
gantt
    title Sprint 5 — STABILISATION buffer (11 – 22 Aug) → Alpha
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section Track 6 QA
    Survival Core regression        :2026-08-11, 2026-08-18
    Prohibited-capability scan      :2026-08-14, 2026-08-19
    Alpha gate evidence package     :2026-08-18, 2026-08-21
    section Track 7 Legal
    RT-16 SOS legal close           :2026-08-11, 2026-08-18
    RT-12 First Aid clinical close  :2026-08-11, 2026-08-18
    section Buffer
    Defect burn-down (contingency)  :active, 2026-08-11, 2026-08-21
    Alpha Gate                      :milestone, crit, 2026-08-22, 0d
```

### Sprint 6 — TrackIQ™ Track Difficulty (25 Aug – 5 Sep) → Beta-Ready
| Feature | Name |
|---|---|
| FEAT-033 | Difficulty grade rendering |
| FEAT-034 | Track Verification Shield rendering |
| FEAT-035 | Deterministic difficulty scoring |
| FEAT-036 | Stop-detection prompt (fixed threshold) |
| FEAT-037 | Track metadata display |
| FEAT-038 | HazTrack™ → TrackIQ™ non-mutation guard |

```mermaid
gantt
    title Sprint 6 — TrackIQ (25 Aug – 5 Sep)
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-008 TrackIQ™
    FEAT-033 Difficulty grade       :2026-08-25, 2026-08-28
    FEAT-034 Verification shield     :2026-08-27, 2026-09-01
    FEAT-035 Deterministic scoring   :2026-08-31, 2026-09-03
    FEAT-037 Metadata display        :2026-09-01, 2026-09-04
    FEAT-036 Stop-detection prompt   :2026-08-25, 2026-08-29
    FEAT-038 Non-mutation guard      :2026-09-03, 2026-09-05
```

### Sprint 7 — PCR — Point Condition Reports (8 – 19 Sep) → Beta-Ready
| Feature | Name |
|---|---|
| FEAT-039 | PCR map markers (6 categories · ring states) |
| FEAT-040 | PCR detail card |
| FEAT-041 | PCR submission (online + offline queue) |
| FEAT-042 | PCR confirmation & supersession resolution |
| FEAT-043 | Unconfirmed-age muted display |
| FEAT-044 | PCR resolution & history view |

```mermaid
gantt
    title Sprint 7 — PCR (8 – 19 Sep)
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-009 PCR
    FEAT-039 Map markers            :2026-09-08, 2026-09-11
    FEAT-040 Detail card            :2026-09-10, 2026-09-12
    FEAT-041 Submission + queue     :2026-09-12, 2026-09-17
    FEAT-042 Confirmation/supersede :2026-09-15, 2026-09-18
    FEAT-043 Unconfirmed-age display :2026-09-17, 2026-09-18
    FEAT-044 Resolution/history     :2026-09-17, 2026-09-19
```

### Sprint 8 — TrackMate™ Peer Communication + history (22 Sep – 3 Oct) → Beta-Ready
| Feature | Name |
|---|---|
| FEAT-045 | Group presence & peer messaging |
| FEAT-046 | Transport stack (BLE Mesh → Wi-Fi Direct → LoRa) |
| FEAT-047 | LoRa hardware onboarding (4 wireframe states) |
| FEAT-048 | Group Health Envelope (binary indicator) |
| FEAT-049 | Offline message queue & deterministic sync |
| FEAT-015 | Persistent multi-session history (BackTrack™) *(pulled from S9)* |

```mermaid
gantt
    title Sprint 8 — TrackMate + history (22 Sep – 3 Oct)
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-010 TrackMate™
    FEAT-046 Transport stack        :2026-09-22, 2026-09-29
    FEAT-045 Presence & messaging   :2026-09-22, 2026-09-26
    FEAT-049 Offline queue/sync     :2026-09-28, 2026-10-02
    FEAT-047 LoRa onboarding        :2026-09-29, 2026-10-03
    FEAT-048 Group Health Envelope  :2026-10-01, 2026-10-03
    section EPIC-003 BackTrack™
    FEAT-015 Multi-session history  :2026-09-22, 2026-09-26
```

### Sprint 9 — OCS full + event-log + POI + Low-tier (6 – 17 Oct) → Beta-Ready · **feature freeze 17 Oct**
All remaining features land here (incl. the 3 Low-tier, pulled from S11) so the RC is **feature-complete by 17 Oct**.

| Feature | Name |
|---|---|
| FEAT-029 | PCR moderation module (OCS) *(after PCR built in S7)* |
| FEAT-030 | User support & account management module (OCS) |
| FEAT-031 | Audit log & compliance-evidence module (OCS) |
| FEAT-026 | Local event-log viewer |
| FEAT-050 | POI display & category iconography *(pulled from S10)* |
| FEAT-016 | Breadcrumb export (GPX / CSV) — Low *(pulled from S11)* |
| FEAT-032 | Remaining OCS operational modules (content / config / analytics) — Low *(pulled from S11)* |
| FEAT-051 | POI metadata & presentation-only indicators — Low *(pulled from S11)* |

```mermaid
gantt
    title Sprint 9 — OCS full + extras + Low (6 – 17 Oct) · Beta feature freeze
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section EPIC-007 Operations Console
    FEAT-029 PCR moderation         :2026-10-06, 2026-10-09
    FEAT-030 User support           :2026-10-09, 2026-10-13
    FEAT-031 Audit log & compliance :2026-10-13, 2026-10-16
    FEAT-032 OCS analytics/config   :2026-10-14, 2026-10-17
    section EPIC-011 Points of Interest
    FEAT-050 POI display            :2026-10-06, 2026-10-09
    FEAT-051 POI metadata           :2026-10-09, 2026-10-11
    section EPIC-006 App Experience
    FEAT-026 Local event-log viewer :2026-10-06, 2026-10-10
    section EPIC-003 BackTrack™
    FEAT-016 Breadcrumb export      :2026-10-10, 2026-10-14
    section Freeze
    Beta feature freeze             :milestone, active, 2026-10-17, 0d
```

### Sprint 10 — 🛡️ STABILISATION buffer (20 – 30 Oct) → Beta-Ready Gate
**No new features** (Beta freeze was 17 Oct). 13-day risk buffer: full validation suite + audits on the frozen RC.

| Activity | Detail |
|---|---|
| 11 TQP-5026 validation domains | Full execution across the device matrix |
| WCAG 2.1 AA audit | Independent audit (RT-11) on feature-complete build |
| 22 Rejection Triggers clearance | Confirm all RT-01→22 resolved |
| Beta hardening + gate evidence | Defect burn-down · Beta-Ready evidence package |

```mermaid
gantt
    title Sprint 10 — STABILISATION buffer (20 – 30 Oct) → Beta-Ready
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section Track 6 QA
    11 TQP validation domains       :2026-10-20, 2026-10-28
    WCAG 2.1 AA audit (RT-11)       :2026-10-20, 2026-10-27
    22 Rejection Triggers clear     :2026-10-24, 2026-10-29
    Beta-Ready evidence package     :2026-10-27, 2026-10-30
    section Buffer
    Defect burn-down (contingency)  :active, 2026-10-20, 2026-10-29
    Beta-Ready Gate                 :milestone, crit, 2026-10-30, 0d
```

### Sprint 11 — 🛡️ RELEASE buffer (31 Oct – 13 Nov) → GA Gate
**No new features** — the RC is feature-complete since 17 Oct (S9). This sprint is pure release: regression on the frozen build, store submission, go/no-go. Maximum risk buffer for the hard commercial deadline.

| Activity | Detail |
|---|---|
| Full regression on frozen RC | All 11 epics end-to-end on the device matrix |
| App Store + Google Play submission | Store review lead-time absorbed within the buffer |
| GA go/no-go sign-off | Written Project Director sign-off |

```mermaid
gantt
    title Sprint 11 — RELEASE buffer (31 Oct – 13 Nov) → GA
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section Release
    Full regression on frozen RC    :2026-10-31, 2026-11-06
    App Store / Play submission     :2026-11-04, 2026-11-10
    Store review lead-time          :active, 2026-11-06, 2026-11-12
    GA go/no-go sign-off            :2026-11-11, 2026-11-12
    GA / Public Launch              :milestone, crit, 2026-11-13, 0d
```

---

## A3. Coverage check

| Bucket | Count | Where (build sprints — buffer sprints excluded) |
|---|---|---|
| Sprint 0 tasks (S0-01→09) | 9 | Sprint 0 (work by 10 Jun) |
| Foundation acceptance criteria (AC-C1→C10) | 45 | Sprint 0 — see [B2.2](#b2-sprint-0-foundation-register) |
| High features | 25 | Sprints 1–4 *(S5 = buffer)* |
| Medium features | 23 | Sprints 6–9 *(S10 = buffer)* |
| Low features | 3 | Sprint 9 *(pulled forward; S11 = release buffer)* |
| **Total business features** | **51** | Sprints 1–4 + 6–9 |

**Per-sprint feature load:** S1=5 · S2=6 · S3=6 · S4=8 · S5=buffer · S6=6 · S7=6 · S8=6 · S9=8 · S10=buffer · S11=release. (= 51)

Every Sprint 0 task and every FEAT is scheduled exactly once; all feature work lands **before each gate's freeze date**, leaving the stabilisation/release buffers (S5, S10, S11). Registers below (Part B) hold the full detail.

---
---

# PART B — REGISTERS (the consolidated backlog)

## B1. Scope rule

Epics/Features are **business-functional only**. Cross-cutting foundations are **Sprint 0 tasks (S0-)** with their acceptance criteria. Standards/criteria are **Acceptance Criteria**, never features.

| Bucket | Goes to | Source doc groups (per `research/spec-docs/READING-GUIDE.md`) |
|---|---|---|
| **Business-functional capability** | Feature (`FEAT-`) in [B3](#b3-consolidated-feature-backlog-9-column-canonical) | NHÓM 2/3/4/6 — AOD · FSD · CDG · MAS · ESF · SFD · BTF · HFG · OSM · WFD · VGD · OCS |
| **Cross-cutting foundation** (architecture · infra/CI-CD · data model · auth · design system · UX guidelines · RBAC · business rules · scaffolds) | Task (`S0-`) + criteria (`AC-Cn-`) in [B2](#b2-sprint-0-foundation-register) | NHÓM 2/6 + the standards from 1/5 that become baselines |
| **Standard / threshold / rule** (colour hex · TTL · battery % · RT/RG · WCAG · 5-Q hierarchy · tier gating) | Acceptance Criterion — see [B7](#b7-cross-cutting-standards-reserved-for-ac) | NHÓM 1 (UXS · TAA · PSB · FQH) + NHÓM 5 (PRD · TQP · BPS) |

> ⭐ **ID = priority order.** Lower ID = higher delivery priority. Epic IDs 3-digit. Sprint 0 tasks `S0-NN` numbered in build order. Rule in `conventions/features-conventions.md`.

---

## B2. Sprint 0 Foundation Register

Two layers:
- **B2.1 Tasks** — everything Sprint 0 does (analysis + documents + site + design + codebase). **Not all are customer hand-overs** — some are internal.
- **B2.2 Topic → Concern → Acceptance Criteria** — the analysis/assurance layer that guarantees each task's output meets requirements. (ACs live here inline — single source, `sprint-0-acs.md` retired.)

### B2.1 Sprint 0 Tasks

Everything Sprint 0 does. **Customer hand-over?** flags whether the output is handed to the client (a Discovery deliverable) or is internal foundation work. 🎯 = carries a committed Discovery artefact (D1–D9 / website).

| ID | Task | Type | Customer hand-over? | Covers (Topic / Concern) | Discovery artefact |
|---|---|---|---|---|---|
| **S0-01** | Business analysis — ingest the 19 spec docs → requirements understanding | 🔍 Analysis | No (internal) | all | — |
| **S0-02** | Build product backlog & delivery plan (Epic→Feature · gate priority · sprint plan) | 🔍 Analysis | Shared (planning) | all | — |
| **S0-03** 🎯 | Solution Architecture Document (SAD) | 📄 Document | Yes | TOPIC-01 · TOPIC-02 (C1·C3·C4·C5) + PCR arch | D1·D2·D3·D4·D5·D6·D7 |
| **S0-04** 🎯 | Compliance & Audit Report | 📄 Document | Yes | TOPIC-04 (C8·C9) + audit (C2) | D8·D9 |
| **S0-05** | Design System & UX Guidelines | 📄 Document | Yes | TOPIC-03 (C6·C7) | — |
| **S0-06** | Engineering & DevOps Handbook | 📄 Document | No (internal) | TOPIC-01 (C2) — repo · CI/CD · coding standards · release | — |
| **S0-07** 🎯 | Companion Website | 🌐 Site | Yes | TOPIC-05 (C10) | website |
| **S0-08** | Design System (Figma library) | 🎨 Design asset | Shared | TOPIC-03 (C7) — components/tokens | — |
| **S0-09** | Foundation Codebase & CI Pipelines | ⚙️ Code/config | No (internal) | all concerns (implementations: store · isolation · CAL · auth · overlay engine · scaffolds · scanners) | — |

**9 tasks** = 2 analysis + 4 documents + site + Figma + codebase/CI. Only the 🎯 (+ shared) outputs are client hand-overs; the rest are internal foundation work. Schedule in the [Sprint 0 Gantt](#a2-sprint-by-sprint-execution).

### B2.2 Topic → Concern → Acceptance Criteria

The analysis framework: **5 Topics** group **10 Concerns**; each Concern carries the **Acceptance Criteria (DoD)** the tasks' outputs must satisfy. Each criterion notes which **Task (S0-)** it validates and which **Discovery artefact (D#)** it evidences.

| Topic | Concerns |
|---|---|
| **TOPIC-01 — Architecture & Delivery Platform** | C1 Architecture · C2 Infra/CI-CD |
| **TOPIC-02 — Data, Connectivity & Identity Core** | C3 Data Model · C4 CAL · C5 Auth/RBAC |
| **TOPIC-03 — Experience Foundation** | C6 Map/Overlay · C7 Design System/UX |
| **TOPIC-04 — Compliance & Phase Governance** | C8 Business Rules · C9 Phase 2 Scaffolds |
| **TOPIC-05 — Public Presence** | C10 Companion Website |

> 📖 Refs in each Concern heading = spec(s) to read first (`research/spec-docs/<DOC-ID>.md` · `Slitigenz §x` · `diagrams/…`). Criteria language: English. All confirmed at the **Discovery gate**.

---

### TOPIC-01 — Architecture & Delivery Platform

#### Concern 1 — Architecture & Technical Design  *(refs: AOD-5026 · FSD-5126 · UXS-5726 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C1-01 | Dual-layer separation enforced — Experience→Core dependency is one-way & read-only; a dependency-lint rule fails any Core mutation from Experience | S0-03·S0-09 · D1/D4 |
| AC-C1-02 | High-Level Architecture Diagram annotates Core isolation boundaries, aligns with AOD-5026, PD-accepted | S0-03 · D1 |
| AC-C1-03 | Deterministic State Transition Matrix enumerates all Core states/transitions, zero probabilistic branch, PD-accepted | S0-03 · D2 |
| AC-C1-04 | Offline-First whitepaper proves 100% Core function with no network (airplane-mode walkthrough per Core path), PD-accepted | S0-03 · D3 |
| AC-C1-05 | Component boundaries defined with interface contracts + published dependency graph; no Core↔Experience cycles | S0-03 · D4 |
| AC-C1-06 | ADRs recorded per stack decision; versions pinned; deviations require a new ADR | S0-03·S0-06 |

#### Concern 2 — Infrastructure & CI/CD  *(refs: VGD-5126 · CDG-5126 · BTF-5126 · TQP-5026 · validates: S0-06, S0-09, S0-04)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C2-01 | CI builds iOS 15+ & Android 13+ on every push to main; signed artefacts; pipeline green | S0-06·S0-09 |
| AC-C2-02 | Static-analysis CI scans for all 14 prohibited mutations + prohibited satellite field names; build fails on any match | S0-06·S0-09 |
| AC-C2-03 | Prohibited-capability & phase-boundary scan detects AI/ML/satellite SDKs (active/dormant) + Phase-2 triggers; build fails on detection | S0-06·S0-09 |
| AC-C2-04 | Per-gate evidence bundle produced (Discovery/Alpha/Beta/GA) with scan + test results | S0-06 |
| AC-C2-05 | SDK inventory warrants no prohibited capability; OSS licences App Store/Play compatible; declaration signed | S0-04 · D8/D9 |
| AC-C2-06 | WFD build-gate tracker blocks subsystem dev without approved wireframe; PD approval recorded per subsystem | S0-06 |

---

### TOPIC-02 — Data, Connectivity & Identity Core

#### Concern 3 — Foundational Data Model & Persistence  *(refs: CDG-5126 · AOD-5026 · BTF-5126 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C3-01 | Local-only Core store (SQLite+WAL) operates fully offline, no Firebase dependency in any Core write path, crash-survivable via WAL replay | S0-03·S0-09 |
| AC-C3-02 | Firebase/Firestore isolation barrier proven by dependency scan; Core writes verified local-only | S0-03·S0-09 · D4 |
| AC-C3-03 | Every data type classified Local-Only or Syncable; breadcrumb confirmed Local-Only & Non-Syncable in writing; rule blocks misclassified sync | S0-03 · D5 |
| AC-C3-04 | Non-Core data (PCR cache · group · profile) uses Firestore offline persistence; Core data excluded from sync | S0-03·S0-09 |
| AC-C3-05 | AES-256 at rest; TLS 1.3 in transit; key management per policy | S0-03·S0-09 |

#### Concern 4 — Connectivity Abstraction Layer (CAL)  *(refs: FSD-5126 §6.1 · AOD-5026 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C4-01 | CAL exposes 4 state flags (satReady/queueEnabled/offlineBeacon/partialSignal); `satReady` locked false & not activatable; schema documented | S0-03 · D6 |
| AC-C4-02 | Degraded states detected deterministically; no automatic recovery/escalation; calm status surfaced | S0-03·S0-09 |
| AC-C4-03 | Reusable connectivity-status component consumed app-wide; reflects CAL flags; no alarmist styling | S0-09 |

#### Concern 5 — Authentication & RBAC  *(refs: OCS-5026 · AOD-5026 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C5-01 | Firebase Auth scoped to non-Core profile only; Core paths require no auth; identity isolated from Core data | S0-03·S0-09 |
| AC-C5-02 | OCS login via Firebase Auth with secure session management (TLS 1.3) | S0-09 |
| AC-C5-03 | OCS 3-role RBAC (Founder/Admin/Operator) enforced server-side; permission matrix documented; unauthorized action blocked + audited | S0-03·S0-09 |

---

### TOPIC-03 — Experience Foundation

#### Concern 6 — Map & Overlay Rendering Foundation  *(refs: MAS-5126 · OSM-5026 · validates: S0-05, S0-09; PCR doc → S0-03)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C6-01 | Mapbox SDK renders OSM vector tiles offline from bundle; no Mapbox-cloud runtime dependency | S0-05·S0-09 |
| AC-C6-02 | Region bundles render offline; cold-start within BPS targets (≤500MB / >500MB) | S0-09 |
| AC-C6-03 | Map provider behind a swappable interface; no provider-specific hard-coding in app logic | S0-05·S0-09 |
| AC-C6-04 | Overlay framework enforces z-index hierarchy (basemap→PCR), LIR-01→06 layer independence, only the 8 valid overlay states; toggles work | S0-05·S0-09 |
| AC-C6-05 | PCR architecture documented — supersession-based resolution (no TTL), isolated from TTL hazard/env layers; PD-accepted | S0-03 · D7 |

#### Concern 7 — Design System, App Shell & UX Guidelines  *(refs: WFD-5126 · UXS-5726 · FQH-5026 · validates: S0-05, S0-08)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C7-01 | Component library published (Figma + code) with design tokens; reused by feature screens | S0-05·S0-08 |
| AC-C7-02 | App shell makes SOS reachable ≤2 taps from every screen state, BackTrack ≤3 taps; chrome consistent | S0-05 |
| AC-C7-03 | Inactive-module placeholders render exactly "Inactive in Phase 1" with no executable logic | S0-05·S0-09 |
| AC-C7-04 | WCAG 2.1 AA on shared components; touch targets ≥44pt (≥60pt Core); glove/low-light/one-handed verified | S0-05·S0-08 |
| AC-C7-05 | Five-Question Cognitive Hierarchy harness checks all 5 questions answerable across 6 archetypes (offline/gloved/low-light); failures reported | S0-05 |

---

### TOPIC-04 — Compliance & Phase Governance

#### Concern 8 — Business Rules & Compliance Baseline  *(refs: UXS · ESF · CDG · BTF · OSM · PSB · PRD · validates: S0-04, S0-09)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C8-01 | Core execution documented & built as non-adaptive / non-inferential; no ML/inference in Core | S0-04·S0-09 |
| AC-C8-02 | 14 prohibited-mutation register + runtime/CI guard reject them (test proves rejection) | S0-04·S0-09 |
| AC-C8-03 | Prohibited satellite field-name register; CI scans data models; build fails on presence | S0-04·S0-09 |
| AC-C8-04 | Zero outbound packets from Core paths (app process), verified by airplane-mode capture; non-dispatch posture confirmed | S0-04·S0-09 |
| AC-C8-05 | 22 Rejection Triggers (RT-01→22) + 11 Rollback Governance (RG-01→11) encoded as gate checks; gate fails on any hit | S0-04 |
| AC-C8-06 | Phase-boundary discipline + exactly 3 permitted scaffolds whitelisted; any other scaffold flagged RT-09 | S0-04 |

#### Concern 9 — Phase 2 Inert Scaffolds  *(refs: PSB-5026 §4 · BTF · FSD · CDG · validates: S0-04, S0-09)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C9-01 | BackTrack™ Emergency Escrow schema present, versioned, inert; no executable logic; surfaces "Inactive in Phase 1" | S0-04·S0-09 |
| AC-C9-02 | CAL `satReady` flag declared false, not activatable, absent from app data models (CAL schema only) | S0-04·S0-09 |
| AC-C9-03 | CAL satellite pathway interface documented, non-executable, no transmission code; extensible for Phase 2 | S0-04·S0-09 |

---

### TOPIC-05 — Public Presence

#### Concern 10 — Companion Website  *(refs: OCS-5026 · Slitigenz §10.2 · validates: S0-07)*
| AC ID | Acceptance Criterion (DoD) | Validates · D# |
|---|---|---|
| AC-C10-01 | Public site live on CMS | S0-07 · website |
| AC-C10-02 | Required Discovery content + legal pages present | S0-07 |
| AC-C10-03 | PD-accepted at Discovery | S0-07 |

---

## B3. Consolidated Feature Backlog (9-column canonical)

Canonical MasterMind layout · 3-row-type pattern (Epic = A+B · Feature = C+D · Story = E–I) · no merged cells. Stories deferred (E–I empty); Priority via [B4](#b4-delivery-gate--priority); Sprint via [A1](#a1-master-delivery-timeline).

| Epic ID | Epic Name | Feature ID | Feature Name | Story ID | User Story | Priority | Status | Lifecycle |
|---|---|---|---|---|---|---|---|---|
| EPIC-001 | Offline Navigation & Mapping |  |  |  |  |  |  |  |
|  |  | FEAT-001 | Map region download & offline bundle management |  |  |  |  |  |
|  |  | FEAT-002 | Current location & orientation indicator (GNSS) |  |  |  |  |  |
|  |  | FEAT-003 | Route planning & display (deterministic · no auto-reroute) |  |  |  |  |  |
|  |  | FEAT-004 | Map interaction controls (pan / zoom / layer) |  |  |  |  |  |
|  |  | FEAT-005 | Navigational instrument overlays (route line + breadcrumb trail) |  |  |  |  |  |
| EPIC-002 | SOS & Emergency Logging |  |  |  |  |  |  |  |
|  |  | FEAT-006 | SOS activation control (persistent · multi-tap confirm) |  |  |  |  |  |
|  |  | FEAT-007 | 3-stage SOS log sequence (timestamp → GPS pending → coords) |  |  |  |  |  |
|  |  | FEAT-008 | SOS confirmation screen (feedback elements · non-dispatch copy) |  |  |  |  |  |
|  |  | FEAT-009 | SOS onboarding acknowledgement (click-through) |  |  |  |  |  |
|  |  | FEAT-010 | QR fallback handover (offline-generated) |  |  |  |  |  |
| EPIC-003 | Breadcrumb & BackTrack™ Return Navigation |  |  |  |  |  |  |  |
|  |  | FEAT-011 | Active-session breadcrumb logging (dual-trigger) |  |  |  |  |  |
|  |  | FEAT-012 | Breadcrumb immutable write (WAL + encryption) |  |  |  |  |  |
|  |  | FEAT-013 | BackTrack™ reverse retrace |  |  |  |  |  |
|  |  | FEAT-014 | Distress-mode breadcrumb capture (elevated interval) |  |  |  |  |  |
|  |  | FEAT-015 | Persistent multi-session history |  |  |  |  |  |
|  |  | FEAT-016 | Breadcrumb export (GPX / CSV) |  |  |  |  |  |
| EPIC-004 | HazTrack™ Hazard Awareness |  |  |  |  |  |  |  |
|  |  | FEAT-017 | Hazard feed ingestion & filter pipeline |  |  |  |  |  |
|  |  | FEAT-018 | Hazard overlay rendering (iconography by type) |  |  |  |  |  |
|  |  | FEAT-019 | Hazard freshness / TTL display |  |  |  |  |  |
|  |  | FEAT-020 | Hazard source attribution |  |  |  |  |  |
|  |  | FEAT-021 | Hazard cache management (offline) |  |  |  |  |  |
| EPIC-005 | First Aid Reference |  |  |  |  |  |  |  |
|  |  | FEAT-022 | First Aid Reference content rendering (structured screens) |  |  |  |  |  |
|  |  | FEAT-023 | Mandatory persistent disclaimer |  |  |  |  |  |
|  |  | FEAT-024 | Offline pre-loaded access |  |  |  |  |  |
| EPIC-006 | Application Experience |  |  |  |  |  |  |  |
|  |  | FEAT-025 | First-use onboarding flow |  |  |  |  |  |  |
|  |  | FEAT-026 | Local event-log viewer (read-only · offline) |  |  |  |  |  |
| EPIC-007 | Operations Console (OCS) — Internal Web App |  |  |  |  |  |  |  |
|  |  | FEAT-027 | HazTrack™ feed administration module |  |  |  |  |  |
|  |  | FEAT-028 | Break-glass intervention module |  |  |  |  |  |
|  |  | FEAT-029 | PCR moderation module |  |  |  |  |  |
|  |  | FEAT-030 | User support & account management module |  |  |  |  |  |
|  |  | FEAT-031 | Audit log & compliance-evidence module |  |  |  |  |  |
|  |  | FEAT-032 | Remaining OCS operational modules (content / config / analytics) |  |  |  |  |  |
| EPIC-008 | TrackIQ™ Track Difficulty Intelligence |  |  |  |  |  |  |  |
|  |  | FEAT-033 | Difficulty grade rendering |  |  |  |  |  |
|  |  | FEAT-034 | Track Verification Shield rendering |  |  |  |  |  |
|  |  | FEAT-035 | Deterministic difficulty scoring |  |  |  |  |  |
|  |  | FEAT-036 | Stop-detection prompt (fixed threshold) |  |  |  |  |  |
|  |  | FEAT-037 | Track metadata display (distance / elevation / surface) |  |  |  |  |  |
|  |  | FEAT-038 | HazTrack™ → TrackIQ™ non-mutation guard |  |  |  |  |  |
| EPIC-009 | PCR — Point Condition Reports |  |  |  |  |  |  |  |
|  |  | FEAT-039 | PCR map markers (6 categories · ring states) |  |  |  |  |  |
|  |  | FEAT-040 | PCR detail card |  |  |  |  |  |
|  |  | FEAT-041 | PCR submission (online + offline queue) |  |  |  |  |  |
|  |  | FEAT-042 | PCR confirmation & supersession resolution |  |  |  |  |  |
|  |  | FEAT-043 | Unconfirmed-age muted display |  |  |  |  |  |
|  |  | FEAT-044 | PCR resolution & history view |  |  |  |  |  |
| EPIC-010 | TrackMate™ Peer Communication & Group Coordination |  |  |  |  |  |  |  |
|  |  | FEAT-045 | Group presence & peer messaging |  |  |  |  |  |  |
|  |  | FEAT-046 | Transport stack (BLE Mesh → Wi-Fi Direct → LoRa) |  |  |  |  |  |
|  |  | FEAT-047 | LoRa hardware onboarding (4 wireframe states) |  |  |  |  |  |
|  |  | FEAT-048 | Group Health Envelope (binary indicator) |  |  |  |  |  |
|  |  | FEAT-049 | Offline message queue & deterministic sync |  |  |  |  |  |
| EPIC-011 | Points of Interest |  |  |  |  |  |  |  |
|  |  | FEAT-050 | POI display & category iconography |  |  |  |  |  |
|  |  | FEAT-051 | POI metadata & presentation-only indicators |  |  |  |  |  |

**Totals:** 11 Epics · 51 Features · 0 Stories (next pass). Plus 44 foundation tasks in [B2](#b2-sprint-0-foundation-register).

### Epic ↔ architecture layer (orthogonal to priority/ID)

| Layer | Epics |
|---|---|
| **A · Survival Core** | EPIC-001 Navigation · EPIC-002 SOS · EPIC-003 BackTrack™ · EPIC-004 HazTrack™ · EPIC-005 First Aid |
| **B · Experience & Intelligence Layer** | EPIC-008 TrackIQ™ · EPIC-009 PCR · EPIC-010 TrackMate™ · EPIC-011 POI |
| **C/D · App & Operations (functional)** | EPIC-006 Application Experience · EPIC-007 Operations Console |

---

## B4. Delivery Gate & Priority

Priority by earliest delivery gate (lower ID = higher priority). Companion mapping — not a backlog column (canonical Priority col G is filled on Story rows; Stories inherit Feature priority here).

| Priority | Gate | Date | Epics | Sprints |
|---|---|---|---|---|
| **(Foundation)** | Discovery | 15 Jun | — (Sprint 0 tasks S0-, [B2](#b2-sprint-0-foundation-register)) | Sprint 0 |
| **High** | Alpha | 22 Aug | EPIC-001 → EPIC-007 | Sprints 1–5 |
| **Medium** | Beta-Ready | 30 Oct | EPIC-008 → EPIC-011 | Sprints 6–10 |
| **Low** | GA | 13 Nov | (deferrable features, see below) | Sprint 11 |

Full locked timeline: **Contract Execution 29 May → Discovery 15 Jun → Alpha 22 Aug → Beta-Ready 30 Oct → GA 13 Nov 2026** (Slitigenz proposal §10.2 — `research/spec-docs/Slitigenz-Proposal-RFT5026.md`).

**Feature tiers (mixed epics carry features at >1 gate):**

- **High (25)** → Sprints 1–5: FEAT-001→005, 006→010, 011→014, 017→024, 025, 027, 028
- **Medium (23)** → Sprints 6–10: FEAT-015, 026, 029→031, 033→038, 039→044, 045→049, 050
- **Low (3)** → Sprint 11: FEAT-016 (breadcrumb export) · FEAT-032 (OCS analytics/config) · FEAT-051 (POI metadata)

---

## B5. Discovery Gate Deliverable Register

The headline Sprint 0 output. Slitigenz committed **9 Architectural Compliance Artefacts + companion website** for acceptance at Discovery (15 Jun 2026). All must be accepted for the gate to pass. Source: `research/spec-docs/Slitigenz-Proposal-RFT5026.md` §2.7 / §10.2.

| Artefact | Committed deliverable | In (task) · evidenced by criterion | Existing project asset |
|---|---|---|---|
| **D1** | High-Level Architecture Diagram (Core isolation boundaries) | S0-03 · AC-C1-02 | `diagrams/1-overview/` |
| **D2** | Deterministic State Transition Matrix | S0-03 · AC-C1-03 | `diagrams/3-flows/state/state-trackaroo-transitions.md` |
| **D3** | Offline-First Execution Explanation (whitepaper) | S0-03 · AC-C1-04 | — (to author) |
| **D4** | Module Isolation Mapping (dependency graph) | S0-03 · AC-C1-05 / AC-C3-02 | `diagrams/4-cross-cutting/` |
| **D5** | Breadcrumb Classification Confirmation (Local-Only / Non-Syncable) | S0-03 · AC-C3-03 | CDG-5126 extract |
| **D6** | CAL Architecture Documentation (4 state flags) | S0-03 · AC-C4-01 | `diagrams/` CAL pages |
| **D7** | PCR Architecture Documentation (supersession, not TTL) | S0-03 · AC-C6-05 | OSM-5026 §10 extract |
| **D8** | SDK Audit Declaration (no prohibited capabilities) | S0-04 · AC-C2-05 | — (CI output) |
| **D9** | OSS Licence Audit | S0-04 · AC-C2-05 | — (CI output) |
| **+** | Companion website live | S0-07 · AC-C10-01 | — |

**Gate exit:** D1–D9 accepted by Project Director + companion website live. Validation per CLR-SLZ-001 (lab GPS-spoofing + Faraday simulating the Australian envelope).

---

## B6. Feature → Governing Spec (traceability)

By code, not by column. Standards from NHÓM 1/5 are cited later as ACs ([B7](#b7-cross-cutting-standards-reserved-for-ac)).

| Feature range | Epic | Governing spec doc(s) |
|---|---|---|
| FEAT-001 → 005 | EPIC-001 | FSD-5126 §4.1 · OSM-5026 §5A · MAS-5126 |
| FEAT-006 → 010 | EPIC-002 | ESF-5026 · SFD-5026 · FSD-5126 §4.4 |
| FEAT-011 → 016 | EPIC-003 | BTF-5126 · FSD-5126 §4.2 |
| FEAT-017 → 021 | EPIC-004 | HFG-5026 · OSM-5026 §6 |
| FEAT-022 → 024 | EPIC-005 | WFD-5126 §5.9 |
| FEAT-025 → 026 | EPIC-006 | WFD-5126 §5.16 · FSD-5126 §4.5 |
| FEAT-027 → 032 | EPIC-007 | OCS-5026 |
| FEAT-033 → 038 | EPIC-008 | OSM-5026 §5 · FSD-5126 · WFD-5126 §5.10 |
| FEAT-039 → 044 | EPIC-009 | OSM-5026 §10 · WFD-5126 §5.17 · FSD-5126 §13 |
| FEAT-045 → 049 | EPIC-010 | FSD-5126 §6.2 · WFD-5126 §5.7–5.8 |
| FEAT-050 → 051 | EPIC-011 | FSD-5126 · WFD-5126 §5.11 |

---

## B7. Cross-cutting standards reserved for AC

Standards are not features. Established as baselines/registers in Sprint 0 ([B2](#b2-sprint-0-foundation-register)), then asserted as **Acceptance Criteria** on the relevant feature during the Story pass.

| Reserved standard | Sprint 0 baseline (criterion) | Applied as AC to |
|---|---|---|
| Five-Question Cognitive Hierarchy | AC-C7-05 | FEAT-001 / 002 / 003 / 006 / 013 |
| ≤2-tap SOS · ≤3-tap/≤3s BackTrack | AC-C7-02 | FEAT-006 · FEAT-013 |
| Difficulty colour hex · shield day-thresholds | (OSM values) | FEAT-033 · FEAT-034 |
| Hazard TTL values by source type | (OSM/HFG values) | FEAT-019 |
| 14 prohibited breadcrumb mutations · prohibited field names | AC-C8-02 · AC-C8-03 | FEAT-012 |
| Zero-transmission / non-dispatch posture | AC-C8-04 | FEAT-008 · all Survival Core paths |
| 22 Rejection Triggers · 11 Rollback Governance | AC-C8-05 | cross-cutting on all features |
| Battery / performance thresholds | (BPS values) | FEAT-001 / 011 / 006 |
| WCAG 2.1 AA · glove / one-handed / low-light | AC-C7-04 | all UI features |
| Subscription tier gating (Free/Plus/Pro) | — | deferred (Phase 1 prohibits entitlement hooks) |
| Archetype / activity-context personalization | — | AC framing on UI features |

---

## Assumptions, risks & next step

- **Sprint allocation** follows priority-ordered IDs + the proposal build sequence (Survival Core first, SOS/BackTrack lead). Day-level durations indicative until Story estimates exist.
- **Parallel tracks:** 8-workstream model (proposal §10.3) lets Survival Core, TrackMate, Mapping, Feed, OCS, QA run concurrently — reflected by the `section` tracks in each gantt.
- **Legal gates LE-01→LE-07** (SOS RT-16, First Aid RT-12) run in Track 7 across Sprints 1–5; must close before Alpha.
- **Remote validation** (CLR-SLZ-001) — lab GPS-spoofing + Faraday substitutes for Australian field testing through Discovery/Alpha; field confirmation deferred to Separable Portion 2.
- **Open mismatch:** 7-vs-8 workstream tracks / 8-expert squad (proposal §10.3) — confirm with PD; affects per-sprint capacity.

**Next step (Story pass):** decompose each Feature → `STORY-XXX` (`[User] can [Action]`) + `en` Given/When/Then AC (pulling the reserved standards in [B7](#b7-cross-cutting-standards-reserved-for-ac)); Stories inherit Feature priority/sprint. Recommended: start Sprint 1 (SOS) — it leads the build. Optionally render `output/Trackaroo-Phase1-Plan.xlsx`.
