# Security & authentication

> **Status:** Draft skeleton — to be filled.
> **Owner:** Security Lead
> **Last updated:** 2026-05-31

## Purpose
Encryption at rest / in transit, auth scoping, zero-outbound-from-Core posture, RBAC enforcement.

## Source artefact(s)
- `research/spec-docs/CDG-5126.md`
- `research/spec-docs/ESF-5026.md`
- `research/spec-docs/SFD-5026.md`
- `research/spec-docs/OCS-5026.md`

## Outline (to fill)

### Encryption
*[TODO: AES-256 at rest · TLS 1.3 in transit · key management policy]*

### Authentication
*[TODO: Firebase Auth (non-Core only) · OCS Firebase Auth + session mgmt]*

### Zero outbound from Core
*[TODO: Verified by airplane-mode packet capture (AC-C8-04) · non-dispatch posture]*

### RBAC server-side enforcement
*[TODO: OCS 3-role RBAC enforced server-side · audit log]*

### PII handling
*[TODO: PCR strictly anonymised (`reporter_archetype` only) · no PII in PCR data path]*

### Phase 2 security scaffolds (inert)
*[TODO: BackTrack Emergency Escrow schema (no transmission code)]*

### Compliance scope
*[TODO: Australia APPs · NZPA · GDPR / CCPA addressed via product design before respective release]*

---
*Draft created from project repo. Source of truth: see repo files above.*
