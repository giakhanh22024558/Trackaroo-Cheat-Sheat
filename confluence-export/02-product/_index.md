# 📗 2. PRODUCT — Product specification

> **What we're building.** All feature-level content lives here. For "why" rules exist → [RULES](../03-rules/_index.md). For architecture → [TECH](../04-tech/_index.md).

## Pages in this section

| Page | What's in it |
|---|---|
| [System overview](./01-system-overview.md) | Dual-layer architecture, the 11 epics, high-level diagrams |
| [User roles](./02-user-roles.md) | 6 user archetypes (TAA-5126) + 3 console roles (OCS-5026) |
| [Modules](./03-modules/_index.md) | The 11 product modules (= Epics) with feature lists |
| [Shared features](./04-shared-features.md) | Cross-module functions (settings, profile, account, attachments, etc.) |

## The 11 product modules (Epics)

| # | Module | Epic | Gate | Spec |
|---|---|---|---|---|
| 1 | [Navigation](./03-modules/01-navigation.md) | EPIC-001 | Alpha | FSD-5126 §4.1 · OSM-5026 §5A · MAS-5126 |
| 2 | [SOS](./03-modules/02-sos.md) | EPIC-002 | Alpha | ESF-5026 · SFD-5026 · FSD-5126 §4.4 |
| 3 | [BackTrack™](./03-modules/03-backtrack.md) | EPIC-003 | Alpha | BTF-5126 · FSD-5126 §4.2 |
| 4 | [HazTrack™](./03-modules/04-haztrack.md) | EPIC-004 | Alpha | HFG-5026 · OSM-5026 §6 |
| 5 | [First Aid Reference](./03-modules/05-first-aid.md) | EPIC-005 | Alpha | FRM-5126 · WFD-5126 §5.9 |
| 6 | [App Experience](./03-modules/06-app-experience.md) | EPIC-006 | Alpha | WFD-5126 §5.16 · FSD-5126 §4.5 |
| 7 | [Operations Console](./03-modules/07-operations-console.md) | EPIC-007 | Alpha+Beta | OCS-5026 |
| 8 | [TrackIQ™](./03-modules/08-trackiq.md) | EPIC-008 | Beta-Ready | OSM-5026 §5 · FSD-5126 · WFD-5126 §5.10 |
| 9 | [PCR (Point Condition Reports)](./03-modules/09-pcr.md) | EPIC-009 | Beta-Ready | OSM-5026 §10 · WFD-5126 §5.17 |
| 10 | [TrackMate™](./03-modules/10-trackmate.md) | EPIC-010 | Beta-Ready | FSD-5126 §6.2 · WFD-5126 §5.7–5.8 |
| 11 | [POI](./03-modules/11-poi.md) | EPIC-011 | Beta-Ready | POI-5026 · WFD-5126 §5.11 |

## Module layer mapping

- **Survival Core (offline, deterministic):** Navigation · SOS · BackTrack™ · HazTrack™ (display only) · First Aid
- **Experience & Intelligence Layer (online-tolerant):** TrackIQ™ · PCR · TrackMate™ · POI · Operations Console
- **App-shell (App Experience):** glue layer, present at both tiers
