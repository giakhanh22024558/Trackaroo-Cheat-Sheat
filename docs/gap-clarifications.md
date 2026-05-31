# Gap & Clarification Register

> **Purpose:** Log of **spec ambiguities, gaps, and clarification questions** discovered while analysing the 19 spec docs / building the backlog. Each entry asks one specific question of the Project Director (or relevant authority) and records a working assumption so build work can continue.
>
> Format modelled on the MasterMind [`document/analysis`](../MasterMind/models/model_001/document/analysis/) pattern + the **Clarification Register** convention used in the Slitigenz proposal §11 (CLR-SLZ-NNN).

## Conventions

| Field | Notes |
|---|---|
| **ID** | `CLR-TRK-NNN` — Clarification · Trackaroo · sequential (distinct from Slitigenz's `CLR-SLZ-NNN`) |
| **Status** | `Open` (awaiting PD) · `Assumed` (working assumption applied, build proceeds) · `Resolved` (PD confirmed) · `Superseded` (replaced by another clarification or spec amendment) |
| **Impact** | What breaks / is at risk if the assumption is wrong |
| **Working assumption** | What the team builds against until clarified — never block; build-and-adjust per WFD-5126 `Build-against-assumptions` principle |
| **Source** | Spec doc + section the question arises from |
| **Logged / Resolved** | dates (YYYY-MM-DD) |
| **Topic** | Free-text label grouping related CLRs (e.g. *"Safe Anchor Point"*, *"SOS Flow"*, *"Data Persistence"*). Reuse existing labels when possible — keeps the register filterable/sortable |

> **Escalation rule:** every `Open` entry should have a logged date + an owner. Anything `Open > 2 weeks` and gating Sprint 0 deliverable → escalate to PD via the gate-evidence channel.

---

## Register

| ID | Topic | Source | Question | Working assumption | Impact | Status | Logged | Client answer | Resolved |
|---|---|---|---|---|---|---|---|---|---|
| **CLR-TRK-001** | Safe Anchor Point | TAA §8.1 / §8.2 · FSD §5.2.1 · TQP §5.5.2 | **Cap appropriateness — commercial vs survival** *(answer this first — gates downstream design)*. Does **Free = 3 anchors** truly satisfy TAA §8.2 *"genuinely survival-capable, not crippled preview"*? Tensions: (a) Anchor is local-only, no infra cost → cap is purely commercial design, not technical; (b) spec self-describes anchors as *"emergency rally points"* (safety-adjacent) → conflicts with §8.1 *"don't monetise survival"*; (c) survival-grade multi-day use (home + trailhead + parking + water + campsite + rally) easily exceeds 3 → *"crippled preview"* risk; (d) industry norm (Google Maps starred, Apple favorites, Gaia) = unlimited local markers. Should caps revise (e.g. Free=10 / Plus=50 / Pro=unlimited) OR Anchor reclassify to Survival Core (uncapped)? | Build to spec as-is (3/20/50) — proceed unchanged. Surface as UX/commercial risk to PD; do not unilaterally re-cap. | **Medium.** Unchanged: marketing risk (perceived crippled preview vs industry norm); safety-adjacent risk if Free user can't save adequate rally points. Revised: commercial revenue model may need re-tune. **Gates CLR-TRK-002:** if Anchor reclassifies to Survival Core (uncapped), the entire downgrade-handling question disappears. | **Open** | 2026-05-28 | *(awaiting PD)* | — |
| **CLR-TRK-002** | Safe Anchor Point | FSD §5.2.4 · OCS §6.6 + AOD §51 / PSB §21 / PRD §182 / UXS §75 / TAA §8.1 / TQP §5.5.2 | **Downgrade handling — detection & UX response** *(only relevant if CLR-TRK-001 confirms tier cap)*. §5.2.4 mandates the 8-step downgrade flow + wireframe but leaves two gaps: **(How) Detection** — what triggers the flow when downgrade source is IAP auto-expiry (Apple/Google not renewed → tier drops while anchors > new cap)? On app launch? Real-time? Other? **(What) Handling** — per 4 authority mandates (E&I Layer must NEVER block Survival Core), the selection screen cannot hard-block app use mid offline-nav, yet §5.2.4 implies a PERMANENT-delete modal. Forcing irreversible deletion under stress (anchor possibly being used as rally point) is dangerous. What is the required UX flow? | **(How) Detection:** App checks IAP state **on app launch** (online refresh if connected, else last-known cache). If tier↓ + count > new cap → enters flow. **(What) Handling:** Over-cap anchors enter **read-only mode** during active nav (visible & navigable, no new creation). Selection screen **deferred** to next safe transition (end of nav session OR app online in safe state). Survival Core never blocked. Anchors never silently deleted (per §5.2.1). Tier-cap = graceful degradation, not hard gate. | **HIGH (safety).** If detection ambiguous → silent anchor loss on offline expiry (violates §5.2.1 + UXS transparency). If handling blocks Survival Core mid-nav → violates 4 authority "never block" mandates + TAA §8.1 *"never monetise survival"* + endangers user under stress (forced permanent delete of rally points) + breaches UXS calm posture. | **Open** | 2026-05-28 | *(awaiting PD)* | — |

---

## How to use

- **Log a new question:** add a row with next `CLR-TRK-NNN`, fill all fields. Status starts `Open`.
- **Apply working assumption:** if the team must proceed before PD answer, document the assumption clearly so the impact of being wrong is known + recoverable. Per WFD-5126 build-against-assumptions: ship against the assumption; adjust on the next iteration when PD clarifies.
- **Record the answer:** when PD/client responds, paste the verbatim answer into **Client answer** (keep their wording — don't paraphrase). If the answer matches the working assumption: set Status `Resolved` + fill Resolved date. If it differs: update assumption to match the answer, set Status `Resolved`, log the implementation delta wherever the change applies. Keep the row either way (audit trail).
- **Link from planning:** if a clarification gates a Sprint 0 task or feature, reference its `CLR-TRK-NNN` in the relevant `docs/planning.md` row.

## Related registers (not duplicated here)

| Register | Where | What it covers |
|---|---|---|
| **Slitigenz vendor clarifications** (`CLR-SLZ-001 → 006`) | `research/spec-docs/Slitigenz-Proposal-RFT5026.md` §11 | Vendor's working assumptions submitted with proposal (Vietnam validation lab, device matrix, WCAG audit method, hazard-feed format, OCS Firebase project, SOS copy delivery format) |
| **Open mismatches (low-impact)** | `research/spec-docs/README.md` → "Open mismatches" | Documentary inconsistencies between spec docs (7-vs-8 tracks, VEG-5026 vs VGD-5126, FRM-5226 vs FRM-5126) — flagged for PD but not gating |
| **Change Requests (post-SRS)** | `docs/gap-analysis.md` | 17-col Gap + Impact analysis for client CRs once SRS exists |
