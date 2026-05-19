# Performance Targets — All Numeric SLAs in One Place

**Status:** 🟡 Partial — NAV section filled (Wave 1); other sections still checklist
**Tier:** 3 (Cross-cutting concern)
**Replaces:** Amber perf banners scattered in master + subsystem diagrams

## Why this document exists

Performance numbers tend to scatter across spec, diagrams, and tickets. This document is the **canonical list** — when "what's the SLA for X?" comes up, this is the only place to update.

---

## Master table — populated targets

### NAV · `MOB-2001` Offline Navigation Engine

| Target ID | Metric | Threshold | Measurement context | Source spec | Verification method |
|---|---|---|---|---|---|
| **PT-NAV-01** | Cold-launch to navigation-ready | **≤ 6 seconds** | Bundle size ≤ 500 MB · validated device matrix · stopwatch from process spawn to interactive map | **CQR-5026** · **BPS-5126 §6.1** | CI perf benchmark suite · manual QA on golden devices |
| **PT-NAV-02** | Cold-launch to navigation-ready (large bundles) | **≤ 8 seconds** | Bundle size > 500 MB · same device matrix as PT-NAV-01 | **CQR-5026** · **BPS-5126 §6.1** | same as PT-NAV-01 |
| **PT-NAV-03** | Warm resume | **≤ 3 seconds** | Process backgrounded then foregrounded · map state restored | **CQR-5026** · **BPS-5126 §6.1** | CI perf benchmark suite |
| **PT-NAV-04** | Initial map tile render | **≤ 2 seconds** | From map screen entry to first painted tile · pre-downloaded bundle present · GNSS fix acquired | **CQR-5026** · **BPS-5126** | CI perf benchmark with frame capture |
| **PT-NAV-05** | Max concurrent map layers | **3 layers** | Simultaneous active overlay count (basemap + 2 overlays max) · enforced by render manager | **MAS-5126** · **BPS-5126** | Static enforcement in render manager · audit code review |
| **PT-NAV-06** | Frame rate — idle | **60 fps** | Map visible, no user interaction · steady-state rendering | **BPS-5126** | Frame profiler in CI |
| **PT-NAV-07** | Frame rate — interaction floor | **≥ 45 fps** | During pan/zoom/route entry interactions | **BPS-5126** | Frame profiler in CI |
| **PT-NAV-08** | Battery — sustained nav | **≤ 8 %/hr** | Active navigation · screen on · GPS engaged · validated device matrix · open-sky conditions | **BPS-5126** · **ESF-5026** (endurance) | Battery profiler · 1-hour soak test |
| **PT-NAV-09** | Endurance — total nav session | **≥ 10 hours** | Continuous navigation from 100% charge to device shutdown · golden device | **BPS-5126** · **ESF-5026** | Endurance bench test (real device, real conditions) |
| **PT-NAV-10** | Heading confidence indicator update | **TBD** (≤ 2 s expected per UXS analog) | UI label changes on GNSS confidence transition · persistent display per spec §3 | **UXS-5726** · spec §3 (Heading Confidence) | TBD — pending vendor proposal · see `design-decisions.md` (NAV gap G1 from Wave 1 audit) |

> **PT-NAV-10 status:** spec mandates the indicator (NAV spec §3) but threshold value + visual semantics are not yet captured. Wave 2 task.

### Cross-component perf (still checklist — Wave 3)

- [ ] **SOS** — ≤2 taps from any screen to trigger distress record
- [ ] **SOS** — ≤20%/hr battery during sustained distress logging
- [ ] **FA Reference** — ≤2 taps from any screen (incl active NAV + SOS confirmation)
- [ ] **Audit log (OCS)** — Minimum 90-day retention for pipeline run history
- [ ] **Event log (mobile)** — Minimum 30-day retention
- [ ] **Bundle Download** — Resumable from interrupt point · integrity validation gate before "Offline-ready"
- [ ] **TrackIQ Alpha-ready** — 22 Aug 2026 milestone
- [ ] **Companion Website Discovery Gate** — 8 Jun 2026 milestone
- [ ] **Tile cost** — Max tile count ceiling per device (number TBD by vendor proposal)
- [ ] **TLS** — 1.3 minimum for all in-transit traffic
- [ ] **Encryption at rest** — AES-256 for mobile SQLite + WAL
- [ ] **HazTrack cache** — TTL-based expiry (specific TTL TBD)
- [ ] **SOS record** — Immutable · forever retention
- [ ] **CAL** — UI label transition ≤ 2 seconds (state matrix `state-cal.md §5`)

### Additional sections

- [ ] **Device validation matrix** — which iOS / Android device models the ≤2s render is benchmarked against
- [ ] **Measurement tooling** — how each target is measured (telemetry, CI test, manual QA)
- [ ] **Failure handling** — what happens when target is missed (alert, block release, log only)

## Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md`
- Compliance siblings: `./compliance-matrix.md`
- Specific subsystem perf details bubble up here from `../2-subsystems/`
- Navigation: `../README.md`
