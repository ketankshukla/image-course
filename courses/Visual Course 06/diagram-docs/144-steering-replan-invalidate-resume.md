# Diagram 144 — Steering, Replanning, Invalidation, and Resume

![On dark navy, an ORIGINAL GOAL target leads to PLAN V1, which has two panels: COMPLETED with two green checkmarks and PENDING with three blue circles. A NEW INPUT speech bubble enters IMPACT ANALYSIS, a magnifier over a bar chart. Green arrows show UNAFFECTED COMPLETED WORK STAYS VALID from PLAN V1 to PLAN V2; red X shows AFFECTED PENDING BRANCHES BECOME INVALIDATED. PLAN V2 has its own COMPLETED and PENDING panels. It passes to POLICY CHECKED, then NEW BUDGET RESERVED, then RESUME. A red PATCH IN PLACE puzzle piece is BLOCKED by a red X. Below, a teal chain runs from CHECKPOINT through RECEIPT, ACKNOWLEDGEMENT, and RESUME.](../diagrams/144-steering-replan-invalidate-resume.png)

**Module:** Human-in-the-loop, steering, and recovery
**Role in the course:** how to change direction during long work without erasing history or reusing stale results
**Layout:** original goal and plan v1 on the left, new input and impact analysis in the centre, plan v2 and policy/budget/resume on the right, with a blocked patch-in-place path

---

## At a glance

**ORIGINAL GOAL** → **PLAN V1**.

A **NEW INPUT** arrives. It goes through **IMPACT ANALYSIS**.

**UNAFFECTED COMPLETED WORK STAYS VALID**.
**AFFECTED PENDING BRANCHES BECOME INVALIDATED**.

The result is **PLAN V2**, which is **POLICY CHECKED**, then gets **NEW BUDGET RESERVED**, then **RESUME**.

And **PATCH IN PLACE** is **BLOCKED**.

---

## What the diagram teaches

### 1. New input is an event, not a mutation

A **NEW INPUT** arrives. The diagram draws it as a speech bubble. It is an event in the workflow's history.

The event is not silently patched into the existing plan. It triggers a new version of the plan. The old plan is not deleted. It is kept as history.

This is the durable-workflow pattern. History is append-only. A new fact is appended, not overwritten.

### 2. Impact analysis separates valid from invalidated work

The **IMPACT ANALYSIS** magnifier looks at the new input and the old plan. It asks: which completed steps are still valid? Which pending steps are affected?

Valid completed work is green. It can be reused. Pending branches that are affected are red. They must be invalidated.

The analysis is not a guess. It compares the inputs, assumptions, permissions, evidence, and acceptance tests of each step with the new input. If the new input changes any of those, the step is affected.

### 3. Completed work stays valid only when its inputs and acceptance remain valid

The green arrows from **PLAN V1** to **PLAN V2** show that some completed work is preserved. But only if it is unaffected.

A completed step is not automatically valid just because it ran. It is valid because its inputs and its acceptance criteria are still true. If the new input changes a material assumption, the step is invalidated even though it already happened.

Invalidation does not undo the step. It marks the result as unusable for the new plan. The historical record is preserved.

### 4. Affected pending branches are cancelled and their budgets released

The red X shows that affected pending branches become invalidated. The workflow must cancel them and release their budgets.

A pending step is easier to cancel than a completed one. It has not yet produced side effects. The important thing is to stop it cleanly and release the resources that were reserved for it.

The budget ledger from the previous diagram is where those resources live. Releasing the budgets is part of invalidation.

### 5. Plan V2 is a new plan, not a patched Plan V1

**PLAN V2** is drawn as a separate box, not as an edited version of Plan V1. It is a new plan with its own completed and pending panels.

Plan V2 may include some completed steps from Plan V1. It may also include new steps, repeated steps, or cancelled steps. It has its own identity.

The diagram keeps both plans. The workflow does not erase Plan V1. It records that Plan V1 existed, what was completed, what was invalidated, and why Plan V2 was created.

### 6. Plan V2 goes through the same policy and budget checks as Plan V1

Plan V2 is **POLICY CHECKED** and gets a **NEW BUDGET RESERVED**. It does not inherit the old policy check or the old budget.

The new plan may have new actions, new amounts, or new constraints. It must pass the policy gate again. It must reserve budgets again.

This is the safety rule. A replan is not a shortcut. It is a new plan, and it must go through the same controls.

### 7. Resume continues from the last valid durable point

The final step is **RESUME**. The workflow continues from the last checkpoint that is still valid.

Resume does not mean restart. It means continue from a known good state. The known good state includes the preserved completed work, the new plan, and the fresh budget.

If the workflow crashed during the transition, it would resume from the checkpoint and re-run the impact analysis. The analysis is deterministic, so the same result is produced.

The same principle appears in replay from a known snapshot:

![On dark navy, a SOURCE OF TRUTH box with a book and a shield sits at top left. A COMMAND enters a red VERSION GATE that checks SCHEMA VERSION. The gate has a red coral path to REJECT. Past the gate, the command becomes blue EVENT in a STREAM. A blue arrow to SNAPSHOT at a point in time; a blue arrow from the snapshot to REPLAY, which sends a READ-ONLY arrow to a TEST and a MIGRATE arrow through a green check to a NEW VERSION. A red X blocks TRANSFORM OLD EVENTS.](../diagrams/127-snapshot-replay-schema-evolution.png)

That diagram is about preserving history and replaying from a known point. This diagram is the same: Plan V1 is history, the new input is an event, and Plan V2 is a replay/continuation from the last valid point. The blocked PATCH IN PLACE here is the same as the blocked TRANSFORM OLD EVENTS there. Do not rewrite history; append and replay.

### 8. Patch in place is blocked

The red puzzle piece at the bottom left is **PATCH IN PLACE**, and it is **BLOCKED**.

This is the diagram's central warning. Do not edit variables inside the running plan. Do not change the state and continue as if the previous plan was still valid.

Patching in place hides which outputs became stale. It can execute a consequential step under old assumptions. The diagram forces a visible plan version, impact analysis, and invalidation instead.

### 9. The receipt, acknowledgement, and checkpoint chain makes resume safe

The teal dashed chain at the bottom runs from **CHECKPOINT** through **RECEIPT, ACKNOWLEDGEMENT,** and **RESUME**. This is the durable contract for continuing.

A checkpoint is not just a save point. It is an authoritative record of what has been committed. A receipt proves that a side effect was observed by an external system. An acknowledgement proves that the workflow accepted the new input. Resume can happen only after all three are durable.

If the process crashes between the new input and the creation of Plan V2, the replay starts from the checkpoint, re-reads the new-input event, and re-runs the impact analysis. Because the analysis is deterministic and the dependencies are explicit, the same Plan V2 is produced. The workflow does not have to guess which completed steps are still valid.

---

## Case study — Moorland Legal, the policy exception that changed

Moorland processes legal case referrals. A long workflow gathers evidence, checks policy, and schedules a hearing.

### What they had

The workflow stored the current plan in a mutable state object. When new evidence arrived, the case worker updated the state object directly.

The plan was not versioned. The workflow did not re-run impact analysis. It just continued with the new facts.

### The incident

A case had gathered witness evidence and completed a policy check. The policy check said the case was eligible for fast-track because the claim was below a threshold.

New evidence arrived: the customer had a second related claim. The second claim pushed the total over the fast-track threshold.

The case worker updated the claim amount in the state object. The workflow continued from the next step, which was already scheduled: book the fast-track hearing.

The hearing was booked incorrectly. The case was not eligible for fast-track. The judge rejected the hearing, and the case was delayed by six weeks.

### The new design

New evidence is recorded as a **NEW INPUT** event.

The workflow runs **IMPACT ANALYSIS**. The witness evidence was unaffected. The policy check was affected because the threshold assumption changed.

The policy check is **INVALIDATED**. The hearing booking, which depended on the policy check, is also **INVALIDATED**.

**PLAN V2** is created. It reuses the witness evidence. It re-runs the policy check with both claims. It reserves a new budget for the updated plan.

The workflow resumes from the last valid point: the witness evidence. The policy check is repeated. The hearing is booked only if the new policy check passes.

### Results

- **Hearings booked under old assumptions after new evidence:** 5 in one quarter → 0.
- **Time to determine which work was affected by a new input:** hours of manual review → seconds, from the impact analysis.
- **Reused invalidated results:** any number → 0, because the impact analysis explicitly marks affected branches.
- **Audits able to explain why a plan changed:** improved, because both plan versions and the new input are preserved.

### The line in their legal-ops standard

*When a material fact changes, version the plan, analyse the impact, invalidate affected branches, and create a new policy-checked, budget-reserved plan before resuming.*

---

## Composition

A left-to-right flow from original goal through two plan versions, with impact analysis in the centre and a blocked patch path below.

**Left:** **ORIGINAL GOAL** — a blue platform with a target and arrow.

**Cyan arrow** → **PLAN V1** — a blue card with two panels:
- **COMPLETED** — two green checkmarks.
- **PENDING** — three blue circles.

**Above centre:** **NEW INPUT** — a blue speech bubble on a platform, sending a **cyan arrow** down to **IMPACT ANALYSIS** — a blue platform with a magnifier over a bar chart.

**From impact analysis:**
- **Green arrow** right to **PLAN V2**, labelled **UNAFFECTED COMPLETED WORK STAYS VALID**.
- **Red arrow with X** left to PLAN V1, labelled **AFFECTED PENDING BRANCHES BECOME INVALIDATED**.

**Right:** **PLAN V2** — same structure as Plan V1.

**Cyan arrows** from PLAN V2 to:
- **POLICY CHECKED** — shield.
- **NEW BUDGET RESERVED** — safe.
- **RESUME** — play button.

**Bottom left:** a **red PATCH IN PLACE** puzzle piece with a red X and **BLOCKED** label.

**Bottom centre:** a **teal dashed chain** from **CHECKPOINT** through **RECEIPT, ACKNOWLEDGEMENT** to **RESUME**.

## Element by element

**ORIGINAL GOAL** — the starting objective.
**PLAN V1** — the first version of the route.

**STEERING** — changing active-work direction without erasing history.
**REPLAN** — a new version of the execution route.
**INVALIDATION** — marking a result unusable because its inputs or assumptions changed.

**NEW INPUT** — a fact or instruction that changes the context.
**IMPACT ANALYSIS** — the comparison of new input against plan dependencies.

**UNAFFECTED COMPLETED WORK STAYS VALID** — preserved results.
**AFFECTED PENDING BRANCHES BECOME INVALIDATED** — cancelled results.

**PLAN V2** — the new version of the route.
**POLICY CHECKED / NEW BUDGET RESERVED** — re-validation of the new plan.
**RESUME** — continue from the last valid durable point.

**PATCH IN PLACE / BLOCKED** — the forbidden silent mutation.

## Colour and flow semantics

- **Cyan arrows** carry forward work and the new plan.
- **Green** marks valid, preserved work.
- **Red X** marks invalidated, affected branches.
- **Coral** on the blocked patch path marks the forbidden shortcut.
- **Teal dashed** carries the checkpoint/receipt/acknowledgement/resume chain.
- The **two plan boxes** are separate, showing that Plan V2 is a new version, not an edit.

## How to present it

**Start by asking what happens when new information arrives during a workflow.** Most rooms will say they update the state and continue. That is the problem.

**Point at NEW INPUT and ask whether it is an event or a mutation.** It must be an event. It is appended to history.

**Trace the impact analysis.** The magnifier compares the new input with every step's inputs and acceptance. Ask the room how they currently do that. Usually they don't.

**Show the two outcomes.** Green: unaffected completed work stays valid. Red X: affected pending branches become invalidated. Both must be visible.

**Point at Plan V2.** It is a new plan, not a patched Plan V1. It is policy checked and has new budgets reserved.

**Point at the blocked patch-in-place.** This is the most important warning. Do not edit the running plan. Version it, analyse it, and resume from the last valid point.

**Tell the Moorland story.** New evidence changed a threshold. The workflow patched the state and booked a wrong hearing. The fix: new input as an event, impact analysis, invalidation of policy and hearing, Plan V2 with reused evidence, re-policy check, new budget, resume.

**Emphasize that resume is not restart.** It continues from the last valid checkpoint. Valid work is preserved; invalid work is replaced.

**Close on the standard.** *When a material fact changes, version the plan, analyse the impact, invalidate affected branches, and create a new policy-checked, budget-reserved plan before resuming.*

**Tell the Maya story.** During Maya's review, she clarifies that the purchase was a gift card. That clarification becomes a **NEW INPUT** event: payment proof stays valid, the policy result is invalidated, pending payment is cancelled, and the revised plan reaches an ineligible outcome with an explanation.

**Map to the Next.js implementation path.** Render plan versions, changed assumptions, invalidated steps, and preserved evidence. Submit steering instructions through an authenticated, versioned server command. Before the user confirms a high-impact replan, explain which work was cancelled, reused, or repeated. Keep the browser view read-only with respect to workflow truth; mutations go through authenticated server boundaries and return stable IDs or receipts.

**Map to the Python implementation path.** Represent plans as immutable versions with explicit dependency edges. Implement impact analysis as a pure, deterministic function over changed facts and step inputs. Propagate cancellation to child workers and create new child identities for invalidated work so old receipts are not silently reused. Model commands, events, states, and error outcomes as typed records so tests can replay the same fixture without network calls.

**Run the dependency lab.** Ask the room to draw a plan dependency graph for one real case, change one input, and mark every step as preserved, invalidated, cancelled, repeated, or newly added.

**Ask the checkpoint question.** "Why not restart the whole workflow after every change?" Answer: a full restart wastes valid work and can repeat effects; dependency-based invalidation preserves safe results while replacing affected work.

**Point to the related patterns and sources.** This pattern appears in Diagram 127 (snapshot, replay, and schema evolution — the blocked patch-in-place here is the same as the blocked transform-old-events there), Diagram 141 (planner/executor/reviewer/policy separation), and Diagram 143 (human interrupts and stale approvals). It is grounded in Temporal's event history, message passing, and cancellation: those systems keep plan versions, propagate cancellation, and resume from durable checkpoints rather than mutating in-memory state.

**Timing.** Twenty-five minutes. Thirty if the room changes one input in a real plan and marks which steps are preserved and which are invalidated.

---

## Lab and checkpoint

**Lab:** Draw a plan dependency graph for one real case. Change one input and mark each step as preserved, invalidated, cancelled, repeated, or newly added. Create Plan V2 as a new plan with its own policy check and budget, then resume from the last valid checkpoint.

**Checkpoint:** Why is patch-in-place blocked?

**Answer:** Because editing a running plan destroys the ability to track what was valid, what was invalidated, and why. Versioning the plan, analysing impact, and creating a new policy-checked plan preserves the durable record and makes resume safe.

## Glossary

- **Cancellation** — stopping pending branches that are no longer valid.
- **Impact analysis** — comparing new input with each step's inputs and acceptance.
- **Invalidation** — marking completed or pending work as no longer valid.
- **New input** — a change that is appended as an event, not a mutation.
- **Patch-in-place** — editing a running plan, which is forbidden.
- **Plan V1 / Plan V2** — versioned plans, where V2 is a new plan, not a patched V1.
- **Policy check** — the gate that the new plan must still pass.
- **Resume** — continuing from the last valid durable point.
- **Restart** — beginning the workflow again, which wastes valid work.
- **Steering** — the process of adjusting a workflow in response to new input.

## Sources

- Steering, replanning, and invalidation
- Plan versioning and impact analysis
- Durable workflow resume and checkpointing
