# Sprint 0 — Discovery delivery plan

> **Parent:** [Planning](./_index.md)
> **Window:** 29 May – 15 Jun 2026 (12 business days)
> **Gate:** → **Discovery Gate** (15 Jun 2026)

## Sprint goal

> **Pass Discovery Gate on 15 June 2026** by delivering **10 PD-deliverable tasks** (9 Architectural Compliance Artefacts · Design + UI · TrackMate Transport + concessions · Operational & Admin Readiness) **+ 1 internal QA pre-study task** (Sprint 1 enablement). Acceptance by PD unblocks all subsequent build work in Sprints 1+.

## Timeline & milestones

```mermaid
gantt
    title Sprint 0 — Discovery delivery plan (29 May – 15 Jun 2026)
    dateFormat YYYY-MM-DD
    axisFormat %a %d/%m
    tickInterval 1day
    excludes weekends
    todayMarker off

    section Architectural
    9 Artefacts D1-D9 (parallel)          :crit, 2026-05-29, 2026-06-10

    section Design
    10 high-fidelity mockups               :crit, 2026-05-29, 2026-06-10
    Design direction statement             :2026-06-04, 2026-06-10

    section Technical & Process
    TrackMate Proposal + Concessions       :2026-05-29, 2026-06-10
    WFD Wireframe Coverage                 :2026-05-29, 2026-06-10
    AI-Tool Register                       :2026-06-01, 2026-06-04
    Companion Website + live anchor        :2026-05-29, 2026-06-10
    System Access established              :crit, 2026-05-29, 2026-06-03
    Continuity Plan                        :2026-06-01, 2026-06-10
    Initial Security & Privacy Evidence    :2026-06-01, 2026-06-10

    section QA pre-study (Sprint 1 enablement)
    QA reads docs + drafts test approach   :2026-06-01, 2026-06-12

    section Gate milestones
    System Access live                     :milestone, 2026-06-03, 0d
    AI-Tool Register complete              :milestone, 2026-06-04, 0d
    Internal foundation freeze (draft v1)  :milestone, 2026-06-05, 0d
    Package submitted to PD                :milestone, crit, 2026-06-10, 0d
    Internal freeze (compressed for preview):milestone, crit, 2026-06-04, 0d
    Pre-preview package to PD (Fri 09:00)  :milestone, crit, 2026-06-05, 0d
    PD Preview Session (Mon 15:00 ICT)     :milestone, crit, 2026-06-08, 0d
    PD review window (3 BD)                :active, 2026-06-10, 2026-06-12
    QA test approach v1 ready              :milestone, 2026-06-12, 0d
    Discovery Gate                         :milestone, crit, 2026-06-15, 0d
```

### Internal milestones (manage proactively)

| Date | Milestone | Why it matters |
|---|---|---|
| **Wed 3 Jun** | System Access live | Other tasks need repo access; unblocks dev infra |
| **Thu 4 Jun** | AI-Tool Register complete | Lowest-effort task; close it early to demonstrate process discipline |
| **Thu 4 Jun EOD** | All 10 PD-deliverable tasks draft v1 complete — **compressed internal freeze** | Pulled forward 1 BD vs original Fri 5 Jun plan, to feed pre-preview submission (agreed at kickoff 2026-06-01) |
| **Fri 5 Jun 09:00 ICT** | **Pre-preview package submitted to PD** | Per kickoff agreement — PD reviews over weekend travel (no signal Sat–Sun, drafts must be self-explanatory) |
| **Mon 8 Jun 15:00 ICT** | **PD Preview Session** (~85 min · 3 parts) | Direction-setting before formal lock — out-of-window slot agreed by PD at kickoff (CMP §6.3.2) |
| **Wed 10 Jun** | Formal package submitted to PD | Hard deadline (per PD: *"Design Intent Submission due by 10 June 2026"*) — incorporates feedback from preview |
| **Fri 12 Jun** | PD review complete | 3 BD window only (Wed–Fri). Any rejection → recovery plan ≤5 BD (per DCA §5.5.2) — extremely risky if rejected this late |
| **Fri 12 Jun** | QA test approach v1 ready | Sprint 1 (SOS) test suite build starts Day 1 — no QA ramp-up time lost |
| **Mon 15 Jun** | **Discovery Gate clearance** | Sprint 1 cannot start without it |

## Task list

| Task | Description | Owner (Squad role) | Effort | Deadline | Related docs |
|---|---|---|---|---|---|
| **9 Architectural Compliance Artefacts** (D1–D9) | The full Discovery artefact package — 7 architecture docs + SDK audit + OSS licence audit. Each D# detailed in [Gate Checklist §1A](./01-gate-deliverable-checklist.md#1a-9-architectural-compliance-artefacts). Demonstrates Survival Core isolation, deterministic state, offline-first execution, breadcrumb classification, CAL/PCR architecture. | **Tech Lead** — Dinh Ba Trung (lead) · Mobile Lead (D8) · DevOps Lead (D9) | High | **Fri 5 Jun** (draft) · **Wed 10 Jun** (submit) | AOD-5026 · FSD-5126 · OSM-5026 §10 · BTF-5126 · CDG-5126 · VGD-5126 · PSB-5026 · DCA §10.7 (D9) |
| **10 high-fidelity mockups** (5 screens × daylight + night) | Design Intent submission — 5 key screens (Map · Archetype Selection · TrackMate™ Group · SOS Confirmation · First Aid Reference) each in **daylight + night** modes. Used by PD to assess Design Quality Obligation. | **UI/UX Lead** — Nguyen Thuy Duong | High | **Wed 10 Jun** | UXS-5726 · WFD-5126 · MAS-5126 · TAA-5126 · DCA §11A |
| **Written design direction statement** (Design Quality Obligation §11A) | 2–4 page document articulating how the visual language meets premium-consumer-safety-app standard. Independent acceptance ground per DCA §11A — PD may reject design quality even if functional spec passes. | **UI/UX Lead** — Nguyen Thuy Duong | Medium | **Wed 10 Jun** *(after mockups v1)* | DCA §11A · UXS-5726 · MAS-5126 |
| **TrackMate™ Transport Proposal + Proposal-Stage Concessions** | (a) Technical proposal for 3-tier peer-comms transport stack (BLE Mesh · Wi-Fi Direct · LoRa) with deterministic fallback logic. (b) Concessions: **methodology + architecture** for deferred empirical validation of **battery performance** (BPS thresholds) + **transport** (range · fallback · HW auto-detection). Foundation for Sprint 8 build + downstream gate validation. | **Mobile Developer** — Nguyen Tien Dat (+ QA Lead for validation methodology) | Medium-High | **Wed 10 Jun** | FSD-5126 §6.2 · WFD-5126 §5.7–5.8 · BPS-5126 · CDG-5126 · TQP-5026 |
| **WFD-5126 Wireframe Coverage** — all Survival Core subsystems | UI state coverage for every Survival Core subsystem (Navigation · SOS · BackTrack™ · HazTrack™ · First Aid). PD-approval prerequisite before any subsystem dev may start (per WFD-5126 build-gate rule). | **UI/UX Lead** — Nguyen Thuy Duong | High | **Wed 10 Jun** | WFD-5126 · UXS-5726 · FQH-5026 · FSD-5126 |
| **AI-Tool Register** (per DCA §10.6) | Disclosure sheet of every AI coding tool in use + data-handling model + human-review process + PD approval status. Schema in [`templates/06-register-schemas.md`](../templates/06-register-schemas.md) §H8. | **Tech Lead** — Dinh Ba Trung | Low | **Thu 4 Jun** | DCA §10.6 · VGD-5126 |
| **Companion Website Staging + live anchor** | Staging env + CMS configured + IA accepted by PD. **Live site with verbatim product anchor statement.** Foundation for Alpha (market-ready). | **Web/Console Lead** — Nguyen Quoc Viet | Medium | **Wed 10 Jun** | OCS-5026 · Slitigenz Proposal §10.2 · DCA §8.4 · CMP-5026 §6.11 |
| **System Access** — Client admin to repos · build envs · credentials | Sets up continuous, unrestricted Client admin access to all repositories · CI/CD · platform accounts (App Store, Play, Mapbox, Firebase) · credentials register. **Strict prerequisite** to any subsequent work per DCA §8.1. | **DevOps Lead** — Nguyen Viet Hoang | Low | **Wed 3 Jun** | DCA §8.1, §8.3, §8.4 · CDG-5126 |
| **Continuity Plan** | Written plan: backup personnel · knowledge-transfer steps · repo/build continuity · escalation arrangements if any Key Personnel unavailable >5 consecutive BD or materially reduced. **Strict precedent before Discovery Gate Clearance** per DCA §14.1. | **Project Manager** — Luong Gia Khanh | Low | **Wed 10 Jun** | DCA §14.1 · CMP-5026 §6.2.2 · Slitigenz Squad (§1.3) |
| **Initial Security & Privacy Evidence** | Documentation of data-isolation architecture (Survival Core local-only · Firebase boundary) + security baselines (AES-256 at rest · TLS 1.3 in transit · MFA · zero outbound from Core verified). Pre-flight for Schedule 9 DPSA executed before env access. | **DevOps Lead** — Nguyen Viet Hoang (+ Tech Lead) | Medium | **Wed 10 Jun** | DCA §9.1–9.7 + Schedule 9 · CDG-5126 · BTF-5126 · ESF-5026 |
| **QA pre-study + Sprint 1 test approach draft** *(internal — not a Discovery deliverable)* | QA Lead reads key spec docs in advance + drafts test approach for Sprint 1 (SOS theme) so test suite build can start Day 1 of Sprint 1. Outputs: TQP domain coverage matrix for SOS · device matrix · test-data plan · early RT/RG checks (RT-16 SOS legal, RT-09 prohibited capabilities). | **QA/Audit Lead** — Nguyen Thi Thom | Medium | **Fri 12 Jun** *(before Sprint 1 starts 16 Jun)* | TQP-5026 (11 domains) · ESF-5026 (SOS, non-dispatch) · SFD-5026 · FSD-5126 §4.4 · BPS-5126 (battery ≤20%/hr SOS) · VGD-5126 (RT-01..23 · RG-01..11) · WFD-5126 §SOS · UXS-5726 (≤2 tap rule) · FQH-5026 |

> **Compressed deadlines** (per kickoff 2026-06-01): **Thu 4 Jun EOD** internal freeze · **Fri 5 Jun 09:00 ICT** pre-preview package to PD · **Mon 8 Jun 15:00 ICT** preview session (~85 min, 3 parts) · **Wed 10 Jun** formal submission · **Mon 15 Jun** Discovery Gate.
> **11 sprint tasks total** — 10 PD-deliverable + 1 internal QA pre-study (Sprint 1 enablement). All track in parallel across the 8-person Squad ([Team & Contacts](../03-team-contacts.md) §2).
> Task IDs + status assigned in the Jira board synced into this page.

## Risk register

> Schema per [`templates/registers/risk.md`](../templates/registers/risk.md) (7-col canonical).

| # | Date | Description | Severity | Owner | Mitigation status | Status |
|---|---|---|---|---|---|---|
| **RISK-001** | 2026-06-01 | 17-day Sprint 0 window = tightest gate · no slack for re-submission · all 8 tasks must clear PD on first review | High | Luong Gia Khanh (PM) | Front-load all 8 tasks from Day 1, parallel across 8 owners; foundation freeze Fri 5 Jun gives 3-BD internal polish before submission | Mitigating |
| **RISK-002** | 2026-06-01 | 9 Artefacts + 10 mockups + WFD Wireframes = highest combined effort + highest PD review risk | High | Dinh Ba Trung (Tech Lead) | Split across 3 owners (Tech / UI/UX / UI/UX) · run fully parallel from Day 1 · daily standups | Mitigating |
| **RISK-003** | 2026-06-01 | System Access task lightweight but critical blocker for any repo-dependent work | Medium | Nguyen Viet Hoang (DevOps Lead) | DevOps Lead closes by Wed 3 Jun (Week 1) before any other task needs repo access | Mitigating |
| **RISK-004** | 2026-06-01 | DCA §11A Design Quality Obligation = independent PD rejection ground for mockups + design statement (premium-consumer-safety standard) | High | Nguyen Thuy Duong (UI/UX Lead) | Pre-review with PD on Tue 9 Jun (informal walkthrough) before formal Wed 10 Jun submission | Open |
| **RISK-005** | 2026-06-01 | Submission Wed 10 Jun → only **3 BD PD review** (Wed–Fri) · recovery plan (5 BD per DCA §5.5.2) would exceed gate date if rejected | High | Luong Gia Khanh (PM) | Submit early Wed 10 Jun AM · daily check-ins during 3-BD review · pre-flag any reviewer concerns before formal review opens | Open |
| **RISK-006** | 2026-06-01 | Compressed internal freeze: Thu 4 Jun EOD vs original Fri 5 Jun — 1 BD pulled forward across all 10 PD-deliverable tasks running in parallel. Risk of incomplete drafts being sent to PD pre-preview. | High | Luong Gia Khanh (PM) | Daily Squad standups Mon–Thu · escalate ASAP if any task slips · pre-preview package allowed to contain explicit *'placeholder pending PD direction'* sections for items needing input | Open |

## Sign-off

| Item | Status |
|---|---|
| All 10 PD-deliverable tasks accepted | ☐ |
| QA test approach v1 ready (internal) | ☐ |
| Discovery Gate Clearance issued | ☐ |
| PD signature | __________ |
| Date | __________ |
| CAR-5026 reference | __________ |
