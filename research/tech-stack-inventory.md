# Trackaroo Phase 1 — Tech Stack Inventory

**Purpose:** A single source of truth for every technology, library, protocol, and pattern used in Phase 1 — with its role and the architectural component(s) it lives in. Use this when onboarding a new vendor, drafting RFT responses, evaluating an alternative, or checking "where does X show up in our system?"

**Source of truth:** Derived from `../diagrams/1-overview/trackaroo-phase1-architecture.md` (and its draw.io twin). When the diagram changes, update this file too.

**Status legend:**
- ✅ **Committed** — locked into Phase 1 spec
- 🟡 **TBD** — direction agreed, specific vendor/version pending
- 🔵 **Phase 2** — present in diagram as inert scaffold, not active in Phase 1

---

## 1. Quick reference (alphabetical)

| Tech | Category | Zone(s) | Status |
|---|---|---|---|
| Adapter Pattern (`ITrackIngestAdapter`) | Software pattern | Cloud Backend | ✅ |
| AES-256 | Encryption | Mobile (Local Data) | ✅ |
| AFAC feeds | External data | External | ✅ |
| AWS Terrain Tiles | External data (DEM) | External → Cloud Backend | ✅ |
| Bad Elf | External GPS receiver | External (Phase 2) | 🔵 |
| BLE Mesh | Comms transport | Mobile (App Layer) | ✅ |
| BOM feeds | External data (hazards) | External | ✅ |
| Dart | Language | Mobile | ✅ |
| Decoupled service / Pipes & Filters | Architectural pattern | Cloud Backend | ✅ |
| Firebase Auth | AuthN/AuthZ | OCS · Sync | ✅ |
| Firebase Firestore | Real-time cloud DB | Sync Engine | ✅ |
| Firestore SDK (offline persistence) | Client cache library | Mobile (Local Data) | ✅ |
| Flutter | App framework | Mobile | ✅ |
| Geoscience Australia feeds | External data | External | ✅ |
| GoTenna Mesh (SDK) | LoRa peripheral | External · Mobile | ✅ |
| Headless CMS / WordPress | Web CMS | Companion Website | ✅ |
| iOS 15+ | Target platform | Mobile | ✅ |
| Android 13+ | Target platform | Mobile | ✅ |
| LoRa | Comms transport | External · Mobile | ✅ |
| Mapbox SDK (Maps) | Mapping library | Mobile (Survival Core) · Cloud Backend (Ingest) | ✅ |
| Mapbox Studio | Map style editor | Tooling (vendor-side) | ✅ |
| Meshtastic (open) | LoRa firmware/peripheral | External · Mobile | ✅ |
| MVT (Mapbox Vector Tiles) | Tile format | Cloud Backend · Mobile | ✅ |
| OSM (OpenStreetMap) | External data | External | ✅ |
| PostgreSQL + PostGIS | Backend DB | Cloud Backend | ✅ |
| RBAC (Role-Based Access Control) | AuthZ model | OCS | ✅ |
| React | Web app framework | OCS | ✅ |
| SES feeds | External data | External | ✅ |
| Shapefile | Geospatial format | External (ingest input) | ✅ |
| SQLite + WAL | On-device DB | Mobile (Local Data) | ✅ |
| SRTM | DEM source | External | ✅ |
| Tile CDN | Distribution infra | Cloud Backend | 🟡 (vendor TBD) |
| TLS 1.3 | Transport security | OCS · Sync | ✅ |
| Trimble | External GPS receiver | External (Phase 2) | 🔵 |
| Wi-Fi Direct | Comms transport | Mobile (App Layer) | ✅ |
| Cloud host (AWS / GCP) | Infrastructure | Cloud Backend | 🟡 (provider TBD) |

---

## 2. By zone — detailed mapping

### 2.1 External Data & Distribution (peach zone)

| Tech | Role | Component(s) | Notes |
|---|---|---|---|
| **Mapbox** (vector basemap + vector tiles) | Source of basemap rendered on-device + raw track source for backend ingest | `EXT-9001a` Basemap · `EXT-9001b` Track Data Feeds | Trackaroo holds the API keys (not the vendor). Pre-journey download only — never hit at runtime on the device. See `mapbox-sdk-overview.md` for SDK deep-dive |
| **OSM (OpenStreetMap)** | Open-license vector tile + geometry source · **the base vector data NAV renders on-device** | `EXT-9001b` Track Data Feeds · `MOB-2001` Offline Navigation Engine (via Mapbox SDK) | Two use modes: (a) raw track input to TrackIQ ingest, (b) the vector geometry inside Mapbox basemap tiles NAV renders offline. Spec mandate: NAV "utilizes the Mapbox SDK integrated with OpenStreetMap (OSM) vector tiles" — see `diagrams/2-subsystems/mob-survival-core.md` |
| **GPX** | GPS Exchange Format — track recordings | `EXT-9001b` Track Data Feeds | Vendor-supplied or community-supplied raw tracks ingested into the pipeline |
| **Shapefile** | ESRI geospatial format | `EXT-9001b` Track Data Feeds | Common format for authority/government datasets |
| **AWS Terrain Tiles** | DEM source — pre-rendered Mapbox-format terrain RGB tiles | `EXT-9002` DEM Sources | Feeds the `CBE-5002` DEM Enrichment Engine |
| **SRTM (Shuttle Radar Topography Mission)** | DEM source — raw elevation grids | `EXT-9002` DEM Sources | Alternative / supplementary to AWS Terrain Tiles |
| **BOM** (Bureau of Meteorology) | Authority hazard feed — weather, fire weather | `EXT-9004` Authority Hazard Feeds | Statutory source — Authority-Origin Mandate enforced |
| **AFAC** (Australasian Fire & Emergency Service Authorities Council) | Authority hazard feed — fire incidents | `EXT-9004` Authority Hazard Feeds | Statutory source |
| **SES** (State Emergency Service) | Authority hazard feed — floods, storms | `EXT-9004` Authority Hazard Feeds | Statutory source |
| **Geoscience Australia** | Authority hazard feed — geological events | `EXT-9004` Authority Hazard Feeds | Statutory source |
| **GoTenna Mesh** (SDK) | Proprietary LoRa peripheral + SDK | `EXT-9005` LoRa Peripherals | Pairs to mobile via BLE; extends comms range beyond cell coverage |
| **Meshtastic** (open) | Open-source LoRa firmware + protocol | `EXT-9005` LoRa Peripherals | Open alternative to GoTenna for hobbyist/community devices |
| **Trimble** 🔵 | Survey-grade external GPS | `EXT-9006` External GPS (Phase 2) | Inert in Phase 1 — diagram scaffold only |
| **Bad Elf** 🔵 | Consumer high-accuracy GNSS receiver | `EXT-9006` External GPS (Phase 2) | Inert in Phase 1 |

---

### 2.2 Cloud Backend (purple zone, `CBE`)

| Tech | Role | Component(s) | Notes |
|---|---|---|---|
| **Cloud host** (AWS or GCP) 🟡 | Compute + DB hosting | All `CBE-*` | Provider TBD |
| **Decoupled service / Pipes & Filters** | Architectural pattern for the pipeline worker | `CBE-5000` TrackIQ Backend Pipeline Worker | Each stage (Ingest → DEM → Score → Tile) is an isolated filter |
| **Adapter Pattern** (`ITrackIngestAdapter`) | Vendor-agnostic ingestion interface | `CBE-5001` Ingestion Adapter | Lets us swap GPX/Shapefile/OSM/Mapbox sources without restructuring the pipeline |
| **PostgreSQL + PostGIS** | Relational DB with geospatial extension | `CBE-6000` Backend Database (`CBE-6001 raw_ingested_tracks`, `CBE-6002 track_review_queue`, `CBE-6003 production_tracks`, `CBE-6004 system_audit_log`) | PostGIS provides GIS types + spatial indices for track geometry. `system_audit_log` is append-only with 7-year retention — backend choice provisional, see design-decisions.md §S1 |
| **MVT (Mapbox Vector Tile)** format | Output tile format from `CBE-5004` Tile Generator | `CBE-5004` Tile Generator · `CBE-7001` Tile Server / CDN | Same format consumed by the mobile Mapbox SDK |
| **Tile CDN** 🟡 | MVT delivery infrastructure | `CBE-7001` Tile Server / CDN | Pre-journey download endpoint; Trackaroo-owned. Specific CDN vendor TBD |

---

### 2.3 Firebase Firestore — Sync Engine (yellow zone, `SYN`)

| Tech | Role | Component(s) | Notes |
|---|---|---|---|
| **Firebase Firestore** (cloud) | Real-time bidirectional cloud DB bridging Cloud Backend ⇄ Mobile | `SYN-7001` Firestore (cloud) | Collections: `user_profiles`, `trackmate_history`, `trackiq_scores`, `haztrack_cache`, `pcr_queue` (append-only) |
| **TLS 1.3** | Transport encryption | `SYN_COMPLIANCE` (V-12 / V-13) | All Firestore traffic in transit |
| **Append-only write rules** | Write-Once Security model | `SYN-7001` (PCR queue) | Enforced via Firestore security rules — PCRs cannot be mutated after write |

---

### 2.4 Operations Console — OCS (teal zone)

| Tech | Role | Component(s) | Notes |
|---|---|---|---|
| **React** | Web app framework | All `OCS-*` modules | Internal staff web app |
| **Firebase Auth** | AuthN provider | `OCS-4101` User & Account Admin | Shared with the Mobile App for unified identity |
| **RBAC** (Role-Based Access Control) | AuthZ model | OCS-wide (esp. `OCS-4301` Track Data & Grade Admin) | Approvers: Authorised Contributor · Project Director |
| **TLS 1.3** | Transport encryption | OCS ↔ Cloud Backend, OCS ↔ Firestore | |

---

### 2.5 Mobile Application (blue zone, `MOB`)

| Tech | Role | Component(s) | Notes |
|---|---|---|---|
| **Flutter** | Cross-platform app framework | All `MOB-*` UI + logic | Single codebase for iOS + Android |
| **Dart** | Programming language | All `MOB-*` | Flutter's native language |
| **iOS 15+** | Target platform | Mobile (deployment) | Minimum supported iOS version |
| **Android 13+** | Target platform | Mobile (deployment) | Minimum supported Android version |
| **Mapbox SDK** (Maps) | On-device map rendering + offline tile store · renders **OSM-derived vector tiles** | `MOB-2001` Offline Navigation Engine | Uses GPU (Metal/OpenGL) for client-side rendering. Vector tile + offline TileStore are critical to "100% offline-first" mandate. Tile content origin = OpenStreetMap (delivered through Mapbox vector tile pipeline · pre-downloaded as regional bundles via bbox/polygon selection). Navigation SDK (voice / turn-by-turn) is **not used** in Phase 1 |
| **SQLite + WAL** | On-device relational DB with Write-Ahead Log | `MOB-3002` Encrypted SQLite + WAL (shared store for Core data + TrackMate Firebase-independent queue) | Crash-survivable, deterministic. Slitigenz proposes AES-256 encrypted SQLite (sqflite or similar). Candidates: sqflite · Isar · Hive/Hive CE · ObjectBox |
| **AES-256** | At-rest encryption | `MOB-3002` · `MOB-3003` Pro Incident Log · all local stores | All Survival Core + App-layer local data encrypted on disk |
| **Read-only asset bundle** | Pre-loaded immutable content at install | First Aid Universal Baseline (inside `MOB-1002`) — not a separate data store | Bundled in app binary, updated only via app version (clinical-review-gated) |
| **Tile file storage (MBTiles or vector tiles)** | Mapbox SDK offline tile bundles | `MOB-3004` Map Tile Cache | User-initiated downloads, integrity-validated, large filesystem |
| **TTL-bounded cache** | Hazard overlay cache (region-synced) | `MOB-3005` HazTrack Overlay Cache | Synced from Firestore haztrack_cache · render-only-local · TTL expiry |
| **Firestore SDK** (mobile, with offline persistence) | Cached cloud DB on device | `MOB-3001` Firestore Local Cache | Auto-persists Firestore data locally; mediates all app-data sync with the cloud |
| **BLE Mesh** | Short-range comms transport | `MOB-1102` Multi-Tier Transport | Peer-to-peer comms for nearby devices |
| **Wi-Fi Direct** | Mid-range comms transport | `MOB-1102` Multi-Tier Transport | Higher-bandwidth peer-to-peer when both devices opt in |
| **LoRa** | Long-range low-power comms transport | `MOB-1102` Multi-Tier Transport | Via paired GoTenna / Meshtastic peripherals |
| **GoTenna Mesh SDK** | LoRa peripheral pairing | `MOB-1102` ↔ `EXT-9005` | Proprietary integration |
| **Meshtastic** | LoRa peripheral pairing | `MOB-1102` ↔ `EXT-9005` | Open integration |

---

### 2.6 Companion Website (beige zone, `CMS`)

| Tech | Role | Component(s) | Notes |
|---|---|---|---|
| **WordPress / Headless CMS** | Public branding site + anchor statement publishing | `CMS-8001` Companion Website | Discovery Gate 8 Jun 2026. Isolated from OCS and Mobile App — no shared data plane |

---

## 3. Cross-cutting concerns

| Concern | Tech | Where enforced |
|---|---|---|
| **Authentication** | Firebase Auth | OCS · Mobile App · Sync |
| **Authorization** | RBAC | OCS · Firestore security rules |
| **Encryption at rest** | AES-256 | `MOB-3002` (mobile SQLite) |
| **Encryption in transit** | TLS 1.3 | All cloud ↔ device + cloud ↔ OCS traffic |
| **Offline persistence (cloud-mirrored)** | Firestore SDK auto-cache | `MOB-3001` |
| **Offline persistence (core)** | SQLite + WAL | `MOB-3002` |
| **Crash survivability** | WAL journaling | `MOB-3002` |
| **Append-only / write-once** | Firestore security rules + SQLite schema | `SYN-7001` (PCR), `MOB-3002` (SOS log) |
| **Tile format consistency** | MVT end-to-end | `CBE-5004` → `CBE-7001` → `MOB-2001` |
| **Vendor-agnostic ingestion** | Adapter Pattern | `CBE-5001` |
| **Pipeline isolation** | Pipes & Filters | `CBE-5000` |

---

## 4. Tech we explicitly do NOT use (Phase 1 negative space)

Documenting what's *out of scope* prevents scope creep and clarifies vendor briefs.

| Tech / Capability | Why excluded |
|---|---|
| AI / ML inference | Compliance constraint `RT-09` — TrackIQ must be deterministic |
| Adaptive scoring logic | Same — grades are objective attributes of terrain, not telemetry-influenced |
| Mapbox Navigation SDK (voice / turn-by-turn) | Out of Phase 1 scope; routing is done locally with custom logic |
| Cloud rerouting | Survival Core is 100% offline-first; routes calculated locally from cached tiles |
| External search APIs (Google Places etc.) | Survival Core forbids external API calls at runtime |
| Geocoding services (runtime) | Same — search uses local POIs + Anchor Points only |
| Telemetry-based grade adjustment | Compliance — Zero Telemetry Weighting |

---

## 5. Open vendor / version decisions

Track these to convergence — each one is a blocker for procurement or contract scoping.

- [ ] Cloud host: **AWS vs GCP** for `CBE-*` compute + Postgres
- [ ] CDN vendor for `CBE-7001` (CloudFront / Cloud CDN / Fastly / Cloudflare)
- [ ] Mapbox SDK pricing tier (MAU projection needed)
- [ ] Confirm Mapbox Maps SDK only (no Navigation SDK)
- [ ] WordPress vs Headless CMS final choice for `CMS-8001`
- [ ] Firebase project layout (single project vs prod/staging split)
- [ ] PostgreSQL hosting model: managed (RDS / Cloud SQL) vs self-hosted on cloud VMs

---

## 6. See also

- `../diagrams/1-overview/trackaroo-phase1-architecture.md` — visual zone map + edges
- `../diagrams/2-subsystems/` — per-zone component deep-dives
- `../diagrams/3-flows/data-flow/dfd-survival-core.md` — on-device data lifecycle
- `../diagrams/3-flows/data-flow/dfd-trackiq-pipeline.md` — backend pipeline data lifecycle
- `../diagrams/4-cross-cutting/` — compliance · performance · tile lifecycle
- `../diagrams/README.md` — navigation map
- `./mapbox-sdk-overview.md` — Mapbox SDK deep-dive
- `../CLAUDE.md` — visual style guide + folder conventions
