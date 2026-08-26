# Diagram 15 — RAG Chunk Size

![Three bordered comparison panels on dark navy. TOO SMALL has a coral header and a coral X badge, showing fifteen tiny fragment cards with coral dashed arrows funnelling into a coral bin. JUST RIGHT has a teal header and a teal check, showing one coherent document with an image block and highlighted line, flanked by dashed teal overlap regions and a dashed double-headed arrow beneath. TOO LARGE has an amber header and an amber exclamation badge, showing one oversized page crammed with four unrelated content blocks.](../diagrams/15-rag-chunk-size.png)

**Module:** 3 — RAG evidence
**Role in the course:** teaching chunk-size tradeoffs
**Layout:** three comparison panels with verdict badges

---

## At a glance

Three panels, three verdicts: **TOO SMALL** with a coral ✗, **JUST RIGHT** with a teal ✓, **TOO LARGE** with an amber **!**.

The answer is given away before you read anything — the middle panel is the only clean, coherent object in the frame, and it is the only one with a green check. What makes the diagram worth teaching is not the verdict but the two failure modes, which are graded differently and fail for different reasons.

---

## What the diagram teaches

### 1. Too small destroys meaning, and the bin says so

The left panel shows **fifteen tiny near-identical fragment cards** in a grid, with coral dashed arrows funnelling all of them down into a **coral waste bin**.

The bin is the strongest statement in the diagram. These fragments are not merely less useful — they are drawn as waste. Over-fragmentation does not degrade retrieval gracefully; it produces chunks that cannot function as evidence at all.

Three specific things break:

**Context is severed.** A fragment reading "this must be completed within fourteen days" is unusable without knowing what "this" is. Retrieved on its own it is worse than nothing, because it looks like an answer.

**Embeddings become undiscriminating.** Very short text produces vectors that are dominated by common words and syntax rather than substance. The fifteen cards are drawn as near-identical for exactly this reason — at small enough sizes, everything looks similar to everything, so the ranking signal collapses.

**Answers require reassembly the model cannot do reliably.** If the information needed to answer is spread across six fragments, retrieval must find all six, rank all six above the noise, and fit all six in context. Each additional required fragment multiplies the failure probability.

### 2. Too large dilutes, and the amber says something different

The right panel shows one oversized page crammed with **four unrelated content blocks** — a photo, a bar chart, a group of people, a pie chart — plus dense body text.

It carries an **amber warning**, not a coral ✗. That grading difference is deliberate and worth teaching: too large is bad, too small is worse.

The reason is recoverability. An oversized chunk contains the answer, surrounded by material that dilutes it. The signal is degraded but present — the embedding is pulled toward an average of four unrelated topics, so it matches every one of them weakly and none strongly, and it burns context budget carrying three topics the reader did not ask about. But the answer is in there.

An undersized chunk may not contain the answer at all. Nothing downstream recovers information that was severed at ingestion time.

The practical implication: **when uncertain, err large**. A chunk that is somewhat too big produces mediocre retrieval. A chunk that is too small produces unusable evidence.

### 3. The middle panel shows two properties, not one

The centre panel is doing more work than it first appears. Look at what is drawn:

**One coherent idea.** A single well-formed document with one image block, one highlighted teal line, and body text. It reads as *a thing about something* — a complete unit with a topic.

**Deliberate overlap.** Dashed teal regions flank the document on both sides, and a **dashed double-headed arrow** runs beneath it showing the overlap span.

The overlap is the property most often omitted in practice, and it solves a specific problem: ideas do not respect chunk boundaries. A procedure whose critical warning sits in the last sentence of one chunk and whose steps begin in the next has been split at exactly the wrong place. Overlap means the boundary region appears in both neighbours, so a query matching content near a boundary retrieves a chunk containing the whole thought.

The cost is straightforward — 15% overlap means roughly 15% more chunks, more storage, more embedding compute, and some duplicate results that need collapsing at retrieval time. It is nearly always worth it.

### 4. "One coherent idea" is a semantic criterion, not a character count

The middle panel is not labelled with a number, and its absence is the point. Chunking is not "split every 800 characters." It is "split where the meaning splits."

What that means depends entirely on the document:

- **A procedure** chunks on procedure boundaries — never mid-sequence, because a fragment of a step list reads like a complete instruction and is not.
- **A policy** chunks on clause or section, because a clause is the unit people cite.
- **A specification table** chunks on logical group, with headers preserved in every chunk.
- **Code** chunks on function or class, because a half-function is not evidence of anything.
- **Narrative prose** chunks on section, which is the case where a character count is a reasonable approximation.

Fixed-size chunking is the default because it is easy, and it is correct only for the last of these. Everything else needs structure awareness, which is why the ingestion pipeline's chunk stage is drawn with a *deliberate selection box* rather than a slicing line:

![Five numbered panels — SOURCES, CLEAN, CHUNK, EMBED, INDEX — with the chunk stage showing a document under a dashed selection box splitting into three cards.](../diagrams/13-rag-ingestion-pipeline.png)

### 5. Chunk size is not one decision

The diagram's three-panel form implies a single global setting. Real corpora do not have one right answer, because real corpora contain several document types with different natural units.

A corpus containing manuals, tables, bulletins and wiki pages needs four strategies. Applying one setting across all of them means at least three of the four are wrong. This is the single most common practical failure after skipping overlap.

### 6. What the flow arrows imply, and why you should correct it

Left-to-right teal arrows connect the three panels, which visually suggests a progression — as though the right-hand panel were a destination.

It is a comparison, not a sequence. When presenting, say so explicitly, because a room reading it as a progression will take away exactly the wrong conclusion.

---

## Case study — Meridian Retail, the handbook experiment

Meridian operates about four hundred stores. Their HR team maintains a staff handbook — roughly 340 pages covering pay, leave, conduct, scheduling, health and safety, and grievance procedures — plus around 200 short policy bulletins.

Store managers were the audience. They ask questions like "how much notice does someone need to give for a shift swap" and "what's the process if someone fails a till reconciliation twice."

The first build used fixed 500-character chunks with no overlap. It was poor, and rather than guess at improvements the team ran a measured experiment.

### The test set

They built 120 questions from real manager queries, each with a human-identified correct passage. The metric was deliberately simple: **is the correct passage in the top five retrieved results?** Answer quality was measured separately.

### Configuration A — 500 characters, no overlap

**Top-5 retrieval accuracy: 41%.**

Inspecting failures showed the fragmentation problem exactly as the left panel depicts.

The grievance procedure is a nine-step process running about 2,400 characters. It had become five chunks. A question about the grievance process retrieved two or three of the five, in no particular order, missing steps in between. The assistant produced answers that were partially correct and skipped stages — including, in one case, the requirement to notify a regional manager, which is a compliance obligation.

Worse, the fragments were nearly indistinguishable to the embedder. Steps 3, 4 and 5 all read like "the manager will then arrange a meeting within X days and confirm in writing." Their embeddings were so similar that ranking between them was effectively random.

### Configuration B — 2,000 characters, no overlap

**Top-5 retrieval accuracy: 67%.**

Better, and a new failure appeared: **boundary loss**. Questions whose answers straddled a chunk boundary failed consistently.

The clearest example involved shift swap notice. The rule — 48 hours — appeared at the end of one chunk; the exceptions to it began the next. A question about exceptions retrieved the chunk containing the exceptions, which did not state the 48-hour baseline they were exceptions to. The answer described exceptions to an unstated rule.

Nineteen of the 120 questions failed this way. All at boundaries.

### Configuration C — 2,000 characters, 15% overlap

**Top-5 retrieval accuracy: 81%.**

Overlap resolved fifteen of the nineteen boundary failures. Chunk count rose about 17%, storage and embedding cost rose proportionally, and nobody noticed the difference.

The four remaining boundary failures involved content spanning more than the overlap window — a table that ran across three chunks.

### Configuration D — structure-aware, variable size, 15% overlap

**Top-5 retrieval accuracy: 94%.**

This is where the gain was. Instead of a character count, they chunked on the handbook's own structure:

- **Procedures** chunk whole, whatever the length. The nine-step grievance procedure became one 2,400-character chunk. Non-negotiable, because partial procedures are a compliance risk.
- **Policy sections** chunk on heading boundaries, typically 800–3,000 characters.
- **Tables** chunk as complete tables with headers, never split.
- **Bulletins** are short enough to be one chunk each.
- **Definitions** are grouped, since a lone definition is not retrievable usefully.

Every chunk carries its section heading and the handbook version prepended, which added retrieval signal and made citation possible.

Chunk sizes now range from about 200 characters (a bulletin) to about 4,000 (the longest procedure). There is no single number, and asking what their chunk size is has no answer.

### What they measured about "too large"

They also tested a deliberately oversized configuration — whole chapters as single chunks, averaging around 14,000 characters.

**Top-5 retrieval accuracy: 76%.** Notably, *better than the 500-character configuration*, which is the diagram's amber-versus-coral grading showing up in data. Oversized chunks retrieved the right chapter most of the time.

But the answers were worse than the retrieval number suggests. A chapter-sized chunk consumed most of the context window, so only two could fit. Questions needing material from three areas failed. And the model, given 14,000 characters covering a whole topic area, produced answers that drifted — including adjacent policies the manager had not asked about, which several managers reported as confusing.

Their summary: **too large retrieves acceptably and answers badly; too small fails at retrieval, which nothing downstream can fix.**

### The unexpected finding

Prepending the section heading to every chunk improved accuracy by about four points on its own, independent of size or overlap.

The reason is that headings contain the vocabulary people actually use in questions. Managers ask about "shift swaps"; the body text says "exchange of rostered hours between colleagues." The heading reads "Shift Swaps." Without it, the vocabulary in the question never appears in the chunk.

Cheapest improvement in the whole experiment.

### Where they landed

94% top-5 retrieval, from 41%. No change to the embedding model, the search implementation, or the prompt. The entire gain came from decisions made at the chunk stage.

---

## Composition

Three bordered comparison panels sit side by side, each with a coloured border, a coloured header pill, and a verdict badge below the header. Teal arrows sit between the panels.

- **Left:** coral border, coral header pill reading **TOO SMALL**, coral **✗** badge.
- **Centre:** teal border, teal header pill reading **JUST RIGHT**, teal **✓** badge.
- **Right:** amber border, amber header pill reading **TOO LARGE**, amber **!** badge.

## Element by element

**TOO SMALL**
A grid of **fifteen tiny white fragment cards**, each showing a single short blue line — deliberately near-identical. Beneath them, **coral dashed arrows** curve down from each card and converge into a **coral waste bin** on a blue plinth.

**JUST RIGHT**
One well-formed white document page containing a **teal image block**, several grey text lines, a **highlighted teal bar**, and further text. Flanking it on both sides are **dashed teal overlap regions**, drawn as translucent panels extending beyond the document's edges. Beneath the platform, a **dashed teal double-headed arrow** spans the overlap width.

**TOO LARGE**
One oversized white page crammed with four coloured content tiles down its left edge — a **blue photo**, a **green bar chart**, a **purple group of people**, a **red pie chart** — each with dense grey text lines beside it. Four unrelated topics in one unit.

## Colour and flow semantics

- **Coral** for the worse failure, including the dashed discard arrows and the bin.
- **Teal** for the correct configuration and for the overlap markers.
- **Amber** for the lesser failure — the only place in the library where a failure mode is graded amber rather than coral, and the grading is meaningful: too large is recoverable, too small is not.
- The **dashed teal overlap regions and span arrow** in the centre panel are the diagram's most easily missed detail and its second most important teaching point.
- The **left-to-right arrows** between panels imply a progression that does not exist. This is a comparison, and it should be stated when presenting.

## How to present it

**Ask for their chunk size before showing the diagram.** Most rooms have a number — 500, 1000, 1500 — and stating it out loud sets up the finding that having *a* number is itself the problem.

**Cover the middle panel and ask which failure is worse.** Most people say too large, because it feels wasteful. Then uncover the badges and point at the coral ✗ versus the amber **!**. Ask why the diagram grades them differently.

Steer to the answer: too large contains the answer diluted; too small may not contain it at all, and nothing downstream recovers severed information. This single comparison is the most useful thing in the session, because it gives a decision rule — **when uncertain, err large**.

**Point at the dashed regions and ask what they are.** Overlap is the detail most rooms have not implemented. Then ask what happens to a rule stated at the end of one chunk whose exceptions begin the next. Meridian's shift-swap example is a good one to tell, because everyone recognises the shape of it.

**Ask what a chunk should contain.** Push past "800 characters" to "one coherent idea." Then ask what one idea is in *their* documents. A procedure? A clause? A table? A function? The realisation that different document types have different natural units is where most teams find their actual bug.

**Correct the arrows.** Say plainly that this is a comparison, not a progression, and that the right-hand panel is not a destination.

**Use the numbers if you have a data-minded room.** 41% → 67% → 81% → 94%, with no change to the model, the search, or the prompt. And the counterintuitive one: the oversized configuration at 76% beat the undersized at 41%, which is the amber/coral grading appearing in measurement.

**Finish with the cheapest win.** Prepending section headings improved accuracy four points on its own, because headings carry the vocabulary people use in questions while body text does not. It costs nothing and almost nobody does it.

**Timing.** Twenty minutes. Thirty if you walk the four configurations, which is worth it for teams who want to justify the work.

---

## Lab and checkpoint

**Lab:** Take one real document from your corpus and create three chunking versions: one under-sized, one over-sized, and one with overlap and headings. Ask the same three questions of each version and measure which version produces complete, well-cited answers. Record the chunk size, overlap, heading treatment, and the answer quality for each.

**Checkpoint:** Why is too small a worse failure than too large?

**Answer:** Because too large may dilute the answer but still contains it; too small may sever the answer across chunks, and no downstream stage can recover information that was never put into the context. When uncertain, err large.

## Glossary

- **Chunk** — a unit of text passed to the embedding model and stored in the index.
- **Chunk size** — the amount of text in one chunk, measured in characters or tokens.
- **Heading** — a structural label that often carries the vocabulary people use in questions.
- **Overlap** — the shared text between adjacent chunks that keeps related ideas from being severed.
- **Too large** — an oversized chunk that mixes multiple ideas and dilutes retrieval relevance.
- **Too small** — an undersized chunk that may not contain a complete idea and cannot be recovered.

## Sources

- RAG chunking and overlap best practices
- Embedding-based retrieval and context-dilution studies
- Document structure and heading-aware chunking guidance
