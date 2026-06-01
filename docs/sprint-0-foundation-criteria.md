# Sprint 0 Foundation — Topic → Concern → Acceptance Criteria

> **Quality requirements** for Sprint 0 foundation work. Each criterion validates one or more Sprint 0 Tasks (`S0-NN`) and feeds the Discovery gate evidence pack.
>
> **Companion:** (delivery plan lives in the Confluence workspace)
> - **Sprint 0 timeline + tasks (S0-01..09) + Discovery gate deliverable checklist (D1–D9 + site)** — all in [Roadmap & Milestones — Sprint 0 section](../confluence-export/01-about/02-planning/02-sprint-0-discovery.md#sprint-0--foundation-29-may--15-jun--discovery-gate)
> - **Feature backlog (EPIC-/FEAT-)** — see [Modules / Feature Backlog](../confluence-export/02-product/03-modules/_index.md)
>
> Criteria language: **English** · all confirmed at **Discovery Gate (15 Jun 2026)**.

## Topic → Concern overview

| Topic | Concerns |
|---|---|
| **TOPIC-01 — Architecture & Delivery Platform** | C1 Architecture · C2 Infra / CI-CD |
| **TOPIC-02 — Data, Connectivity & Identity Core** | C3 Data Model · C4 CAL · C5 Auth / RBAC |
| **TOPIC-03 — Experience Foundation** | C6 Map / Overlay · C7 Design System / UX |
| **TOPIC-04 — Compliance & Phase Governance** | C8 Business Rules · C9 Phase 2 Scaffolds |
| **TOPIC-05 — Public Presence** | C10 Companion Website |

**Counts:** 5 Topics · 10 Concerns · 45 Acceptance Criteria (`AC-C{concern}-{nn}`).

> 📖 Refs in each Concern heading = spec(s) to read first (`research/spec-docs/<DOC-ID>.md` · `Slitigenz §x` · `diagrams/…`).

---

## TOPIC-01 — Architecture & Delivery Platform

### Concern 1 — Architecture & Technical Design  *(refs: AOD-5026 · FSD-5126 · UXS-5726 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C1-01 | Dual-layer separation enforced — Experience→Core dependency is one-way & read-only; a dependency-lint rule fails any Core mutation from Experience |
| AC-C1-02 | High-Level Architecture Diagram annotates Core isolation boundaries, aligns with AOD-5026, PD-accepted |
| AC-C1-03 | Deterministic State Transition Matrix enumerates all Core states/transitions, zero probabilistic branch, PD-accepted |
| AC-C1-04 | Offline-First whitepaper proves 100% Core function with no network (airplane-mode walkthrough per Core path), PD-accepted |
| AC-C1-05 | Component boundaries defined with interface contracts + published dependency graph; no Core↔Experience cycles |
| AC-C1-06 | ADRs recorded per stack decision; versions pinned; deviations require a new ADR |

### Concern 2 — Infrastructure & CI/CD  *(refs: VGD-5126 · CDG-5126 · BTF-5126 · TQP-5026 · validates: S0-06, S0-09, S0-04)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C2-01 | CI builds iOS 15+ & Android 13+ on every push to main; signed artefacts; pipeline green |
| AC-C2-02 | Static-analysis CI scans for all 14 prohibited mutations + prohibited satellite field names; build fails on any match |
| AC-C2-03 | Prohibited-capability & phase-boundary scan detects AI/ML/satellite SDKs (active/dormant) + Phase-2 triggers; build fails on detection |
| AC-C2-04 | Per-gate evidence bundle produced (Discovery/Alpha/Beta/GA) with scan + test results |
| AC-C2-05 | SDK inventory warrants no prohibited capability; OSS licences App Store/Play compatible; declaration signed |
| AC-C2-06 | WFD build-gate tracker blocks subsystem dev without approved wireframe; PD approval recorded per subsystem |

---

## TOPIC-02 — Data, Connectivity & Identity Core

### Concern 3 — Foundational Data Model & Persistence  *(refs: CDG-5126 · AOD-5026 · BTF-5126 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C3-01 | Local-only Core store (SQLite+WAL) operates fully offline, no Firebase dependency in any Core write path, crash-survivable via WAL replay |
| AC-C3-02 | Firebase/Firestore isolation barrier proven by dependency scan; Core writes verified local-only |
| AC-C3-03 | Every data type classified Local-Only or Syncable; breadcrumb confirmed Local-Only & Non-Syncable in writing; rule blocks misclassified sync |
| AC-C3-04 | Non-Core data (PCR cache · group · profile) uses Firestore offline persistence; Core data excluded from sync |
| AC-C3-05 | AES-256 at rest; TLS 1.3 in transit; key management per policy |

### Concern 4 — Connectivity Abstraction Layer (CAL)  *(refs: FSD-5126 §6.1 · AOD-5026 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C4-01 | CAL exposes 4 state flags (satReady/queueEnabled/offlineBeacon/partialSignal); `satReady` locked false & not activatable; schema documented |
| AC-C4-02 | Degraded states detected deterministically; no automatic recovery/escalation; calm status surfaced |
| AC-C4-03 | Reusable connectivity-status component consumed app-wide; reflects CAL flags; no alarmist styling |

### Concern 5 — Authentication & RBAC  *(refs: OCS-5026 · AOD-5026 · validates: S0-03, S0-09)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C5-01 | Firebase Auth scoped to non-Core profile only; Core paths require no auth; identity isolated from Core data |
| AC-C5-02 | OCS login via Firebase Auth with secure session management (TLS 1.3) |
| AC-C5-03 | OCS 3-role RBAC (Founder/Admin/Operator) enforced server-side; permission matrix documented; unauthorized action blocked + audited |

---

## TOPIC-03 — Experience Foundation

### Concern 6 — Map & Overlay Rendering Foundation  *(refs: MAS-5126 · OSM-5026 · validates: S0-05, S0-09; PCR doc → S0-03)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C6-01 | Mapbox SDK renders OSM vector tiles offline from bundle; no Mapbox-cloud runtime dependency |
| AC-C6-02 | Region bundles render offline; cold-start within BPS targets (≤500MB / >500MB) |
| AC-C6-03 | Map provider behind a swappable interface; no provider-specific hard-coding in app logic |
| AC-C6-04 | Overlay framework enforces z-index hierarchy (basemap→PCR), LIR-01→06 layer independence, only the 8 valid overlay states; toggles work |
| AC-C6-05 | PCR architecture documented — supersession-based resolution (no TTL), isolated from TTL hazard/env layers; PD-accepted |

### Concern 7 — Design System, App Shell & UX Guidelines  *(refs: WFD-5126 · UXS-5726 · FQH-5026 · validates: S0-05, S0-08)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C7-01 | Component library published (Figma + code) with design tokens; reused by feature screens |
| AC-C7-02 | App shell makes SOS reachable ≤2 taps from every screen state, BackTrack ≤3 taps; chrome consistent |
| AC-C7-03 | Inactive-module placeholders render exactly "Inactive in Phase 1" with no executable logic |
| AC-C7-04 | WCAG 2.1 AA on shared components; touch targets ≥44pt (≥60pt Core); glove/low-light/one-handed verified |
| AC-C7-05 | Five-Question Cognitive Hierarchy harness checks all 5 questions answerable across 6 archetypes (offline/gloved/low-light); failures reported |

---

## TOPIC-04 — Compliance & Phase Governance

### Concern 8 — Business Rules & Compliance Baseline  *(refs: UXS · ESF · CDG · BTF · OSM · PSB · PRD · validates: S0-04, S0-09)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C8-01 | Core execution documented & built as non-adaptive / non-inferential; no ML/inference in Core |
| AC-C8-02 | 14 prohibited-mutation register + runtime/CI guard reject them (test proves rejection) |
| AC-C8-03 | Prohibited satellite field-name register; CI scans data models; build fails on presence |
| AC-C8-04 | Zero outbound packets from Core paths (app process), verified by airplane-mode capture; non-dispatch posture confirmed |
| AC-C8-05 | 22 Rejection Triggers (RT-01→22) + 11 Rollback Governance (RG-01→11) encoded as gate checks; gate fails on any hit |
| AC-C8-06 | Phase-boundary discipline + exactly 3 permitted scaffolds whitelisted; any other scaffold flagged RT-09 |

### Concern 9 — Phase 2 Inert Scaffolds  *(refs: PSB-5026 §4 · BTF · FSD · CDG · validates: S0-04, S0-09)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C9-01 | BackTrack™ Emergency Escrow schema present, versioned, inert; no executable logic; surfaces "Inactive in Phase 1" |
| AC-C9-02 | CAL `satReady` flag declared false, not activatable, absent from app data models (CAL schema only) |
| AC-C9-03 | CAL satellite pathway interface documented, non-executable, no transmission code; extensible for Phase 2 |

---

## TOPIC-05 — Public Presence

### Concern 10 — Companion Website  *(refs: OCS-5026 · Slitigenz §10.2 · validates: S0-07)*
| AC ID | Acceptance Criterion (DoD) |
|---|---|
| AC-C10-01 | Public site live on CMS |
| AC-C10-02 | Required Discovery content + legal pages present |
| AC-C10-03 | PD-accepted at Discovery |

---

## Notes for BA analysis (downstream work)

- These 45 ACs are the **assurance layer** for Sprint 0. A separate Story-pass for business features (EPIC-/FEAT- in [Modules / Feature Backlog](../confluence-export/02-product/03-modules/_index.md)) will assert the cross-cutting standards (5-Q hierarchy · prohibited mutations · WCAG · RT/RG · BPS thresholds · tier gating) as their own ACs.
- ID convention: `AC-C{concern}-{nn}` (e.g. `AC-C1-02` = Concern 1, criterion 02). IDs are stable — never renumber after issue; new criteria append to the tail of the relevant Concern.
- Each AC notes which **Task (`S0-`)** it validates; cross-check the [Sprint 0 deliverable checklist](../confluence-export/01-about/02-planning/02-sprint-0-discovery.md#sprint-0--foundation-29-may--15-jun--discovery-gate) (D1–D9 + site) to map AC → committed artefact.
