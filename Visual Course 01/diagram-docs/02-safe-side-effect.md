# Diagram 02 — Safe Side Effect

![Four numbered panels on a dark navy background — CONFIRM, AUTHORIZE, IDEMPOTENCY KEY, CHANGE + RECEIPT — connected by teal arrows, with a thick teal SAFE RETRY loop running underneath from the receipt back through a rejected duplicate write into the key stage.](../diagrams/02-safe-side-effect.png)

**Module:** 1 — See the whole system
**Role in the course:** explaining safe writes and retries
**Layout:** four numbered panels in a row, plus a return loop underneath

---

## At a glance

This is the diagram for the moment an agent stops reading and starts changing something. It breaks a single write into four required steps and then shows what happens when that same write is attempted a second time.

The four panels along the top are the setup. The loop underneath is the payload. Most teams can recite the four steps; far fewer have looked closely at the small circular badge on the return path, which shows a duplicate write being **rejected** — and that rejection is the only reason the word "safe" belongs in the title.

---

## What the diagram teaches

### 1. The colour flips at the point of no return

Read the four headings and watch the palette. **CONFIRM** and **AUTHORIZE** are titled in coral. **IDEMPOTENCY KEY** and **CHANGE + RECEIPT** are titled in teal.

That flip is placed precisely. Everything to the left of it is a question that can still be answered *no*. Everything to the right of it is machinery for making a decision that has already been taken execute exactly once and leave a trace.

This gives you a useful way to audit your own write paths. Find the point in your code where the answer stops being "should we?" and becomes "how do we do this correctly?" Everything before that point needs the ability to refuse. Everything after it needs the ability to be replayed without harm. Systems get into trouble when those two responsibilities are mixed — when a retry can re-trigger an authorization decision, or when a confirmation dialog is the only thing preventing a duplicate.

### 2. Confirmation is a human physically touching the trigger

The first panel does not show a config flag called `require_confirmation`. It shows a person reaching out with an extended finger and pressing a coral button.

The literalism is the lesson. Confirmation means a human being, in possession of the relevant facts, taking an action that they understand commits something. Three things commonly get called confirmation and are not:

- **A prompt instruction** telling the agent to ask before acting. The agent complies most of the time. "Most of the time" is not a control.
- **A confirmation the human cannot evaluate.** If the dialog says "Proceed with 47 changes?" and does not show what the 47 changes are, the click is theatre. The person is confirming their trust in the system, not the action.
- **A default-yes.** If the flow continues on timeout, or the approve button is pre-focused and enter-to-continue works, you have consent from inattention.

The person in the panel is looking at a screen that shows the change before the button. That ordering matters.

### 3. Authorization is per-item, not a boolean

The second panel is the one people skim past. It shows a coral shield — and beside it, a card with **three rows: two green checks and one coral warning**.

Authorization is drawn as a *verdict on each element of the request*, not a gate that opens or closes. This reflects how real permission systems behave and how agent requests actually arrive. An agent proposes a batch: update these five records, notify these three people, adjust this amount. The correct answer is frequently "three of those yes, one no, one needs a higher approval."

Systems that model authorization as a single boolean handle this badly in one of two ways. They fail the whole batch, which trains users to make batches smaller until the control is meaningless. Or they pass the whole batch on the strength of the caller's role, which means the one item that should have been refused goes through with the four that were fine.

Note also that confirmation comes *before* authorization in this diagram. The human says what they want; the system then decides what they are permitted to have. Doing it the other way — filtering to what is permitted, then asking — hides from the user that they asked for something they cannot have.

### 4. The fingerprint on the key is the whole idea

The third panel could have shown a plain key entering a lock. It shows a key whose head is a **fingerprint**.

A plain key is about permission: does the holder have the right to open this? A fingerprint is about identity: is this specific one, and no other? An idempotency key is the second thing. It does not grant access. It asserts that *this particular operation* has a unique identity, so that the system can recognise it if it ever sees it again.

The practical consequences follow from that:

- **The key must be derived from the operation, not generated fresh.** If your retry generates a new key, you have no protection at all. Derive it from the stable facts — the entity being changed, the amount, the originating request, the approval that authorised it.
- **The key must be supplied by the caller.** The server cannot infer that two requests are "the same" from their contents, because two genuinely distinct requests can look identical. Two $40 refunds to the same customer on the same day might be a duplicate or might be two refunds.
- **The window matters.** A key remembered for sixty seconds protects against network retries. A key remembered for a day protects against a user clicking again after lunch. Choose deliberately.
- **The response must be replayable.** On seeing a known key, the correct behaviour is to return the *original result*, not an error. A retry that receives a 409 has to guess whether it succeeded.

### 5. The receipt is what makes the loop possible

Look at where the SAFE RETRY path physically originates: a teal ribbon leaving the **receipt** in panel 4, curling downward into the return route.

That is not a routing convenience. It is a causal claim. You can only detect and suppress a duplicate if the first attempt left a durable record behind. A system that performs a change without recording it cannot recognise the change coming round again. The receipt is not paperwork produced after the fact for auditors — it is load-bearing infrastructure for correctness.

This is also why the change and the receipt share a single panel rather than getting one each. Writing the change and recording the change are one operation. If they can diverge — if the ledger can update while the audit write fails — then you have two sources of truth that disagree, and the duplicate check is reading the one that might be missing.

### 6. What the coral ✗ badge actually depicts

On the return path sits a dark circular badge containing a **dashed-outline database marked with a coral ✗**.

That is the second write. Dashed because it never became real. Coral because the system refused it.

This is the single most important object in the diagram and the easiest to miss. Without it, the bottom loop reads as "retries happen" — a statement of fact with no design content. With it, the loop reads as "retries happen *and are absorbed*," which is a property you have to build.

It is worth being clear about what is being claimed. The retry is not safe because retries are harmless; a second $340 credit is very harmful. The retry is safe because stages 1 through 3 established the conditions under which a duplicate can be identified and dropped. Safety is manufactured upstream and collected here.

---

## Case study — Cadence, subscription billing refunds

Cadence runs subscription billing for around three thousand small software companies. Their support team processes refunds: a customer disputes a charge, an agent investigates, and money moves. About four hundred refunds a day, average value $180, occasional values in the thousands.

They built an assistant to handle refund investigation and execution. The first version shipped without this diagram. The second version was built from it.

### What the first version did

The assistant could read the subscription record, the invoice, and the usage data, then call `issue_refund(invoice_id, amount)`. A support agent typed "refund the March charge for Acme," the assistant worked out which invoice that was, and issued it. Fast, popular with the support team, and in production for eleven weeks.

Three problems accumulated.

**The confirmation was uninspectable.** The assistant replied "Refund $240 for invoice INV-88213?" and the agent clicked yes. What the agent could not see was *which* March charge had been selected when a customer had two, or that the amount included a prorated credit the customer was not entitled to. Agents were confirming the assistant's confidence, not the action.

**Authorization was role-only.** Support agents had refund permission, so every refund passed. There was no per-refund ceiling and no distinction between a $40 refund and a $4,000 one. A new hire in week three refunded an annual enterprise contract in full because the customer asked nicely.

**There was no idempotency at all.** The billing API occasionally timed out under load while still committing the refund. The assistant, seeing a timeout, retried. Over eleven weeks this produced nineteen duplicate refunds totalling a little over $6,000, discovered during a month-end reconciliation rather than at the time.

### What the second version did

They rebuilt the write path as the four stages.

**Confirm.** The assistant now renders the full proposed change before the button: the specific invoice with its date and description, the exact amount with any proration broken out line by line, the customer's refund history, and the reason string that will be recorded. The support agent presses approve on a screen that shows them what they are approving. Confirmation time went up by about eleven seconds per refund. Nobody objected once the first mis-selected invoice was caught in review.

**Authorize.** Refund authority became a per-item decision evaluated against four rules: the agent's ceiling, the account's lifetime refund total, whether the invoice was already partially refunded, and whether the subscription was under an enterprise contract with negotiated terms. A refund can now come back as *approved*, *refused*, or *escalated to a supervisor* — and refused refunds show the specific rule that refused them, so the agent knows whether to escalate or explain.

Crucially, this evaluation happens **after** the support agent has confirmed and **regardless** of what they confirmed. The new hire in week three now gets an escalation, not a $4,000 refund.

**Idempotency key.** Every refund carries a key derived from the invoice ID, the amount in minor units, and the approval record ID. Keys are retained for seventy-two hours. On a repeat key, the billing service returns the original refund object with a `duplicate_suppressed` flag rather than an error, so the assistant can distinguish "already done" from "failed."

**Change + receipt.** The refund and its audit record are written in one transaction. The receipt captures the invoice, amount, approving agent, the authorization rules that were evaluated and their outcomes, the reason string, and the idempotency key itself.

### The week the loop earned its keep

Fourteen days after launch, their billing provider had a partial outage: requests were being accepted and processed, but responses were timing out for roughly forty minutes. In the old system this was precisely the condition that generated the nineteen duplicates.

During the incident the assistant retried sixty-three refund submissions. All sixty-three came back duplicate-suppressed with the original refund object. Zero duplicate money moved. The incident produced a log full of suppression events and no financial impact — which is exactly what the small coral ✗ badge on the diagram depicts, happening sixty-three times in forty minutes.

The reconciliation that used to find duplicates at month end now finds none, and the finance team stopped budgeting time for it.

### What this cost

Worth stating honestly, because the four stages are not free.

The confirmation screen took three weeks to build properly, mostly because rendering "what will actually change" required the assistant to produce a structured preview rather than a sentence. The authorization rules required finance to write down policies that had previously lived in people's heads, which surfaced two disagreements that took a month to resolve. Idempotency required a schema change to the refunds table and a retention job.

The whole thing took about a quarter. The nineteen duplicates it would have prevented were worth $6,000. That is not the return — the return is that the refund path is now something the company can let an agent touch at all.

---

## Composition

Four dark rounded panels sit in a row, each with a blue numbered circle and a heading:

**1 CONFIRM → 2 AUTHORIZE → 3 IDEMPOTENCY KEY → 4 CHANGE + RECEIPT**

Solid teal arrows connect the panels. Below the row, a thick teal path leaves panel 4, runs left along the bottom of the frame, passes through a circular badge, and turns upward into panel 3. The words **SAFE RETRY** sit in large teal capitals at the lower left.

Panels 1 and 2 are titled in coral; panels 3 and 4 are titled in teal.

## Element by element

**Panel 1 — CONFIRM**
A person seen from behind and slightly to the left, seated in a dark chair, wearing a blue top, reaching out with an extended index finger to press a coral **CONFIRM** button on a monitor. Behind the button the screen shows a small form: a check mark and two lines of content.

**Panel 2 — AUTHORIZE**
A coral shield bearing a white check, raised on a blue pedestal. To its right, a dark card listing three rows: two with green check circles, one with a coral warning triangle.

**Panel 3 — IDEMPOTENCY KEY**
A blue octagonal key head stamped with a fingerprint, its shaft inserted into a large blue padlock whose keyhole glows teal, with faint dashed detail running along the shaft into the lock.

**Panel 4 — CHANGE + RECEIPT**
A blue database stack topped with a green check badge, a teal cube on a small pad, and a printer emitting a white receipt with a green check and text lines. A teal ribbon leaves the receipt and curls downward off the panel. To the right, a dark card shows a small vertical timeline with teal dots.

**The SAFE RETRY loop**
A thick teal line from panel 4, passing through a dark circular badge containing a dashed-outline database with a coral ✗ circle, then continuing left and turning up into panel 3.

## Colour and flow semantics

- **Coral** marks the things that can say no: the button a human must press, the authorization shield, and the rejected duplicate write.
- **Teal** marks the things that are committed and recorded: the key, the change, the receipt, and the retry path itself.
- **Green checks** operate at row level inside panels, indicating individual passed checks rather than overall success.
- The heading colour flip between panels 2 and 3 marks the transition from refusable to committed.

## How to present it

**Start by hiding the bottom third.** Cover the SAFE RETRY loop and walk the four panels. The room will find this agreeable and slightly over-engineered — which is the reaction you want, because it makes the reveal land.

**Then reveal the loop and ask what the coral ✗ database is.** Do not tell them. Let the room work out that it is the same request arriving a second time. The moment someone says "oh, that's the retry being rejected" is when idempotency stops being a word from a specification and becomes a thing they can see.

**Ask for war stories.** "Who here has shipped a duplicate?" In any room of ten engineers, three hands go up, and one of those stories will involve money. Use the volunteered story rather than the case study — it is more persuasive and it means the room is teaching itself.

**Run the removal drill.** Take each of the four stages out in turn and name the resulting system:

- Without **confirm**: a system that acts without consent.
- Without **authorize**: a system where anyone who can ask can do.
- Without **the key**: a system that charges twice whenever the network hiccups.
- Without **the receipt**: a system that cannot prove what it did — and, less obviously, cannot detect duplicates either, because there is nothing to compare against.

The fourth one is the payoff, because it shows the receipt is not for the auditors, it is for the mechanism.

**Connect it forward to where it gets applied.** This pattern is protocol-agnostic — nothing in it is specific to MCP or A2A, which is why it sits in the opening module. It reappears as the final gate of the delegation security pipeline:

![Five stages — MINIMIZE CONTEXT, ALLOWLIST AGENT, BIND TASK, VALIDATE ARTIFACT, LOCAL APPROVAL — with coral reject paths dropping into bins and a final teal SIDE EFFECT ALLOWED badge.](../diagrams/23-a2a-security-gates.png)

The rightmost stage there — a person pressing approve, producing a **SIDE EFFECT ALLOWED** badge — is this diagram's panels 1 and 2, sitting at the end of a delegation chain. Showing the two together makes the point that no amount of upstream agent machinery removes the need for the human at the commit boundary.

**Anticipate the objection.** Someone will say this is too heavy for low-value operations. Agree, and ask them to name the threshold. The productive version of that conversation is not "always do all four" — it is "write down the value above which you do all four, and then check whether your agent can distinguish the two cases at runtime." Most cannot, which is the actual finding.

**Timing.** Twenty minutes with the reveal and the removal drill. Add fifteen if you run the war-story discussion, which is usually worth it.

---

## Lab and checkpoint

**Lab:** Pick one high-value side effect in a system you work on — a payment, a refund, an account change, or a data export. Write down the four gates from this diagram — confirm, authorize, key, receipt — and map each one to a control that already exists in your system. For any missing gate, write the smallest change that would add it and one test that would catch a duplicate or unauthorized execution.

**Checkpoint:** Why is the receipt load-bearing for the mechanism, not just for the auditors?

**Answer:** Because the receipt is what a later retry compares against to detect that the same request has already been executed. Without a durable receipt, the system cannot distinguish a duplicate from a new request, and the same side effect can run twice.

## Glossary

- **Authorization** — a per-item decision that a specific actor may perform a specific action.
- **Confirmation** — an explicit human action, such as pressing a key, that triggers the side effect.
- **Coral ✗ badge** — the visual marker that a duplicate or unauthorized request is rejected.
- **Idempotency key** — a unique identifier attached to a request so the system can recognise and reject duplicates.
- **Receipt** — a durable record that a side effect occurred, including enough detail to detect duplicates.
- **Safe retry** — a retry that is blocked when a matching receipt already exists.
- **Side effect** — an action that changes state or moves value outside the system.

## Sources

- Idempotency keys in payment and billing systems
- A2A side-effect and artifact validation patterns
- Human-in-the-loop authorization and confirmation controls
