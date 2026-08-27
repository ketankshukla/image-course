# Diagram 74 — Progress, Artifacts, and Recovery UX

![Three columns on dark navy. LIVE PROGRESS lists four numbered steps with teal progress bars — UNDERSTANDING, CHECKING POLICY, VERIFYING PAYMENT, PREPARING RESULT. ARTIFACTS lists three cards — EVIDENCE PACK, DECISION SUMMARY, AUDIT RECEIPT — with a COMPLETED EARLIER badge beneath. Between the middle and right columns sits a coral PARTIAL FAILURE tile. RECOVERY lists four options — RETRY SAFE STEP, CONTINUE TASK, CHANGE INPUT, CONTACT HUMAN. Coral dashed arrows run from the artifacts through the failure tile to the recovery options, and a cyan line returns along the base to the progress column.](../diagrams/74-progress-artifacts-and-recovery-ux.png)

**Module:** The complete system
**Role in the course:** what the user sees when something half-works
**Layout:** three columns — progress, artifacts, recovery — joined by a partial-failure tile

---

## At a glance

Three columns. **LIVE PROGRESS** shows what is happening. **ARTIFACTS** shows what has been produced so far. **RECOVERY** shows what the user can do when something breaks.

Between the middle and right columns sits a coral **PARTIAL FAILURE** tile, and it is the diagram's subject. Not total failure — partial. Some of the work succeeded, produced real artifacts, and then something stopped.

The design question this answers is one most interfaces get wrong: **what do you show a user when half the job is done?**

---

## What the diagram teaches

### 1. Progress steps are named, not numbered

**UNDERSTANDING, CHECKING POLICY, VERIFYING PAYMENT, PREPARING RESULT.**

Each is a phrase describing what is happening, not "step 2 of 4."

The difference matters when something is slow. A user watching "step 3 of 4" for ninety seconds has no idea whether that is normal. A user watching "verifying payment" for ninety seconds can form a judgement — and, importantly, can tell support something useful.

Each step also has its own **teal progress bar**, so a long step shows internal movement rather than appearing frozen.

### 2. Artifacts are surfaced as they are produced, not at the end

The middle column lists three artifacts — **EVIDENCE PACK**, **DECISION SUMMARY**, **AUDIT RECEIPT** — with arrows from the progress steps that produced them.

Each becomes available when it exists. The evidence pack is complete after the understanding step; the decision summary after the policy check.

Beneath them sits a **COMPLETED EARLIER** badge, which is the diagram's quiet insistence: **things that finished stay finished.** A failure at step three does not invalidate what steps one and two produced.

That is not how most interfaces behave. The common pattern is an error screen that replaces everything, discarding the visible evidence of completed work.

### 3. Partial failure is a distinct state, and it gets its own tile

The coral **PARTIAL FAILURE** tile sits between what was produced and what can be done about it.

Three states, not two:

**Success** — everything completed.
**Failure** — nothing completed.
**Partial failure** — some completed, some did not, and artifacts exist.

The third is the most common in multi-step work and the least often designed for. Interfaces that model only success and failure show a partial failure as a failure, which throws away real work and tells the user nothing about what state they are actually in.

### 4. Four recovery options, and they are genuinely different actions

**RETRY SAFE STEP** — re-attempt the step that failed. Available only when the step is safe to repeat, which is why the word *safe* is in the label.

**CONTINUE TASK** — proceed past the failure. Appropriate when the failed step was not essential, or when its output can be supplied another way.

**CHANGE INPUT** — the failure was caused by something the user provided. Amend it and proceed.

**CONTACT HUMAN** — escalate, with everything produced so far attached.

Four options because four different situations. Offering only "try again" covers one of them.

Note that the options are offered **to the user**, not chosen by the system. The system knows what failed; the user often knows why.

### 5. The word "safe" in RETRY SAFE STEP is load-bearing

Not every step can be retried. A step that took a payment, sent a notification, or filed something cannot simply be run again.

The label acknowledges that the system must know, per step, whether retry is safe — which requires the idempotency and side-effect machinery from earlier in this volume:

![A flow showing USER INTENT producing an IDEMPOTENCY KEY, a FIRST ATTEMPT and a RETRY both carrying KEY-7F3A, passing a DOMAIN GATE to ONE RECEIPT with a coral NO SECOND WRITE branch and a SAME RECEIPT return.](../diagrams/54-retry-and-idempotency.png)

Offering "retry" on a step that is not idempotent is offering the user a way to cause a duplicate. The option should only appear when it is genuinely safe.

### 6. The recovery column returns to progress, and the loop closes

A **cyan line** runs from the recovery column along the base and back into the progress column.

Recovery resumes the work rather than restarting it. The user picks an option, and the task continues from where it stopped — with everything already produced still in place.

That is only possible because the artifacts persisted and the workflow checkpointed. The UX in this diagram is the visible surface of the durability machinery underneath.

### 7. Contact human carries the context with it

The fourth option is drawn with a headset icon, and the arrow into it comes from the same place as the others — after the artifacts.

An escalation that arrives with the evidence pack, the decision summary and the audit receipt attached is a very different thing from one that arrives as "it didn't work."

The person receiving it can see what succeeded, what failed, and what was produced, without asking the user to re-explain.

---

## Case study — Kestrelbank, the mortgage application that failed at step three

Kestrelbank is a mid-sized lender. Their application assistant takes a mortgage application through affordability assessment, credit checking, property valuation instruction, and a decision in principle.

Four steps, typically two to five minutes, and the third step depends on an external credit bureau.

### The old failure experience

When the credit bureau was slow or unavailable — which happened on roughly 3% of applications — the assistant showed an error.

The error replaced the screen. It read: *"We were unable to process your application. Please try again later."*

What that discarded:

- The affordability assessment, which had completed and taken the applicant eleven minutes of data entry.
- The evidence pack, which had been assembled.
- The applicant's entire input.

Applicants returning "later" started from the beginning. Their analytics showed that **62% did not return at all.**

At roughly 3% of applications and their volume, that was around 400 abandoned applications a year, each representing an applicant who had already invested a quarter of an hour.

### What they built

**Named progress steps.** Understanding your application, checking affordability, verifying credit history, preparing your decision. Applicants watching "verifying credit history" for two minutes now had something to tell support other than "it's stuck."

**Artifacts surfaced as produced.** After affordability completes, the applicant sees a summary of what was assessed — income, commitments, the affordability figure. It is theirs, it exists, and it survives a later failure.

**Partial failure as a distinct state.** The credit bureau failing now produces:

> **We've completed part of your application.**
> ✓ Application details captured
> ✓ Affordability assessed — you can view the summary
> ✗ Credit check unavailable — the credit reference agency is not responding
> Your progress is saved. What would you like to do?

Then four options.

**The four options, with real logic behind which appear.**

*Try the credit check again* — offered, because the credit check is a read and is safe to repeat.

*Continue without it* — **not offered**, because a decision in principle cannot be issued without a credit check. Kestrelbank were explicit that the option should not appear when it is not genuinely available.

*Change your details* — offered, since some credit-check failures are caused by an address mismatch or a mistyped date of birth.

*Speak to someone* — offered, and it carries the completed affordability assessment and the evidence pack to the adviser.

### The retry-safety audit

Building the retry option required them to classify every step.

**Understanding** — safe, no side effects.
**Affordability** — safe, computation only.
**Credit check** — safe *with a caveat*. A hard credit search leaves a footprint on the applicant's file, and repeated searches are visible to other lenders and can affect their score.

That caveat changed the design. Retry is offered, and it is **rate-limited to two attempts within 24 hours**, with an explanation: *"Credit checks leave a record. We'll try once more; after that we'll ask an adviser to help."*

**Property valuation instruction** — **not safe**. Instructing a valuation costs money and books a surveyor. Retry is never offered on this step; a failure routes to a human.

That classification exercise found something else: their old system had been retrying valuation instructions automatically on failure, and had produced **11 duplicate valuation bookings** over the preceding year, each costing about £280.

### Results

- **Applications abandoned after a partial failure:** 62% → 19%.
- **Applicants choosing "speak to someone":** 34% of partial failures, arriving with completed work attached.
- **Duplicate valuation bookings:** 11/year → 0.
- **Support contacts saying "it's stuck":** dropped sharply, replaced by contacts naming the specific step.

That last change was unexpected and useful. Named steps meant applicants reported *"it's been on verifying credit history for five minutes"* rather than *"your website is broken."*

### What their design lead says

*The failure screen was throwing away eleven minutes of the applicant's work to tell them something had gone wrong at our end. That was the whole problem.*

---

## Composition

Three vertical columns beneath bordered headers.

**Left — LIVE PROGRESS:** four numbered rows, each with an icon, a label and a **teal segmented progress bar**. Cyan arrows run downward between them and rightward from each into the artifacts column.

**Centre — ARTIFACTS:** three cards, each with a teal icon: **EVIDENCE PACK** (folder with magnifier), **DECISION SUMMARY** (clipboard with checks), **AUDIT RECEIPT** (receipt with shield). Beneath, a **COMPLETED EARLIER** badge with a teal check, with a dashed teal arrow up into the audit receipt.

**Between centre and right:** a **coral PARTIAL FAILURE tile** with a white warning triangle, receiving **coral dashed arrows** from the artifacts.

**Right — RECOVERY:** four rows, each with a teal icon: **RETRY SAFE STEP** (circular arrows), **CONTINUE TASK** (play button), **CHANGE INPUT** (pencil), **CONTACT HUMAN** (headset). Coral dashed arrows enter the first three from the failure tile.

**Base:** a **cyan line** running from the recovery column leftward and up into the progress column.

## Element by element

**LIVE PROGRESS rows**
**1 UNDERSTANDING** (brain) · **2 CHECKING POLICY** (shield with check) · **3 VERIFYING PAYMENT** (payment card) · **4 PREPARING RESULT** (document). Each with a partially-filled teal bar.

**ARTIFACTS**
**EVIDENCE PACK** — a teal folder with a magnifier. **DECISION SUMMARY** — a teal clipboard with checked rows. **AUDIT RECEIPT** — a teal receipt with a shield badge.

**COMPLETED EARLIER**
A teal badge with a white check and a dashed arrow upward.

**PARTIAL FAILURE**
A **coral rounded tile** with a white warning triangle and two-line label.

**RECOVERY options**
**RETRY SAFE STEP** — teal circular arrows. **CONTINUE TASK** — teal play disc. **CHANGE INPUT** — teal pencil. **CONTACT HUMAN** — teal headset.

## Colour and flow semantics

- **Cyan arrows** carry progress downward and rightward, and carry the recovery return along the base.
- **Coral dashed arrows** carry the failure path from artifacts through the tile into the recovery options.
- **Teal** marks every progress bar, every artifact icon and every recovery icon.
- The **COMPLETED EARLIER badge** with its dashed upward arrow asserts that finished work persists through the failure.
- The **coral tile sits between artifacts and recovery**, not at the end — failure is mid-flow, not terminal.

## How to present it

**Ask what their interface shows when step three of four fails.** Most rooms describe an error screen. Then ask what happens to what steps one and two produced.

**Tell the Kestrelbank number first.** Eleven minutes of applicant data entry, discarded by an error message, 62% never returning, around 400 abandoned applications a year.

**Introduce partial failure as a third state.** Success, failure, and *some of it worked and produced real things*. Ask which of the three their system models. Usually two.

**Point at the COMPLETED EARLIER badge.** Things that finished stay finished. Ask why an error screen that replaces everything is the common pattern — usually because failure handling was built as an afterthought at the outermost layer.

**Read the four recovery options and ask why four.** Four situations. Then ask what "try again" alone covers — one of them.

**Dwell on the word "safe."** Not every step can be retried. Then walk the Kestrelbank classification: affordability safe, credit check safe-with-a-caveat because a hard search leaves a footprint, valuation not safe because it books a surveyor.

**Give them the duplicate-valuation finding.** The old system retried valuation instructions automatically and produced 11 duplicate bookings at £280 each. Classifying steps for the UI found a production bug.

**Make the point about not offering unavailable options.** Kestrelbank do not show "continue without it" when a decision genuinely cannot proceed. An option that will fail is worse than no option.

**Ask what an escalation carries.** "It didn't work," or the evidence pack, the decision summary and the audit receipt. Then note that 34% of Kestrelbank's partial failures choose the human route, arriving with completed work attached.

**Close on named steps.** Support contacts changed from "your website is broken" to "it's been on verifying credit history for five minutes." A named step turns a complaint into a diagnosis.

**Timing.** Twenty-five minutes. Thirty-five if you classify the retry-safety of the room's own steps, which reliably finds one that should not be retried and currently is.

---

## Lab and checkpoint

**Lab:** For one multi-step workflow in your product, classify each step as safe to retry, safe with a caveat, or not safe to retry. Then design a partial-failure UI that preserves completed artifacts and offers only the valid recovery options: retry safe step, continue task, change input, or contact human. Write what each recovery option would actually do.

**Checkpoint:** Why should partial failure preserve completed artifacts rather than replacing the screen with an error?

**Answer:** Because steps one and two may have already produced real, valuable work. Throwing it away on a failure turns a recoverable state into data loss and abandonment. Preserving completed artifacts and offering targeted recovery respects the user's effort.

## Glossary

- **Artifact** — a produced object, such as an evidence pack, decision summary, or audit receipt.
- **Change input** — the recovery option that lets the user fix the input and continue.
- **Completed earlier** — the badge that shows finished work survives the failure.
- **Contact human** — the recovery option that escalates with the completed artifacts attached.
- **Continue task** — the recovery option that proceeds around a failed step if possible.
- **Partial failure** — the state where some steps succeeded and produced artifacts but the whole workflow is not complete.
- **Recovery UX** — the interface that helps the user recover from a partial failure.
- **Retry safe step** — the recovery option that re-executes a step that is safe to retry.
- **Safe** — a step that can be retried without side effects or extra cost.

## Sources

- Partial-failure UX and recovery design
- Workflow artifacts and retry-safety classification
- Human escalation and completed-work preservation
