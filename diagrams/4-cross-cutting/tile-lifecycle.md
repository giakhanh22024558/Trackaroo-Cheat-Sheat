# Tile Lifecycle — Vector Tile Journey End-to-End

**Status:** 🚧 Stub — scope declared, content TBD
**Tier:** 3 (Cross-cutting concern)
**Spans:** External · Cloud Backend · Mobile (Survival Core)

## Why this document exists

A vector tile in Trackaroo crosses **3 zones and at least 7 components** between sourcing and on-screen rendering. No single zone-level diagram tells the full story. This document traces one tile end-to-end so devs, vendors, and reviewers can answer "where exactly does it go between origin and render?"

## What this document will contain (TODO)

### Lifecycle stages to document

- [ ] **Stage 0 — Sourcing**
  - [ ] Mapbox basemap (vector tiles) from Mapbox infra
  - [ ] Raw track data from OSM / GPX / Shapefile via `EXT-9001b`
  - [ ] DEM tiles from AWS Terrain Tiles / SRTM via `EXT-9002`

- [ ] **Stage 1 — Ingest** (`CBE-5001`)
  - [ ] Adapter Pattern normalizes vendor format → `TrackSegmentGroup`
  - [ ] Lands in `raw_ingested_tracks` (PostgreSQL + PostGIS)

- [ ] **Stage 2 — Enrich** (`CBE-5002`)
  - [ ] Slope calculation (Δelev/Δdist) attached as metadata
  - [ ] No mutation of original geometry

- [ ] **Stage 3 — Score** (`CBE-5003`)
  - [ ] Pure-function · idempotent · Hardest-Criterion-Wins
  - [ ] Schemas applied: Vehicle / Trail / Foot / Snow (stub)
  - [ ] Thresholds loaded from OCS config (not hardcoded)
  - [ ] Output: `Proposed Grade Event` → `track_review_queue`

- [ ] **Stage 4 — Manual approval** (`OCS-4301 TDGA`)
  - [ ] Authorised Contributor or Project Director reviews
  - [ ] Approved → `production_tracks` (immutable · reviewer_id + ts)
  - [ ] Rejected → stays in queue with reject reason

- [ ] **Stage 5 — Tile bake** (`CBE-5004`)
  - [ ] MVT/PBF compression
  - [ ] Bakes approved grade attributes into tile
  - [ ] Publishes to `CBE-7001` CDN

- [ ] **Stage 6 — Distribution** (`CBE-7001`)
  - [ ] TrackIQ-baked MVT/PBF tiles served from CDN
  - [ ] Tile manifest delivery
  - [ ] Tile Cost Governance — max ceiling per device

- [ ] **Stage 7 — Pre-journey download** (`MOB-2007 Bundle Manager`)
  - [ ] User selects bbox or polygon region
  - [ ] Bundle Manager downloads basemap (Mapbox) + TrackIQ tiles (CDN) + DEM
  - [ ] Resumable on interrupt · integrity validation (checksum)
  - [ ] Marks bundle "Offline-ready" only after validation passes
  - [ ] Stores in `MOB-3002` Encrypted SQLite + WAL (AES-256)

- [ ] **Stage 8 — Runtime render** (`MOB-2001 NAV`)
  - [ ] Consumes validated bundles from Bundle Manager
  - [ ] Mapbox SDK renders on-device using GPU (Metal / OpenGL / Vulkan)
  - [ ] Initial render ≤2s · max 3 concurrent layers
  - [ ] Zero network calls

### Diagram

- [ ] **Single Mermaid `graph LR`** with 9 stages as columns, components as nodes within. Use the tile journey as the spine. Show side-arrows where governance / prohibition affects flow.

### Failure / branch paths

- [ ] What happens when user enters a region with no pre-downloaded tiles (map blank, but GNSS + tracking continue per Survival Core compliance)
- [ ] What happens when Bundle Manager integrity check fails (bundle marked corrupt · re-download required · no partial offline-ready state)
- [ ] What happens when CDN is unreachable during pre-journey download (user prompted to retry · no fallback to runtime fetch)

## Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md`
- TrackIQ pipeline DFD: `../3-flows/data-flow/dfd-trackiq-pipeline.md`
- Survival Core DFD: `../3-flows/data-flow/dfd-survival-core.md`
- Subsystem deep-dives:
  - CBE pipeline: `../2-subsystems/cbe-trackiq-pipeline.md`
  - Survival Core: `../2-subsystems/mob-survival-core.md`
- Mapbox SDK reference: `../../research/mapbox-sdk-overview.md`
- Compliance: `./compliance-matrix.md` — tile cost governance, runtime-no-network
- Performance: `./performance-targets.md` — ≤2s render, max layers
- Navigation: `../README.md`
