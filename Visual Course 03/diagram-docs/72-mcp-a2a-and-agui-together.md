# Diagram 72 — MCP, A2A, and AG-UI Together

![Three horizontal lanes on dark navy, each with a labelled block at the left and an outcome card at the right. AG-UI USER EXPERIENCE runs USER, REACT APP, EVENTS, SHARED STATE, INTERRUPTS to USER SEES PROGRESS. A2A AGENT COLLABORATION runs ORCHESTRATOR AGENT, SPECIALIST AGENT, TASK, ARTIFACT to AGENTS SHARE WORK. MCP TOOLS AND CONTEXT runs MCP CLIENT, MCP SERVER, TOOL, RESOURCE to TOOLS DO BOUNDED ACTIONS. A teal return line runs beneath each lane back to its start.](../diagrams/72-mcp-a2a-and-agui-together.png)

**Module:** The complete system
**Role in the course:** how the three protocols divide the work
**Layout:** three parallel lanes, each with its own stages and its own outcome statement

---

## At a glance

Three lanes, three protocols, three one-line outcomes:

**AG-UI → USER SEES PROGRESS.** **A2A → AGENTS SHARE WORK.** **MCP → TOOLS DO BOUNDED ACTIONS.**

The lanes are parallel and separate. None feeds into another. That geometry is the argument: these are three different concerns operating at three different levels, and a production system runs all three simultaneously rather than choosing between them.

---

## What the diagram teaches

### 1. Three lanes, three questions, three audiences

**AG-UI answers: what does the person see while this is happening?** Its stages are all about the interface — events, shared state, interrupts. Its audience is a human watching.

**A2A answers: how does work move between agents?** Orchestrator, specialist, task, artifact. Its audience is another agent.

**MCP answers: how does an agent do a bounded thing to a system?** Client, server, tool, resource. Its audience is a capability provider.

They do not compete because they do not overlap. A request can involve all three: the user watches progress (AG-UI) while an orchestrator delegates to a specialist (A2A) which calls a tool (MCP).

### 2. The lane order is top to bottom by proximity to the human

AG-UI at the top, A2A in the middle, MCP at the bottom.

That ordering is not arbitrary. It runs from **closest to the person** to **furthest from them**.

The user interacts with AG-UI directly. A2A is machinery they never see. MCP is machinery that the machinery uses.

Reading it as a stack is useful: each lane is served by the one below it. The UI shows progress *of* agent work; agent work is performed *using* tools.

### 3. Each lane has its own return path, and they are separate

Beneath each lane, a **teal line** runs back from the outcome to the lane's first stage.

Three separate returns, not one shared one. Each lane closes its own loop:

- AG-UI returns rendered state to the user.
- A2A returns artifacts to the orchestrator.
- MCP returns results to the client.

Drawing them separately says each protocol is responsible for its own round trip. A failure in the MCP lane produces an MCP-level error that the A2A lane must handle; it does not propagate raw to the user.

### 4. AG-UI's stages name what a progress interface actually needs

**USER → REACT APP → EVENTS → SHARED STATE → INTERRUPTS → USER SEES PROGRESS.**

Three of those are worth separating.

**EVENTS** — a stream of things that happened, ordered. Not a final response; a sequence the interface can render as it arrives.

**SHARED STATE** — a synchronised view. The client and the server agree on what the current state is, which is what allows a reconnecting client to catch up rather than restart.

**INTERRUPTS** — drawn with a **coral badge**, the only coral in the diagram. The user can intervene: approve, redirect, cancel. This is the stage that makes the interface bidirectional rather than a progress display.

An interface with events but no interrupts shows the user what is happening and gives them no way to affect it.

What those events actually look like is the subject of its own diagram:

![Eight numbered event types — RUN STARTED, STEP STARTED, TEXT DELTA, TOOL CALL STARTED, TOOL CALL RESULT, STATE SNAPSHOT, ARTIFACT READY, RUN FINISHED — funnelling into a React reducer and fanning out to five UI surfaces, with a coral RECONNECT path resuming after the last event.](../diagrams/73-typed-agent-event-stream.png)

The **STATE SNAPSHOT** event there is this lane's **SHARED STATE** stage, and the reconnect path is what makes it worth having.

### 5. A2A's four stages are the object model, compressed

**ORCHESTRATOR AGENT → SPECIALIST AGENT → TASK → ARTIFACT.**

Two parties and two objects. The orchestrator holds the overall work; the specialist does a bounded piece of it; the task is what crosses between them; the artifact is what comes back.

Note the ordering: task and artifact appear **after** both agents, as products of the relationship rather than as stages the agents pass through. The task is the thing handed over; the artifact is the thing returned.

### 6. MCP's four stages separate the two primitives

**MCP CLIENT → MCP SERVER → TOOL → RESOURCE.**

Tool and resource are drawn as separate stages, not as one "capability" box.

The distinction is the one from the primitives model: a **tool** does something and may have effects; a **resource** is addressable content that is read. Different caching, different permissions, different risk.

The outcome card says **TOOLS DO BOUNDED ACTIONS** — bounded being the operative word, and the subject of the least-privilege diagram earlier in this volume.

### 7. The three outcome cards are the takeaway

**USER SEES PROGRESS. AGENTS SHARE WORK. TOOLS DO BOUNDED ACTIONS.**

Nine words that cover what each protocol is for. A learner who holds those three sentences can place almost any design question in the right lane.

The common confusions the three sentences resolve:

- *Should we use A2A to call our pricing service?* No — a service call is a bounded action. MCP.
- *Should we stream tool results to the user over MCP?* No — showing a user progress is AG-UI's job.
- *Should the UI talk directly to the specialist agent?* No — the orchestrator owns the work; the UI observes it.

---

## Case study — Halden Freight, three protocols and one screen

Halden arranges international shipping for about 700 exporters. They built a booking desk where an operator submits a shipment and watches it being processed: rates checked, customs classification determined, capacity confirmed, documents generated.

The whole flow takes between 40 seconds and four minutes.

### What they built first

One protocol for everything.

Their first version used MCP for all of it — including the customs classification, which was performed by a specialist system owned by their compliance team, and including streaming progress to the operator's screen.

Three problems, one per lane.

**The UI lane did not exist.** Progress reached the operator as a series of tool results rendered as they arrived. There was no notion of shared state, so a browser refresh lost everything and the operator had to start again. There was no interrupt mechanism, so an operator who realised mid-flow that they had entered the wrong port had to wait for completion and then cancel.

**The A2A lane was modelled as a tool call.** Customs classification is judgement work owned by another team, takes 20–90 seconds, and sometimes needs a clarifying question. As a tool call it had no task identity, no way to pause for input, and no artifact — it returned a string.

**The MCP lane was fine**, and was doing three jobs.

### The rebuild across three lanes

**MCP for bounded actions.** Rate lookup, capacity check, document generation, port and vessel data. All fast, all deterministic, all bounded. Fourteen narrow tools.

**A2A for customs classification.** The compliance team's agent receives a task carrying the shipment details and the goods description, and returns an artifact: the commodity code, the duty rate, the reasoning, and any flags. It can move to an input-required state when the description is ambiguous, which happens on about 28% of shipments.

That last capability was impossible under the tool-call design and it is the reason 47 shipments a year had previously been held at customs.

**AG-UI for the operator's screen.** Events stream as the booking progresses. Shared state means a refresh resumes rather than restarts. Interrupts let the operator cancel or amend mid-flow.

### What the interrupt capability changed

The operator screen now offers three interventions during a booking: **cancel**, **amend a field**, and **answer** a pending classification question.

The third is the one that mattered. Under the old design, an ambiguous goods description meant the classification tool guessed. Now the booking pauses, the operator sees the question on the same screen they are already watching, and answers it in a few seconds.

Median time in the input-required state: **40 seconds**, because the operator is already looking at the screen. The pause costs almost nothing and it removed the guessing entirely.

### The lane separation in their incident handling

Six months in, their rate-lookup provider had an outage.

The MCP lane failed. Because the lanes were separate, the failure surfaced as an MCP-level error that the orchestrator handled — it retried, then routed the booking to a fallback rate source, then reported a degraded-rate warning through the AG-UI lane.

The operator saw: *"Live rates unavailable — using contracted rates. This booking may need a rate review."*

Under the single-protocol design, a tool failure had propagated raw to the screen as a stack trace, and operators had learned to refresh and retry, which restarted the whole booking.

### Results

- **Shipments held at customs for misclassification:** 47/year → 3.
- **Bookings restarted due to refresh or error:** ~120/month → under 5.
- **Median booking time:** 3.1 minutes → 1.9, mostly from parallelising MCP calls once they were separated from the UI stream.
- **Operator-reported "had to start again":** eliminated as a category.

### How their team explains it to new engineers

*Three questions. What is the person seeing? Who else is doing work? What bounded thing are we asking a system to do? Different answers, different protocols, all at once.*

---

## Composition

Three horizontal lanes, each structured identically.

**Left:** a bordered block naming the protocol and its role — **AG-UI / USER EXPERIENCE**, **A2A / AGENT COLLABORATION**, **MCP / TOOLS AND CONTEXT**.

**Centre:** the lane's stages on blue platforms, connected by cyan arrows.

**Right:** a white outcome card with a teal circular icon and a two- or three-word statement.

**Beneath each lane:** a **teal line** running back from the outcome card to the lane's first stage.

## Element by element

**AG-UI lane**
**USER** (teal person figure) → **REACT APP** (browser window with a React atom) → **EVENTS** (calendar with a bell) → **SHARED STATE** (database with a share glyph) → **INTERRUPTS** (**coral speech bubble with an exclamation**) → **USER SEES PROGRESS** (teal eye).

**A2A lane**
**ORCHESTRATOR AGENT** (teal robot head) → **SPECIALIST AGENT** (blue robot head) → **TASK** (white card headed **TASK** with three green-ticked rows) → **ARTIFACT** (document emerging from a teal tray) → **AGENTS SHARE WORK** (teal group glyph).

**MCP lane**
**MCP CLIENT** (teal terminal tile showing `>_`) → **MCP SERVER** (blue server stack) → **TOOL** (white card with a teal wrench) → **RESOURCE** (teal folder with documents) → **TOOLS DO BOUNDED ACTIONS** (teal shield with a check).

## Colour and flow semantics

- **Cyan arrows** carry each lane's sequence left to right.
- **Teal return lines** beneath each lane close three separate loops.
- **Coral** appears exactly once, on **INTERRUPTS**, marking it as the point where a human can intervene.
- **Teal** dominates the AG-UI and MCP lanes; the A2A lane uses **teal and blue robots** to distinguish the two parties.
- The three lanes are **parallel and unconnected**, which is the diagram's structural claim.

## How to present it

**Read the three outcome cards aloud.** User sees progress. Agents share work. Tools do bounded actions. Nine words, and they resolve most protocol-choice arguments.

**Ask why the lanes do not connect.** Three concerns at three levels, all running at once. Then ask the room to describe a single request in their system and identify what is happening in each lane simultaneously.

**Point out the top-to-bottom ordering.** Closest to the human, then further, then furthest. Each lane is served by the one below it.

**Run the three confusions.** Should we use A2A to call our pricing service? Should we stream tool results over MCP? Should the UI talk to the specialist directly? Each has an obvious answer once the three sentences are in place, and each is a real mistake teams make.

**Point at the coral INTERRUPTS badge.** The only coral in the diagram. Ask what an interface with events but no interrupts is — a progress display. Then ask what their users can do while work is in flight. Usually nothing.

**Ask what SHARED STATE buys.** A reconnecting client catches up rather than restarts. Then give them Halden's number: 120 restarted bookings a month, from refreshes and errors, down to under 5.

**Tell the Halden customs story.** Classification modelled as a tool call had no task identity, no pause state, and no artifact. As an A2A task with input-required, it pauses and the operator answers in 40 seconds — because they are already watching the AG-UI stream. Three lanes cooperating.

**Use the outage story for lane separation.** An MCP failure handled at the A2A level and reported through AG-UI as a degraded-rate warning, rather than a stack trace on the operator's screen. Separated lanes mean a failure surfaces at the right level.

**Close with the three questions.** What is the person seeing? Who else is doing work? What bounded thing are we asking a system to do?

**Timing.** Twenty minutes. Thirty if you trace one of the room's own requests through all three lanes, which usually reveals a missing one.

---

## Lab and checkpoint

**Lab:** Trace one real user request through the three lanes. For the AG-UI lane, write what the user sees and which interrupts are possible. For the A2A lane, write which agents collaborate and what task and artifact they exchange. For the MCP lane, write which tool, resource, and bounded action is used. Identify any lane that is missing or misused.

**Checkpoint:** Why are the three lanes unconnected?

**Answer:** Because they are three separate concerns at three levels: user experience, agent collaboration, and bounded tool actions. Each lane can run simultaneously and fail at its own level. Mixing them produces protocol-choice mistakes such as calling a service over A2A or streaming tool results over MCP.

## Glossary

- **A2A lane** — the agent-to-agent collaboration lane.
- **AG-UI lane** — the user-experience lane with progress, shared state, and interrupts.
- **Bounded action** — a tool call with a narrow, well-defined effect.
- **Interrupt** — the point where a human can intervene while work is in flight.
- **MCP lane** — the lane for calling tools and retrieving resources.
- **Orchestrator agent** — the agent that coordinates the work.
- **Shared state** — the state that lets a reconnecting client catch up.
- **Specialist agent** — the agent that receives a delegated task and returns an artifact.
- **Task** — the A2A work object with an identity and lifecycle.

## Sources

- AG-UI, A2A, and MCP protocol roles
- Multi-lane user experience and agent coordination
- Shared state, interrupts, and progress streaming
