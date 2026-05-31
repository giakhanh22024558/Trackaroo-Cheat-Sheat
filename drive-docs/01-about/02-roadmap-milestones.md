# Roadmap & Milestones — Trackaroo® Phase 1 Delivery Plan

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

### Risk-buffer policy

| Gate | Date | Feature freeze | Buffer | Buffer sprint |
|---|---|---|---|---|
| Discovery | 15 Jun | ~10 Jun | ~5 days *(constrained: contract starts 29 May)* | within Sprint 0 |
| Alpha | 22 Aug | **8 Aug** | **14 days** | Sprint 5 |
| Beta-Ready | 30 Oct | **17 Oct** | **13 days** | Sprint 10 |
| GA | 13 Nov | 17 Oct (RC frozen) | RC stable; Sprint 11 = release-only | Sprint 11 |

---

## A2. Sprint-by-sprint execution

### Sprint 0 — Foundation (29 May – 15 Jun) → Discovery Gate

**Deliverable checklist (Discovery Gate 15 Jun):**

| ✓ | Gate deliverable | Composed of (task) | Validated by |
|---|---|---|---|
| ☐ | **D1** High-Level Architecture Diagram | S0-03 | AC-C1-02 |
| ☐ | **D2** Deterministic State Transition Matrix | S0-03 | AC-C1-03 |
| ☐ | **D3** Offline-First Execution Explanation | S0-03 | AC-C1-04 |
| ☐ | **D4** Module Isolation Mapping | S0-03 | AC-C1-05 / AC-C3-02 |
| ☐ | **D5** Breadcrumb Local-Only Classification | S0-03 | AC-C3-03 |
| ☐ | **D6** CAL Architecture Documentation | S0-03 | AC-C4-01 |
| ☐ | **D7** PCR Architecture Documentation | S0-03 | AC-C6-05 |
| ☐ | **D8** SDK Audit Declaration | S0-04 | AC-C2-05 |
| ☐ | **D9** OSS Licence Audit | S0-04 | AC-C2-05 |
| ☐ | Companion website live | S0-07 | AC-C10-01 |
| ☐ | *Internal:* Backlog + delivery plan | S0-01 / S0-02 | (planning ready) |
| ☐ | *Internal:* Design System (Figma) + UX Guide | S0-05 / S0-08 | AC-C7-01..05 |
| ☐ | *Internal:* Eng & DevOps Handbook | S0-06 | AC-C2-01..04 |
| ☐ | *Internal:* Foundation Codebase + CI | S0-09 | AC-C2-01..04 |
| **✅** | **Discovery Gate passed** | All D1–D9 + site accepted by PD | — |

```mermaid
gantt
    title Sprint 0 — Foundation (29 May – 10 Jun) → Discovery 15 Jun
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    section Workstreams (parallel)
    Analysis & backlog              :2026-05-29, 2026-06-05
    Architectural docs (D1–D9)      :2026-06-01, 2026-06-10
    Design System + Website         :2026-05-29, 2026-06-09
    Codebase + CI                   :2026-05-29, 2026-06-10
    section Gate
    Foundation freeze               :milestone, active, 2026-06-10, 0d
    Acceptance buffer (~5d)         :active, 2026-06-11, 2026-06-15
    Discovery Gate (D1–D9 + site)   :milestone, crit, 2026-06-15, 0d
```

### Sprint 1 — SOS & Emergency Logging (16 – 27 Jun) → Alpha

**Deliverable checklist (towards Alpha 22 Aug):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | SOS subsystem | FEAT-006 / 007 / 008 / 009 / 010 |
| ☐ | SOS legal-review (RT-16) kickoff | Track 7 Legal — closes in S5 |

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

**Deliverable checklist (towards Alpha 22 Aug):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | BackTrack™ core (capture + immutable write + retrace + distress mode) | FEAT-011 / 012 / 013 / 014 |
| ☐ | Navigation foundation (offline map + location/orientation) | FEAT-001 / 002 |

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

**Deliverable checklist (towards Alpha 22 Aug):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | Navigation complete (routing + controls + instrument overlays) | FEAT-003 / 004 / 005 |
| ☐ | HazTrack™ ingestion + overlay rendering | FEAT-017 / 018 |
| ☐ | First-use onboarding flow | FEAT-025 *(pulled from S5)* |

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

**Deliverable checklist (towards Alpha 22 Aug · feature freeze 8 Aug):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | HazTrack™ complete (TTL + attribution + offline cache) | FEAT-019 / 020 / 021 |
| ☐ | First Aid Reference module (content + disclaimer + offline access) | FEAT-022 / 023 / 024 |
| ☐ | OCS Stage 1 (HazTrack admin + break-glass) | FEAT-027 / 028 *(pulled from S5)* |
| ☐ | First Aid clinical review (RT-12) kickoff | Track 7 Legal — closes in S5 |
| **✅** | **Alpha feature freeze (8 Aug)** | All Sprint 1–4 features complete |

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

**Deliverable checklist (Alpha Gate 22 Aug):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | Survival Core regression | Full E2E: Nav · SOS · BackTrack™ · HazTrack™ · First Aid · OCS Stage 1 |
| ☐ | RT-16 SOS legal sign-off | Qualified counsel (kicked off in S1) |
| ☐ | RT-12 First Aid clinical sign-off | Clinical reviewer (kicked off in S4) |
| ☐ | Prohibited-capability scan clean | No AI / satellite / Phase 2 triggers detected |
| ☐ | Alpha evidence package | Defect burn-down + signed evidence pack |
| **✅** | **Alpha Gate passed** | All deliverables accepted by PD |

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

**Deliverable checklist (towards Beta-Ready 30 Oct):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | TrackIQ™ difficulty grading + verification shield + metadata | FEAT-033 / 034 / 035 / 037 |
| ☐ | Stop-detection prompt | FEAT-036 |
| ☐ | HazTrack™ → TrackIQ™ isolation guard (LIR-05) | FEAT-038 |

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

**Deliverable checklist (towards Beta-Ready 30 Oct):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | PCR module (markers + detail + submission + supersession + history) | FEAT-039 / 040 / 041 / 042 / 043 / 044 |

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

**Deliverable checklist (towards Beta-Ready 30 Oct):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | TrackMate™ peer comms (presence + transport stack + LoRa onboarding + offline queue) | FEAT-045 / 046 / 047 / 049 |
| ☐ | Group Health Envelope (binary indicator) | FEAT-048 |
| ☐ | BackTrack™ multi-session history | FEAT-015 *(pulled from S9)* |

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

**Deliverable checklist (towards Beta-Ready 30 Oct · feature freeze 17 Oct):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | OCS full operational (moderation + user mgmt + audit log + analytics/config) | FEAT-029 / 030 / 031 / 032 |
| ☐ | Local event-log viewer | FEAT-026 |
| ☐ | POI module (display + metadata) | FEAT-050 / 051 *(pulled from S10/S11)* |
| ☐ | BackTrack™ export (GPX / CSV) | FEAT-016 *(pulled from S11, Low)* |
| **✅** | **Beta-Ready feature freeze (17 Oct)** | All Sprint 6–9 + pulled Low features complete |

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

**Deliverable checklist (Beta-Ready Gate 30 Oct):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | 11 TQP-5026 validation domains executed | Full pass on device matrix |
| ☐ | WCAG 2.1 AA audit (RT-11) | Independent audit on feature-complete build |
| ☐ | 22 Rejection Triggers cleared | RT-01..22 all resolved + evidence logged |
| ☐ | Beta-Ready evidence package | Defect burn-down + signed evidence pack |
| **✅** | **Beta-Ready Gate passed** | All deliverables accepted by PD |

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

**Deliverable checklist (GA Gate 13 Nov):**
| ✓ | Gate deliverable | Composed of (this sprint) |
|---|---|---|
| ☐ | Full regression on frozen RC | All 11 epics E2E on device matrix |
| ☐ | App Store + Google Play submission | Submission package + store review pass-through |
| ☐ | GA go/no-go sign-off | Written Project Director sign-off |
| **✅** | **GA Public Launch (13 Nov)** | All deliverables accepted; launch confirmed |

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
---

# PART B — REGISTERS (the consolidated backlog)

## B4. Delivery Gate & Priority

| Priority | Gate | Date | Epics | Sprints |
|---|---|---|---|---|
| **(Foundation)** | Discovery | 15 Jun | — (Sprint 0 tasks S0-, [B2](#b2-sprint-0-foundation-register)) | Sprint 0 |
| **High** | Alpha | 22 Aug | EPIC-001 → EPIC-007 | Sprints 1–5 |
| **Medium** | Beta-Ready | 30 Oct | EPIC-008 → EPIC-011 | Sprints 6–10 |
| **Low** | GA | 13 Nov | (deferrable features, see below) | Sprint 11 |

---
