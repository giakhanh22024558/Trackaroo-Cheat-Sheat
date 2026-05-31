# Infrastructure & environments

> **Status:** Draft skeleton — to be filled.
> **Owner:** DevOps Lead
> **Last updated:** 2026-05-31

## Purpose
Dev / staging / prod environments. CI/CD pipeline. Deployment topology.

## Source artefact(s)
- `research/spec-docs/VGD-5126.md`
- `research/spec-docs/CDG-5126.md`
- `research/spec-docs/TQP-5026.md`

## Outline (to fill)

### Environment matrix
*[TODO: Dev (local emulator) · Staging (Firebase staging project) · Prod (Firebase prod project + AWS/GCP backend)]*

### CI/CD pipeline
*[TODO: GitHub Actions · iOS 15+ / Android 13+ build matrix · signed artefacts · prohibited-capability scan · static analysis]*

### Per-gate evidence bundle
*[TODO: Discovery / Alpha / Beta / GA — what evidence is collected automatically]*

### Mobile distribution
*[TODO: TestFlight (iOS) · Internal track (Android) for Alpha/Beta · App Store + Play for GA]*

### OCS deployment
*[TODO: Web app (React) · cloud-hosted (AWS/GCP) · internal-only access (no public DNS)]*

### Validation lab (Phase 1)
*[TODO: GPS-spoofing + Faraday simulating Australian envelope (per CLR-SLZ-001)]*

---
*Draft created from project repo. Source of truth: see repo files above.*
