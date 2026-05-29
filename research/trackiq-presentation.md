# TrackIQ™ Cloud Backend Pipeline — Presentation Script
## Diagram walkthrough · ~5 minutes

**Topic:** TrackIQ Backend Pipeline Worker — explaining the pipeline + governance-flow diagrams
**Diagram referenced:** `diagrams/2-subsystems/cbe-trackiq-pipeline.md` (4-stage pipeline + segment-lifecycle state machine)
**Language:** English
**Target length:** ~5:00 (≈ 760 words)

---

## SPOKEN SCRIPT

**[0:00 – 0:35 · Opening]** *— point to the diagram.*

"This diagram describes **TrackIQ** — the cloud system that turns raw track data into a difficulty grade. It has two halves. On one side, a **four-stage pipeline** that processes the data. On the other, a **governance lifecycle** — the states a single track passes through before its grade is ever published. Let me walk both."

---

**[0:35 – 2:35 · The four-stage pipeline]** *— move stage to stage.*

"First, the pipeline. It is built as **pipes and filters** — four independent stages, each one consuming data, transforming it, and passing it on. The stages never call each other directly; they are connected only through data stores. That isolation is deliberate — it means any single stage can be re-run on its own.

**Stage one — Ingest.** Raw track data arrives in many formats: Mapbox tiles, OpenStreetMap, GPX recordings, authority shapefiles. An adapter for each format converts them all into one common internal shape. Supporting a new format later means adding one adapter — nothing downstream changes.

**Stage two — DEM Enrichment.** Here we attach *real terrain*. Every segment is matched against authoritative elevation data, and we calculate the actual slope — rise over distance. Crucially, this stage only *appends* terrain facts; it never alters the original track geometry.

**Stage three — Scoring.** This is the deterministic core. Each enriched segment is run against a fixed rulebook — a rule matrix — and assigned a difficulty grade. It is a **pure function**: the same segment always produces the same grade. And the thresholds in that rulebook are not hardcoded — they live in configuration that only an authorised operator can change.

**Stage four — Tile Publish.** Approved grades are baked into compressed map tiles and published to the distribution network, ready for the app to download offline."

---

**[2:35 – 4:15 · The governance lifecycle]** *— trace the state machine.*

"Now the other half — the governance lifecycle. This is the state machine that a single track segment travels through, and the important thing is that **a human sits in the middle of it**.

A segment is **Ingested**, then **Enriched**, then it is scored — which produces a **Pending** grade. Pending does not mean published. It means the grade is sitting in a review queue. A qualified reviewer — an Authorised Contributor, or the Project Director — opens it, and the state becomes **Reviewed**. From there, two paths. The reviewer **Approves** it — which writes their identity and a timestamp, and moves it into production. Or they **Reject** it, with a mandatory reason, and it stays in the queue.

Only an Approved grade continues — it is **Baked** into a tile, then **Published**. And here is the key property of the diagram: once a grade is **Approved, it is immutable**. There is no arrow leading out of that state. Changing an approved grade is not an edit — it requires a deliberate, logged 're-run' by the Project Director, and that creates an entirely new record. Nothing is ever silently overwritten."

---

**[4:15 – 4:45 · The compliance invariants]**

"Three rules are built into this whole diagram. There is **no artificial intelligence** anywhere in scoring — it is a fixed rulebook, not a model. There is **no telemetry feedback** — a grade is never influenced by how fast, or how often, people drive a track. And when one segment qualifies for several difficulty levels at once, the **hardest one wins** — the grade is never averaged, never softened. It always errs toward caution."

---

**[4:45 – 5:05 · Closing]**

"So — a four-stage deterministic pipeline, a governance lifecycle with a human approval gate, and an immutable, fully audited result. That is how TrackIQ produces a difficulty grade you can actually trust. Thank you."

---

## DELIVERY NOTES

| Aspect | Guidance |
|---|---|
| **Length** | ~760 words ≈ 4:55–5:10. If overrunning, trim the format list in Stage 1. |
| **Diagram sync** | Pipeline half: di chuyển tay theo 4 stage trái→phải. Governance half: trace từng state Ingested→…→Published, dừng lâu ở **Approved** (self-loop = immutable). |
| **Emphasis beats** | *pipes and filters* · *pure function* · *a human sits in the middle* · *Approved, it is immutable* · *hardest one wins* · *errs toward caution*. |
| **Pause points** | Trước mỗi "Stage one/two/three/four" · trước "once a grade is Approved" · trước "Thank you". |
| **If asked deeper** | "No AI / no telemetry" = rejection trigger RT-09. Schemas (Phase 1): Vehicle · Trail · Foot · Snow (stub). Approval gateway = OCS-4301. Audit retention ≥ 90 days. Full detail: `cbe-trackiq-pipeline.md`. |

---

## Document status

| Field | Value |
|---|---|
| Purpose | ~5-minute diagram-walkthrough script — TrackIQ 4-stage pipeline + segment-lifecycle governance state machine |
| Source | `diagrams/2-subsystems/cbe-trackiq-pipeline.md` |
| Companion | `research/cal-presentation.md` · `research/delivery-plan-presentation.md` |
