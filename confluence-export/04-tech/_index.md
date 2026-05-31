# 📙 4. TECH — Architecture & engineering

> **How the system is built.** Architecture, ERD, APIs, infrastructure, security, decisions, code standards.

## Pages in this section

| Page | What's in it |
|---|---|
| [Architecture overview](./01-architecture-overview.md) | Dual-layer model, 5 subsystems (CBE · MOB · OCS · SYN · CAL), C4 view |
| [ERD](./02-erd.md) | Core entities × relationships across local + cloud |
| [API contract / Integration](./03-api-integration.md) | External integrations (Mapbox, BOM, Firebase) + internal API surface |
| [Infrastructure & environments](./04-infrastructure-environments.md) | Dev / staging / prod · CI/CD pipeline · deployment topology |
| [Security & authentication](./05-security-auth.md) | AES-256 at rest · TLS 1.3 in transit · Firebase Auth scoping · zero outbound from Core |
| [ADR (Architectural Decision Records)](./06-adr-decision-records.md) | Recorded decisions: Flutter, Mapbox SDK choice, Firestore boundary, dual-layer split |
| [Tech standards](./07-tech-standards.md) | Code style · error codes · logging · branching · commit format |

## High-level architecture map

```
┌─────────────────────────────────────────────────────────────┐
│  MOBILE APP — Flutter · iOS 15+ / Android 13+              │
│                                                             │
│  ┌─────────────────────────┐  ┌──────────────────────────┐ │
│  │ MOB-1000 Application    │  │ MOB-2000 Survival Core   │ │
│  │ (Experience & Intel)    │  │ (offline · deterministic)│ │
│  └─────────┬───────────────┘  └──────────────────────────┘ │
│            │                                                │
│  ┌─────────▼───────────────┐                                │
│  │ CAL — Connectivity      │  ← 4 state flags                │
│  │ Abstraction Layer       │                                │
│  └─────────┬───────────────┘                                │
└────────────┼────────────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────┐    ┌─────────────────────────┐
│ SYN-7000 Firebase Firestore│◄───┤ CBE-5000 Cloud Backend │
│ (sync engine · App data)   │    │ (TrackIQ pipeline, etc.) │
└────────────────────────────┘    └────────┬────────────────┘
                                            │
                                  ┌─────────▼─────────┐
                                  │ OCS-5026 Console  │
                                  │ (operator-only)   │
                                  └───────────────────┘
```

Full detail: see [`diagrams/1-overview/trackaroo-phase1-architecture.md`](../../diagrams/1-overview/trackaroo-phase1-architecture.md) and sub-system deep-dives in [`diagrams/2-subsystems/`](../../diagrams/2-subsystems/).

## Top decisions (links to ADR)

- **Flutter** for mobile (cross-platform with iOS/Android parity at low cost)
- **Mapbox SDK + OSM tiles** for offline-first mapping
- **Firebase / Firestore** for sync ONLY (NEVER for Survival Core writes)
- **Dual-layer split** with one-way Experience → Core read-only dependency
