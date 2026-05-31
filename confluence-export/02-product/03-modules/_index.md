# 2.3 Modules - Feature Backlog (canonical)

> **The full Phase 1 product backlog.** 11 Epics, 51 Features. Each Epic = one product module (page below). Each Feature lives under exactly one Epic.

The 9-column MasterMind canonical layout. Stories (col E-I) deferred to the Story-pass (planned post-Discovery). Priority is gate-driven - see [Roadmap & Milestones - B4](../../01-about/02-roadmap-milestones.md#b4-delivery-gate--priority).

## Per-module pages

| # | Module | Epic | Gate | Page |
|---|---|---|---|---|
| 1 | Navigation | EPIC-001 | Alpha | [01-navigation.md](./01-navigation.md) |
| 2 | SOS | EPIC-002 | Alpha | [02-sos.md](./02-sos.md) |
| 3 | BackTrack™ | EPIC-003 | Alpha | [03-backtrack.md](./03-backtrack.md) |
| 4 | HazTrack™ | EPIC-004 | Alpha | [04-haztrack.md](./04-haztrack.md) |
| 5 | First Aid Reference | EPIC-005 | Alpha | [05-first-aid.md](./05-first-aid.md) |
| 6 | App Experience | EPIC-006 | Alpha | [06-app-experience.md](./06-app-experience.md) |
| 7 | Operations Console | EPIC-007 | Alpha + Beta | [07-operations-console.md](./07-operations-console.md) |
| 8 | TrackIQ™ | EPIC-008 | Beta-Ready | [08-trackiq.md](./08-trackiq.md) |
| 9 | PCR (Point Condition Reports) | EPIC-009 | Beta-Ready | [09-pcr.md](./09-pcr.md) |
| 10 | TrackMate™ | EPIC-010 | Beta-Ready | [10-trackmate.md](./10-trackmate.md) |
| 11 | POI | EPIC-011 | Beta-Ready | [11-poi.md](./11-poi.md) |

Each module page contains: purpose, feature list with 1-line description, wireframe states, Phase 1 prohibitions, cross-module dependencies, open clarifications (CLR-TRK).

---

## Consolidated Feature Backlog (9-column canonical)


Canonical MasterMind layout · 3-row-type pattern (Epic = A+B · Feature = C+D · Story = E–I) · no merged cells. Stories deferred (E–I empty); Priority via [Roadmap & Milestones - B4](../../01-about/02-roadmap-milestones.md#b4-delivery-gate--priority); Sprint via [Roadmap & Milestones - A1](../../01-about/02-roadmap-milestones.md#a1-master-delivery-timeline).

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

**Totals:** 11 Epics · 51 Features · 0 Stories (next pass). Plus 44 foundation tasks in Sprint 0 register - see `docs/sprint-0-foundation-criteria.md`.

### Epic ↔ architecture layer (orthogonal to priority/ID)

| Layer | Epics |
|---|---|
| **A · Survival Core** | EPIC-001 Navigation · EPIC-002 SOS · EPIC-003 BackTrack™ · EPIC-004 HazTrack™ · EPIC-005 First Aid |
| **B · Experience & Intelligence Layer** | EPIC-008 TrackIQ™ · EPIC-009 PCR · EPIC-010 TrackMate™ · EPIC-011 POI |
| **C/D · App & Operations (functional)** | EPIC-006 Application Experience · EPIC-007 Operations Console |

---
