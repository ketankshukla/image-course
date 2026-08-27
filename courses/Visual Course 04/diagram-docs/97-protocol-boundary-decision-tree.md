# Diagram 97 — Protocol Boundary Decision Tree

![A decision tree on dark navy. A top banner reads WHO OWNS THE OTHER SIDE with a person glyph. Four cyan arrows descend to four white cards — SAME PROCESS with two people, APP TO CAPABILITY SERVER with servers, AGENT TO INDEPENDENT AGENT with a robot, AGENT TO USER INTERFACE with a monitor. Each leads down to a labelled outcome — INTERNAL FUNCTION, MCP, A2A, AG-UI. All four route into a wide coral banner reading DO NOT STACK PROTOCOLS WITHOUT A REAL BOUNDARY.](../diagrams/97-protocol-boundary-decision-tree.png)

**Module:** Choosing boundaries
**Role in the course:** which protocol, and when none
**Layout:** one question, four branches, four outcomes, one prohibition beneath

---

## At a glance

One question — **WHO OWNS THE OTHER SIDE** — with four answers, each producing a different protocol. And beneath all four, a coral banner: **DO NOT STACK PROTOCOLS WITHOUT A REAL BOUNDARY.**

The question is about **ownership**, and the fourth option is that there is no other side at all — in which case the answer is an internal function and no protocol.

---

## What the diagram teaches

### 1. The question is about ownership, and it is the only question

Not "which protocol should we use." Not "what does this feature need." **Who owns the other side.**

Ownership determines everything downstream: who deploys it, who is on call for it, who decides its interface, who is accountable when it is wrong.

If the answer is "we do, in this process," there is no boundary to cross and no protocol to speak. If the answer is "someone else," the nature of that someone determines which protocol.

Starting from the technology question produces teams that adopt a protocol and then look for boundaries to justify it.

### 2. Four answers, and the first one is the most important

**SAME PROCESS → INTERNAL FUNCTION.**

Listed first, drawn with two people (the same team), and terminating in a plain function call.

A great deal of what gets built as a protocol integration is a function that somebody wrapped because a protocol was on the roadmap.

The cost of wrapping a same-process call in a protocol: serialisation, a network hop, a new failure mode, a schema to version, and a boundary to secure — in exchange for nothing, because the two sides deploy together and are owned by the same team.

The diagram giving this the leftmost position and the plainest outcome is an editorial choice worth pointing at.

### 3. APP TO CAPABILITY SERVER → MCP

The second answer. An application needs a bounded thing done by a system it does not own.

The word **capability** is precise. Not "another service" and not "another team's code" — a *capability server*, which is a thing that exposes tools, resources and prompts under a contract.

MCP is the answer when the other side is passive: it does what you ask and has no view about whether you should have asked.

### 4. AGENT TO INDEPENDENT AGENT → A2A

The third answer, and the word **independent** carries it.

Not "another agent" — an **independent** one. It has its own owner, its own rules, its own judgement, and its own decision about whether to accept your work.

The distinction from MCP: a capability server executes; an independent agent decides. You send a task, not a call, and what comes back may be a refusal.

### 5. AGENT TO USER INTERFACE → AG-UI

The fourth answer. The other side is a person, mediated by an interface.

That is a genuinely different boundary from the other three. The other side is not a system with a contract; it is a human with attention, patience, and the ability to intervene.

AG-UI exists because streaming progress, surfacing artifacts, and accepting interrupts are a distinct set of concerns that neither MCP nor A2A addresses.

### 6. The coral banner is the diagram's warning, and it names a real failure

**DO NOT STACK PROTOCOLS WITHOUT A REAL BOUNDARY.**

All four outcomes route into it, including the internal function — which is the tell. Even the no-protocol answer is subject to the warning, because the temptation is to add one.

What stacking means in practice: wrapping an internal function in MCP, then exposing that MCP server through an A2A agent, then surfacing that agent through AG-UI — when all four layers are owned by the same team, deployed together, and separated by no boundary anyone can point at.

Each layer adds serialisation, latency, a failure mode, a schema, and a security surface. The justification for each is that the layer beneath it exists.

### 7. A real boundary has three properties, and the diagram implies them

The banner says *real boundary* without defining it. Worth supplying:

**Different owner.** Someone else decides what it does.

**Independent deployment.** It ships on its own schedule, and you cannot change both sides atomically.

**A contract you cannot unilaterally change.** Changing the interface requires agreement.

If all three are absent, the boundary is decorative and the protocol is overhead.

If one or two are present, it is worth thinking about — a boundary that is currently internal may be about to become external, and building for that can be right.

Where a boundary is real, what crosses it needs an adapter and a declared contract:

![An orchestrator feeding an MCP adapter and an A2A adapter, with a correlation spine listing five identifiers beneath and coral LOSSY MAPPINGS warnings dropping from each contract map.](../diagrams/98-adapter-correlation-contract.png)

That is the cost of a real boundary, and it is worth paying only where one exists. Each adapter is a contract map, a correlation obligation and a declared set of losses — which is a great deal to accept for a call you could have made directly.

---

## Case study — Netherby Software, four protocols and one team

Netherby builds a compliance monitoring product for financial firms. Their engineering team is 22 people.

They adopted MCP, A2A and AG-UI over eighteen months, and by the end had all three in a system where none of them crossed a real boundary.

### How it happened

Reasonably, one step at a time.

**MCP first.** They had a set of internal functions — rule evaluation, data lookup, report generation — and wrapped them in an MCP server so their agent could call them as tools.

Both sides were the same codebase, deployed together, owned by the same six people.

**A2A second.** One category of work — adverse-media screening — felt specialised, so they built it as a separate agent and integrated over A2A.

The screening agent was in the same repository, deployed by the same pipeline, maintained by the same team.

**AG-UI third.** Correct, and the only one that was.

### The cost

Their compliance check ran through four layers.

A user action in the interface produced an AG-UI event. The orchestrator issued an A2A task to the screening agent. The screening agent made MCP tool calls. The MCP server invoked internal functions.

**Median latency: 3.4 seconds**, of which their own measurement attributed about 2.1 to serialisation, transport and protocol handling across the three boundaries.

**Four schemas to version.** A change to a rule evaluation function required changes to the MCP tool schema, sometimes to the A2A task shape, and sometimes to the AG-UI event type. A one-line logic change became a four-file change.

**Debugging across four layers.** A wrong result meant tracing through four protocol boundaries, each with its own logging format.

**Three security surfaces** that were, on inspection, three implementations of the same authorisation check against the same identity.

### The audit

A new principal engineer asked the ownership question of each boundary.

**AG-UI → orchestrator.** Other side is a user in a browser. Different trust domain, cannot be changed atomically. **Real boundary.** Keep.

**Orchestrator → screening agent (A2A).** Same team, same repository, same deploy. No independent owner, no independent deployment, no contract that could not be changed unilaterally. **Not a real boundary.**

**Screening agent → MCP server.** Same repository, same deploy, same team. **Not a real boundary.**

**MCP server → internal functions.** Literally function calls behind a protocol. **Not a real boundary.**

Three of four.

### What they removed

**The MCP layer went first**, replaced by direct function calls. Two weeks. Latency dropped about 700ms.

**The A2A layer went second.** The screening agent became a module. Three weeks, mostly untangling the task lifecycle handling that had been built around the delegation.

**AG-UI stayed**, unchanged.

### Results

- **Median latency:** 3.4s → 1.1s.
- **Files touched by a typical rule change:** 4 → 1.
- **Authorisation implementations:** 3 → 1.
- **Lines of code:** down about 11,000, net.

### The part that was not a simplification argument

Their review also identified **one boundary that should exist and did not**.

Their rule evaluation logic is maintained by a compliance team of four people who are not engineers. They specify rules; engineers implement them.

That is a real ownership boundary — different owner, different competence, different change cadence — and it was expressed as a code review process rather than as an interface.

They built it as a rule definition service with a contract. Compliance now changes rules without an engineering release.

**That is the diagram used correctly.** Three protocols removed because no boundary existed, and one interface created because a boundary did.

### The rule they adopted

Every proposed protocol boundary must answer three questions in writing:

*Who owns the other side?*
*Can it deploy independently?*
*Could we change both sides atomically if we wanted to?*

Three noes means no boundary and no protocol.

### The line in their architecture guidance

*A protocol is what you use when you cannot just call the function. If you can just call the function, call the function.*

---

## Composition

A three-tier decision tree with a prohibition banner beneath.

**Top:** a wide blue banner with a white person glyph, reading **WHO OWNS THE OTHER SIDE**.

**Second tier:** four **cyan arrows** descend to four white cards on blue hexagonal platforms — **SAME PROCESS** (two blue people), **APP TO CAPABILITY SERVER** (blue server stack), **AGENT TO INDEPENDENT AGENT** (blue robot), **AGENT TO USER INTERFACE** (blue monitor).

**Third tier:** a **cyan arrow** from each card down to an outcome on a blue platform — **INTERNAL FUNCTION** (teal node diagram), **MCP** (teal node graph), **A2A** (two teal robots with circulating arrows), **AG-UI** (teal interface grid).

**Bottom:** **cyan arrows** from all four outcomes route into a wide **coral banner** with a white warning triangle, reading **DO NOT STACK PROTOCOLS WITHOUT A REAL BOUNDARY**.

## Element by element

**WHO OWNS THE OTHER SIDE** — a blue banner with a white person glyph. The only question.

**SAME PROCESS** — two blue person glyphs. → **INTERNAL FUNCTION**, a teal connected-nodes glyph.

**APP TO CAPABILITY SERVER** — a blue stacked server. → **MCP**, a teal node graph.

**AGENT TO INDEPENDENT AGENT** — a blue robot face. → **A2A**, two teal robots with circulating arrows.

**AGENT TO USER INTERFACE** — a blue monitor with content blocks. → **AG-UI**, a teal interface grid.

**The prohibition banner** — a wide coral panel with a white warning triangle.

## Colour and flow semantics

- **Cyan arrows** carry the decision down through all three tiers and into the banner.
- **Blue** marks the question and the four situations; **teal** marks the four outcomes.
- **Coral** appears once, on the banner, which receives from all four branches — including the no-protocol one.
- The four branches are given **identical treatment**, refusing to present any as the default.

## How to present it

**Ask the question and insist on the wording.** Not "which protocol" — who owns the other side. Then ask what ownership means: who deploys it, who is on call, who decides its interface.

**Point at the leftmost option.** Same process, internal function, no protocol. Ask how much of what the room has built as an integration is this.

**Walk the three protocol answers and stress the distinguishing word in each.** *Capability* server — passive, does what you ask. *Independent* agent — has its own judgement and can refuse. *User* interface — a person with attention and the ability to intervene.

**Ask what makes a boundary real.** Supply the three properties: different owner, independent deployment, a contract you cannot unilaterally change. Then ask the room to test one of their own boundaries against all three.

**Tell the Netherby stack.** Four layers, one team, one repository, one deploy pipeline. 3.4 seconds median, 2.1 of it protocol handling. A one-line rule change touching four files.

**Walk their audit.** Three of four boundaries were not real. Then give the outcome: 3.4s → 1.1s, four files → one, three authorisation implementations → one, 11,000 lines removed.

**Then give the other half.** They found a boundary that *should* have existed — compliance staff who specify rules, expressed as a code review process rather than an interface. Building it let compliance change rules without an engineering release.

**Make that the point.** The diagram is not an argument against protocols. It is an argument for putting them where boundaries are, which means removing them where boundaries are not and adding them where boundaries are unserved.

**Give them the three questions.** Who owns the other side, can it deploy independently, could we change both sides atomically. Three noes means no protocol.

**Close on the guidance line.** *A protocol is what you use when you cannot just call the function.*

**Timing.** Twenty minutes. Thirty if you test the room's own boundaries against the three properties, which usually finds at least one decorative layer.

---

## Lab and checkpoint

**Lab:** List four internal or external boundaries in your architecture. For each, test the three properties: different owner, independent deployment, and a contract you cannot change unilaterally. Classify each as same-process, MCP, A2A, or AG-UI, and identify any decorative protocol layer that should be removed or any missing boundary that should get a protocol.

**Checkpoint:** What makes a boundary real enough to justify a protocol?

**Answer:** A real boundary has three properties: the other side is owned by a different party, it can be deployed independently, and the contract between you cannot be changed by one side alone. If all three are true, a protocol is appropriate. If not, an internal function call is usually better.

## Glossary

- **A2A** — the protocol for agent-to-agent communication across independent agents.
- **AG-UI** — the protocol for agent-to-user-interface communication.
- **Boundary** — the edge between two systems or owners.
- **Capability server** — a passive server that does what the client asks.
- **Contract** — the agreed interface that cannot be unilaterally changed.
- **Decorative protocol** — a protocol used where there is no real boundary.
- **Independent agent** — an agent with its own judgement that can refuse work.
- **MCP** — the protocol for an app to call a capability server.
- **Ownership** — who deploys, runs, and decides the interface of the other side.
- **Protocol** — the communication rules used when a boundary is real.

## Sources

- MCP, A2A, and AG-UI protocol roles
- Boundary-driven protocol selection
- Architecture simplification and real versus decorative boundaries
