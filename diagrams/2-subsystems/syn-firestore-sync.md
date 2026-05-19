# SYN-7000 · Firebase Firestore Cloud Sync Engine — Subsystem Deep-Dive

**Status:** 🚧 Stub — scope declared, content TBD
**Tier:** 2 (Subsystem / C4 Component level)
**Zone in master:** `SYN` (Firestore · yellow)

## Scope

The bidirectional bridge between Cloud Backend ⇄ Mobile App. Firestore real-time DB with auto offline persistence on the device side.

## What this diagram will show (TODO)

- [ ] **All Firestore collections** with schema sketches:
  - [ ] `user_profiles` — read/write by Mobile + OCS
  - [ ] `trackmate_history` — TrackMate session metadata
  - [ ] `trackiq_scores` — published TrackIQ grades (read-only from Mobile perspective)
  - [ ] `haztrack_cache` — authority hazard cache (read-only from Mobile)
  - [ ] `pcr_queue` — append-only · write-once PCRs
- [ ] **Per-collection security rules** — who can read/write under what conditions (RBAC + write-once semantics)
- [ ] **Offline persistence behavior** on device — Firestore SDK auto-cache · queue-and-forward model
- [ ] **Silent-failure when offline** model (V-13)
- [ ] **Sync thread isolation** from Survival Core (V-12)
- [ ] **Prohibited paths**:
  - [ ] `MOB_CORE` → `Firestore Local Cache` (Core data never syncs)
  - [ ] `SQLite + WAL` → `Firestore` (no SQLite-to-cloud path)
  - [ ] `Firestore` → `MOB_CORE` (Zero Reconciliation — cloud can't mutate Core)
- [ ] **Write-Once Security** model for PCR collection
- [ ] **TLS 1.3** in transit

## Diagram type

**Mermaid `graph LR`** with cloud Firestore on left, mobile Local Cache on right, OCS + CBE on top. Collections rendered as cylinders. Plus a markdown table for security rules per collection.

## Cross-references

- Master: `../1-overview/trackaroo-phase1-architecture.md` — see SYN zone
- OCS (consumer): `./ocs-operations-console.md`
- Application Layer (consumer): `./mob-application-layer.md`
- Survival Core (explicitly NOT consumer): `./mob-survival-core.md` — see compliance barrier
- Compliance: `../4-cross-cutting/compliance-matrix.md` — V-12 · V-13 · Write-Once
- Navigation: `../README.md`
