# OCS-5026 · Operations Console — Subsystem Deep-Dive

**Status:** 🚧 Stub — scope declared, content TBD
**Tier:** 2 (Subsystem / C4 Component level)
**Zone in master:** `OCS` (Operations Console · teal)

## Scope

Internal staff web app (React) for human-in-the-loop governance over the platform. RBAC-gated.

## What this diagram will show (TODO)

- [ ] **All OCS modules** with their internal structure across 3 sub-zones:
  - [ ] `OCS_USER` General & Settings — `OCS-4101` User & Account Admin · `OCS-4102` Beta & Alpha Tester Mgmt
  - [ ] `OCS_CONTENT` Metrics Monitoring — `OCS-4201` HazTrack Feed Mgmt · `OCS-4202` TrackIQ Scoring Operations · `OCS-4203` PCR Management
  - [ ] `OCS_GRADE` Verification — `OCS-4301` Track Data & Grade Admin · `OCS-4302` First Aid Content Admin · `OCS-4303` Audit Log Viewer
- [ ] **RBAC matrix** — role × module × action (who can do what)
  - Roles: Project Director · Authorised Contributor · Reviewer (read-only) · Beta/Alpha Tester (no OCS access)
- [ ] **Approval workflow** — Grade Review Queue lifecycle through TDGA (`Pending → Reviewed → Approved/Rejected → Immutable production_tracks row`)
- [ ] **Break-glass intervention** — Project Director can re-trigger TrackIQ pipeline stages (auditable)
- [ ] **Audit log model** — 90-day retention · read-only · reviewer + timestamp + payload
- [ ] **Configurable thresholds** — TIQADMIN → SCORE config plumbing
- [ ] **Authentication** — Firebase Auth integration · session management
- [ ] **Cross-zone reads/writes** — OCS ↔ CBE Postgres · OCS ↔ Firestore · OCS reads from EXT_HAZARD feeds

## Per-module audit findings

### `OCS-4201` HazTrack Feed Management — audited (spec landed)

- [ ] Inputs (metadata only · NO raw hazard data): integrated feed status (BOM/AFAC/SES) · perf metrics (cadence + latency alerts) · TTL compliance per OSM-5026 §8 · Five-Pillar Inclusion Filter results (Authority Origin · Jurisdiction · Format · Compatibility · Stability) · schema validation alerts
- [ ] Outputs: Feed Status Dashboard · Feed Eligibility Register (visual UI) · audit log writes to Firestore (append-only · 7yr retention)
- [ ] Capability: **read-only + break-glass intervention** (manual cache refresh) — **prohibited from making feed configuration changes** (requires formal delivery amendment)
- [ ] RBAC visibility: Project Director · Operations roles only
- [ ] **Survival Core Isolation** (CDG-5126) — strictly prohibited from accessing/searching/visibility of any Survival Core data (breadcrumbs · SOS logs)
- [ ] **Architecture status** — generic touchpoints covered at group-level; Gap #1 fixed (edge `OCS_CONTENT → SYN` label now mentions audit log writes); Gap #2 deferred — blocked by design-decision **S1** (System Audit Log backend: Postgres CBE-6004 vs Firestore vs S3) — current architecture shows PostgreSQL CBE-6004 cylinder but OCS-4201 spec mandates Firestore collection. Resolution required before architecture commits to one model. Gap #3 (explicit `OCS → MOB_CORE [X] PROHIBITED` edge) skipped — keep negative-space (no edge = no path = sufficient)

### `OCS-4202` TrackIQ Scoring Operations — audited (spec landed)

- [ ] Inputs (metadata only · NO raw track data): real-time pipeline status per stage (Ingest · DEM Enrichment · Scoring · Tile Publish · status running/idle/error + last run duration) · pipeline run history (run IDs · timestamps · stage outcomes) · error details · governance metadata (scoring algorithm version · last change date · vendor attestations confirming NO AI inference or adaptive logic)
- [ ] Outputs: monitoring dashboards · alerts · audit log writes to Firestore (append-only · 7yr) · pipeline run history (≥90-day retention)
- [ ] Capability: monitoring + **break-glass intervention** (manual re-run trigger) — implicitly read-only on scoring configuration (no spec mention of config changes)
- [ ] RBAC visibility: Project Director · Operations roles
- [ ] **Survival Core Isolation** (CDG-5126) — same as OCS-4201, strictly prohibited from accessing Core data (breadcrumbs · SOS · event logs)
- [ ] **Compliance reinforcements**: spec confirms `RT-09 No ML inference in TrackIQ pipeline` + `§4 Deterministic execution` mandates via "vendor attestations no AI/adaptive logic" requirement
- [ ] **Architecture status** — no new edges needed (audit log generic edge covers · same negative-space Core isolation as OCS-4201). **NEW STRUCTURAL ADDITION:** Preemptive provisional cylinder **`CBE-6005 pipeline_run_history`** added to `CBE_DB` container to address spec mandate "≥90-day pipeline run history storage" which was not previously visible. Cell visually marked PROVISIONAL (amber dashed border + warning badge) pending design-decision **S2** (Pipeline run history backend) resolution. Same Firestore-vs-PostgreSQL question as S1 — both should resolve together. Gap #3 skipped (negative-space sufficient for Core isolation, same as OCS-4201)

### `OCS-4203` PCR Management — audited (spec landed)

- [ ] Inputs: active PCR submissions (`pcr_id` · category · ts · WGS84 coords · optional text · resolution state) · anonymised archetype tokens **(NO PII exposure)** · 90-day age alerts (unconfirmed-age queue) · PCR history per coord (chronological query) · operator governance inputs (4 reason codes: Duplicate · Incorrect Location · Condition Resolved · Data Quality + suppression flags)
- [ ] Outputs: **superseding PCR records** (new immutable · original archived not deleted · linked) · **suppression state** (flag removes from public map view · data preserved) · audit log writes (every view/supersede/suppress action)
- [ ] Storage: Community PCR data → Firestore · audit log → Firestore isolated collection (write-once · ≥7yr) — both subject to S1 blocker
- [ ] Capability: governance interface — supersede + suppress actions write to community data layer; **Project Directors** can apply suppression flag (RBAC-gated)
- [ ] **Survival Core Isolation** (CDG-5126) — strictly prohibited from accessing Core data (breadcrumbs · SOS · event logs). Same negative-space pattern as OCS-4201/4202
- [ ] **PII prohibition** — console receives only anonymised archetype tokens · architecturally prohibited from exposing personally identifiable information
- [ ] **Architecture status** — **NEW EDGE APPLIED:** `OCS_CONTENT → SYN` converted to **bidirectional `OCS_CONTENT <--> SYN`** (R/W Firestore data) — Gap #1 fix from OCS-4203 audit. Previously edge was write-only; OCS-4203 explicitly reads PCRs for governance (review/supersede surface) which prompted formalising the read path. Same edge now covers ALL OCS modules' reads (PCR review · hazard metadata · audit log queries · etc.). Audit log writes still subject to **S1** blocker (Firestore vs PostgreSQL destination). Gap #2 N/A (no separate PCR cache cylinder needed — uses Firestore directly · M0l mobile-side question only). Gap #3 skipped (negative-space sufficient for Core isolation)
- [ ] **Compliance reinforcements** confirmed by spec: `compliance §3 Write-Once Security` (Firestore append-only) · `F3` (PCR write semantics) · `§7` (APP 3 / PII handling patterns)

## Diagram type

**Mermaid `graph TB`** with OCS modules in 3 columns, plus an RBAC matrix in markdown table form.

## Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md` — see OCS zone
- TrackIQ pipeline (governance target): `./cbe-trackiq-pipeline.md`
- Sync engine: `./syn-firestore-sync.md`
- Compliance: `../4-cross-cutting/compliance-matrix.md` — manual-only approval mandate
- Performance: `../4-cross-cutting/performance-targets.md` — 90-day audit retention
- Navigation: `../README.md`
