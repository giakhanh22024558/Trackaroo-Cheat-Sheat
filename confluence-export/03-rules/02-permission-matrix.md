# Permission Matrix (RBAC)

> **Status:** Draft skeleton — to be filled.
> **Owner:** BA Lead
> **Last updated:** 2026-05-31

## Purpose
Who can do what. Two matrices: end-user archetypes × app capability, and console roles × OCS module.

## Source artefact(s)
- `research/spec-docs/TAA-5126.md`
- `research/spec-docs/OCS-5026.md §5.2`
- `research/spec-docs/POI-5026.md §6.3.2`

## Outline (to fill)

### End-user archetype × capability matrix
*[TODO: 6 archetypes × {Nav, SOS, BackTrack, HazTrack, PCR, TrackMate, POI groups}]*

### POI group defaults by archetype
*[TODO: 10 groups × 6 archetypes — pull from POI-5026 §6.3.2]*

### Subscription tier matrix
*[TODO: Free / Plus / Pro × {anchors cap, history depth, advanced features}]*

### OCS console roles × module matrix
*[TODO: PD / Operations / Authorised Contributor × {PCR · Grade Admin · TrackIQ · Feed · User Admin · First Aid Content · Audit Log}]*

### Server-side enforcement
*[TODO: All RBAC enforced server-side · OCS UI hides but does not gate]*

### Audit log scope
*[TODO: Every console action logged · PD = all actions · others = own actions only]*

---
*Draft created from project repo. Source of truth: see repo files above.*
