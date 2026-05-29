# CAL State Machine — Presentation Script
## Diagram walkthrough · ~5 minutes

**Topic:** CAL (Comms Abstraction Layer) status & flags — explaining the state-machine diagram
**Diagram referenced:** `diagrams/2-subsystems/mob-cal-architectural-diagram.drawio` Page 2 (State Machine) · `diagrams/3-flows/state/state-cal.md §3`
**Language:** English
**Target length:** ~4:45 (≈ 700 words)

---

## SPOKEN SCRIPT

**[0:00 – 0:30 · Opening]** *— point to the diagram.*

"This diagram is the **state machine for CAL** — the Comms Abstraction Layer, the part of Trackaroo that keeps a group connected when there is no phone signal. The point of a state machine is this: at any moment, no matter what the radios are doing, CAL is in **exactly one** of these states — and each state has a precise, defined meaning. Let me walk you through it."

---

**[0:30 – 1:15 · The four flags]**

"Every state is described by **four true/false signals** — we call them flags. **satReady** — is satellite available? In Phase 1, always false. **queueEnabled** — is a TrackMate session active? **offlineBeacon** — can we currently hear other group members? And **partialSignal** — is the link degraded? Read those four flags together and you know exactly which state CAL is in. On the diagram they appear as a vector on each state — four letters, T for true, F for false."

---

**[1:15 – 3:25 · Walking the five states]** *— move across the diagram as you speak.*

"Now the states themselves — there are **five reachable ones**.

It starts at the top. **S0, AppLaunch** — the app has started, CAL is initialised, but there is no session yet. All four flags false. It moves immediately into **S1, Idle** — TrackMate isn't running, CAL is quiet, nothing shown on screen.

When the user starts a TrackMate session, CAL enters **S2, SessionActive**. This state is *transient* — think of it as a waiting room. queueEnabled has just flipped true, peer discovery is coming online, and within about two seconds CAL settles into one of the three resting states below it. It never stays in S2.

Where it settles depends on what it finds. If it discovers a group member and the link is fast, it enters **S3, BeaconingFull** — the healthy state. offlineBeacon true, partialSignal false. The user sees the label **'Beacon active'**.

If it discovers a member but the link is *slow* — latency above the threshold — it enters **S4, BeaconingPartial**. The same as S3, except partialSignal is now true. The user sees **'Limited Connectivity'**.

And if it finds *no one* in range, it enters **S5, QueueOnly**. No active transport — outgoing messages are written to a local, crash-safe queue and held there. The user sees **'Queue pending'**, or **'Offline'** if the queue is empty."

---

**[3:25 – 4:10 · The transitions]**

"The arrows between the states are where the discipline shows. **Every transition has a single, deterministic trigger.** S3 to S4 and back — latency crossing a threshold. Any active state down to S5 — the last peer is lost. S5 back up to S3 — a new peer comes into range, and the held queue flushes. And from any session state back to S1 — the user simply stops the session. There is nothing probabilistic on this diagram: the same trigger always produces the same transition."

---

**[4:10 – 4:40 · The invariants]**

"Two things hold in **every** state on this diagram. First — **satReady is always false**. There is no reachable state where satellite turns on; that is a Phase 2 capability, and it is architecturally enforced, not merely intended. Second — the labels are deliberately calm. Notice that not one state says 'Reconnecting' or 'Searching'. CAL only ever tells you the state you are *in* — never an action it is pretending to take."

---

**[4:40 – 5:00 · Closing]**

"So — five states, four flags, deterministic transitions, and one honest label per state. That is the entire runtime behaviour of CAL, captured on a single diagram. Thank you."

---

## DELIVERY NOTES

| Aspect | Guidance |
|---|---|
| **Length** | ~700 words ≈ 4:40–5:00. |
| **Diagram sync** | Vừa nói vừa chỉ vào diagram: chỉ S0→S1 khi nói "starts at the top", chỉ S2 khi nói "waiting room", quét xuống S3/S4/S5. |
| **Emphasis beats** | *exactly one* state · *transient* (S2) · *deterministic trigger* · *satReady is always false* · *honest label*. |
| **Pause points** | Sau "Let me walk you through it" · trước mỗi state name S0…S5 · trước "Thank you". |
| **If asked deeper** | M6 = the latency threshold cho partialSignal (provisional, vendor-calibrated). S2 settle deadline ≤ 2s là UXS-5726 Visual Calm requirement. Full matrix: `state-cal.md`. |

---

## Document status

| Field | Value |
|---|---|
| Purpose | ~5-minute diagram-walkthrough script — CAL state machine (5 states · 4 flags · transitions · invariants) |
| Source | `mob-cal-architecture.md` · `state-cal.md` · `mob-cal-architectural-diagram.drawio` Page 2 |
| Companion | `research/trackiq-presentation.md` · `research/delivery-plan-presentation.md` |
