# Data Flow Diagram — TrackIQ™ Backend Pipeline (CBE-5000)

**Purpose:** Map data lifecycle for the TrackIQ™ Difficulty Scoring pipeline, from raw vendor ingestion through governance approval to MVT tile distribution.

**Scope:** The decoupled backend service `CBE-5000` (Pipes & Filters architecture), its PostgreSQL+PostGIS data stores (`CBE-6xxx`), the OCS-5026 governance gateway, and downstream Firestore sync + CDN distribution.

**Notation:**
- `([Entity])` = external entity (data provider, staff, downstream consumer)
- `((Process))` = pipeline stage / engine
- `[(data_store)]` = PostgreSQL table
- `-->` solid = control / verb-form action
- `-.->` dashed = data payload (noun label)
- Compliance constraint: deterministic · idempotent · no telemetry feedback · no ML inference

```mermaid
---
config:
  layout: elk
  theme: base
  themeVariables:
    fontFamily: Arial
    fontSize: 13px
---
graph TB

%% ============================================================
%% EXTERNAL ENTITIES (data providers, staff, downstream consumers)
%% ============================================================
subgraph EXT_ENTITIES["<b>External Entities</b>"]
    direction LR
    MAP_VENDORS(["<b>Map Data Providers</b><br/>Mapbox · OSM · GPX · Shapefile<br/><i>(Trackaroo-licensed)</i>"])
    DEM_VENDORS(["<b>DEM Providers</b><br/>AWS Terrain Tiles · SRTM<br/><i>(elevation source)</i>"])
    OCS_STAFF(["<b>OCS Staff</b><br/><i>Project Director / Authorized Contributor</i>"])
    CDN(["<b>Tile Server / CDN</b><br/><i>MVT distribution endpoint</i>"])
    MOBILE_APP(["<b>Mobile App</b><br/><i>(downstream consumer)</i>"])
end

%% ============================================================
%% BACKEND PIPELINE PROCESSES (numbered Yourdon-style)
%% ============================================================
subgraph PIPELINE["<b>TrackIQ™ Backend Pipeline</b> · <i>Decoupled · Pipes &amp; Filters · server-side</i>"]
    direction LR

    INGEST(("<b>1.0</b><br/>Ingestion<br/>Adapter"))
    DEM_ENG(("<b>2.0</b><br/>DEM<br/>Enrichment"))
    SCORE(("<b>3.0</b><br/>Scoring<br/>Engine"))
    TILE_GEN(("<b>4.0</b><br/>Tile<br/>Generator"))
end

%% ============================================================
%% GOVERNANCE PROCESS (OCS-5026)
%% ============================================================
subgraph GOVERNANCE["<b>Governance Gateway</b> · <i>OCS-5026 web app · manual approval queue</i>"]
    direction LR
    APPROVER(("<b>5.0</b><br/>Track Data &amp;<br/>Grade Admin"))
    AUDITOR(("<b>6.0</b><br/>Audit Log<br/>Viewer<br/><i>(read-only)</i>"))
    SCORING_OPS(("<b>7.0</b><br/>TrackIQ™<br/>Scoring Ops<br/><i>(visibility / break-glass)</i>"))
end

%% ============================================================
%% DATA STORES (PostgreSQL + PostGIS · server-side)
%% ============================================================
subgraph STORES["<b>Backend Database</b> · <i>PostgreSQL + PostGIS</i>"]
    direction LR
    D1[("<b>D1</b><br/>raw_ingested_tracks<br/><i>Source lineage · raw geometry</i>")]
    D2[("<b>D2</b><br/>track_review_queue<br/><i>Pending / Approved / Rejected<br/>reviewed_by audit trail</i>")]
    D3[("<b>D3</b><br/>production_tracks<br/><i>Human-approved definitive tracks</i>")]
end

%% ============================================================
%% SYNC + DISTRIBUTION (Firestore + CDN)
%% ============================================================
subgraph DISTRIBUTION["<b>Distribution Layer</b>"]
    direction LR
    FIRESTORE[("<b>Firestore</b><br/><i>collection: trackiq_scores</i><br/><i>(syncs baked scores to mobile)</i>")]
    TILE_BUCKET[("<b>MVT Tile Bucket</b><br/><i>(staging before CDN publish)</i>")]
end

%% ============================================================
%% INPUT DATA FLOWS (purple dotted = data payload)
%% ============================================================
    MAP_VENDORS -.->|"<b>vendor_track_data</b><br/><i>(GPX · Shapefile · OSM · Mapbox)</i>"| INGEST
    DEM_VENDORS -.->|"<b>elevation_tiles</b><br/><i>(raster · per bbox)</i>"| DEM_ENG

%% ============================================================
%% INGESTION → RAW STORAGE + DOWNSTREAM
%% ============================================================
    INGEST -->|"writes raw lineage record"| D1
    INGEST -.->|"<b>TrackSegmentGroup</b><br/><i>(normalised coords + metadata)</i>"| DEM_ENG

%% ============================================================
%% DEM ENRICHMENT
%% ============================================================
    DEM_ENG -.->|"<b>enriched_segments</b><br/><i>(slope = Δelev/Δdist appended)</i>"| SCORE

%% ============================================================
%% SCORING (deterministic, idempotent)
%% ============================================================
    SCORE -.->|"<b>Proposed Grade Event</b><br/><i>(track_id, calc_grade, reason, ts)</i>"| D2

%% ============================================================
%% GOVERNANCE — MANUAL APPROVAL
%% ============================================================
    APPROVER <-->|"reads pending items<br/>writes verdict (approved/rejected)<br/>logs reviewed_by"| D2
    APPROVER -.->|"<b>approval_verdict</b>"| OCS_STAFF
    OCS_STAFF -->|"opens review queue<br/>clicks Approve / Reject"| APPROVER

    SCORING_OPS -.->|"<b>pipeline_status · run_history</b><br/><i>(visibility)</i>"| OCS_STAFF
    OCS_STAFF -->|"manual re-run<br/>(break-glass intervention)"| SCORING_OPS
    SCORING_OPS -->|"triggers stage re-run"| INGEST
    SCORING_OPS -->|"triggers stage re-run"| DEM_ENG
    SCORING_OPS -->|"triggers stage re-run"| SCORE

    AUDITOR -.->|"<b>approval_history</b><br/><i>(read-only · reviewer · ts · reason)</i>"| OCS_STAFF
    AUDITOR -->|"reads approval log (read-only)"| D2

%% ============================================================
%% PROMOTION & TILE BAKING
%% ============================================================
    D2 -.->|"<b>approved rows</b><br/><i>(filtered by status=APPROVED)</i>"| D3
    D3 -.->|"<b>production_track_records</b><br/><i>(definitive, baked)</i>"| TILE_GEN

%% ============================================================
%% DISTRIBUTION OUTPUTS
%% ============================================================
    TILE_GEN -.->|"<b>MVT vector tiles</b><br/><i>(z/x/y indexed)</i>"| TILE_BUCKET
    TILE_BUCKET -.->|"<b>baked tiles + manifest</b>"| CDN
    CDN -.->|"<b>tile_manifest</b><br/><i>(pre-journey download only)</i>"| MOBILE_APP

    SCORE -->|"publishes baked scores"| FIRESTORE
    FIRESTORE -.->|"<b>trackiq_scores</b><br/><i>(synced via Firestore Local Cache)</i>"| MOBILE_APP

%% ============================================================
%% COMPLIANCE / PROHIBITED PATHS (red dashed)
%% ============================================================
    MOBILE_APP -.->|"<b>[X] PROHIBITED</b><br/>No telemetry feedback to scoring engine<br/>(usage data cannot lower difficulty grade)"| SCORE

%% ============================================================
%% STYLES
%% ============================================================
    classDef entity fill:#fff3e0,stroke:#e65100,stroke-width:1.5px,color:#000
    classDef process fill:#ede7f6,stroke:#5e35b2,stroke-width:1.5px,color:#000
    classDef govProcess fill:#e0f2f1,stroke:#00695c,stroke-width:1.5px,color:#000
    classDef store fill:#e1f5ff,stroke:#0277bd,stroke-width:1.5px,color:#000
    classDef firestoreStore fill:#fff9c4,stroke:#f9a825,stroke-width:1.5px,color:#000

    class MAP_VENDORS,DEM_VENDORS,OCS_STAFF,CDN,MOBILE_APP entity
    class INGEST,DEM_ENG,SCORE,TILE_GEN process
    class APPROVER,AUDITOR,SCORING_OPS govProcess
    class D1,D2,D3,TILE_BUCKET store
    class FIRESTORE firestoreStore

    style EXT_ENTITIES fill:#fff8e7,stroke:#e65100,stroke-width:1.5px,color:#000
    style PIPELINE fill:#d1c4e9,stroke:#5e35b2,stroke-width:2px,color:#000
    style GOVERNANCE fill:#b2dfdb,stroke:#00695c,stroke-width:2px,color:#000
    style STORES fill:#ede7f6,stroke:#5e35b2,stroke-width:1.5px,color:#000
    style DISTRIBUTION fill:#fff9c4,stroke:#f9a825,stroke-width:1.5px,color:#000

%% Red prohibited edge — adjust index if more edges added
    linkStyle 19 stroke:#c62828,stroke-width:2px,stroke-dasharray:5 5
```

## Process descriptions

| # | Process | Inputs | Outputs | Stores accessed |
|---|---|---|---|---|
| **1.0** | Ingestion Adapter | `vendor_track_data` (Adapter Pattern via `ITrackIngestAdapter`) | `TrackSegmentGroup` (normalised) | W `D1` (raw_ingested_tracks — source lineage) |
| **2.0** | DEM Enrichment Engine | `TrackSegmentGroup`, `elevation_tiles` | `enriched_segments` (with slope) | (none — pure compute) |
| **3.0** | Scoring Engine | `enriched_segments` | `Proposed Grade Event` | W `D2` (track_review_queue, status=PENDING) |
| **4.0** | Tile Generator | `production_track_records` | `MVT vector tiles` | R `D3` (production_tracks) → W `TILE_BUCKET` |
| **5.0** | Track Data & Grade Admin (OCS-4301) | OCS_STAFF clicks Approve/Reject | `approval_verdict` | R/W `D2` (writes status + reviewed_by) |
| **6.0** | Audit Log Viewer (OCS-4303) | (none — read-only) | `approval_history` to OCS_STAFF | R `D2` (read-only) |
| **7.0** | TrackIQ Scoring Ops (OCS-4202) | OCS_STAFF triggers re-run | `pipeline_status`, stage re-run signals | (none — orchestrator) |

## Data store schema sketch

| Store | Key fields | Write source | Mutation rules |
|---|---|---|---|
| `D1 raw_ingested_tracks` | `track_id (UUID)`, `source_vendor`, `raw_geometry`, `ingested_at` | Process 1.0 (INGEST) | **Append-only** — source lineage preserved |
| `D2 track_review_queue` | `track_id`, `calculated_grade`, `calculated_reason`, `status (Pending/Approved/Rejected)`, `reviewed_by (FK)`, `reviewed_at` | 3.0 (writes PENDING), 5.0 (updates verdict) | Status mutates · `reviewed_by` immutable audit trail |
| `D3 production_tracks` | `track_id`, `definitive_grade`, `approved_by`, `tile_ready_at` | Promoted from `D2` on approval | **Append-only** — replaced via new track_id on regrade |
| `TILE_BUCKET` | `bbox`, `z`, `x`, `y`, `tile_data`, `version` | Process 4.0 (TILE) | Overwritten per tile on re-bake |
| `FIRESTORE / trackiq_scores` | `track_id`, `grade`, `bbox`, `published_at` | Publish job from D3 / SCORE | Read-only from mobile (mobile cannot write back) |

## Pipeline state machine

```text
[raw vendor data]
       │
       ▼
[1.0 INGEST] ──→ writes D1 (lineage) ──→ emits TrackSegmentGroup
       │
       ▼
[2.0 DEM ENRICH] ──→ pure compute (slope) ──→ emits enriched segments
       │
       ▼
[3.0 SCORE] ──→ writes D2 (status=PENDING)
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │  GOVERNANCE GATEWAY  │
                       │  Project Director    │
                       │  reviews & decides   │
                       └──────────┬───────────┘
                                  │
                  ┌───────────────┼───────────────┐
                  ▼               ▼               ▼
              REJECTED        APPROVED        deferred
                  │               │               │
                  ▼               ▼               ▼
            (terminal)    promote → D3       (stays PENDING)
                                  │
                                  ▼
                          [4.0 TILE GEN] ──→ MVT tiles ──→ CDN ──→ mobile pre-download
                                  │
                                  ▼
                          publish baked scores ──→ Firestore ──→ mobile sync
```

## Architectural constraints visualised

- ❌ **No automated approval** — every grade change requires manual OCS-5026 sign-off
- ❌ **No telemetry feedback loop** — Mobile app's usage data cannot mutate scoring (red prohibited edge from MOBILE_APP → SCORE)
- ❌ **No ML inference** — Scoring Engine is pure-function Rule Matrix (Hardest-Criterion-Wins)
- ✅ **Idempotent** — Re-running pipeline on same input → same output (RT-09)
- ✅ **Source lineage preserved** — `D1 raw_ingested_tracks` retains pre-processing snapshot
- ✅ **Audit trail mandatory** — Every approval writes `reviewed_by` (FK to user table)
- ✅ **Break-glass intervention** — OCS staff can manually re-trigger any stage via Process 7.0
- ✅ **Two consumption paths** — heavy tile data via CDN (pre-journey download), lightweight scores via Firestore real-time sync

## See also

- Master architecture: `../../1-overview/trackaroo-phase1-architecture.md`
- TrackIQ pipeline subsystem deep-dive: `../../2-subsystems/cbe-trackiq-pipeline.md`
- Survival Core DFD: `./dfd-survival-core.md`
- Compliance matrix: `../../4-cross-cutting/compliance-matrix.md`
- Navigation map: `../../README.md`
