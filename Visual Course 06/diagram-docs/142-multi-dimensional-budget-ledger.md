# Diagram 142 — Time, Cost, Token, Tool, and Retry Budgets

![On dark navy, a wide blue PARENT BUDGET LEDGER panel at the top lists six columns: TIME, MONEY, TOKENS, TOOL CALLS, RETRIES, CONCURRENCY, each with an icon. From it, three cyan ALLOCATE arrows drop to three CHILD ENVELOPE cards — POLICY AGENT, FINANCE AGENT, RISK AGENT — each showing the six budget icons. From each child, a teal SPEND arrow drops to a RECEIPT, then to a REMAINING AMOUNT wallet. Three red arrows converge from the remaining wallets to a red BUDGET EXHAUSTED bar. Below that, three coral paths fan to PARTIAL RESULT, DEGRADE, and ESCALATE.](../diagrams/142-multi-dimensional-budget-ledger.png)

**Module:** Human-in-the-loop, steering, and recovery
**Role in the course:** bounding agent work with independent budgets and making exhaustion a safe, explicit outcome
**Layout:** parent ledger above, child envelopes in the middle, receipts and remaining amounts below, exhaustion outcomes at the bottom

---

## At a glance

A **PARENT BUDGET LEDGER** has six columns: **TIME, MONEY, TOKENS, TOOL CALLS, RETRIES, CONCURRENCY**.

It **ALLOCATE**s smaller **CHILD ENVELOPES** to **POLICY AGENT, FINANCE AGENT, RISK AGENT**.

Each child **SPEND**s, produces a **RECEIPT**, and reports **REMAINING AMOUNT**.

If a budget is exhausted, the flow goes to **BUDGET EXHAUSTED**, then branches to **PARTIAL RESULT, DEGRADE, ESCALATE**.

A budget is not just a token limit. Time, money, tool calls, retries, and concurrency are all separate resources, and each one can run out.

---

## What the diagram teaches

### 1. Six dimensions, not one

The parent ledger has six independent columns. They are not added together. Each is its own limit.

**TIME** — wall-clock deadline.
**MONEY** — cost, in currency.
**TOKENS** — model input and output budget.
**TOOL CALLS** — number of external calls.
**RETRIES** — number of attempts for transient failures.
**CONCURRENCY** — number of simultaneous workers.

A workflow can run out of time while it still has tokens. It can run out of tool calls while it still has money. Each dimension has its own meaning and its own exhaustion behaviour.

### 2. Allocate means reserve, not share

The **ALLOCATE** arrows from the parent to the children are reservations. Each child gets an envelope with limits for each dimension.

The parent does not give the child its full remaining budget. It reserves a bounded envelope. That prevents one child from starving its siblings, or from consuming the entire workflow budget and leaving nothing for recovery.

A child cannot spend more than its envelope. If it needs more, it must ask the parent for an extension. The parent can extend, or it can decide the work is not worth the extra cost.

### 3. Every spend returns a receipt

Each **SPEND** arrow points to a **RECEIPT**, then to **REMAINING AMOUNT**. The receipt is the durable record of what was spent.

The receipt is not optional. It is the evidence. Without it, the remaining amount is a guess. With it, the parent can reconcile the budget, audit the spend, and decide whether to extend or stop.

### 4. Remaining amount is a first-class state

The **REMAINING AMOUNT** is drawn as a wallet. It is not a hidden counter. It is a state that the workflow can observe and act on.

A child can read its remaining amount and decide whether to continue, simplify, or return. The parent can read the remaining amount and decide whether to reallocate, degrade, or escalate.

### 5. Budget exhausted is not a failure

The red **BUDGET EXHAUSTED** bar is a workflow state, not an exception. When a budget runs out, the workflow must choose what to do.

The three outcomes are:
- **PARTIAL RESULT** — return whatever was completed within the budget.
- **DEGRADE** — switch to a simpler, cheaper method.
- **ESCALATE** — ask a human for more budget or a decision.

Each of these is a valid business outcome. The important thing is that the workflow does not silently continue past a budget. It makes an explicit decision.

### 6. A deadline and a retry count answer different questions

A deadline says *do not spend more wall-clock time on this*. A retry count says *do not try more than N times*. They should not be merged.

If they are the same limit, the workflow can retry quickly and run out of time, or wait a long time and run out of retries, without a clear reason. Independent budgets let the workflow make precise trade-offs.

A retry budget should also be separated from a tool-call budget. One retry consumes one tool call, but the limit on retries is about uncertainty, not about external calls.

### 7. Children cannot spend what they do not have

The child envelope is the contract. The child cannot spend capacity that the parent did not reserve or explicitly extend.

This is the safety rule. A child that can spend the parent's full budget is not a child. It is a runaway process. The envelope limits the blast radius.

The parent is the only entity that can move budget between children. That is the allocation and reallocation authority.

### 8. Budget exhaustion is a durable workflow outcome

The flow from budget exhausted to partial result, degrade, or escalate must be checkpointed. The decision must be recorded with the state of each budget dimension at the moment of exhaustion.

This is the same durable vocabulary: acknowledgement, receipt, checkpoint, resume. The budget is part of the workflow state.

The same idea appears earlier in the admission gate that protects workers and important users:

![On dark navy, a stack of white cubes labelled REQUEST FLOOD sends three cyan arrows into a tall blue ADMISSION GATE, which shows four white stacked panels — CAPACITY, TENANT LIMIT, PRIORITY, DEADLINE. A cyan arrow labelled ACCEPTED leaves the gate into three blue queues — HIGH, NORMAL, BULK — each with a signal-strength bar. Each queue sends a cyan arrow to a worker pool: HIGH WORKER POOL (FEW, FAST), NORMAL WORKER POOL (MORE), BULK WORKER POOL (MANY). A red OVERLOAD arrow leaves the bottom of the gate to a red RETRY LATER clock on a red platform. A dashed teal CAPACITY SIGNAL arrow loops from the worker pools back to the left side of the gate.](../diagrams/130-backpressure-admission-priority.png)

That diagram controls demand before it enters the system. This diagram controls spend after work has been allocated. Both are admission control: one at the door, one inside each child task. The budget ledger is the internal admission gate. It protects the parent from a single child consuming all capacity.

### 9. Every scarce resource has its own ledger column

The six columns are not a decorative checklist. **TIME, MONEY, TOKENS, TOOL CALLS, RETRIES,** and **CONCURRENCY** each measure a different kind of scarcity, and each can run out before the others.

Concurrency is easy to miss because it is not a speed or token limit. It is the number of simultaneous workers a child may have in flight. A child that opens too many parallel streams can starve its siblings, overwhelm an external API, or hide the real spend because each stream only reports its own. The parent sets a concurrency envelope to stop one branch from becoming a noisy neighbor.

Unused capacity also matters. When a child finishes, the remaining portion of its envelope is released and can be reallocated. The ledger must record not only **SPEND** but also **RELEASE**, otherwise the parent cannot tell whether capacity is available again. Merging these dimensions into a single token or time pool would hide the real bottleneck.

### 10. The budget ledger is part of the durable workflow record

A budget is not a runtime decoration. The ledger is an explicit contract between parent and child. It must record what was requested, who owns the envelope, what changed, which attempt produced it, and what may legally happen next.

That means every reserve, spend, release, and exhaustion outcome is a typed event under the workflow identity. Estimated and actual spend can diverge, especially after retries or slow calls, so the receipt captures the real cost. Optional branches should stop early when the expected cost is higher than the remaining value, and that early stop should be recorded too.

A transport can retry, a worker can disappear, and an agent can revise its proposal, but the budget record must remain inspectable. That keeps business meaning intact across restarts, so a replayed workflow reaches the same exhaustion decision for the same reasons.

---

## Case study — Northfield Support, the retrieval storm

Northfield uses an agent to answer customer support tickets. The agent can retrieve documents, call a payment provider, and generate a response.

### What they had

A token limit of 8,000 tokens per ticket. No limit on tool calls, retries, or time.

For most tickets, this was fine. But for a complex refund case, the agent could keep retrieving documents, calling the provider, and retrying failed calls. The token limit was the only thing that stopped it, and by then the ticket had consumed hundreds of external calls and taken several minutes.

### The incident

A customer asked about a refund status. The agent retrieved 47 documents, called the provider 12 times, and retried 8 times because the provider was slow. The token limit finally stopped it, but the response was incomplete and the customer had waited over five minutes.

Worse, the agent's retries were not idempotent. Some of the provider calls duplicated work on the provider side. The support team's monthly tool-call bill doubled.

### The budget design

The parent workflow sets six budgets for each ticket:
- **TIME** — 30 seconds.
- **MONEY** — £0.50 per ticket.
- **TOKENS** — 8,000.
- **TOOL CALLS** — 10.
- **RETRIES** — 3.
- **CONCURRENCY** — 2.

It allocates child envelopes for each sub-task: document retrieval, provider lookup, response generation.

If the retrieval child exhausts its tool-call budget, the workflow returns a **PARTIAL RESULT** with the documents it found and a note that the full record was not retrieved.

If the provider child exhausts its retry budget, the workflow **DEGRADES** to a simpler provider query or returns a *we are checking, please wait* status.

If the case is high-value and budgets are exhausted, the workflow **ESCALATES** to a human with the partial evidence.

Every spend is recorded as a receipt. The parent can see exactly how much each child used and why.

### Results

- **Tickets with more than 10 tool calls:** 12% → 0.4%.
- **Average ticket response time:** 4.2 minutes → 18 seconds.
- **Provider bill from retry storms:** reduced by 60%.
- **Incomplete responses returned without explanation:** any number → 0, because every budget-exhausted path returns a meaningful partial or escalation state.

### The line in their operations standard

*Every scarce resource has its own budget and a named safe outcome when it runs out. A child cannot spend more than its envelope.*

---

## Composition

A wide parent ledger at the top, child envelopes in the middle, spend/receipt/remaining chains, and an exhaustion fan at the bottom.

**Top:** **PARENT BUDGET LEDGER** — a wide blue panel with six icons and labels:
- **TIME** — clock.
- **MONEY** — dollar.
- **TOKENS** — coin stack.
- **TOOL CALLS** — code brackets.
- **RETRIES** — circular arrow.
- **CONCURRENCY** — group of people.

**Three cyan arrows** from the parent ledger, labelled **ALLOCATE**, drop to three **CHILD ENVELOPE** cards:
- **POLICY AGENT**
- **FINANCE AGENT**
- **RISK AGENT**

Each child envelope shows the six budget icons.

**From each child, a teal arrow** labelled **SPEND** drops to a **RECEIPT** card, then to a **REMAINING AMOUNT** wallet.

**Three red arrows** from the remaining wallets converge on **BUDGET EXHAUSTED** — a red bar.

**Below the bar, three coral arrows** fan to:
- **PARTIAL RESULT** — document icon.
- **DEGRADE** — speedometer icon.
- **ESCALATE** — upward arrow icon.

## Element by element

**PARENT BUDGET LEDGER** — the source of all budget authority.
**TIME / MONEY / TOKENS / TOOL CALLS / RETRIES / CONCURRENCY** — the six dimensions.

**ALLOCATE** — the reservation from parent to child.

**CHILD ENVELOPE** — the bounded budget for a child task.

**SPEND** — the act of consuming budget.
**RECEIPT** — the durable record of spend.
**REMAINING AMOUNT** — the observable state after spend.

**BUDGET EXHAUSTED** — the terminal state for a dimension.

**PARTIAL RESULT / DEGRADE / ESCALATE** — the safe next actions.

## Colour and flow semantics

- **Cyan arrows** carry allocation from parent to child — authority given.
- **Teal arrows** carry spend, receipt, and remaining amount — durable state.
- **Red arrows** carry budget exhaustion — a terminal condition.
- **Coral arrows** carry the three recovery outcomes — partial, degrade, escalate.
- The **six columns on the parent ledger** are equally sized, showing that every dimension is independent.
- The **red bar** across all children shows that any child can hit exhaustion, and it is a shared workflow condition.

## How to present it

**Ask what limits the room currently has.** Most have a token limit. Some have a timeout. Few have all six.

**Point at the six columns and ask why they are separate.** A token limit does not stop tool-call storms. A timeout does not stop retries. Each budget answers a different question.

**Trace ALLOCATE.** It is a reservation, not a gift. The parent keeps unallocated capacity. A child that needs more must ask.

**Show the receipt chain.** Every spend has a receipt. Without receipts, the remaining amount is a guess. With receipts, the workflow can reconcile and audit.

**Point at BUDGET EXHAUSTED.** It is not a crash. It is a state. Ask what their system does when a budget runs out. If the answer is nothing, the work may continue silently.

**Discuss the three outcomes.** Partial result, degrade, escalate. Each should be wired to a concrete step. A budget hit without a next action is a hang.

**Tell the Northfield story.** A token limit let an agent make hundreds of tool calls and retries. The fix: six independent budgets, child envelopes, receipts, and explicit partial/degrade/escalate outcomes.

**Emphasize that children cannot spend unreserved capacity.** The envelope is the contract. Without it, one child can consume the entire workflow budget.

**Close on the standard.** *Every scarce resource has its own budget and a named safe outcome when it runs out. A child cannot spend more than its envelope.*

**Ask the room to name a hidden budget.** Most systems have implicit limits: one reviewer, one API quota, one queue length, one concurrency slot. Hidden budgets become failures when exhausted without a name.

**Map the ledger to one real payload.** For one incoming case, fill in the initial value, the reservation per child, the estimated spend, the actual receipt, and the released amount. The exercise usually shows only tokens and time are explicit.

**Show why estimates are not enough.** A budget that relies on estimates alone leaks because real spend includes retries, duplicates, and overhead. The receipt is the evidence.

**Discuss the UI boundary.** A Next.js front end can show remaining time and meaningful state, but not raw provider costs. A Python adapter should reserve, spend, release, and receipt atomically.

**Run the checkpoint question.** Should a child receive the parent’s full remaining budget? The envelope is the contract; a child that spends unreserved capacity is a runaway process, not a child.

**Point to the lab challenge.** Ask the room to draw a budget ledger with initial, reserved, spent, remaining, and exceeded columns across all six dimensions. The first draft usually merges time and retries.

**Teaching note.** This diagram pairs with the admission-gate lesson (Diagram 130). The gate protects the front door; the budget ledger is the same idea inside each child. Teaching them together shows admission control happens at every boundary.

**Timing.** Twenty minutes. Thirty if the room creates a budget ledger for one real case, which usually reveals that most limits are implicit.

---

## Lab and checkpoint

**Lab:** Create a budget ledger for one real case. Include six dimensions: tokens, time, tool calls, retries, concurrency, and cost. For each, set the initial budget, allocate a child envelope, record spend and receipts, and define the safe outcome when the budget is exhausted.

**Checkpoint:** Why must children receive an envelope rather than the parent's full remaining budget?

**Answer:** Because a child with the full remaining budget can consume all of it. An envelope is a reserved, bounded amount that the child may spend. This prevents one child from starving others and lets the parent reconcile remaining capacity.

## Glossary

- **Allocate** — reserving a portion of the budget for a child.
- **Budget** — the limit for a scarce resource.
- **Budget exhausted** — the state where a budget is spent, not a failure.
- **Child** — a subtask or worker that spends from an envelope.
- **Concurrency** — the number of simultaneous workers or calls.
- **Cost** — the monetary budget.
- **Envelope** — the reserved budget a child may spend.
- **Ledger** — the record of budget reservations, spends, and receipts.
- **Parent** — the workflow that owns and allocates the budget.
- **Receipt** — the record that a spend occurred.
- **Retries** — the limit on repeated attempts.
- **Time** — the wall-clock budget.
- **Token** — the model context budget.
- **Tool call** — the count of tool invocations.

## Sources

- Multi-dimensional budget and ledger design
- Admission control and child envelopes
- Token, time, and cost budgeting
