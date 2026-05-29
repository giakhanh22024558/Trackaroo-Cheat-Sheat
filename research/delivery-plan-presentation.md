# Delivery Plan — Trackaroo® Phase 1
## 6–7 minute vendor presentation script

**Audience:** Client / evaluators (vendor pitch)
**Language:** English
**Target length:** ~6:45 (≈ 1,010 words at a measured pitch pace)

---

## SPOKEN SCRIPT

**[0:00 – 0:35 · Opening]** *— slow, confident; let the date land.*

"Good morning. Trackaroo Phase 1 has one fixed point that everything else bends around — the public launch on the **13th of November 2026**. We acknowledge that as the non-negotiable commercial anchor, and our entire delivery plan is engineered backwards from it. To reach it, we compress the schedule by a **full six weeks** against a traditional sequential build — without compromising the engineering standard. I'll cover that in four parts: the squad and the parallel model; the gate schedule and its hard dependencies; how we execute; and how we govern and de-risk delivery."

---

**[0:35 – 2:30 · Part 1 — The Squad & the Parallel Model]**

"First — the team and the model. We deliver Phase 1 as a **900 man-day effort, led by a lean squad of eight senior experts** — no junior blending. That gives one hundred percent senior oversight on every milestone, which is what lets us run at high concurrency without the quality risk that usually brings. The squad is led by a **project manager focused on gate-model governance** and a **technical architect who personally governs Survival Core isolation**, with senior leads owning mobile, web and console, backend, QA, and UX.

A sequential build cannot reach November — so we run **eight workstreams in parallel** from the point of appointment: the Survival Core; TrackMate transport; Mapping and Visual; the Experience Layer; Feed Integration; QA and Validation; Legal and Regulatory; and Web and Operations Console.

Six weeks of compression is a specific claim, so let me show where it comes from — two levers. The first is **validation throughput**: a unified automation harness in our dedicated lab takes continuous QA from around 160 man-days down to 110, because the validation domains run automated, around the clock, across the full device matrix. The second is **integration efficiency**: locking a single, type-safe data schema between the Survival Core and the Operations Console early eliminates roughly 40 man-days of interoperability rework. Those two levers *are* the six weeks — measured, not asserted."

---

**[2:30 – 4:05 · Part 2 — Gate Schedule & Hard Dependencies]**

"Second — the gate schedule. Those eight tracks are sequenced against **four binary release gates**: Discovery on the 15th of June, Alpha on the 22nd of August, Beta-Ready MVP on the 30th of October, and GA on the 13th of November. Every gate is **all-or-nothing** — partial satisfaction does not authorize progression — and we **cannot self-certify**: only written Project Director sign-off clears a gate.

Parallel does not mean reckless. Several **hard dependencies are non-compressible**, and we respect each one. No subsystem development begins without **approved wireframes**. TrackMate transport waits for an approved transport proposal. And critically — **SOS and BackTrack are the highest priority**: the Survival Core must reach acceptance before the Experience Layer, TrackIQ and TrackMate, is prioritized. That sequencing establishes evidentiary integrity early, where it matters most.

At the Discovery Gate we don't just describe this — we evidence it. We bring a defined artefact set: an **architecture diagram decomposing Firebase isolation**; a **deterministic state matrix** showing the app handles its logic with no network dependency; a **module isolation map** proving a fault in the comms layer can never stall the Survival Core; and the **CVs of the senior squad** who personally sign each compliance artefact."

---

**[4:05 – 5:30 · Part 3 — Agile Execution]** *— pick up pace slightly; this is your team's strength.*

"Third — how we execute, day to day. We run **Agile and Scrum** — a method our team has used for years and trusts. Within every sprint we manage two things in tension: **deliverable** — being on time — and **value** — being on quality.

For on-time: **two team meetings a week**, and internal deadlines set **ten percent earlier** than the planned date — a buffer that keeps the team focused and absorbs surprises before they reach the client.

For quality — *fast, but never sloppy* — we apply **atomic responsibility**: every developer owns their feature end to end. We measure that ownership with a clear KPI — the bugs QA finds in features marked as delivered. To keep that honest, **QA is a separate team from development**; they communicate not ad hoc but through a single, curated, version-controlled document source — which forces every developer to self-test thoroughly before handover. And before anything reaches QA, every pull request passes **two independent code reviewers** — for transparency, execution-logic safety, and clean, handover-ready code. Each sprint carries a defined goal, and every feature is reviewed for progress and risk at each meeting."

---

**[5:30 – 6:45 · Part 4 — Governance & Risk]**

"Finally — governance and risk. Every decision is **traceable to the project's Authority Stack** — a layered hierarchy of governance documents. At the top sits the UX and behavioural authority that owns the offline-first mandate; beneath it the product, functional, testing, wireframe, and vendor-delivery authorities; and supporting them, specialist guides covering safety, battery, mapping, hazard feeds and more. The rule is simple: **any conflict resolves strictly upward** toward the highest document. So when a change request arises, we trace its origin, reconcile it against the governing document, and raise any new feature to Ian Moore for approval before implementation.

On risk — our most significant schedule risks are **external dependencies we don't control**: the legal reviews, and the clinical approval of First Aid content. We've identified those explicitly and built contingency around the mandatory review periods. And to remove geography as a risk entirely, we validate Australian conditions from our dedicated lab — **CLR-SLZ-001** — using **GPS-simulation and Faraday-shielded rigs**: repeatable, lab-grade stress testing across the full continental Australian coordinate envelope, ten to forty-four degrees south — so Survival-Grade compliance is proven before the Beta-Ready gate."

---

**[6:45 – 7:05 · Closing]** *— slow down; land each point.*

"To close — a senior-only squad, eight parallel workstreams, four binary gates, and six weeks of *measured* compression. Disciplined Agile protects quality while we move fast. And every line we ship is traceable to an approved requirement. That is how we deliver Trackaroo Phase 1 — **on time, and on standard.** Thank you."

---

## DELIVERY NOTES

| Aspect | Guidance |
|---|---|
| **Length** | ~1,010 words ≈ 6:40–7:00 at measured pace. If overrunning, cut the coordinate-envelope detail in Part 4 and the "with senior leads owning…" clause in Part 1. |
| **Emphasis beats** | *13 November 2026* · *full six weeks* · *all-or-nothing* · *fast, but never sloppy* · *measured* (closing) · *on time, and on standard*. |
| **Pause points** | Sau opening date · trước mỗi "First / Second / Third / Finally" · sau mỗi gate date · trước "Thank you". |
| **Key numbers** | 8 workstreams · 8 senior experts · 900 man-days · 6 weeks compression · 4 gates · QA 160→110 days · ~40 md integration saving. |
| **Tone** | Vendor pitch — confident, evidence-led. Mỗi claim đều có cơ chế phía sau (6 weeks = 2 levers; quality = KPI + separated QA). Tránh nói chung chung. |

### Q&A preparation

| Likely question | Answer line |
|---|---|
| **(Ian Moore) "Rủi ro treo luồng — nếu Experience Layer lỗi thì sao?"** | "The Experience Layer and the Survival Core run as **separate processes / isolates in Flutter**. A fault, freeze, or crash in the CAL or TrackMate layer is contained — it can never block or hang the Survival Core's execution path. Navigation, SOS and BackTrack keep running regardless." |
| "6 tuần compression từ đâu ra?" | "Two levers — QA automation harness (160→110 man-days) + unified type-safe schema (~40 man-days). Measured, not asserted." |
| "KPI dựa trên QA-found bugs có tạo đối đầu QA↔dev không?" | "Đó là lý do QA giao tiếp qua tài liệu curated tập trung, không đối đầu trực tiếp — đo lường khách quan, không cá nhân hoá." |
| "Validate điều kiện Úc khi team ở Việt Nam?" | "CLR-SLZ-001 Lab — GPS-simulation + Faraday-shielded rigs, continental envelope 10°S–44°S, repeatable lab-grade testing." |

---

## APPENDIX A — Gate Schedule

Anchored to the non-negotiable GA deadline **13 November 2026**.

| Gate | Target date | Key criteria & mandatory conditions |
|---|---|---|
| **Discovery** | **15 Jun 2026** | Acceptance of all 9 architectural compliance artefacts · TrackMate™ transport proposal approved · WFD-5126 wireframe coverage per subsystem · documented CAL architecture · companion website live |
| **Alpha** | **22 Aug 2026** | Survival Core subsystems functional + validated · SOS onboarding click-through implemented · Universal Baseline clinical review complete · SOS legal review (LE-02) complete · prohibited-capability scan clear · Stage 1 Operations Console modules ready |
| **Beta-Ready MVP** | **30 Oct 2026** | All 11 TQP-5026 validation domains executed · full-tier clinical review + APPs compliance review complete · WCAG 2.1 AA audit passed · ToS + Privacy Policy published · all 22 rejection triggers resolved |
| **GA / Release** | **13 Nov 2026** | Final compliance confirmation · App Store + Google Play submissions approved and live · all open rejection triggers resolved |

**Gate progression rules:** detection of any rejection trigger (RT-01…RT-22) at any gate halts progression immediately · gate criteria are all-or-nothing · on a halt condition the build is quarantined, remediation + full revalidation mandatory · only written Project Director sign-off allows progression (no self-certification).

---

## APPENDIX B — Optimized Parallel Workstream Map (8 tracks · 900 man-day effort)

Milestones: Contract Execution 29 May · Discovery Gate 15 Jun · Alpha Gate 22 Aug · Beta-Ready Gate 30 Oct · GA / Public Launch 13 Nov.

| # | Track | Scope | Start dependency |
|---|---|---|---|
| **1** | **Survival Core** | Offline deterministic integrity — Navigation, SOS, BackTrack™ | Highest priority · leads · starts at appointment |
| **2** | **TrackMate™** | BLE Mesh + CAL logic | Begins only after transport proposal approved |
| **3** | **Mapping & Visual** | Custom TRK styling · offline tile-budget management | Parallel with Survival Core from Discovery |
| **4** | **Experience Layer** | TrackIQ™ scoring · archetype presets | Commences only after Survival Core reaches acceptance |
| **5** | **Feed Integration** | Normalization of BOM / AFAC feeds into the TrackIQ™ pipeline | Parallel with Survival Core from Discovery |
| **6** | **QA & Validation** | Continuous execution of the 11 TQP-5026 domains | Runs continuously from appointment |
| **7** | **Legal / Regulatory** | Clinical + legal review coordination (LE-01 to LE-07) | Sequenced around mandatory review periods |
| **8** | **Web & Ops Console** | Companion Website (Discovery gate) + staged Operations Console (OCS-5026) delivery | Parallel stream |

**Hard dependencies (non-compressible · per vendor-delivery authority §7.2):**
1. No subsystem development without **approved wireframes (WFD-5126 build gate)**.
2. TrackMate™ transport proposal **approved by the Project Director** before any TrackMate™ development.
3. **SOS and BackTrack™** are the highest priority — Survival Core reaches acceptance before the Experience Layer is prioritized.
4. Timeline explicitly accounts for **mandatory clinical + legal review rest periods** without compromising GA.

---

## APPENDIX C — Lean Senior Squad (900 man-day effort · 100% senior oversight)

| Role | Name |
|---|---|
| Project Manager — gate-model governance | **Khanh** |
| Tech Lead / Architect — Survival Core isolation | **Tru** |
| Mobile lead | **Khoi** |
| Web / Console lead | **Viet** |
| Backend / DevOps lead | **Hoang** |
| QA / Audit lead | **Thom** |
| UI / UX lead | **Duong** |
| *(8th senior expert)* | ⚠️ **Not named in source note** — confirm name + role |

> ⚠️ **Reconciliation flag:** the source note states "eight named Senior Experts" but lists only **seven** roles/names. Confirm the 8th expert before this appendix or any CV pack is finalised.

---

## APPENDIX D — Efficiency levers (how the 6 weeks is achieved)

| Lever | Track | Mechanism | Saving |
|---|---|---|---|
| **Validation throughput** | Track 6 — QA | Unified Automation Harness in the **CLR-SLZ-001 Lab** · 24/7 automated parallel execution of the 11 TQP-5026 domains across the full device matrix, geography-independent | Continuous QA effort **160 → 110 man-days** |
| **Integration efficiency** | Track 8 — Web & Ops Console | Strict **unified type-safe data schema** between Survival Core ↔ Operations Console locked early in the cycle | **~40 man-days** interoperability contingency eliminated |

**Risk mitigation — remote high-fidelity validation:** GPS-simulation + Faraday-shielding in CLR-SLZ-001 Lab enables repeatable lab-grade stress testing across the continental Australian coordinate envelope (**10°S–44°S**) — Survival-Grade compliance proven before the Beta-Ready gate, without geographic dependency.

---

## APPENDIX E — Authority Stack (governance hierarchy, reference)

Conflict resolution rule: **any ambiguity resolves strictly upward** toward the highest-priority document. In the spoken presentation, refer to *categories* — do not enumerate codes.

- **Primary stack (top → down):** UX & behavioural authority → product & acceptance authority → functional specification → testing & QA authority → wireframe & UI-state authority → vendor delivery & guidance authority.
- **Specialist supporting guides:** overlay semantics · hazard-feed governance · emergency safety framework · cloud & data governance · battery performance standard · BackTrack™ framework · target archetypes · mapping architecture.
- **Operational governance:** Central Amendment Register (amendment history) · Operations Console specification.

---

## APPENDIX F — Discovery Gate artefacts (the evidence the squad brings)

| Artefact | Demonstrates |
|---|---|
| **Mode B architecture diagram** | Detailed decomposition of Firebase isolation |
| **Deterministic State Matrix** | Flutter handles logic with zero network dependency |
| **Module Isolation Map** | A fault in the CAL / TrackMate™ layer never hangs the Survival Core execution path |
| **Senior Squad CVs** | The 8 senior experts who personally sign off compliance artefacts |

---

## APPENDIX G — Timeline revisions & commercial concessions

- **Revised procurement timeline:** process amendment 13 Apr 2026 extended the vendor submission deadline to **1 May 2026**.
- **Proposal concessions:** vendors permitted to **defer certain empirical proof obligations to the Discovery gate** (high-variance areas — battery, transport range), provided methodology + risk treatment are described in the proposal.
- **Separable portions:** commercial model amended to allow independent pricing of high-uncertainty areas (e.g. **Separable Portion 2: TrackMate™ Transport Validation**), provided those portions clear the relevant gates.

---

## RECONCILIATION NOTES (delivery note vs this script)

| # | Item | Status |
|---|---|---|
| 1 | **8 senior experts vs 7 named** | ⚠️ Open — 8th expert not named in source. See Appendix C. |
| 2 | **Spec ID VEG-5026 vs VGD-5126** | ⚠️ Open — note cites VEG-5026 §7.2/§7.3; Authority Stack documents VGD-5126. Script avoids the code, says "vendor delivery authority". Confirm whether same doc or distinct. |
| 3 | **Track 8 = "Web & Ops Console"** | ✅ Reconciled — Appendix B updated; Companion Website now under Track 8 (was a Discovery-criterion line). |
| 4 | **Legal reviews LE-01 to LE-07** | ✅ Applied (note supersedes Figure 3's "LE-01 to LE-03") — confirm range if needed. |
| 5 | **GPS-simulation / Faraday capability** | ✅ Confirmed as Slitigenz capability — now in script Part 4 + Appendix D. |
| 6 | **6-week compression mechanism** | ✅ Enriched — 2 levers added (Part 1 + Appendix D). |

---

## Document status

| Field | Value |
|---|---|
| Purpose | 6–7 minute vendor-pitch script for Trackaroo Phase 1 delivery plan + reference appendices |
| Source | Proposal (parallel delivery model · gate schedule · Authority Stack) + Slitigenz delivery note (Lean Senior Squad · efficiency levers · CLR-SLZ-001 lab) + presenter's Agile/Scrum methodology |
| Outstanding | (1) 8th senior expert name · (2) VEG-5026 vs VGD-5126 disambiguation · (3) LE review range confirmation |
| Trigger to update | Gate date amendment (via CAR-5026) · squad change · scope change raised to Ian Moore · presenter feedback after rehearsal |
