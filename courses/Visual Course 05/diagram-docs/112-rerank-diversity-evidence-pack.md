# Diagram 112 — Rerank, Diversity, and the Evidence Packet

![A CANDIDATE POOL 60 cylinder on dark navy leads through five stages connected by cyan arrows — RERANKER with a bar chart, DEDUPLICATE with a folder and magnifier, DIVERSIFY with a funnel holding coloured spheres, AUTHORITY CHECK with a teal shield, TOKEN BUDGET with a gauge — arriving at EVIDENCE PACKET, a bordered panel listing POLICY, TRANSACTION, EXCEPTION and CITATION. A teal dashed line beneath the five stages drops to two red platforms, REDUNDANT and LOW AUTHORITY, each leading to a coral REASON tile.](../diagrams/112-rerank-diversity-evidence-pack.png)

**Module:** Query and retrieval
**Role in the course:** from sixty candidates to a packet you can defend
**Layout:** a five-stage reduction with two logged discard paths and a four-type output

---

## At a glance

Sixty candidates through five stages — **RERANKER, DEDUPLICATE, DIVERSIFY, AUTHORITY CHECK, TOKEN BUDGET** — producing an **EVIDENCE PACKET** with four labelled types.

Beneath, a teal dashed line runs under all five stages and drops to two discard outcomes: **REDUNDANT** and **LOW AUTHORITY** — and each of those leads to a coral **REASON**.

The reason tiles are the diagram's distinguishing feature. Discarding is not enough; the system records **why** each candidate was dropped.

---

## What the diagram teaches

### 1. Five stages, and each removes candidates for a different reason

**RERANKER** — reorders by true relevance, using a model that reads the query and the candidate together. Expensive, accurate, and the reason the pool was capped at sixty.

**DEDUPLICATE** — removes candidates that are the same content. Different chunks of the same passage, the same clause appearing in two documents.

**DIVERSIFY** — removes candidates that are *different content saying the same thing*. Distinct from deduplication and more subtle.

**AUTHORITY CHECK** — removes candidates from sources that do not carry enough weight for this question.

**TOKEN BUDGET** — removes whatever does not fit.

Five different criteria. A single "select top N" collapses all five into relevance, and the four other properties go unexamined.

### 2. DEDUPLICATE and DIVERSIFY are different operations

The distinction is easy to miss and it matters.

**Deduplication** is about identity. Two candidates containing the same text are one piece of evidence.

**Diversification** is about redundancy of *meaning*. Five different documents each stating the same rule are five distinct texts and one fact.

The diversify glyph — a funnel holding **differently-coloured spheres** — makes the point. The output should be varied, not merely non-identical.

Without diversification, an evidence packet can be full and narrow: eight passages, all making the same point, and nothing addressing the other half of the question.

### 3. AUTHORITY CHECK is a teal shield, and it is where the source register pays off

The fourth stage, and it depends entirely on the governance work at the start of the volume.

Authority was one of the five fields every source declares. This is where it is consumed.

A question about a regulatory obligation should be answered from the regulation, not from an internal summary of the regulation, even if the summary matches the query better. The reranker cannot know that; the authority check can.

The teal shield marks it as a validation stage rather than a ranking one.

### 4. TOKEN BUDGET comes last, and its position is deliberate

A gauge, immediately before the packet.

Budget enforcement after all four quality stages means the packet contains the **best** evidence that fits, rather than the **first** evidence that fits.

The alternative ordering — cutting to budget early and then reranking what remains — discards high-quality candidates before they have been assessed.

### 5. The two discard paths are logged with reasons, and that is the diagram's distinctive claim

A teal dashed line runs beneath all five stages, with drops into **REDUNDANT** and **LOW AUTHORITY**, each producing a coral **REASON** tile.

Two properties.

**The line touches every stage.** Discards can originate anywhere in the pipeline, and they all route to the same recording mechanism.

**Each discard carries a reason.** Not a count — a reason, per candidate.

Why that matters: an evidence packet is a claim about what the best available evidence was. Without discard reasons, that claim is unfalsifiable. With them, you can ask *why was this passage not used*, and get an answer.

### 6. The evidence packet has four typed entries, and the types are not decorative

**POLICY** (shield), **TRANSACTION** (card), **EXCEPTION** (purple warning), **CITATION** (quotation marks).

Four different kinds of evidence, and a good packet contains a mixture.

**Policy** — the rule.
**Transaction** — the facts of this case.
**Exception** — the qualification that changes the outcome.
**Citation** — the reference making it checkable.

Typing them means the packet's *composition* can be assessed, not just its size. A packet with four policy entries and no transaction evidence is answering a general question when a specific one was asked.

The **EXCEPTION** entry is rendered in purple rather than blue, which marks it as the one that changes conclusions.

### 7. The pipeline is a reduction, and the numbers should be measured

Sixty candidates in; a handful out.

The ratio at each stage is worth measuring. A diversify stage removing nothing means the pool was already varied — or that diversification is not working. An authority check removing forty percent means the corpus has a lot of low-authority content matching well.

Those ratios are diagnostics about the corpus, not just about the pipeline.

The packet's fourth entry type is where it connects to everything downstream:

![A five-column lineage carrying three claims through evidence spans, chunks, source versions, original pages and owners, with an unsupported claim removed before publication and a VERIFIED CITATION panel listing page, bbox, as-of and access check.](../diagrams/121-claim-citation-lineage.png)

**CITATION** here is what makes that lineage possible. A packet entry without one produces a claim that cannot be traced, and that diagram removes such claims before publication — which means a packet composition failure becomes an answer with fewer claims than it should have had.

---

## Case study — Marchford Insurance, the packet that agreed with itself

Marchford underwrites commercial property and liability insurance. Their claims assistant assembles evidence for handlers assessing whether a claim is covered.

A coverage decision needs the policy wording, the claim facts, any endorsements or exclusions, and the basis for the conclusion.

### The failure mode

Handlers began reporting that the assistant was "confident and shallow."

Investigation found a consistent pattern: evidence packets contained six to eight passages, of which typically five or six said substantially the same thing.

Their policy wordings are highly repetitive by design — the same exclusion appears in the general conditions, in the section-specific conditions, and in the schedule. A query matching that exclusion matched all three, plus the two other product wordings containing near-identical language.

The packet was full. It was also narrow, and the passage that would have changed the answer — an endorsement modifying the exclusion — was ranked eleventh and never made it in.

### The incident

A claim for water damage was declined on the basis of a gradual-deterioration exclusion.

The policy carried an endorsement extending cover for gradual deterioration where the insured had a maintenance contract in place. The insured did.

The endorsement was in the index, matched the query moderately well, and was displaced from the packet by five near-identical statements of the exclusion it modified.

The decline was overturned on complaint. Marchford paid the claim — about £86,000 — plus the complaint handling costs, and their conduct function opened a review.

### The audit

They analysed 300 evidence packets against handler assessments of what should have been included.

**Median distinct facts per packet: 2.4.** Median passages per packet: 7.

**Endorsements were present in 31% of packets where they were relevant.** The other 69% had been displaced by redundant policy language.

That figure is the one that stopped the system. Endorsements are precisely the content that changes an outcome, and they were being crowded out by content that did not.

### The rebuild

**DEDUPLICATE and DIVERSIFY separated.**

Deduplication removes textually identical or near-identical passages. That alone cut median packet size from 7 to 5.

Diversification then operates on meaning. Marchford's implementation clusters candidates by the assertion they make and admits at most two per cluster.

Median distinct facts per packet went from 2.4 to 4.8.

**AUTHORITY CHECK using their source register.**

Their authority scale places the policy schedule and endorsements above the general wording, because an endorsement modifies the wording and therefore outranks it for coverage questions.

That ordering is a domain judgement their underwriting function made, and encoding it meant endorsements rank above the clauses they modify rather than competing with them.

**A composition requirement on the packet.**

Their packet must contain at least one entry of each type where the type is available: policy wording, claim facts, and any applicable endorsement or exclusion.

If an endorsement exists for the policy and is not in the packet, the packet is flagged before it reaches a handler.

That check is what would have caught the water damage claim.

**Discard reasons recorded and surfaced.**

Every candidate that does not reach the packet is recorded with the stage that dropped it and the reason.

Handlers can expand a packet to see what was considered and rejected. About 12% of handlers use this routinely, and it has produced 40 or so reports of a rejected passage that should have been included.

Each of those is a tuning signal that would otherwise have been invisible.

### The finding from the discard log

Reviewing three months of discard reasons showed that their authority check was dropping a category it should not have been: **broker correspondence** confirming cover terms.

Their source register had classified broker correspondence as low authority, which is right for most purposes and wrong for questions about what was agreed at inception.

The classification was refined to be question-type-dependent. That refinement came directly from reading discard reasons, and nothing else would have surfaced it.

### Results

- **Median distinct facts per packet:** 2.4 → 4.8.
- **Median passages per packet:** 7 → 5.
- **Endorsements present when relevant:** 31% → 96%.
- **Packets failing composition check:** ~4%, flagged before reaching a handler.
- **Declines overturned on complaint citing missed endorsements:** 3 in the preceding year → 0.
- **Source classification errors found via discard log:** 1 category, affecting broker correspondence.

### The line in their claims technology standard

*A full packet is not a good packet. Count the distinct facts, not the passages, and record why everything else was left out.*

---

## Composition

A left-to-right reduction pipeline with a discard rail beneath and a typed output on the right.

**Left:** **CANDIDATE POOL 60** — a blue cylinder with a group-of-people glyph.

**Five stages**, connected by cyan arrows, each a blue platform with an icon: **RERANKER** (bar chart), **DEDUPLICATE** (folder with a magnifier), **DIVERSIFY** (funnel holding coloured spheres), **AUTHORITY CHECK** (teal shield with a check), **TOKEN BUDGET** (gauge).

**Right:** a cyan arrow to **EVIDENCE PACKET** — a bordered blue panel containing four white cards: **POLICY** (blue shield), **TRANSACTION** (teal payment card), **EXCEPTION** (purple warning triangle), **CITATION** (blue quotation marks).

**Beneath:** a **teal dashed rail** running under all five stages, with teal drop lines into two red platforms — **REDUNDANT** (a red document with a white ✗) and **LOW AUTHORITY** (a red document with a person glyph) — each sending a **coral arrow** down to a coral **REASON** tile.

## Element by element

**CANDIDATE POOL 60** — the fixed-size input.

**RERANKER** — a bar chart. True relevance, expensively computed.
**DEDUPLICATE** — a folder with a magnifier. Same content.
**DIVERSIFY** — a funnel with differently-coloured spheres. Same meaning, different content.
**AUTHORITY CHECK** — a teal shield. Source weight.
**TOKEN BUDGET** — a gauge. What fits.

**EVIDENCE PACKET** — four typed entries: policy, transaction, exception, citation.

**REDUNDANT / LOW AUTHORITY** — two discard outcomes, each producing a **REASON**.

## Colour and flow semantics

- **Cyan arrows** carry the pipeline left to right through the five stages.
- The **teal dashed rail** runs beneath all five, collecting discards from any stage.
- **Coral** marks the two discard outcomes and their reason tiles.
- **Teal** marks the authority shield — a validation stage among ranking stages.
- The **EXCEPTION card is purple** among three blue-and-teal cards, marking it as the entry that changes conclusions.

## How to present it

**Ask what happens between a candidate pool and an evidence packet.** Most rooms describe reranking and taking the top N. Then show five stages and ask what each removes.

**Draw the deduplicate/diversify distinction.** Same content versus same meaning. Then ask what a packet of eight passages all making one point is worth.

**Point at the coloured spheres in the diversify funnel.** Varied, not merely non-identical.

**Tell the Marchford numbers.** Seven passages, 2.4 distinct facts. Then the consequence: endorsements present in only 31% of packets where they were relevant.

**Tell the water damage claim.** An endorsement extending cover, ranked eleventh, displaced by five near-identical statements of the exclusion it modified. £86,000, overturned on complaint.

**Ask where authority comes from.** The source register, from the first diagram in the volume. This is where that field is consumed.

**Give them the Marchford authority ordering.** Endorsements outrank the wording they modify, because an endorsement changes it. A domain judgement, encoded.

**Ask why token budget comes last.** Best evidence that fits, rather than first evidence that fits. Cutting early discards candidates before they have been assessed.

**Point at the discard rail and the reason tiles.** Not a count — a reason per candidate. Then make the argument: a packet is a claim about the best available evidence, and without discard reasons that claim is unfalsifiable.

**Tell the broker correspondence finding.** Reading three months of discard reasons revealed a source classification that was right in general and wrong for one question type. Nothing else would have surfaced it.

**Introduce the composition check.** At least one entry of each available type. Marchford flag about 4% of packets, and it is the check that would have caught the water damage claim.

**Close on the standard.** *Count the distinct facts, not the passages.*

**Timing.** Twenty-five minutes. Thirty-five if you count distinct facts in a sample of the room's own packets, which is usually a lower number than expected.

---

## Lab and checkpoint

**Lab:** Trace one query through the rerank and evidence-pack pipeline. Start with 60 candidates and apply: deduplication, diversification, authority check, evidence typing, and token-budget fit. For each step, record how many were removed and why. Then count the distinct facts in the final packet and check whether each evidence type is represented.

**Checkpoint:** Why is the token budget applied last, not first?

**Answer:** Because the token budget must be applied to the best evidence after all other quality steps have run. If you apply it first, you may cut candidates before they have been deduplicated, diversified, and authority-checked, and you can end up with a packet of near-identical passages that do not include the most important evidence.

## Glossary

- **Authority** — the source-level property that resolves conflicts between chunks.
- **Authority check** — the step that orders or filters by source authority.
- **Candidate pool** — the set of chunks entering the rerank stage.
- **Composition check** — the requirement that the packet contains relevant evidence types.
- **Deduplicate** — removing passages with the same content.
- **Discard log** — the record of why each candidate was removed.
- **Diversify** — selecting passages that make different points, not merely different words.
- **Evidence packet** — the final selected set of passages used to generate an answer.
- **Evidence type** — the category of evidence, such as rule, procedure, or example.
- **Token budget** — the maximum amount of context that fits into the model.

## Sources

- Reranking and evidence-pack construction
- Diversity and authority in evidence selection
- Token budget and composition checks in RAG
