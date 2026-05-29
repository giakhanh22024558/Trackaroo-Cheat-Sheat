# Sprint 0 — Foundation Task Acceptance Criteria (ACs)

> Acceptance Criteria (Definition-of-Done) for the Sprint 0 foundation **Tasks** (`FND-`). Split out of `docs/planning.md` §B2 to keep the plan tidy.
> Keyed by Task ID · AC ID format `AC-FND-{task}-{nn}` · language **English** · all confirmed at the **Discovery gate (15 Jun 2026)**.
> Structure mirrors §B2: **Topic → Concern → Task → ACs**. Task descriptions + references live in `planning.md` §B2; this file holds only the ACs.

🎯 = Task is a committed Discovery Gate deliverable (D1–D9 + website, see `planning.md` §B5).

---

## TOPIC-01 — Architecture & Delivery Platform

### Concern 1 — Architecture & Technical Design
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-001 Dual-layer architecture baseline | AC-FND-001-01 | Core & Experience are separate modules with a one-way **read-only** dependency |
|  | AC-FND-001-02 | Boundary documented and enforced by a dependency-lint rule |
|  | AC-FND-001-03 | No Experience code path can write Core state |
| FND-002 Component / module boundaries | AC-FND-002-01 | Each component (MOB-1xxx/2xxx · CBE · OCS · SYN) has a defined interface contract |
|  | AC-FND-002-02 | Dependency graph published |
|  | AC-FND-002-03 | No cyclic dependency between Core and Experience |
| FND-003 ADR baseline + tech-stack lock | AC-FND-003-01 | ADRs recorded for each stack decision (Flutter/Dart · Mapbox+OSM · Firebase non-core) |
|  | AC-FND-003-02 | Stack versions pinned |
|  | AC-FND-003-03 | Any deviation requires a new ADR |
| 🎯 FND-040 High-Level Architecture Diagram (D1) | AC-FND-040-01 | Diagram annotates Core isolation boundaries |
|  | AC-FND-040-02 | Aligns with the AOD-5026 reference model |
|  | AC-FND-040-03 | PD-accepted at Discovery |
| 🎯 FND-041 Deterministic State Transition Matrix (D2) | AC-FND-041-01 | All Core states + transitions enumerated (Idle/Navigating/SOS/BackTrack™) |
|  | AC-FND-041-02 | Same input → same output (zero probabilistic branch) |
|  | AC-FND-041-03 | PD-accepted |
| 🎯 FND-042 Offline-First Execution whitepaper (D3) | AC-FND-042-01 | Documents 100% Core function with no network |
|  | AC-FND-042-02 | Airplane-mode walkthrough provided per Core path |
|  | AC-FND-042-03 | PD-accepted |

### Concern 2 — Infrastructure & CI/CD
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-004 Repo + Flutter build pipeline | AC-FND-004-01 | CI builds iOS 15+ & Android 13+ on every push to main |
|  | AC-FND-004-02 | Signed artefacts produced |
|  | AC-FND-004-03 | Pipeline green |
| FND-005 Compliance static-analysis CI | AC-FND-005-01 | Scans for all 14 prohibited breadcrumb mutations |
|  | AC-FND-005-02 | Scans for prohibited satellite field names (ESF §8) |
|  | AC-FND-005-03 | Build **fails** on any match |
| FND-006 Prohibited-capability & phase-boundary scan | AC-FND-006-01 | Detects AI/ML/satellite SDKs (active or dormant) |
|  | AC-FND-006-02 | Detects Phase-2 trigger paths |
|  | AC-FND-006-03 | Build fails on detection |
| FND-007 Release-gate evidence packaging | AC-FND-007-01 | Pipeline emits a per-gate evidence bundle (Discovery/Alpha/Beta/GA) |
|  | AC-FND-007-02 | Bundle includes scan results + test reports |
| 🎯 FND-008 SDK & OSS license audit (D8/D9) | AC-FND-008-01 | Full SDK inventory (active+dormant) warrants no prohibited capability |
|  | AC-FND-008-02 | All OSS licences App Store / Play compatible |
|  | AC-FND-008-03 | Declaration signed |
| FND-009 WFD build-gate adherence tracking | AC-FND-009-01 | Tracker blocks subsystem dev without approved wireframe |
|  | AC-FND-009-02 | PD approval recorded per subsystem |

---

## TOPIC-02 — Data, Connectivity & Identity Core

### Concern 3 — Foundational Data Model & Persistence
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-010 Local-only Survival Core store | AC-FND-010-01 | Store operational fully offline |
|  | AC-FND-010-02 | No Firebase dependency in any Core write path |
|  | AC-FND-010-03 | Crash-survivable via WAL replay |
| FND-011 Firebase / Firestore isolation barrier | AC-FND-011-01 | Core data never reaches Firebase (dependency scan proves it) |
|  | AC-FND-011-02 | Barrier documented |
|  | AC-FND-011-03 | Test confirms Core writes stay local |
| 🎯 FND-012 Data classification + enforcement (D5) | AC-FND-012-01 | Every data type tagged Local-Only or Syncable |
|  | AC-FND-012-02 | Breadcrumb confirmed Local-Only & Non-Syncable in writing |
|  | AC-FND-012-03 | Rule blocks misclassified sync |
| FND-013 Firestore offline persistence (non-Core) | AC-FND-013-01 | Non-Core data (PCR cache · group · profile) syncs with offline persistence |
|  | AC-FND-013-02 | Core data excluded from sync |
|  | AC-FND-013-03 | Conflict handling defined for non-Core only |
| FND-014 Encryption baseline | AC-FND-014-01 | AES-256 on local stores |
|  | AC-FND-014-02 | TLS 1.3 on all transit |
|  | AC-FND-014-03 | Key management per policy |

### Concern 4 — Connectivity Abstraction Layer (CAL)
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| 🎯 FND-015 CAL state-flag schema (D6) | AC-FND-015-01 | 4 flags implemented (satReady/queueEnabled/offlineBeacon/partialSignal) |
|  | AC-FND-015-02 | `satReady` locked **false**, not activatable |
|  | AC-FND-015-03 | Schema documented |
| FND-016 Connectivity detection & degraded-state | AC-FND-016-01 | Degraded states detected deterministically |
|  | AC-FND-016-02 | No automatic recovery / escalation |
|  | AC-FND-016-03 | Calm status surfaced |
| FND-017 Connectivity status indicator components | AC-FND-017-01 | Reusable component consumed app-wide |
|  | AC-FND-017-02 | Reflects CAL flags |
|  | AC-FND-017-03 | No alarmist styling |

### Concern 5 — Authentication & RBAC
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-018 App identity / profile | AC-FND-018-01 | Firebase Auth scoped to non-Core profile only |
|  | AC-FND-018-02 | Core paths require no auth |
|  | AC-FND-018-03 | Identity isolated from Core data |
| FND-019 OCS authentication | AC-FND-019-01 | OCS login via Firebase Auth |
|  | AC-FND-019-02 | Secure session management (TLS 1.3) |
| FND-020 OCS 3-role RBAC + permission matrix | AC-FND-020-01 | 3 roles (Founder/Admin/Operator) enforced server-side |
|  | AC-FND-020-02 | Permission matrix documented |
|  | AC-FND-020-03 | Unauthorized action blocked + audited |

---

## TOPIC-03 — Experience Foundation

### Concern 6 — Map & Overlay Rendering Foundation
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-021 Mapbox SDK + OSM vector-tile pipeline | AC-FND-021-01 | Mapbox SDK renders OSM vector tiles |
|  | AC-FND-021-02 | No Mapbox-cloud runtime dependency |
|  | AC-FND-021-03 | Renders offline from bundle |
| FND-022 Offline tile-bundle infrastructure | AC-FND-022-01 | Region bundles download & render offline |
|  | AC-FND-022-02 | Cold-start within BPS targets (≤500MB / >500MB) |
| FND-023 Map-provider abstraction | AC-FND-023-01 | Provider behind an interface |
|  | AC-FND-023-02 | No provider-specific hard-coding in app logic |
|  | AC-FND-023-03 | Provider swappable |
| FND-024 Overlay rendering framework | AC-FND-024-01 | Z-index hierarchy enforced (basemap → PCR) |
|  | AC-FND-024-02 | LIR-01→06 layer independence holds |
|  | AC-FND-024-03 | Only the 8 valid overlay states composable; toggles work |
| 🎯 FND-043 PCR Architecture Documentation (D7) | AC-FND-043-01 | Supersession-based resolution documented (no TTL) |
|  | AC-FND-043-02 | PCR isolated from TTL hazard/env layers |
|  | AC-FND-043-03 | PD-accepted |

### Concern 7 — Design System, App Shell & UX Guidelines
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-025 Design system / component library | AC-FND-025-01 | Component library published (Figma + code) |
|  | AC-FND-025-02 | Design tokens defined |
|  | AC-FND-025-03 | Reused by feature screens |
| FND-026 Application shell & navigation chrome | AC-FND-026-01 | SOS reachable **≤2 taps** from every screen state |
|  | AC-FND-026-02 | BackTrack reachable **≤3 taps** |
|  | AC-FND-026-03 | Chrome consistent app-wide |
| FND-027 Inactive-module placeholder pattern | AC-FND-027-01 | Placeholders render exactly "Inactive in Phase 1" |
|  | AC-FND-027-02 | No executable logic behind them |
| FND-028 Accessibility baseline | AC-FND-028-01 | WCAG 2.1 AA on shared components |
|  | AC-FND-028-02 | Touch targets ≥44pt (≥60pt Core) |
|  | AC-FND-028-03 | Glove / low-light / one-handed verified |
| FND-029 Five-Question Cognitive Hierarchy harness | AC-FND-029-01 | Harness checks all 5 questions answerable across 6 archetypes |
|  | AC-FND-029-02 | Offline / gloved / low-light conditions covered |
|  | AC-FND-029-03 | Failures reported |

---

## TOPIC-04 — Compliance & Phase Governance

### Concern 8 — Business Rules & Compliance Baseline
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-030 Deterministic execution rule-set | AC-FND-030-01 | Core execution documented as non-adaptive / non-inferential |
|  | AC-FND-030-02 | No ML / inference in Core |
|  | AC-FND-030-03 | Rules testable |
| FND-031 14 prohibited-mutation register + guard | AC-FND-031-01 | Register lists all 14 mutations |
|  | AC-FND-031-02 | Runtime + CI guard reject them |
|  | AC-FND-031-03 | Test proves rejection |
| FND-032 Prohibited satellite field-name register | AC-FND-032-01 | Register lists banned fields |
|  | AC-FND-032-02 | CI scans data models |
|  | AC-FND-032-03 | Build fails on presence |
| FND-033 Zero-transmission / non-dispatch enforcement | AC-FND-033-01 | Zero outbound packets from Core paths (app process) |
|  | AC-FND-033-02 | Verified by airplane-mode network capture |
|  | AC-FND-033-03 | Non-dispatch posture confirmed |
| FND-034 22 Rejection Triggers register | AC-FND-034-01 | RT-01→22 encoded as gate checks |
|  | AC-FND-034-02 | Each maps to a verifiable signal |
|  | AC-FND-034-03 | Gate fails on any RT hit |
| FND-035 11 Rollback Governance triggers register | AC-FND-035-01 | RG-01→11 encoded |
|  | AC-FND-035-02 | Overlay rollback triggers detectable |
|  | AC-FND-035-03 | Gate check wired |
| FND-036 Phase-boundary + scaffold whitelist | AC-FND-036-01 | Exactly 3 scaffolds whitelisted |
|  | AC-FND-036-02 | Any other scaffold flagged RT-09 |
|  | AC-FND-036-03 | Boundary documented |

### Concern 9 — Phase 2 Inert Scaffolds
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-037 BackTrack™ Emergency Escrow schema | AC-FND-037-01 | Schema present, versioned, inert |
|  | AC-FND-037-02 | No executable logic |
|  | AC-FND-037-03 | Surfaces "Inactive in Phase 1" |
| FND-038 CAL `satReady` flag | AC-FND-038-01 | Declared false |
|  | AC-FND-038-02 | Not activatable |
|  | AC-FND-038-03 | Absent from app data models (CAL schema only) |
| FND-039 CAL satellite transport pathway | AC-FND-039-01 | Interface documented, non-executable |
|  | AC-FND-039-02 | No transmission code |
|  | AC-FND-039-03 | Extensible for Phase 2 |

---

## TOPIC-05 — Public Presence

### Concern 10 — Companion Website
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| 🎯 FND-044 Companion website live | AC-FND-044-01 | Public site live on CMS |
|  | AC-FND-044-02 | Required Discovery content + legal pages present |
|  | AC-FND-044-03 | PD-accepted at Discovery |

---

**Totals:** 44 Tasks · ~125 ACs. Source/refs for each Task: `docs/planning.md` §B2. Standards these ACs encode: `planning.md` §B7 + the spec extracts in `research/spec-docs/`.
