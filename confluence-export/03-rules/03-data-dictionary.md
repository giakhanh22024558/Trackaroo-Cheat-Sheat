# Data Dictionary

> **Status:** Draft skeleton — to be filled.
> **Owner:** Engineering Lead + BA Lead
> **Last updated:** 2026-05-31

## Purpose
Entity × field × meaning. The contract between BA semantics and engineering schemas.

## Source artefact(s)
- `research/spec-docs/CDG-5126.md §5`
- `research/spec-docs/BTF-5126.md §5`
- `research/spec-docs/OSM-5026.md §10.5`

## Outline (to fill)

### Entity inventory
*[TODO: Anchor · Breadcrumb · PCR · POI · SOS Log · Hazard Feed · TrackIQ Score · TrackMate Session · User Account · Subscription]*

### Per-entity field tables
*[TODO: Field name · type · required · meaning · mutability · authority spec]*

### Data classification (CDG-5126)
*[TODO: Local-Only · Local-cached-syncable · Cloud-permitted]*

### Prohibited fields
*[TODO: satellite-related field names (PSB-5026) · `confirmation_count` (CDG §5.5) · telemetry-derived]*

### ID / UUID conventions
*[TODO: All safety records use UUID at creation · immutable post-write]*

### Schema change governance
*[TODO: Schema changes = CR + CAR-5026 record · never silent migration on production data]*

---
*Draft created from project repo. Source of truth: see repo files above.*
