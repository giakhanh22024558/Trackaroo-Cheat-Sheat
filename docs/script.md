# Kickoff Meeting — Presentation Script

> **Audience:** Project Director Ian Moore + Trackaroo team
> **Speaker:** Slitigenz PM (Luong Gia Khanh) — Tech Lead present for technical Q&A
> **Duration target:** ~6–8 min for the 2 slides
> **Language:** English

---

## Slide 1 — Discovery Deliverables Overview

Since this is a brief kickoff and not a status meeting, I won't dive too deep into progress detail — otherwise this turns into a weekly report. But to give you an overview of the plan and where we're heading, I'll walk you through these sections briefly.

### 9 Architectural Artefacts

Most of these already had a structured first version in our **Vendor Demonstration Program (VDP) / PoC** submitted with the original proposal — that's the foundation we've been refining since day one of execution. So what we're handing over is essentially the **finalized, gate-ready** form of work whose architectural intent was already locked in at proposal stage.

Items in **Finalizing** status today — 5 of 9:

- High-Level Architecture Diagram
- Deterministic State Transition Matrix
- Module Isolation Mapping
- Breadcrumb Classification Confirmation
- CAL Architecture Documentation

These are essentially complete — we're doing the last pass of internal review against your authority stack before submission.

Items still **In Progress** — 4 of 9:

- Offline-First Execution Explanation
- PCR Architecture Documentation
- SDK Audit Declaration
- OSS Licence Audit

We mapped these out from day one. They're tracking on plan, no surprises, no blockers. Clear ownership across the Squad.

### TrackMate™ Transport & Comms

Three items on the build path before comms development begins:

- **Transport Proposal** — *Finalizing.* Technical proposal for BLE Mesh, Wi-Fi Direct, and LoRa transport. Must be approved before any comms code is written.
- **Proposal-Stage Concessions — Battery validation methodology + architecture** — *In Progress.* Deferred empirical-proof methodology for battery performance validation against BPS-5126 thresholds.
- **Proposal-Stage Concessions — Transport validation methodology** — *In Progress.* Range, fallback behaviour, and hardware auto-detection methodology.

### Operational & Administrative Readiness — all In Progress

Five items covering the project's operational baseline:

- **Companion Website Staging + Live anchor statement** — staging environment, CMS configuration, information architecture accepted. Site live with the verbatim product anchor statement.
- **System Access** — continuous, unrestricted Client admin access to all repositories, build environments, and credentials (per DCA §8.1).
- **AI-Tool Register** — disclosure of all AI coding tools and human-review processes (per DCA §10.6).
- **Continuity Plan** — identifies backup personnel, knowledge-transfer steps, repository continuity, and escalation if any Key Personnel is unavailable for more than 5 consecutive business days (per DCA §14.1 — **strict precedent**).
- **Initial Security & Privacy Evidence** — documentation of data-isolation architecture and security baselines (encryption at rest, TLS 1.3 in transit, Survival Core network-zero proof).

We mapped these out from day one. They're tracking on plan, no surprises, no blockers. We have clear ownership across the Squad and the work is already underway.

**Net message:** We're on track across all three categories. The Discovery package is on a path to being submitted in the required window, and the items in Finalizing are not last-minute scrambling — they're work that's been maturing since proposal stage.

---

## Slide 2 — UI/UX · 10 Design Intent Mockups

On the design intent side, I want to show you something concrete.

We've already produced **4 of the 10 high-fidelity mockups** ahead of schedule:

- **Archetype Selection** — light mode and dark mode
- **SOS Confirmation** — light mode and dark mode

These are working artefacts — happy to walk you through visual decisions whenever you have time.

Which brings me to a request.

Ian — I know you're extremely busy, **but** given the Discovery Gate is on **15 June** and the formal Design Intent submission is due **10 June**, we'd like to propose a **preview review session earlier than the formal submission date** — ideally so we have time to incorporate any direction you'd like to give before we lock the artefacts.

What we're proposing is a single block we'd split into three focused parts:

- **30 minutes** — Design Intent walkthrough (mockups + design direction statement)
- **40 minutes** — Technical artefact preview (architecture diagrams + TrackMate proposal)
- **15 minutes** — Companion Website preview (staging environment + CMS + information architecture)

Total ~85 minutes.

Our preferred date is **Monday, 8 June** — which happens to coincide with our standing Weekly Status Call.

Two options for your consideration:

- **Option A** — Extend the 8 June weekly call into a combined session. You don't add a meeting; we just restructure that slot to cover the preview.
- **Option B** — Keep the weekly call as-is and book a separate preview session on a different day that suits you better.

Either works for us. **Let us know your preference and we'll structure the agenda + materials accordingly.**

If Option A — we'll have the materials ready and circulated 24 hours in advance per the CMP protocol.
