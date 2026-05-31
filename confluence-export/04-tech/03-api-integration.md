# API contract & integrations

> **Status:** Draft skeleton — to be filled.
> **Owner:** Engineering Lead
> **Last updated:** 2026-05-31

## Purpose
External integrations (Mapbox, Firebase, BOM hazard feeds, IAP) + internal API surface (CAL).

## Source artefact(s)
- `research/spec-docs/HFG-5026.md`
- `research/spec-docs/MAS-5126.md`
- `research/spec-docs/CDG-5126.md`

## Outline (to fill)

### External integrations
*[TODO: Mapbox SDK (offline tiles) · Firebase Auth + Firestore (sync only) · BOM hazard feeds (HFG) · Apple/Google IAP (subscription)]*

### Internal API — CAL
*[TODO: 4 state flags · contract surface · 1-way Experience → Core read-only]*

### Auth flow
*[TODO: Firebase Auth scoped to non-Core profile only · Core paths require no auth]*

### Offline contract
*[TODO: Every external integration MUST degrade gracefully to cached state · no auto-retry storms]*

---
*Draft created from project repo. Source of truth: see repo files above.*
