# MOB-2000 · Survival Core — Subsystem Deep-Dive

**Status:** 🚧 Stub — scope declared, content TBD
**Tier:** 2 (Subsystem / C4 Component level)
**Zone in master:** `MOB_CORE` (Mobile · Survival Core · green)

## Scope

Component-level breakdown of the on-device safety-critical layer — 100% offline-first, deterministic, never makes a network call at runtime.

## What this diagram will show (TODO)

- [ ] **All 7 core components** with their internal structure: NAV · BackTrack · HazTrack · SOS · Event Log · Safe Anchor Points · Bundle Download Manager
- [ ] **`MOB-2001` NAV** — Mapbox SDK integration · vector tile rendering · local routing engine · GPU rendering path
- [ ] **`MOB-2007` Bundle Download Manager** — bbox/polygon selection UI · resumable download state machine · integrity validation (checksum) · "Offline-ready" gate
- [ ] **Local data store interactions** — which component writes to which store in `MOB-3002 Encrypted SQLite + WAL`
- [ ] **GNSS subscription model** — how NAV, BackTrack, SOS all share the same position fix stream
- [ ] **Performance budgets** — initial render ≤2s · max 3 layers · ≤2 tap SOS · WAL crash recovery
- [ ] **Prohibition barriers** — no runtime network · no external search · no cloud rerouting · no telemetry leakage from Core to Application Layer
- [ ] **Hazard cache TTL semantics** — how HazTrack expires authority data offline
- [ ] **Dual-trigger BackTrack capture** — what 2 triggers, what coords get stored

## Diagram type

**Mermaid `graph TB`** zoomed into MOB_CORE only, with external touchpoints (GNSS, MOB-3002, OCS hazard feed via SYN). Possibly augmented with a sequence diagram for "pre-journey bundle download" scenario in `../3-flows/sequence/`.

## Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md` — see MOB_CORE zone
- Behavioral view: `../3-flows/data-flow/dfd-survival-core.md`
- Compliance: `../4-cross-cutting/compliance-matrix.md` — no runtime network, no SQLite-to-cloud, etc.
- Performance: `../4-cross-cutting/performance-targets.md` — ≤2s render · max 3 layers
- Artifact lifecycle: `../4-cross-cutting/tile-lifecycle.md`
- Mapbox SDK reference: `../../research/mapbox-sdk-overview.md`
- Navigation: `../README.md`
