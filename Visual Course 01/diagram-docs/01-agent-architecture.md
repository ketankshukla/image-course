# Diagram 01 — Agent Architecture

![Five platforms in a row on a dark navy background, labelled PERSON, APPLICATION AGENT, MCP CAPABILITIES, A2A SPECIALIST, and DOMAIN + POLICY, joined by cyan arrows, with a dashed teal return line running along the bottom back to the person.](../diagrams/01-agent-architecture.png)

**Module:** 1 — See the whole system
**Role in the course:** opening architecture slide
**Layout:** single horizontal row, five stages, one forward route and one return route

---

## At a glance

Five stages in a straight line: a person, the agent they talk to, the capabilities that agent can call, the specialist agents it can hand work to, and the policy layer that everything eventually touches. A second, quieter route runs back underneath, from the policy layer all the way to the person.

Almost every architecture diagram of an agent system stops at the fourth box. This one adds a fifth and then adds a return line, and those two additions are the entire argument of the course. What the picture claims is that an agent system is not finished when the action succeeds — it is finished when the person who asked can see what was done in their name.

---

## What the diagram teaches

### 1. Five stages means four boundaries

The temptation when reading this diagram is to count the boxes. Count the arrows instead. There are four, and each one is a place where something crosses out of one trust domain and into another.

**Person → Application Agent.** The person states an intent in natural language. What crosses this boundary is ambiguous, under-specified, and occasionally wrong. The agent's first job is to turn it into something precise. Nothing downstream can recover from a misunderstanding here, which is why the request journey diagram later gives planning its own numbered stage.

**Application Agent → MCP Capabilities.** The agent stops reasoning and starts calling. What crosses this boundary is a structured call against a published contract. The agent does not know how the capability is implemented and must not care. This is the boundary where schemas, validation, and rate limits live.

**MCP Capabilities → A2A Specialist.** Work leaves your process and goes to another actor with its own agency, its own model, its own failure modes, and possibly its own vendor. What crosses is a task, not a function call — and critically, it is a task the specialist can accept, work on, take time over, and return something unexpected from.

**A2A Specialist → Domain + Policy.** The proposed change meets the rules. What crosses is an intent to modify the system of record. This is the last point at which anything can be stopped.

Once you see the diagram as four boundaries rather than five boxes, the design questions become obvious: *what is the contract at each crossing, what can be refused there, and what evidence does the crossing produce?* An architecture review that answers those three questions for all four arrows is most of the way to a safe system.

### 2. A capability is a tool; a specialist is an actor

The two middle stages look similar in a list — "things the agent talks to" — and are profoundly different in practice. The diagram separates them visually on purpose: MCP is drawn as a **toolbox**, an inert object full of labelled instruments, and A2A is drawn as **two robots exchanging arrows in both directions**.

A capability is passive. It has no opinion, it does not decide whether your request is a good idea, it returns quickly or it errors, and it holds no view about the work. You call `get_shipment_status`, you get a status. If you call it a hundred times you get a hundred statuses. All the intelligence stays on your side of the boundary.

A specialist is active. You hand it a *task* — a bounded description of an outcome you want — and it decides how to achieve it. It may take minutes. It may come back with a partial result, a request for clarification, or a refusal. It might use its own tools and its own retrieval to get there, and you will not see any of that. What you get back is an artifact.

This distinction determines almost everything about how you build:

| | Capability (MCP) | Specialist (A2A) |
| --- | --- | --- |
| You send | A call with arguments | A task with an outcome |
| It returns | A result, quickly | An artifact, eventually |
| Errors look like | Exceptions, status codes | Refusals, partials, timeouts |
| Intelligence lives | On your side | On its side |
| You must validate | The schema | The schema *and* the content |
| Retry semantics | Your problem to make idempotent | The task already has an identity |

The last row is the one people get wrong. Retrying a tool call is a decision you make; a task already has an ID, so re-asking about it is a *status check*, not a re-submission. Teams that treat a specialist like a function end up submitting the same work three times.

### 3. Policy is the far wall, not a step

Notice where DOMAIN + POLICY sits. Not near the person, where it would function as a permission check on the request. Not next to the agent, where it would be a guardrail on reasoning. It is at the **far end**, past the specialist, adjacent to the database and the receipt.

That placement encodes a specific and slightly uncomfortable claim: **policy is enforced where the change lands, not where the request starts.**

The reason is that upstream checks are advisory. An agent can be prompted to respect a rule and will mostly comply, but "mostly" is not an enforcement model. Rules that live in a prompt can be argued out of, forgotten under context pressure, or bypassed entirely by a specialist agent that never saw your prompt in the first place. Rules that live at the write boundary cannot.

The three objects sharing that final platform — the **database**, the **coral shield**, and the **receipt** — are grouped deliberately. Your system of record, the rules governing it, and the evidence of what happened to it are one concern. Teams that split them across three systems discover that the audit log and the actual data disagree, and that nobody can say which one is right.

### 4. The dashed line is the diagram's real argument

The longest single element in the picture is the dashed teal line running from the policy layer back to the person. It gets no label, no icon, and no numbered stage. It is also the thing that separates this architecture from an ordinary integration diagram.

Ask what happens if you delete it. The system still functions. Requests still arrive, tools still get called, specialists still work, changes still land. What is lost is the ability of the person who asked to find out what was done. And that loss compounds:

- The person cannot tell a *successful* action from a *silently failed* one.
- Nobody can reconstruct why a change was made three weeks later.
- A wrong action cannot be distinguished from a correct action with a bad outcome.
- Trust in the system decays, because it can only be extended, never verified.

Note that the return line is **dashed**, while the forward arrows are solid. That is not decoration. The forward arrows carry the request itself. The dashed line does not carry the request back — it carries *evidence about* the request. Different kind of thing, drawn differently.

This is also why the line runs to the **person** and not back to the agent. The agent already knows what it did. The point of the return route is to close the loop with the human who is accountable for it.

### 5. The straight line is a narrative device

The five stages read as a sequence, and reality is not sequential. Most requests never reach a specialist. Many never call a capability at all. Some hit policy immediately and stop. The straight line is there because it is the clearest way to introduce five ideas in order, not because it is a required call path.

The system map corrects this, and it is worth showing the two together:

![The same components drawn as a fan-out: USER to APP AGENT, which branches into three parallel lanes labelled RAG KNOWLEDGE, MCP CAPABILITIES, and A2A TEAM, all reconverging on a single DOMAIN + POLICY platform.](../diagrams/03-modern-agent-system-map.png)

Here the middle stages are drawn as **parallel lanes** rather than a chain, and a third lane — retrieval — appears alongside them. Same components, different claim: these are alternatives the agent chooses between, not steps it marches through. The only thing that stays fixed is the convergence on policy at the right-hand end.

Teach the straight line first because it is learnable. Correct it immediately, because leaving it uncorrected produces engineers who think they must call a tool before they are allowed to delegate.

---

## Case study — Northwind Freight, "Ops Assistant"

A mid-sized freight brokerage runs a customer operations team of about forty coordinators. They handle roughly nine hundred shipments a day across a dozen carriers. When a shipment goes late, a coordinator has to work out why, tell the customer, and decide whether to issue a service credit. That last step touches money, so it is governed.

The team is drowning in tab-switching: carrier portals, the internal transport management system, the billing platform, the CRM, and a policy wiki. Leadership approves a project to build an internal assistant. Here is how it maps onto the five stages.

### Stage 1 — Person

**Priya, a customer operations coordinator.** She types into the assistant panel inside the existing ops console: *"Shipment 4471 is two days late and the customer is asking for a credit. What happened and what can we offer them?"*

That single sentence contains an investigation, a policy question, and a request for a financial decision. It is exactly as under-specified as real requests are. Note what Priya has **not** said: which carrier, what the contract terms are, whether this customer has had credits before, or what she is authorised to approve. All of that has to be recovered downstream.

### Stage 2 — Application Agent

The assistant embedded in the ops console. Its job is to decompose Priya's sentence into a plan:

1. Establish the facts of the delay.
2. Establish what the customer's contract entitles them to.
3. Establish this customer's credit history.
4. Determine whether a credit is warranted and at what amount.
5. Present a recommendation to Priya with evidence.

Critically, the agent decides that step 4 is **not its call**. Credit determination is a governed decision owned by the finance team, with its own rules that change quarterly. The agent's plan routes that step outward rather than attempting it. This is the boundary decision that shapes the entire build.

### Stage 3 — MCP Capabilities

Northwind's platform team stands up a capability server exposing the tools the assistant is allowed to use:

- `get_shipment(id)` — pulls the shipment record from the TMS.
- `get_carrier_events(shipment_id)` — pulls the scan and exception history from the carrier integration layer.
- `get_contract_terms(customer_id)` — reads the service-level terms attached to the account.
- `get_credit_history(customer_id, window)` — reads prior credits issued.
- `search_policy(query)` — reads the ops policy corpus.

Every one of these is a **read**. This is the single most important design choice in the project, and it was deliberate: the capability server exposes no tool that changes anything. There is no `issue_credit`. There is no `update_shipment`. The blast radius of a confused agent calling the wrong tool with the wrong arguments is bounded at "it read something it did not need."

The assistant calls four of these five tools and assembles the facts: shipment 4471 was tendered on time, sat at a carrier hub for thirty-one hours against a four-hour standard, and the carrier logged a weather exception that the contract's force majeure clause arguably covers. The customer has had two credits in the past ninety days.

That last fact is why this cannot be automated. It is a judgement call about a customer relationship, and it has money attached.

### Stage 4 — A2A Specialist

Finance operates its own **Credit Adjudication Agent**, on its own infrastructure, maintained by its own team, with its own version of the credit rules. The ops assistant does not have those rules and should never have a copy of them — they change quarterly and a stale copy is worse than no copy.

The ops assistant creates a **task**:

> Assess service credit eligibility for shipment 4471, customer NW-2213. Evidence attached: shipment record, carrier event log, contract terms extract, ninety-day credit history. Return an eligibility determination, a recommended amount, and the reasoning.

Three things about this crossing are worth pausing on.

**It is a task, not a call.** The ops assistant does not invoke `calculate_credit()`. It describes an outcome it wants and hands over the evidence. The adjudication agent may take forty seconds. It may come back and say the evidence is insufficient. It may refuse.

**The context is minimised.** The task carries the four evidence items and nothing else. Not Priya's original phrasing, not the rest of her conversation, not other shipments she has open, not her credentials. The specialist gets exactly what it needs to adjudicate.

**Northwind's policy does not travel with it.** The adjudication agent applies *finance's* rules and returns a *recommendation*. It has no authority to move money. The ops side retains the decision about whether to act on that recommendation — which is precisely what the diagram shows by placing DOMAIN + POLICY after the specialist rather than inside it.

The specialist returns an artifact: **eligible, recommended credit $340, reasoning cites the hub dwell breach as outside the force majeure carve-out, flags the two prior credits as a relationship risk for human attention.**

### Stage 5 — Domain + Policy

Now something wants to change. The five stages have produced a recommendation; issuing the credit is a write against the billing ledger.

This is where the safe side-effect pipeline applies in full:

![Four numbered panels — CONFIRM, AUTHORIZE, IDEMPOTENCY KEY, CHANGE + RECEIPT — with a SAFE RETRY loop running underneath from the receipt back through a rejected duplicate write.](../diagrams/02-safe-side-effect.png)

Applied to Northwind:

- **Confirm.** Priya sees the recommendation, the evidence, and the relationship flag. She presses approve. The agent does not act on the specialist's recommendation by itself.
- **Authorize.** Priya's role permits credits up to $500. At $340 this passes. At $900 it would have routed to a supervisor — and the policy check would have refused, regardless of what the specialist recommended or what Priya clicked.
- **Idempotency key.** The credit is submitted with a key derived from the shipment and the adjudication task. When the billing API times out and the assistant retries, the ledger recognises the key and returns the original result rather than issuing a second $340 credit.
- **Change + receipt.** The ledger is updated and a receipt is written recording the amount, the approver, the adjudication task ID, and the evidence used.

The timeout in the third bullet is not hypothetical. It happened in the second week of the pilot. Because the key was in place, it produced a duplicate-suppressed log line instead of a $680 problem.

### The return path

The dashed line at the bottom of the diagram is, in this project, three concrete things:

1. **Priya sees a confirmation** in the console: what was credited, to whom, against which shipment, citing the adjudication reasoning.
2. **The audit record** links the ledger entry to the adjudication task, the evidence items, and Priya's approval — so a question in March about a credit issued in January can be answered in one query rather than a week of archaeology.
3. **The relationship flag** surfaces on the account, so the third credit in ninety days is visible to whoever handles that customer next.

None of these are the *result* of the request. They are evidence about it. That is why the diagram draws the line dashed and separate from the cyan forward arrows.

### What breaks when a stage is missing

The clearest way to test whether the five stages are real is to remove them one at a time.

**Remove the application agent** — put Priya directly in front of the tools. This is the status quo the project was meant to fix: she does the tab-switching, the assembly, and the reasoning by hand. Works, but slowly, and inconsistently between coordinators.

**Remove MCP capabilities** — let the agent hit the underlying systems directly with credentials. Now every system integration is bespoke, there is no single place to see what the agent is allowed to touch, and the read-only guarantee evaporates because nothing is enforcing it. The capability layer's value is that it is a *chokepoint you can inspect*.

**Remove the specialist** — copy finance's credit rules into the ops assistant. This works for one quarter. Then the rules change, nobody updates the copy, and the assistant confidently issues credits under superseded policy. The specialist boundary exists because the rules belong to someone else and should stay with them.

**Remove domain + policy** — let the assistant write to the ledger directly on the specialist's recommendation. Now an agent issues money based on another agent's opinion with no human in between and no authorization ceiling. This is the failure mode the entire course is organised around preventing.

**Remove the return path** — everything works and nobody can prove it. The first disputed credit becomes an incident. The compliance review that follows finds the system unauditable, and it gets switched off.

The fifth removal is the instructive one, because it is the only failure that is invisible until the day it matters.

---

## Composition

Five cobalt-blue floating platforms sit evenly spaced on a dark midnight-navy background, each carrying one 3D object and titled above in large uppercase white text:

**PERSON → APPLICATION AGENT → MCP CAPABILITIES → A2A SPECIALIST → DOMAIN + POLICY**

Four short, solid cyan arrows connect them left to right at roughly mid-height, stubby and evenly weighted so the eye moves at a constant pace rather than emphasising any one hop.

Beneath the whole row, a dashed teal line runs from under the rightmost platform, travels the full width of the frame, turns upward at the far left, and terminates in an arrowhead pointing into the underside of the PERSON platform.

## Element by element

**PERSON**
A small neutral human figure — dark hair, teal-green top, dark trousers — standing on the platform, facing right toward the rest of the system. Deliberately generic: no desk, no device, no role. At this stage the person is only the origin of intent.

**APPLICATION AGENT**
A 3D application window rendered as a physical object with depth: a blue title bar with three window dots, a left sidebar containing an avatar tile and stacked text lines, and a main area with one large teal content block and several white cards. This is the software the person actually interacts with — the thing that holds the conversation and decides what to do next.

**MCP CAPABILITIES**
A green toolbox with a dark rounded handle, a front latch, and three dark square tiles showing a **plug**, a **gear**, and a **database**. The three icons are shorthand for connect, operate, and read — the classes of thing a capability server exposes. This toolbox means MCP wherever it appears.

**A2A SPECIALIST**
Two cube-headed robots on separate glowing discs, arranged diagonally: a **blue** robot above, a **teal** robot below. Two curved cyan arrows loop between them, one in each direction. The vertical offset and the two-way arrows are what make this read as a peer exchange rather than another link in the chain.

**DOMAIN + POLICY**
Three objects share the final platform: a **stacked blue database** (the system of record), a **coral shield with a white check** (the policy gate), and a **white printed receipt** with blue text lines and a curled bottom edge (the record of what happened).

## Colour and flow semantics

- **Solid cyan arrows** carry forward work — the request travelling outward.
- **The dashed teal line** carries evidence back. Dashed rather than solid because it is not the request returning; it is a record *about* the request.
- **Coral** appears exactly once, on the policy shield. In a diagram containing no failures and no rejections, coral is reserved for the one thing with authority to refuse.
- Everything the agent uses sits *between* the person and the policy layer, never beside or around it.

## How to present it

**Open with the deletion question, not the walkthrough.** Put the diagram up and ask: "which single element could you remove and still have a working system?" Let the room answer. Most people pick the dashed line, because it is the only thing with no label and no icon. Then agree with them — it *is* the one you can remove and still ship — and spend the next ten minutes on why removing it is how these systems die. Starting here means the audit argument lands before anyone has decided the diagram is obvious.

**Then walk the four arrows, not the five boxes.** At each arrow ask three questions and make the room answer them: what crosses here, what can be refused here, and what evidence does this crossing leave behind. The exercise takes about fifteen minutes and it converts a passive slide into a design checklist people can take back to their own systems.

**Use the toolbox and the robots to separate tool from actor.** Point at the toolbox: "this has no opinion." Point at the robots: "this one can say no." Ask what changes about retry logic between the two. This is the highest-value five minutes in the session, because the tool/actor confusion causes more real production incidents than anything else in the diagram.

**Anticipate the two objections.**

*"This looks like a normal service architecture."* Correct, and that is the point — the novelty is not the topology, it is that one of the boxes is non-deterministic and another one is owned by someone else. Ask what a retry means when the callee is a language model.

*"Real requests don't go through all five stages."* Also correct. Show the system map at that point rather than defending the straight line, and let the parallel lanes settle it.

**Close by re-telling it as verbs.** The request journey covers the same architecture as six actions rather than five components:

![Six numbered panels reading ASK, PLAN, RETRIEVE, ACT, DELEGATE, VERIFY, each with an isometric icon, connected by cyan arrows.](../diagrams/05-request-journey.png)

Ask the room to map each verb onto a component in diagram 01. Four map cleanly. Two — **PLAN** and **VERIFY** — have no box of their own, and that gap is the closing point of the session: the two stages with no component are the two where most real failures happen.

**Timing.** Fifteen minutes as a pure opener. Forty-five if you run the four-arrows exercise and the deletion discussion properly, which is the better use of it.

---

## Lab and checkpoint

**Lab:** Draw your own system's architecture on the same five-stage model. Label the four arrows with: what crosses, what can be refused, and what evidence is produced. Identify the two missing stages — planning and verification — and write the artifact or meeting that would make each one visible.

**Checkpoint:** What happens if you remove the dashed return line?

**Answer:** The system still runs, but the person cannot tell a success from a silent failure, nobody can reconstruct why a change was made later, and trust in the system decays because it can never be verified.

## Glossary

- **A2A specialist** — an autonomous agent that can accept, refuse, and work on a delegated task.
- **Application agent** — the software that converses with the person and decides what to do next.
- **Capability** — a tool the agent discovers and invokes through a published contract.
- **Domain + Policy** — the final boundary where changes meet the system of record and rules.
- **MCP capabilities** — the structured tools the agent calls.
- **Person** — the human origin of intent.
- **Policy gate** — the authority that can refuse a proposed change.
- **Receipt** — the durable evidence of what was done.
- **Return line** — the dashed path that carries evidence about the request back to the person.

## Sources

- MCP and A2A architecture overview
- Agent system boundary and evidence design
- Audit and return-path patterns in service architecture
