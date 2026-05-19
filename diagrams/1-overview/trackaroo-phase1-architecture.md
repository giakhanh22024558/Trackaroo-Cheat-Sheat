# Trackaroo® Phase 1 — System Architecture (Overview)

**Tier 1 · C4 Container level.** Bird's-eye view of the whole system — zones, components by name, and inter-zone relationships only. For component internals (schemas, control flow, performance budgets, prohibited edges), follow the deep-dive links below.

**Scope:** Cross-zone architecture covering External providers, Cloud Backend (CBE), Operations Console (OCS), Firebase Firestore sync, Mobile App (Experience + Survival Core + Local Data), and Companion Website (CMS).

**Companion artifacts:**
- Draw.io equivalent: `./trackaroo-phase1-architecture.drawio` — page **Architecture** (overview) + **Legend** + per-subsystem detail pages
- Subsystem deep-dives: `../2-subsystems/` — `cbe-trackiq-pipeline.md` · `mob-survival-core.md` · `mob-application-layer.md` · `ocs-operations-console.md` · `syn-firestore-sync.md`
- Behavioral views: `../3-flows/` — data-flow DFDs · state
- Cross-cutting: `../4-cross-cutting/` — compliance matrix · performance targets · tile lifecycle
- Navigation: `../README.md`

**What's intentionally NOT in this overview** (moved out as part of C4-style split):

| Removed from here | Now lives in |
|---|---|
| Component descriptions beyond ID + name | `../2-subsystems/<zone>.md` |
| Compliance banners + PROHIBITED edges (RT-09, V-12/V-13, HazTrack isolation, Core/Cloud isolation) | `../4-cross-cutting/compliance-matrix.md` |
| Performance targets (≤2s render, max 3 layers, 90-day audit, etc.) | `../4-cross-cutting/performance-targets.md` |
| Intra-zone control/data flows (e.g. CBE pipeline stages, OCS TIQ→TDGA→Queue) | `../2-subsystems/<zone>.md` |
| Phase 2 inert scaffolds (External GPS, etc.) | `../2-subsystems/` (where applicable) |
| Tile data lifecycle end-to-end | `../4-cross-cutting/tile-lifecycle.md` |

---

## Legend

Visual vocabulary for this diagram (and its draw.io twin). Mirrors the **Legend** page in `trackaroo-phase1-architecture.drawio`.

### Shape vocabulary (Level 1 — minimal, only where semantics genuinely differ)

| Shape | Semantic | When to use |
|---|---|---|
| **Rectangle** (default) | Generic component / service / UI module / document | Anything that doesn't fit one of the three below — covers the vast majority |
| **Cylinder** `[(name)]` | Data store | Local SQLite, Firestore collection, cloud DB, tile cache |
| **Process box** (`shape=process` in draw.io) | Pipeline / transformation stage | TrackIQ ingest, DEM enrichment, scoring, tile publish |
| **Stadium / Pill** (`rounded=1;arcSize=80`) | External provider / actor | Mapbox, BOM, AFAC, app stores |

### Arrow vocabulary

| Arrow | Style | Label form | Meaning |
|---|---|---|---|
| **Solid** `-->` | grey/black solid | **Verb phrase** | Control / operational / runtime dependency |
| **Dashed dotted purple** `-.->` w/ `stroke-dasharray:2 3` + `stroke:#6a1b9a` | tight purple dots | **Noun** | Data payload flow |
| **Bidirectional** `<-->` | solid, both ends | "R/W <store>" | Read + write relationship with a data store |
| **Red dashed** `-.->` w/ `stroke:#c62828,stroke-dasharray:5 5` | red dashes | `[X] PROHIBITED` | Forbidden path (see compliance matrix) |
| **Grey dashed** `-.->` w/ `stroke:#9e9e9e` | grey dashes | *italic note* | Phase 2 / inert / placeholder |

### Zone color palette

| Zone | Fill | Stroke | Role |
|---|---|---|---|
| External data & distribution | `#fff3e0` peach | `#e65100` | Third-party providers, hardware |
| Cloud Backend (CBE) | `#d1c4e9` purple | `#5e35b2` | Compute + DB + Distribution |
| CBE nested sub-groups | `#ede7f6` lighter purple | `#5e35b2` | Compute / DB / Distribution |
| Operations Console (OCS) | `#b2dfdb` teal | `#00695c` | Web app for staff |
| OCS nested sub-groups | `#e0f2f1` lighter teal | `#00695c` | User / Content / Grade |
| Firebase Firestore (SYN) | `#fff9c4` yellow | `#f9a825` | Cloud sync engine |
| Mobile App (outer) | `#bbdefb` light blue | `#0277bd` | Experience + Core + Data |
| Mobile — Application sub-layer | `#e3f2fd` lighter blue | `#1976d2` | UX / Experience |
| Mobile — Survival Core | `#c8e6c9` green | `#2e7d32` | 100% offline safety-critical |
| Mobile — Local Data | `#f3e5f5` lavender | `#6a1b9a` | Encrypted SQLite + WAL |
| Companion Website (CMS) | `#f5f5dc` beige | `#827717` | Public-facing WordPress |
| Canvas background (draw.io) | `#eceff1` BlueGrey 50 | — | Improves label readability |

### Component ID naming conventions

| Prefix | Domain | Examples |
|---|---|---|
| `EXT-9xxx` | External providers / hardware | `EXT-9001a` Mapbox basemap, `EXT-9004` Authority hazards |
| `CBE-5xxx / 6xxx / 7xxx` | Cloud Backend — Compute / DB / Distribution | `CBE-5000` TrackIQ pipeline, `CBE-6001` Postgres |
| `OCS-4xxx` | Operations Console | `OCS-4202` TrackIQ Scoring Operations |
| `SYN-7xxx` | Sync engine (Firestore) | `SYN-7001` Firestore collections |
| `MOB-1xxx` | Mobile — Application layer | `MOB-1001` TrackMate |
| `MOB-2xxx` | Mobile — Survival Core | `MOB-2001` NAV, `MOB-2007` Bundle Manager |
| `MOB-3xxx` | Mobile — Local Data | `MOB-3002` Survival Core Data + Comms Queue *(spec alias: "Encrypted SQLite + WAL"; renamed in diagram to disambiguate from parent SQLITE_STORE container — see design-decisions M0k)* |
| `CMS-8xxx` | Companion Website | `CMS-8001` WordPress site |

---

## Diagram

```mermaid
---
config:
  layout: elk
  theme: base
  themeVariables:
    fontFamily: Arial
    fontSize: 13px
  elk:
    mergeEdges: true
    nodePlacementStrategy: BRANDES_KOEPF
    'elk.alignment': CENTER
---
graph TB

%% ============================================================
%% EXTERNAL DATA & DISTRIBUTION (peach, top)
%% ============================================================
subgraph EXT["<b>EXTERNAL DATA &amp; DISTRIBUTION</b><br/><i>Third-party providers · Trackaroo retains account ownership</i>"]
    direction LR

    subgraph EXT_DATA["<b>Data Inputs</b>"]
        direction TB
        EXT_BASEMAP["<i>EXT-9001a</i> · <b>Basemap (Mapbox)</b>"]
        EXT_TRACKDATA["<i>EXT-9001b</i> · <b>Track Data Feeds</b>"]
        EXT_DEM["<i>EXT-9002</i> · <b>DEM Sources</b>"]
        EXT_HAZARD["<i>EXT-9004</i> · <b>Authority Hazard Feeds</b>"]
        EXT_BASEMAP ~~~ EXT_TRACKDATA
        EXT_DEM ~~~ EXT_HAZARD
    end

    subgraph EXT_HW["<b>External Peripherals</b> · <i>Separate physical devices · BLE/USB-paired</i>"]
        direction TB
        EXT_LORA["<i>EXT-9005</i> · <b>LoRa Peripherals</b>"]
        EXT_GPS["<i>EXT-9006</i> · <b>External GPS [PHASE 2]</b><br/><b>Inactive in Phase 1.</b><br/><i>Trimble · Bad Elf (Pro tier)</i>"]
    end

    EXT_DATA ~~~ EXT_HW
end

%% ============================================================
%% CLOUD BACKEND (purple) + OCS (teal) — row 2
%% ============================================================
subgraph BACKEND_ROW[" "]
    direction LR

    subgraph CBE["<b>CLOUD BACKEND</b><br/><i>Tech: Cloud-hosted (provider TBD) · Pipes &amp; Filters</i>"]
        direction TB

        subgraph CBE_COMPUTE["<i>CBE-5000</i> · <b>TrackIQ™ Backend Pipeline Worker</b>"]
            direction LR
            INGEST["<i>CBE-5001</i> · <b>Ingestion Adapter</b>"]
            DEM["<i>CBE-5002</i> · <b>DEM Enrichment Engine</b>"]
            SCORE["<i>CBE-5003</i> · <b>Scoring Engine</b>"]
            TILE["<i>CBE-5004</i> · <b>Tile Generator</b>"]
            INGEST ~~~ DEM
            DEM ~~~ SCORE
            SCORE ~~~ TILE
        end

        subgraph CBE_DB["<i>CBE-6000</i> · <b>Backend Database</b> <i>(PostgreSQL + PostGIS)</i>"]
            direction LR
            RAW[("<i>CBE-6001</i> · <b>raw_ingested_tracks</b>")]
            QUEUE[("<i>CBE-6002</i> · <b>track_review_queue</b>")]
            PROD[("<i>CBE-6003</i> · <b>production_tracks</b>")]
            SYS_AUDIT[("<i>CBE-6004</i> · <b>system_audit_log</b>")]
            RUN_HIST[("<i>CBE-6005</i> · <b>pipeline_run_history</b><br/><i>🟡 PROVISIONAL · S2 pending</i>")]
            RAW ~~~ QUEUE
            QUEUE ~~~ PROD
            PROD ~~~ SYS_AUDIT
            SYS_AUDIT ~~~ RUN_HIST
        end

        subgraph CBE_DISTRIBUTION["<i>CBE-7000</i> · <b>Tile Distribution</b>"]
            CBE_CDN["<i>CBE-7001</i> · <b>Tile Server / CDN</b>"]
        end

        CBE_COMPUTE ~~~ CBE_DB
        CBE_DB ~~~ CBE_DISTRIBUTION
    end

    subgraph OCS["<b>OPERATIONS CONSOLE (OCS-5026)</b><br/><i>Tech: React · Firebase Auth · RBAC</i>"]
        direction TB

        subgraph OCS_USER["<b>General &amp; Settings</b>"]
            direction LR
            ADMIN["<i>OCS-4101</i> · <b>User &amp; Account Admin</b>"]
            BETAADMIN["<i>OCS-4102</i> · <b>Beta &amp; Alpha Tester Mgmt</b>"]
            ADMIN ~~~ BETAADMIN
        end

        subgraph OCS_CONTENT["<b>Metrics Monitoring</b>"]
            direction LR
            HAZADMIN["<i>OCS-4201</i> · <b>HazTrack™ Feed Mgmt</b>"]
            TIQADMIN["<i>OCS-4202</i> · <b>TrackIQ™ Scoring Operations</b>"]
            PCRADMIN["<i>OCS-4203</i> · <b>PCR Management</b>"]
            HAZADMIN ~~~ TIQADMIN
            TIQADMIN ~~~ PCRADMIN
        end

        subgraph OCS_GRADE["<b>Verification</b>"]
            direction LR
            TDGA["<i>OCS-4301</i> · <b>Track Data &amp; Grade Admin</b>"]
            FACA["<i>OCS-4302</i> · <b>First Aid Content Admin</b>"]
            AUDIT["<i>OCS-4303</i> · <b>Audit Log Viewer</b>"]
            TDGA ~~~ FACA
            FACA ~~~ AUDIT
        end

        OCS_USER ~~~ OCS_CONTENT
        OCS_CONTENT ~~~ OCS_GRADE
    end

    CBE ~~~ OCS
end

%% ============================================================
%% FIREBASE FIRESTORE (yellow, sync engine)
%% ============================================================
subgraph SYN["<b>FIREBASE FIRESTORE — Cloud Sync Engine</b><br/><i>Tech: Firestore real-time DB · auto offline persistence · TLS 1.3</i>"]
    FIRESTORE[("<i>SYN-7001</i> · <b>Firestore (cloud)</b>")]
end

%% ============================================================
%% MOBILE APPLICATION (blue) — Flutter, Dual-Layer
%% ============================================================
subgraph MOB["<b>MOBILE APPLICATION</b><br/><i>Tech: Flutter · Dart · Dual-Layer Architecture · iOS 15+ / Android 13+</i>"]
    direction TB

    subgraph MOB_TOP[" "]
        direction LR

        subgraph MOB_APP["<i>MOB-1000</i> · <b>Application Layer</b>"]
            direction LR
            TM["<i>MOB-1001</i> · <b>TrackMate™</b>"]
            FA["<i>MOB-1002</i> · <b>First Aid Reference</b>"]
            PRESETS["<i>MOB-1003</i> · <b>Six Archetype Presets</b>"]
            PCRFW["<i>MOB-1004</i> · <b>PCR Framework</b>"]
        end

        subgraph MOB_CORE["<i>MOB-2000</i> · <b>Survival Core</b><br/><i>100% offline-first · deterministic · data-flow order →</i>"]
            direction LR
            BUNDLE["<i>MOB-2007</i> · <b>Map Bundle Download Manager</b>"]
            NAV["<i>MOB-2001</i> · <b>Offline Navigation Engine</b>"]
            BT["<i>MOB-2002</i> · <b>BackTrack™</b><br/><span style='background-color:#ffe082;color:#000;padding:1px 4px;font-size:8px;'>P2 ESCROW SCAFFOLD · Inactive in Phase 1.</span>"]
            SAP["<i>MOB-2006</i> · <b>Safe Anchor Points</b>"]
            HT["<i>MOB-2003</i> · <b>HazTrack™</b>"]
            SOS["<i>MOB-2004</i> · <b>SOS Emergency Logging</b>"]
            EVT["<i>MOB-2005</i> · <b>Local Event Log</b>"]
        end

        MOB_APP ~~~ MOB_CORE
    end

    %% MOB_G2 (Comms & Transport) — STANDALONE LAYER between App+Core and MOB_DATA
    %% Reflects CAL's role as "buffer and gateway" serving both App (TrackMate)
    %% and Survival Core (Phase 2 BackTrack Emergency Escrow via Satellite Relay)
    subgraph MOB_G2["<i>MOB-1100</i> · <b>Comms &amp; Transport</b><br/><i>Buffer + gateway · serves App (TrackMate now) · Core (BackTrack Phase 2 escrow)</i>"]
        direction TB
        CAL["<i>MOB-1101</i> · <b>CAL · Comms Abstraction Layer</b><br/><i>4 mandatory flags: satReady · queueEnabled · offlineBeacon · partialSignal</i><br/><span style='background-color:#ffe082;color:#000;padding:1px 4px;font-size:8px;'>satReady = FALSE · Inactive in Phase 1.</span>"]
        MTT["<i>MOB-1102</i> · <b>Multi-Tier Transport</b><br/><i>BLE Mesh · Wi-Fi Direct · LoRa · (Sat Phase 2)</i>"]
        CAL ~~~ MTT
    end

    MOB_TOP ~~~ MOB_G2

    subgraph MOB_DATA["<i>MOB-3000</i> · <b>Mobile Local Data</b>"]
        direction LR
        FCACHE[("<i>MOB-3001</i> · <b>Firestore Local Cache</b><br/><i>[CLOUD SYNC]</i>")]
        %% SQLITE_STORE: visual grouping of all data physically stored in Slitigenz unified SQLite + WAL file
        subgraph SQLITE_STORE["<b>Encrypted SQLite + WAL Store</b> · <i>Slitigenz unified</i>"]
            direction LR
            SQL[("<i>MOB-3002</i> · <b>Survival Core Data + Comms Queue</b><br/><i>[LOCAL-ONLY]</i>")]
            PRO_LOG[("<i>MOB-3003</i> · <b>Professional Incident Log</b><br/><i>[APP 3 SENSITIVE · CONSENT-GATED SYNC]</i>")]
            HAZ_CACHE[("<i>MOB-3005</i> · <b>HazTrack Overlay Cache</b><br/><i>[Firebase-cache-only · TTL]</i>")]
            SQL ~~~ PRO_LOG
            PRO_LOG ~~~ HAZ_CACHE
        end
        MAP_CACHE[("<i>MOB-3004</i> · <b>Map Tile Cache</b><br/><i>[Mapbox SDK native]</i>")]
        FCACHE ~~~ SQLITE_STORE
        SQLITE_STORE ~~~ MAP_CACHE
    end

    MOB_G2 ~~~ MOB_DATA

    %% Device Hardware foundation layer (bottom of MOB, below MOB_DATA)
    subgraph MOB_HW["<i>MOB-0000</i> · <b>Device Hardware</b> · <i>Built-in sensors + transport radios</i>"]
        direction LR
        HW_GNSS["<i>MOB-0001</i> · <b>GNSS Sensor</b>"]
        HW_BLE["<i>MOB-0002</i> · <b>BLE Mesh Radio</b><br/><i>Tier 1 Primary</i>"]
        HW_WIFI["<i>MOB-0003</i> · <b>Wi-Fi Direct / MPC</b><br/><i>Tier 1 Fallback · ≤0.8%/hr aggregate</i>"]
        HW_SAT["<i>MOB-0004</i> · <b>Satellite Relay [PHASE 2]</b><br/><b>Inactive in Phase 1.</b><br/><i>Future: BackTrack Emergency Escrow</i>"]
    end
    MOB_DATA ~~~ MOB_HW
end

%% ============================================================
%% COMPANION WEBSITE (beige, isolated)
%% ============================================================
subgraph CMS["<b>COMPANION WEBSITE</b><br/><i>Tech: WordPress / Headless CMS</i>"]
    WEB["<i>CMS-8001</i> · <b>Companion Website</b>"]
end

%% ============================================================
%% ZONE VERTICAL STACK
%% ============================================================
    EXT --> BACKEND_ROW
    BACKEND_ROW --> SYN
    SYN --> MOB

%% ============================================================
%% LAYER-LEVEL / GROUP-LEVEL EDGES ONLY
%% Edges connect zones / sub-groups · never individual components.
%% Component-level detail lives in 2-subsystems/<zone>.md
%% ============================================================

    %% EXT → CBE / OCS / MOB
    EXT_DATA -.->|"<b>track + DEM data</b>"| CBE_COMPUTE
    EXT_DATA -.->|"<b>authority hazard alerts</b>"| OCS_CONTENT
    EXT_DATA -.->|"<b>basemap tiles</b><br/><i>(pre-journey)</i>"| MOB_CORE
    EXT_HW <-->|"Pairs over BLE · exchanges LoRa frames"| MOB_G2
    HW_GNSS -.->|"<b>GNSS position fix</b><br/><i>(continuous · NAV/BT/SOS)</i>"| MOB_CORE
    MOB_G2 <-->|"Drives BLE · Wi-Fi · LoRa radios"| MOB_HW
    HW_SAT -.->|"<i>Phase 2 pathway · Inactive in Phase 1.</i>"| MOB_G2

    %% CBE_DISTRIBUTION → MOB (baked tiles to Bundle Manager in Core)
    CBE_DISTRIBUTION -.->|"<b>baked tiles + manifest</b><br/><i>(pre-journey)</i>"| MOB_CORE

    %% OCS ↔ CBE (governance — layer level)
    OCS -->|"Governance: configures · approves · audits"| CBE

    %% Backend / OCS → SYN
    CBE_DB -->|"Publishes baked scores"| SYN
    OCS_CONTENT <-->|"<b>R/W Firestore data</b><br/><i>Writes: PCR updates · cached hazard data · audit log (OCS-5026 append-only · 7yr)</i><br/><i>Reads: PCRs (review/supersede surface) · hazard metadata · audit log queries</i>"| SYN

    %% SYN ↔ MOB (sync) — per-store edges (storage exception extended to SYN)
    %% V4 storage exception: which MOB-3000 component accepts FB ingress matters
    %% for Firebase Independence audit (SQL/PRO_LOG/MAP_CACHE must NOT receive).
    SYN -.->|"<b>scores · PCRs · profiles</b><br/><i>(auto-sync · Firestore SDK)</i>"| FCACHE
    SYN -.->|"<font color='#c62828'><b>cached hazard data</b><br/><i>(Firebase ingress EXCEPTION per §7 · TTL refill · sync-when-online only)</i></font>"| HAZ_CACHE
    MOB_APP -->|"User data writes"| SYN

    %% linkStyle for SYN → HAZ_CACHE edge:
    %% Counted across ALL edges (including ~~~ layout-hint links) — index = 41
    %% Keep stroke purple (still data flow) · font RED to flag Firebase ingress EXCEPTION per §7
    %% Belt-and-suspenders: inline <font color='#c62828'> in label above ensures red text
    %% even if linkStyle index drifts as the diagram evolves
    linkStyle 41 stroke:#6a1b9a,stroke-width:2px,stroke-dasharray:2 3,color:#c62828,fill:#c62828

    %% ============================================================
    %% MOB intra-layer · storage relationships at COMPONENT level
    %% V4 exception (storage only): per-store edges make data-integrity
    %% boundaries explicit (which layer touches which sensitivity class).
    %% All other layer-↔-layer edges remain at group level per V4.
    %% ============================================================

    %% Application Layer ↔ stores
    MOB_APP <-->|"R/W app data<br/><i>(profiles · presets · PCR drafts)</i>"| FCACHE
    MOB_APP <-->|"<b>R/W App-layer queues</b><br/><i>(CAL Comms · M0f Firebase-independent)<br/>+ (PCR submissions · offline-queue-first)</i>"| SQL
    MOB_APP <-->|"R/W Pro tier incidents<br/><i>(APP 3 sensitive · FA Pro)</i>"| PRO_LOG

    %% Survival Core ↔ stores
    MOB_CORE <-->|"R/W Core data<br/><i>(breadcrumbs · SOS · events · anchors)</i>"| SQL
    MOB_CORE <-->|"R/W tile bundles<br/><i>(BUNDLE writes · NAV reads)</i>"| MAP_CACHE
    HAZ_CACHE -->|"Reads hazard overlays<br/><i>(HT runtime · local-only)</i>"| MOB_CORE

    %% ============================================================
    %% CONSENT-GATED SYNC — Pro Incident Log opt-in cloud sync
    %% APP 3 sensitive · explicit user consent required
    %% ============================================================
    PRO_LOG -.->|"<b>User-consent-gated sync</b><br/><i>(APP 3 · opt-in only · explicit consent)</i>"| SYN

    %% ============================================================
    %% SURVIVAL CORE ISOLATION BOUNDARIES
    %% Detail rationale → ../4-cross-cutting/compliance-matrix.md
    %% ============================================================
    %% MOB_APP ⇎ MOB_CORE: rendered as visual ISOLATION BOUNDARY wall
    %% in the draw.io twin (no arrow — the two are architecturally
    %% independent, not "prohibited from interacting"). Mermaid lacks
    %% native wall primitives so we use a barrier note node below.
    BARRIER{{"<b>━━━ IMMUTABLE SEPARATION BOUNDARY ━━━</b><br/>Experience Layer ⇎ Survival Core<br/><i>architecturally independent — no shared state, no shared lifecycle</i>"}}
    MOB_APP ~~~ BARRIER
    BARRIER ~~~ MOB_CORE

    %% Cloud / Sync prohibitions (kept as arrows — these ARE data-flow restrictions)
    SYN -.->|"<b>[X] PROHIBITED</b><br/>Cloud cannot push to Core<br/>(Firebase Independence)"| MOB_CORE
    MOB_CORE -.->|"<b>[X] PROHIBITED</b><br/>Zero Transmission —<br/>Core never outbound"| SYN

%% ============================================================
%% STYLES
%% ============================================================
    classDef whiteBox fill:#ffffff,stroke:#555,stroke-width:1px,color:#000
    classDef pipelineBox fill:#ffffff,stroke:#5e35b2,stroke-width:1.2px,color:#000
    classDef ocsBox fill:#ffffff,stroke:#00695c,stroke-width:1.2px,color:#000
    classDef firestore fill:#ffffff,stroke:#f9a825,stroke-width:1.5px,color:#000
    classDef sqliteBox fill:#ffffff,stroke:#6a1b9a,stroke-width:1.5px,stroke-dasharray:3 2,color:#000
    classDef cacheBox fill:#ffffff,stroke:#f9a825,stroke-width:1.2px,color:#000
    classDef dbBox fill:#ffffff,stroke:#5e35b2,stroke-width:1.2px,color:#000
    classDef externalBox fill:#ffffff,stroke:#e65100,stroke-width:1.2px,color:#000
    classDef webBox fill:#ffffff,stroke:#827717,stroke-width:1.2px,color:#000
    classDef barrierWall fill:#fff5f5,stroke:#c62828,stroke-width:3px,stroke-dasharray:8 4,color:#c62828

    class TM,FA,PRESETS,PCRFW,CAL,MTT whiteBox
    class NAV,BT,HT,SOS,EVT,SAP,BUNDLE whiteBox
    class INGEST,DEM,SCORE,TILE,CBE_CDN pipelineBox
    class RAW,QUEUE,PROD,SYS_AUDIT dbBox
    class RUN_HIST provisionalDbBox

    %% Provisional cylinder style — preemptive structural commit pending design-decision S2
    classDef provisionalDbBox fill:#fff8e1,stroke:#f57c00,stroke-width:1.5px,stroke-dasharray:6 3,color:#e65100
    class ADMIN,BETAADMIN,HAZADMIN,TIQADMIN,PCRADMIN,TDGA,FACA,AUDIT ocsBox
    class FIRESTORE firestore
    class FCACHE cacheBox
    class SQL,PRO_LOG,HAZ_CACHE sqliteBox
    classDef mapboxStore fill:#ffffff,stroke:#1976d2,stroke-width:1.5px,color:#000
    class MAP_CACHE mapboxStore
    class EXT_BASEMAP,EXT_TRACKDATA,EXT_DEM,EXT_HAZARD,EXT_LORA externalBox
    classDef hardwareBox fill:#ffffff,stroke:#555,stroke-width:1px,color:#000
    class HW_GNSS,HW_BLE,HW_WIFI hardwareBox
    classDef phase2Hardware fill:#fafafa,stroke:#9e9e9e,stroke-width:1px,stroke-dasharray:5 3,color:#616161
    class HW_SAT phase2Hardware
    class WEB webBox
    class BARRIER barrierWall

    style BACKEND_ROW fill:none,stroke:none,color:#fff
    style MOB_TOP fill:none,stroke:none,color:#fff
    style MOB_FEATURES fill:none,stroke:none,color:#fff
    style EXT fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#000
    style EXT_DATA fill:#fff8e7,stroke:#e65100,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style EXT_HW fill:#fff8e7,stroke:#e65100,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style CBE fill:#d1c4e9,stroke:#5e35b2,stroke-width:2px,color:#000
    style CBE_COMPUTE fill:#ede7f6,stroke:#5e35b2,stroke-width:1.5px,color:#000
    style CBE_DB fill:#ede7f6,stroke:#5e35b2,stroke-width:1.5px,color:#000
    style CBE_DISTRIBUTION fill:#ede7f6,stroke:#5e35b2,stroke-width:1.5px,color:#000
    style OCS fill:#b2dfdb,stroke:#00695c,stroke-width:2px,color:#000
    style OCS_USER fill:#e0f2f1,stroke:#00695c,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style OCS_CONTENT fill:#e0f2f1,stroke:#00695c,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style OCS_GRADE fill:#e0f2f1,stroke:#00695c,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style SYN fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#000
    style MOB fill:#bbdefb,stroke:#0277bd,stroke-width:2px,color:#000
    style MOB_APP fill:#e3f2fd,stroke:#1976d2,stroke-width:1.5px,color:#000
    style MOB_G2 fill:#e3f2fd,stroke:#1976d2,stroke-width:1px,stroke-dasharray:3 2,color:#000
    style MOB_CORE fill:#c8e6c9,stroke:#2e7d32,stroke-width:1.5px,color:#000
    style MOB_DATA fill:#f3e5f5,stroke:#6a1b9a,stroke-width:1.5px,color:#000
    style SQLITE_STORE fill:#f3eaf7,stroke:#6a1b9a,stroke-width:1.5px,stroke-dasharray:5 3,color:#000
    style MOB_HW fill:#f5f5f5,stroke:#757575,stroke-width:1.5px,stroke-dasharray:5 3,color:#000
    style CMS fill:#f5f5dc,stroke:#827717,stroke-width:2px,color:#000
```

---

## Where to drill down

| You want to understand… | Open this |
|---|---|
| Internals of TrackIQ pipeline (4 stages, schemas, governance flow) | `../2-subsystems/cbe-trackiq-pipeline.md` |
| Internals of Survival Core (NAV, BackTrack, SOS, Bundle Manager, etc.) | `../2-subsystems/mob-survival-core.md` |
| Internals of Application Layer (TrackMate, PCR, First Aid, Comms) | `../2-subsystems/mob-application-layer.md` |
| Internals of OCS (RBAC, approval workflow, audit) | `../2-subsystems/ocs-operations-console.md` |
| Firestore collections + sync semantics | `../2-subsystems/syn-firestore-sync.md` |
| Every PROHIBITED edge + rationale | `../4-cross-cutting/compliance-matrix.md` |
| All performance SLAs (≤2s render etc.) | `../4-cross-cutting/performance-targets.md` |
| Tile lifecycle Mapbox → CDN → Bundle → NAV | `../4-cross-cutting/tile-lifecycle.md` |
| How data moves at runtime in Survival Core | `../3-flows/data-flow/dfd-survival-core.md` |
| How data moves through TrackIQ pipeline | `../3-flows/data-flow/dfd-trackiq-pipeline.md` |
| State transitions across system | `../3-flows/state/state-trackaroo-transitions.md` |

---

## See also

- Draw.io twin (multi-page): `./trackaroo-phase1-architecture.drawio`
- Navigation map: `../README.md`
- Visual style guide: `../../CLAUDE.md`
- Tech stack inventory: `../../research/tech-stack-inventory.md`
- Mapbox SDK reference: `../../research/mapbox-sdk-overview.md`
