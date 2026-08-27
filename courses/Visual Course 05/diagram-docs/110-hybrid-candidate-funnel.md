# Diagram 110 — Hybrid Candidate Funnel

![A QUERY magnifier on dark navy fans to three search platforms — LEXICAL SEARCH with an open book, DENSE SEARCH with a brain-network glyph, OPTIONAL SPECIALIST with a starred person. Each produces a ranked result card listing 1, 2, 3 through n. Teal lines carry all three into RRF FUSION, a blue funnel, then DEDUPLICATE, then CANDIDATE POOL 60. A coral dashed line from the specialist's results leads to EMPTY CHANNEL and then PARTIAL RESULTS CONTINUE.](../diagrams/110-hybrid-candidate-funnel.png)

**Module:** Query and retrieval
**Role in the course:** three channels into one candidate pool
**Layout:** one query fanning to three searches, fused and deduplicated into a fixed pool, with an empty-channel tolerance

---

## At a glance

Three search channels — **LEXICAL**, **DENSE**, **OPTIONAL SPECIALIST** — each producing a ranked list, fused by **RRF**, deduplicated, and reduced to a **CANDIDATE POOL 60**.

And a coral path: if a channel returns nothing, that is an **EMPTY CHANNEL**, and **PARTIAL RESULTS CONTINUE**.

Two numbers matter. **RRF** names the fusion method specifically. **60** names the pool size specifically. Both are choices, and naming them makes them arguable.

---

## What the diagram teaches

### 1. The third channel is labelled OPTIONAL, and that word is doing work

**LEXICAL SEARCH** and **DENSE SEARCH** are unqualified. The third is **OPTIONAL SPECIALIST**.

A specialist channel is one built for a particular query type or content type — a graph traversal, a structured lookup, a domain-specific matcher, a late-interaction index.

It is optional in two senses. It may not exist in a given deployment. And it may not run for a given query, because the query does not have the characteristics it serves.

That optionality is what makes the empty-channel path necessary.

### 2. Each channel produces the same shape, which is what makes fusion possible

Three result cards, all listing **1, 2, 3, …, n** with score bars.

Identical rendering, deliberately. Three completely different retrieval mechanisms, three ranked lists, one shape.

Fusion operates on rank position. It does not need to understand how a ranking was produced, only that it is ordered.

### 3. RRF is named, and naming it rules out the alternative

**RRF FUSION** — reciprocal rank fusion — drawn as a funnel.

The alternative, and the thing RRF exists to avoid, is blending raw scores.

Lexical relevance scores and vector similarity scores are on incomparable scales. A BM25 score of 8.4 and a cosine similarity of 0.82 cannot be averaged, and normalising them produces rankings that shift with query length and corpus statistics.

RRF discards the scores and uses only positions. A document ranked second in one list and fifth in another gets a combined score derived from those positions, and the arithmetic is stable regardless of what scale each channel used.

The consequence worth stating: **a document appearing in several lists rises**, because appearing in two independent rankings is stronger evidence than a high score in one.

### 4. DEDUPLICATE sits after fusion, and its position is necessary

A card-stack glyph between fusion and the pool.

The same chunk can appear in all three lists. Fusion combines the rankings; deduplication removes the repeats.

Order matters. Deduplicating before fusion would discard the corroboration signal — the fact that a chunk appeared in three lists is exactly what should raise it, and you can only observe that if all three arrive at the fusion stage.

### 5. CANDIDATE POOL 60 is a specific number, and specific is the point

Not "candidate pool." **Sixty.**

A fixed pool size makes the next stage's cost predictable. Reranking is expensive per candidate; a pool of 60 has a known cost, a pool of "whatever came back" does not.

Sixty is large enough that the correct answer is very likely present — recall at the pool level is what matters here, not precision — and small enough that a cross-encoder reranker can process it in acceptable time.

The number is a trade between recall and rerank cost, and it should be set by measurement rather than convention.

### 6. EMPTY CHANNEL is coral and leads to PARTIAL RESULTS CONTINUE, not to failure

The coral dashed path from the specialist's results.

A channel returning nothing is a normal condition. A graph channel has nothing to say about a question with no entities. A structured channel has nothing for a narrative question.

The system continues on what it has.

That tolerance is the correct behaviour and it needs stating, because the naive implementation — waiting for all channels, or failing if one is empty — turns an optional channel into a required one.

### 7. Degrading is not the same as degrading silently

The diagram shows continuation and does not show reporting, which is worth adding when teaching.

A query that ran on two of three channels produced a smaller candidate pool from a narrower search. That may be entirely fine. It may also mean the specialist channel is broken rather than legitimately empty.

The distinction between *this query had nothing for the graph channel* and *the graph channel is down* is invisible from the result, and only monitoring separates them.

Sixty candidates is not an answer. The pool is the input to a second, quite different reduction:

![A candidate pool of 60 passing through RERANKER, DEDUPLICATE, DIVERSIFY, AUTHORITY CHECK and TOKEN BUDGET into an EVIDENCE PACKET listing POLICY, TRANSACTION, EXCEPTION and CITATION, with discard paths to REDUNDANT and LOW AUTHORITY each producing a REASON.](../diagrams/112-rerank-diversity-evidence-pack.png)

This diagram optimises for **recall** — get the right answer into the pool. That one optimises for **precision and composition** — get the right handful out of it. Conflating the two produces a pool sized for reranking cost rather than for recall.

---

## Case study — Wardlow Clinical Information, the channel that had been down for five weeks

Wardlow provides clinical decision support to a group of hospital trusts. Their assistant answers questions from national guidance, local protocols, drug formularies, and a structured medicines database.

Four content types, and they built four channels.

### The four channels

**Lexical** — for drug names, code identifiers, and guideline references.

**Dense** — for clinical concepts and paraphrase.

**Structured** — a specialist channel querying their medicines database directly for dose, interaction and contraindication data.

**Graph** — a specialist channel over a relationship graph linking conditions, treatments and contraindications.

The last two are genuinely optional. A question about a guideline's wording has nothing for the structured channel; a question about a specific dose has little for the graph.

### The incident

A pharmacist asked about interactions for a patient on four medications.

The assistant returned guidance about two of the four and said nothing about the pair with a clinically significant interaction.

The interaction was in the structured medicines database, and the structured channel had returned nothing.

The pharmacist caught it — they knew the interaction and were checking. Had they not known, the omission would have been invisible, because the answer was well-formed and cited real guidance.

### What was wrong

The structured channel had been failing for **five weeks**.

A schema change in the medicines database had broken its query. The channel caught the exception, logged it at debug level, and returned an empty result set.

Empty is a valid state for an optional channel. Nothing distinguished a broken channel from a channel that legitimately had nothing to say.

The system degraded gracefully, continuously, for five weeks, and reported success on every query.

### The audit

They compared five weeks of answers against what the structured channel would have contributed.

**About 3,100 queries** had characteristics that should have engaged the structured channel.

**Of those, roughly 340** would have received materially different evidence — dose ranges, interaction warnings, contraindications.

They reviewed all 340. Twelve had been given to clinicians in a form where the missing information could have affected a decision. None had resulted in patient harm; three had been caught by the clinician, as the pharmacist's case was.

### The rebuild

**Channel health separated from channel emptiness.**

Every channel now returns a status alongside its results: `results`, `empty` (ran successfully, nothing matched), or `error` (did not run).

`Empty` continues silently. `Error` raises.

That distinction is the entire fix, and it is one field.

**Per-channel monitoring with expected engagement rates.** Wardlow measured how often each channel legitimately returns results for queries with matching characteristics.

The structured channel engages on about 22% of all queries and returns results on 94% of those. A drop below 85% raises an alert.

That would have caught the five-week failure on day one.

**Answers state which channels contributed.** Their evidence packet lists the channels that produced candidates, and the interface shows it:

> Evidence from: guidance (lexical, dense) · medicines database (structured)

A pharmacist asking an interaction question and seeing no structured contribution now knows something is missing.

That display is what their clinical governance function considers the most important change, because it moves the detection to the person best placed to notice.

**Pool size measured rather than assumed.** They had been using 40, chosen arbitrarily.

Measuring recall at the pool level across their test set showed 40 captured the correct answer 91% of the time, 60 captured it 97%, and 80 captured 97.4%.

They moved to 60. The rerank cost increase was acceptable; the jump from 91% to 97% was not something they were willing to leave on the table.

### The RRF finding

Their original fusion had normalised and blended scores.

Moving to RRF produced a modest quality improvement and a large stability improvement: their rankings had been shifting noticeably with query length, because their normalisation was sensitive to score distribution, and that variability disappeared.

The clinicians noticed. Asking the same question twice with slightly different wording had previously produced visibly different result orderings.

### Results

- **Silent channel failures:** 1 lasting five weeks → detected within a day by engagement-rate monitoring.
- **Queries with missing structured evidence:** ~3,100 over five weeks → 0.
- **Pool-level recall:** 91% (pool 40) → 97% (pool 60).
- **Ranking stability across paraphrased queries:** substantially improved by RRF.
- **Channel contribution shown to clinicians:** newly visible.

### The line in their engineering standard

*An optional channel returning nothing and an optional channel that is broken look identical in the results. They must not look identical in the status.*

---

## Composition

One query fanning to three channels, each producing a ranked list, converging through fusion and deduplication into a fixed pool, with a coral tolerance path.

**Left:** **QUERY** — a blue tile with a magnifier. Three cyan arrows fan right.

**Three channels**, top to bottom: **LEXICAL SEARCH** (open book), **DENSE SEARCH** (brain-network glyph), **OPTIONAL SPECIALIST** (person with a star badge) — each a blue tile on a platform.

**Each** sends a cyan arrow to a white **ranked result card** listing **1, 2, 3, …, n** with blue score bars.

**Teal lines** from all three cards converge on **RRF FUSION** — a blue funnel tile — then a teal arrow to **DEDUPLICATE** — a stacked-documents tile — then a teal arrow to **CANDIDATE POOL 60** — a tile with a group-of-people glyph.

**Coral dashed path:** from the specialist's result card rightward to **EMPTY CHANNEL** — a red tile with a warning triangle — then a coral dashed arrow to **PARTIAL RESULTS CONTINUE** — a red tile with a right-arrow glyph.

## Element by element

**QUERY** — a blue magnifier tile.

**LEXICAL SEARCH** — an open book. Exact matching.
**DENSE SEARCH** — a brain-network glyph. Semantic matching.
**OPTIONAL SPECIALIST** — a person with a star. Domain-specific or content-specific.

**Ranked result cards** — three identical cards listing positions with score bars.

**RRF FUSION** — a funnel. Rank-based combination.
**DEDUPLICATE** — stacked documents. After fusion, not before.
**CANDIDATE POOL 60** — a fixed-size pool.

**EMPTY CHANNEL / PARTIAL RESULTS CONTINUE** — the coral tolerance path.

## Colour and flow semantics

- **Cyan arrows** carry the query into the three channels and their results into cards.
- **Teal lines** carry results through fusion and deduplication into the pool.
- **Coral dashed** carries the empty-channel path — a tolerance, not a failure.
- The **three result cards are rendered identically**, which is what makes rank-based fusion possible.
- **RRF** and **60** are both named specifically, presenting them as choices rather than defaults.

## How to present it

**Ask how they combine results from two search methods.** If the answer involves normalising and averaging scores, that is the thing RRF exists to avoid.

**Give them the incomparable-scales problem.** BM25 8.4 and cosine 0.82. Then note what normalisation does — rankings that shift with query length.

**Explain RRF's central property.** It uses positions, not scores, so a document appearing in several lists rises. Corroboration from independent mechanisms is the signal.

**Ask why deduplication comes after fusion.** Deduplicating first would discard the corroboration. You can only observe that a chunk appeared in three lists if all three reach the fusion stage.

**Point at the number 60 and ask where it came from.** Then give Wardlow's measurement: 40 gave 91% pool recall, 60 gave 97%, 80 gave 97.4%. A number chosen by measurement rather than convention.

**Ask what OPTIONAL means.** May not exist; may not run for this query. Then ask what happens if the system waits for it or fails without it — an optional channel becomes required.

**Tell the Wardlow five weeks.** A structured channel broken by a schema change, catching its exception, logging at debug level, and returning empty. Empty is valid for an optional channel, so nothing noticed.

**Give them the one-field fix.** Status alongside results: `results`, `empty`, `error`. Empty continues silently; error raises.

**Introduce engagement-rate monitoring.** Wardlow's structured channel engages on 22% of queries and returns results on 94% of those. A drop below 85% alerts. That would have caught it on day one.

**Point at the channel-contribution display.** A pharmacist asking an interaction question and seeing no structured contribution knows something is missing. Detection moved to the person best placed to notice.

**Close on the standard.** *Empty and broken look identical in the results. They must not look identical in the status.*

**Timing.** Twenty-five minutes. Thirty-five if you measure the room's own pool-recall curve, which frequently shows their pool is too small.

---

## Lab and checkpoint

**Lab:** Build a hybrid-candidate funnel for one query type. Run keyword, vector, and an optional structured channel. Fuse the ranked lists with reciprocal rank fusion, deduplicate after fusion, and cut the pool at a measured number. Then add status fields so that empty and broken channels look different.

**Checkpoint:** Why must deduplication happen after fusion, not before?

**Answer:** Because a chunk that appears in multiple lists is corroborated by independent methods, which is the signal that reciprocal rank fusion uses. If you deduplicate before fusion, you lose the evidence that the same chunk was found by multiple channels, and the ranking becomes less reliable.

## Glossary

- **BM25** — a keyword ranking function.
- **Candidate pool** — the set of chunks that proceed to reranking.
- **Channel** — one search method in the funnel.
- **Corroboration** — agreement across independent methods.
- **Deduplicate** — removing duplicate candidates after fusion.
- **Empty channel** — a channel that returned no results, which is valid for an optional channel.
- **Fusion** — combining ranked lists from multiple channels.
- **Hybrid search** — using multiple search methods together.
- **Optional channel** — a channel that may not run or may not exist for every query.
- **Reciprocal rank fusion (RRF)** — a fusion method based on rank positions, not raw scores.
- **Structured channel** — a search over structured data, such as a database or graph.

## Sources

- Hybrid retrieval and reciprocal rank fusion
- Channel failure detection and degradation
- Candidate-pool sizing and recall
