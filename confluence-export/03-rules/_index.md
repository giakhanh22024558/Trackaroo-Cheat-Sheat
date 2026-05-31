# 📕 3. RULES — Business rules & cross-cutting conventions

> **Rules and constraints that apply across the product.** Each Story/Feature references these by ID. If a rule applies to only one feature, it belongs in that feature's page (PRODUCT), not here.

## Pages in this section

| Page | What's in it |
|---|---|
| [Business Rules](./01-business-rules.md) | Catalog of BR-XXXX with rationale + spec authority |
| [Permission Matrix (RBAC)](./02-permission-matrix.md) | 6 user archetypes × app capability · 3 console roles × OCS module |
| [Data Dictionary](./03-data-dictionary.md) | Entity × field × meaning · per CDG-5126 + BTF-5126 |
| [UX Guidelines](./04-ux-guidelines.md) | Date format · error states · validation · 5-Question Hierarchy · accessibility |

## Why these rules exist (top 5)

1. **Non-adaptive · non-inferential** — Survival Core must NEVER use AI/ML/inference. *(UXS-5726, OSM-5026)*
2. **Offline-first · zero-network for Core** — every Survival Core path works in airplane mode. *(FSD-5126, BPS-5126)*
3. **Immutable safety records** — breadcrumbs, SOS logs, anchors cannot be edited/silently overwritten. *(BTF-5126 §5.2, ESF-5026)*
4. **Layer independence** — no overlay system may mutate another (LIR-01..06). *(OSM-5026)*
5. **Phase 1 prohibitions** — no satellite transmission, no AI scoring, no telemetry weighting. *(PSB-5026)*

## Source authority hierarchy

Conflicts resolve upward:

```
UXS-5726 (Highest — behavioural / cognitive authority)
   ↑
PRD-5126 (Acceptance criteria)
   ↑
FSD-5126 (Functional execution)
   ↑
TQP-5026 (Validation)
   ↑
WFD-5126 (UI states · wireframe gate)
   ↑
Specialist docs (OSM · OCS · HFG · BTF · CDG · POI · MAS · ESF · SFD · BPS · TAA · FQH · AOD · PSB · FRM · VGD · CRG · CRQ)
```
