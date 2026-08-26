# Diagram 06 — Protocol Comparison

![Four tall panels on dark navy reading RAG = KNOWLEDGE with books and a database, MCP = CAPABILITIES with a toolbox fanning out to three surfaces, A2A = AGENT WORK with two robots exchanging arrows, and ACP = HISTORY rendered as a faded sepia blueprint on a grey plinth.](../diagrams/06-protocol-comparison.png)

**Module:** 1 — See the whole system
**Role in the course:** interview-ready acronym comparison
**Layout:** four side-by-side definition panels

---

## At a glance

Four acronyms, four one-word definitions. **RAG = KNOWLEDGE. MCP = CAPABILITIES. A2A = AGENT WORK. ACP = HISTORY.**

Three of the panels are built in the same bright isometric style as the rest of the library. The fourth is not — it is a faded, sepia-toned rolled blueprint on a grey plinth, drawn in dashed coral outlines, with an arrow leaving its right edge. That styling difference is the diagram's most efficient piece of teaching: it tells you ACP's status before you have read a word.

---

## What the diagram teaches

### 1. One word each, and the words are chosen carefully

The value of this diagram is that it refuses to elaborate. Four acronyms, four nouns. Anyone who can hold these four words and use them correctly can navigate almost any conversation about agent architecture.

**KNOWLEDGE.** Not "search," not "documents," not "vector databases." Knowledge is the *thing you get*, and it is deliberately technology-free — the definition survives you swapping out the embedding model, the index, or the chunking strategy.

**CAPABILITIES.** Not "tools," not "APIs," not "function calling." Capabilities is broader and more accurate: it covers the things you can do, the things you can read, and the guidance on how to do them. The three-part structure behind that word is the subject of the primitives diagram.

**AGENT WORK.** Two words, and both are necessary. Not "agent communication," which suggests chat. Not "multi-agent," which suggests a topology. *Work* is the unit: something bounded, delegable, and completable, that produces an artifact.

**HISTORY.** Not "deprecated," not "obsolete," not "don't use." History is a status with dignity — it says the ideas mattered and their lineage is worth knowing, while being unambiguous that it is not a build target.

### 2. Three of these are complementary; the fourth is on a different axis

The most common misreading of this diagram is that it presents four options to choose between. It does not. The first three are complementary — a serious system uses all three — and the fourth is not an option at all.

RAG, MCP and A2A answer different questions and do not compete. You do not pick between knowing things, doing things, and delegating things. You need all three, and the design question is which one owns each unit of work.

ACP sits on a different axis entirely: it is a point in time, not a choice in a design space. Including it in a comparison of four panels is a slight abuse of the format, done deliberately, because the acronym still circulates and people need to be told where to file it.

### 3. Each panel's icon defines the term better than its label

Look at what each panel shows rather than what it says.

**RAG** shows books and documents with an arrow pointing *down into* a database that displays a node graph. The direction is the definition: source material goes in, becomes structured, and sits there. Retrieval is reading from a thing someone prepared earlier. Nothing in this panel moves outward.

**MCP** shows a toolbox with three arrows fanning *down and outward* to three different surfaces — a UI window, a code editor, and an analytics dashboard. Outward, and to multiple different consumers. This is the panel that captures why MCP exists: one catalogue, many clients. The same capability server serves the app, the IDE, and the dashboard.

**A2A** shows two robots exchanging arrows in *both directions*, with a checklist card floating above and a teal cube below. Bidirectional, with a task above and an artifact below. Every structural element of the A2A model is in that small composition.

**ACP** shows a rolled blueprint with a sketched diagram on it — dashed lines, plan symbols, no built structure — and an arrow leaving the panel to the right. Ideas, drawn but never constructed here, moving onward.

### 4. The styling of the fourth panel is the argument

Everything about the ACP panel is different: desaturated sepia instead of saturated blue-teal, a grey plinth instead of a glowing cobalt platform, dashed coral outlines instead of solid forms, paper instead of built objects, and a coral heading where the others are cyan.

None of that is decorative. In a library where colour carries meaning consistently, coral means "risk, rejection, retired," and this is the only whole panel rendered in it.

The arrow leaving the right edge is the redeeming detail. It stops the panel from reading as a dead end. ACP's ideas were not wrong and did not vanish — they moved into A2A. The timeline diagram makes that explicit as a river flowing from one into the other.

### 5. It is an interview aid, and that is a real use

The course guide describes this as interview-ready, and it is worth taking that literally. These four words are the ones that come up when someone is asked to explain modern agent architecture under pressure.

Four things go wrong in that conversation, and this diagram fixes all four:

- **Conflating RAG and MCP.** "We use RAG to get data from our systems." Live system data is a capability. RAG is for the corpus.
- **Conflating MCP and A2A.** "We use A2A to call the pricing service." Calling a service is a capability. A2A is for handing work to something with judgement.
- **Treating multi-agent as a goal.** A2A is a boundary you use when work genuinely belongs elsewhere, not an architecture badge.
- **Citing ACP as current.** Anyone who names ACP as something they are building on has learned from material that has not been updated.

Being able to say "RAG is knowledge, MCP is capabilities, A2A is agent work, ACP is history" and then defend each in a sentence is a complete answer.

---

## Case study — Kestrel Logistics, the integration inventory

Kestrel is a freight and warehousing company with an internal platform team of about thirty. Over eighteen months, various squads had built agent features independently. Nobody had a list.

The platform team ran a two-week inventory to find out what existed, and used these four words as the sorting scheme. They found twelve integrations. Three were misclassified, and each misclassification had produced a specific, ongoing problem.

### What they found

**Correctly built as RAG (four integrations).** The safety handbook, the customs documentation corpus, the carrier contract library, and the resolved-ticket archive. All static-ish text, all changing on a scale of weeks to months, all correctly indexed. No issues.

**Correctly built as MCP (five integrations).** Shipment lookup, carrier tracking, warehouse stock levels, the rate calculator, and the customer record read. All live state behind contracts. One had a rate-limiting problem; otherwise sound.

**Correctly built as A2A (zero integrations).** They had none. This was itself a finding — two of the misclassifications should have been.

**Misclassified (three integrations).** These are the interesting ones.

### Misclassification 1 — live state indexed as knowledge

The **warehouse capacity assistant** answered questions like "can we take another forty pallets at Wakefield this week?" It was built as RAG over a nightly export of capacity data.

Capacity changes hourly. The index was up to twenty-three hours stale. The assistant had been confidently telling planners there was room when there was not, roughly twice a week, and the planners had learned to double-check it — which meant it was providing no value while consuming a nightly pipeline.

**Diagnosis:** this is a capability. It changes far faster than the ingestion cycle. **Fix:** a `get_capacity(site, date_range)` tool against the warehouse system. The nightly export was deleted.

### Misclassification 2 — a document corpus behind a tool call

The **customs classification helper** suggested commodity codes for goods being shipped. It was built as an MCP tool that returned the relevant section of the tariff schedule.

The tariff schedule is enormous. The tool returned large blocks of text, which consumed most of the context window, and it could only return the section for a code you already knew — which was useless, because knowing the code was the question.

**Diagnosis:** this is knowledge. A large, slowly-changing corpus where the access pattern is semantic search, not lookup by key. **Fix:** ingested, chunked and indexed, with retrieval over descriptions. The helper went from unusable to the team's most-used feature within a month.

### Misclassification 3 — someone else's judgement pasted into a prompt

The **dangerous goods checker** determined whether a shipment required hazardous-materials handling. It was implemented as a prompt inside the shipping assistant, containing a summarised version of the DG classification rules.

Those rules are owned by Kestrel's compliance team, are legally significant, and change when regulations change. The summary in the prompt was written once, by a developer, from a version of the rules that was by then fourteen months old.

**Diagnosis:** this is agent work. The judgement belongs to compliance, who maintain the rules and are accountable for them. **Fix:** compliance stood up their own adjudication agent. The shipping assistant now sends a task with the shipment details and receives a determination plus a reasoning trace. Their first A2A integration, driven by finding a copy of someone else's rules in a prompt.

### The ACP finding

One squad's design document specified an "ACP-style manifest" for describing their agent's capabilities. The engineer had learned the model from a course written before the A2A merge and had built accordingly — a manifest, a run endpoint, input and output objects.

Nothing was broken. It worked. But it was a private vocabulary that matched nothing anyone else was building, which meant the compliance team's new adjudication agent could not talk to it without a translation layer.

The migration was mostly renaming, which is exactly what the concept map diagram covers:

![Five coral pills on the left labelled MANIFEST, RUN, INPUT, OUTPUT, STATUS with arrows to five teal pills on the right labelled AGENT CARD, TASK, MESSAGE, ARTIFACT, TASK STATE, under headers reading OLD TERMS and CURRENT MODEL.](../diagrams/26-acp-a2a-concept-map.png)

Manifest became an agent card, run became a task, input became a message, output became an artifact, status became task state. Two days of work. The engineer's mental model was sound; only the names and a few shapes were out of date.

### What the exercise cost and returned

Two weeks of one person's time to inventory twelve integrations. It found a stale nightly pipeline to delete, a useless feature to rebuild, a fourteen-month-old copy of regulated rules that nobody knew existed, and a vocabulary mismatch that would have surfaced later as an integration failure.

The sorting scheme was four words. That is the argument for this diagram.

---

## Composition

Four tall panels of equal size sit side by side. Each has a heading combining the acronym in colour with its definition in white:

**RAG = KNOWLEDGE** · **MCP = CAPABILITIES** · **A2A = AGENT WORK** · **ACP = HISTORY**

The first three acronyms are set in cyan. The fourth, ACP, is set in coral.

## Element by element

**RAG = KNOWLEDGE**
Books and documents grouped on a platform, with an arrow pointing down into a stacked blue database displaying a teal node graph. Inward and downward — source material becoming structured storage.

**MCP = CAPABILITIES**
The green toolbox with plug, gear and database tiles, with three arrows fanning down and outward to three separate surfaces: a UI window with an avatar, a dark code editor showing `</>`, and an analytics dashboard with a pie chart and bars. One catalogue, several different consumers.

**A2A = AGENT WORK**
A blue cube robot and a teal cube robot with cyan arrows running between them in both directions, a checklist card with three green ticks floating above, and a small teal cube below. Task above, artifact below, conversation between.

**ACP = HISTORY**
A rolled sepia blueprint on a grey plinth. The drawing on it is rendered in dashed coral outlines — boxes, circles and a cylinder connected by dashed lines, in the manner of a plan rather than a built thing. A teal arrow leaves the right edge of the panel.

## Colour and flow semantics

- **Cyan headings** for the three current concepts; **coral heading** for the retired one.
- The ACP panel is the only element in the library rendered in desaturated sepia on a grey plinth rather than saturated colour on a cobalt platform. Given how consistently the palette is used elsewhere, that difference alone communicates its status.
- Arrow direction differs meaningfully per panel: **inward** for RAG, **outward and fanning** for MCP, **bidirectional** for A2A, **exiting the frame** for ACP.

## How to present it

**Give them the four words before anything else.** Say them, have the room say them back, and only then discuss. "RAG is knowledge, MCP is capabilities, A2A is agent work, ACP is history." The compression is the product.

**Then attack each definition.** Ask what is wrong with each of these statements and let the room correct them:

- "We use RAG to look up a customer's current balance." *(Live state — that is a capability.)*
- "We use A2A to call our pricing service." *(A call, not a delegation — that is a capability.)*
- "We're multi-agent, so we use A2A everywhere." *(A2A is a boundary, not a badge.)*
- "We're building on ACP." *(You are building on history — your source material is out of date.)*

Four sentences, four misconceptions, five minutes. This is the fastest diagnostic in the course.

**Do the icon reading.** Cover the headings and ask what each panel means from its picture alone. The arrow directions give it away — inward, outward, bidirectional, exiting — and once someone notices that, the four definitions stop being arbitrary labels.

**Ask why ACP looks different, and let them answer.** Nobody needs to be told that a faded blueprint on a grey plinth means something is not current. The question is worth asking anyway, because the follow-up — *why an arrow leaving the panel rather than a cross through it?* — gets to the point that ACP's ideas were absorbed rather than discarded.

**Run the inventory exercise if you have time.** Ask the room to list their own integrations and sort them into the four columns. In any organisation with more than a handful, at least one will be in the wrong column, and it will usually be live state that somebody indexed. Kestrel found three out of twelve.

**Sequence it with the decision tree.** This diagram defines the terms; the boundary diagram tells you how to choose between them:

![A signpost reading WHAT OWNS THE WORK? branching into LOCAL FUNCTION, RAG, MCP and A2A, all routing down into a coral shield above a DOMAIN + POLICY ALWAYS banner.](../diagrams/04-choose-the-boundary.png)

Note the asymmetry between the two: the decision tree has a fourth option — **local function** — that this comparison does not, and drops ACP, which is not a choice. Pointing that out is worth a minute, because the option missing from this diagram is the one that is correct most often.

**Timing.** Ten minutes standalone. It is the compressed version of the boundary session, so use it when you do not have forty-five minutes for the real thing.

---

## Lab and checkpoint

**Lab:** List four real integrations or data sources in your system. For each one, classify it as RAG, MCP, A2A, or ACP-legacy, using the direction-of-work test: does the work move inward (retrieval), outward (capability call), bidirectionally (task with another agent), or is it pre-merge material? For any that land in the wrong column or in ACP, write the migration or correction.

**Checkpoint:** Why is ACP drawn as a faded blueprint rather than crossed out?

**Answer:** Because ACP's ideas were absorbed into A2A rather than discarded. The arrow leaving the panel shows that its concepts flowed into the current model. The faded blueprint means it is not a current build choice, but it is also not a mistake.

## Glossary

- **A2A** — agent-to-agent protocol for delegating tasks to another autonomous agent.
- **ACP** — the earlier Agent Communication Protocol whose concepts were merged into A2A.
- **Capability** — a tool that the agent discovers and invokes through a structured contract.
- **Knowledge** — stable, indexed information that the agent retrieves rather than invokes.
- **MCP** — Model Context Protocol, a capability-discovery and tool-calling pattern.
- **RAG** — retrieval-augmented generation: retrieving indexed information to inform an answer.
- **Task** — a unit of work with a lifecycle that can be delegated to another agent.

## Sources

- MCP 2026-07-28 specification and capability model
- A2A Agent Card, task, and artifact documentation
- ACP vocabulary and A2A merge notes
