# Diagram 14 — RAG Answer Pipeline

![Five numbered panels on dark navy — QUESTION showing a thinking person with a teal question bubble; SEARCH showing a large magnifying glass with dashed arrows fanning out to six candidate cards; RERANK showing a board listing scores 0.92, 0.78, 0.55, 0.23 and 0.07 with three cards emerging; CONTEXT showing selected cards stacked inside a translucent teal container in an app window; and ANSWER showing a blue robot above a clean white answer card.](../diagrams/14-rag-answer-pipeline.png)

**Module:** 3 — RAG evidence
**Role in the course:** debugging an answer path
**Layout:** five numbered stages, left to right

---

## At a glance

Five stages that turn a question into a grounded answer: **QUESTION → SEARCH → RERANK → CONTEXT → ANSWER**.

This is the runtime half of RAG — what happens after somebody asks something. Its centrepiece is the third panel, which shows retrieval producing a **scored, ranked shortlist with a visible cut-off** rather than "the database returns the answer." That single depiction corrects the most common misconception about how RAG works.

---

## What the diagram teaches

### 1. Search casts a wide net and returns a mess

The second panel shows an oversized magnifying glass with **dashed arrows fanning out to six candidate cards** — three above, three below, unordered.

Two properties are being asserted. Search returns **many** results, not one. And it returns them **unordered** relative to actual usefulness, because the similarity function that found them is a crude proxy for relevance.

This is the stage where a lot of intuition goes wrong. People imagine retrieval as lookup: ask a question, get the passage. It is not. It is a recall-oriented sweep designed to make sure the useful passage is *somewhere* in the set, accepting that most of what comes back is not useful.

Setting recall high at this stage is correct. Missing the right passage here is unrecoverable — nothing downstream can rank a document it never received. Returning too much is recoverable, because that is what the next stage exists for.

### 2. The scored list is the most instructive object in the diagram

The third panel shows five candidates with explicit scores: **0.92, 0.78, 0.55, 0.23, 0.07**. The top two chips are teal, the **0.55 is amber**, and the bottom two are grey. Three cards emerge on the right.

Everything about this is deliberate.

**Scores are visible.** Relevance is a number, not a verdict. Two documents can both be "relevant" and one can be twice as relevant.

**The distribution is realistic.** A steep drop from 0.92 to 0.07 is what real result sets look like — a couple of strong matches and a long tail of weak ones.

**There is a cut-off, and it is a decision.** Three of five pass. The amber 0.55 sitting exactly at the boundary is the diagram's sharpest detail: it is the marginal case, and colouring it differently from both the passes and the rejects says that borderline candidates need a policy rather than a default.

**Reranking is a second, different judgement.** The first pass found candidates by vector similarity. The rerank stage evaluates them properly — usually with a model that reads the question and the passage together, which is far more accurate and far too expensive to run over the whole corpus. Cheap and wide, then expensive and narrow.

### 3. Context assembly is a stage, and it is where the budget lives

The fourth panel shows the selected cards stacked inside a **translucent teal container** within an application window.

The container is the important object: it is a bounded space, and it is smaller than what you would like to put in it. Context assembly is the point where you decide what actually reaches the model, and it involves choices the previous stages do not:

- **How many chunks fit** given the question, the instructions, and the room needed for a response.
- **In what order** they appear — position affects how strongly the model weights them.
- **What surrounds them** — source labels, section headings, dates, and the identifiers that make citation possible downstream.
- **What to do about redundancy** — three chunks saying the same thing consume three slots and add nothing.

Teams routinely treat this as plumbing. It is a stage with its own failure mode: perfect retrieval, correctly ranked, assembled badly, producing a worse answer than a mediocre retrieval assembled well.

### 4. The answer panel is deliberately small

The fifth panel is the least elaborate: a robot above a clean white card. In a five-stage pipeline about generating an answer, generation gets the simplest picture.

The proportions carry the argument. Four stages of finding, ranking, and assembling evidence; one stage of writing it up. When a RAG system gives a bad answer, the probability that the problem is in the fifth panel is low. The problem is nearly always that the right evidence never reached it.

This reframes debugging. The instinct is to change the prompt or the model. The diagram says: look at what was in the container.

### 5. Each stage fails differently, and the failures look alike from the outside

The practical value of the five-stage split is that a bad answer has five possible origins, and they are distinguishable if you look at the right artefact.

| Stage | Failure | How you detect it |
| --- | --- | --- |
| **QUESTION** | Ambiguous or under-specified; resolved silently and wrongly | The resolved interpretation is not shown in the output |
| **SEARCH** | The right chunk was never retrieved | Search the index directly for the known-good passage — is it findable at all? |
| **RERANK** | Retrieved but ranked below the cut-off | Inspect the scored list; is the good chunk present with a low score? |
| **CONTEXT** | Ranked highly but truncated, buried, or crowded out | Inspect what actually reached the model |
| **ANSWER** | All the right evidence present, answer still wrong | The rarest case, and the only one that is genuinely a model problem |

From the user's perspective these are one symptom: a wrong answer. Without the stage boundaries, teams guess. With them, each stage has an artefact you can inspect.

### 6. It only works if ingestion worked

Nothing in this pipeline can retrieve a passage that was never indexed, or index a passage that was destroyed during extraction. The runtime pipeline is entirely downstream of the build pipeline:

![Five numbered panels — SOURCES, CLEAN, CHUNK, EMBED, INDEX — showing heterogeneous documents being cleaned, split, embedded as float matrices and stored.](../diagrams/13-rag-ingestion-pipeline.png)

A useful sequencing when debugging: before investigating any of the five stages here, confirm the passage exists in the index in a usable form. Roughly a third of "retrieval problems" are ingestion problems presenting as retrieval problems.

---

## Case study — Corwin & Blake, the clause that was never retrieved

Corwin & Blake, a commercial law firm, run an assistant over their precedent and contract corpus. A senior associate asked it about limitation-of-liability provisions in a specific class of supply agreement and received an answer that was fluent, well-structured, and missing the firm's standard carve-out for wilful misconduct.

The associate knew it was wrong because they had drafted that carve-out. Nobody else would have.

### The instinct, and why it was wrong

The team's first hypothesis was a generation problem. The answer read as if the model had summarised generic principles rather than the firm's position. Two days went into prompt changes — stronger instructions to rely only on retrieved material, explicit demands to quote source language.

Nothing improved. The answers stayed fluent and stayed wrong.

They then walked the five stages in order.

### Stage 1 — Question

The question was *"What limitation of liability wording do we use in managed services supply agreements?"*

Reasonably specific. One ambiguity: the firm has two managed-services templates, one for public sector and one for commercial, with materially different liability provisions. The question did not distinguish them and the assistant did not ask.

**Finding:** a real defect, but not this one. The answer was wrong in a way that applied to both templates.

### Stage 2 — Search

They queried the index directly for the known carve-out language.

**It was not there.** Not ranked low — absent. No chunk in the index contained the wilful misconduct carve-out.

This is where the investigation should have started, and it took them to the ingestion pipeline rather than the answer pipeline.

The clause library had been ingested from a set of Word documents containing the firm's standard provisions. Those documents use Word's numbered-list formatting heavily, and the carve-out lived in a nested sub-list under a main liability clause.

Their extraction had flattened the nesting. Sub-list items were being emitted without their parent context, and — because of a bug in how the extractor handled a specific list style the firm used for carve-outs — items at the third nesting level were being **dropped entirely**.

Every carve-out in the clause library, across every template, was missing from the index. About sixty provisions. The system had been running for five months.

### Why nobody noticed

The answers were never obviously broken. A liability answer without the carve-out is not nonsense — it is a correct description of the main provision, missing an exception. It reads as complete. Only someone who knew the exception existed could tell.

This is the property that makes retrieval failures dangerous in professional domains: **the failure mode of missing evidence is a confident, plausible, incomplete answer**. There is no error, no hedge, no signal.

### Stages 3, 4 and 5 — checked and clear

Having found the cause, they walked the remaining stages anyway, to establish whether anything else was wrong.

**Rerank.** They constructed a test set of thirty questions with known-correct source passages and examined the scored lists. Reranking was performing well — correct passages ranked in the top three in twenty-seven of thirty cases. Two of the three failures involved questions where the correct passage was a table, which reranked poorly, and one was a genuine near-tie between two similar provisions.

**Context.** They inspected what reached the model. They found a real inefficiency: the assembly step was including up to eight chunks with no redundancy check, and for common questions three or four of those were near-duplicates from different templates. Roughly 40% of context budget was spent on redundant content, crowding out material that would have been useful.

**Answer.** With correct evidence present, answers were accurate. The prompt changes made in the first two days were reverted; they had been treating a symptom that did not exist.

### What they fixed

**The extractor.** The list-style bug was corrected and the entire clause library re-ingested. Sixty missing provisions appeared in the index.

**A structural assertion in ingestion.** The extractor now counts list items in the source and in the output and fails the ingestion if they disagree. The original bug had been silent because nothing compared input to output.

**Redundancy filtering in context assembly.** Near-duplicate chunks are collapsed, keeping the highest-scoring representative and noting the others. This freed roughly a third of the context budget.

**Clarification on the template ambiguity.** The assistant now asks which template when a question could apply to either, rather than choosing.

**A retrieval-level evaluation set.** This is what would have caught it. Thirty questions with known-correct passages, run nightly, scoring whether the correct passage appears in the retrieved set at all — independent of what the final answer says:

![A circular loop of five panels — RETRIEVAL, FAITHFULNESS, COVERAGE, LATENCY, IMPROVE — with green ticks and red crosses on the retrieval and faithfulness panels and amber warnings on coverage and latency.](../diagrams/18-rag-evaluation-loop.png)

The retrieval metric would have shown sixty provisions with zero retrievability from the first day the clause library was ingested. Instead it took five months and an associate who happened to have drafted the missing text.

### The lesson they wrote down

*Evaluate retrieval separately from answers.* An answer-quality metric would have scored the liability responses well — fluent, on-topic, correctly citing the main provision. Only a metric asking "was the right passage retrieved?" could have detected that a whole category of content was invisible.

---

## Composition

Five tall dark rounded panels in an even row, each headed by a blue numbered circle and a white uppercase label:

**1 QUESTION → 2 SEARCH → 3 RERANK → 4 CONTEXT → 5 ANSWER**

Cyan arrows connect the panels. Within panels 2 and 3, additional dashed and solid arrows show internal fan-out and filtering.

## Element by element

**1 QUESTION**
A standing person in a thinking pose, hand to chin, beside a large **teal speech bubble containing a white question mark**. A small white card floats to the right, beginning the flow.

**2 SEARCH**
A large blue **magnifying glass** on a platform, with **dashed teal arrows** fanning outward to six small white candidate cards — three arranged upper-right, three lower. Unordered and plural.

**3 RERANK**
A tall dark board listing five rows. Each row has a **score chip** on the left and a white result card on the right. The chips read **0.92** (teal), **0.78** (teal), **0.55** (amber), **0.23** (grey) and **0.07** (grey). Three teal-outlined cards emerge on the right side, connected by short dashed arrows — the survivors.

**4 CONTEXT**
An application window with a blue title bar. Inside it, three white cards are stacked, and a **translucent teal container** sits at the base holding them. The bounded space into which evidence must fit.

**5 ANSWER**
A blue cube robot on a glowing disc, above a clean white card with a teal marker and text lines. The simplest panel in the diagram.

## Colour and flow semantics

- **Solid cyan arrows** move between stages; **dashed arrows** appear inside stages 2 and 3, marking candidate movement rather than pipeline progression.
- **Teal score chips** mark accepted candidates; **grey** marks rejected; **amber** marks the single borderline case at 0.55.
- The **translucent container** in stage 4 is the only object in the diagram drawn as a bounded volume, which is precisely its meaning.
- No coral appears. Rejection here is drawn in grey rather than coral, which reads as "not selected" rather than "refused" — an accurate distinction.

## How to present it

**Ask what happens between the question and the answer.** Most rooms describe two stages: search the index, generate. Then show the diagram and point at the three stages in between. The gap between their mental model and the picture is the session.

**Spend the most time on the scored list.** Read the five numbers aloud. Ask what the amber 0.55 means and what should happen to it. There is no correct answer, and the discussion — do you include marginal evidence and risk diluting context, or exclude it and risk missing the answer — is the real content. Then ask what their own system's cut-off is. Many teams do not know they have one.

**Ask why rerank exists at all.** If search already scored things, why score again? The answer — cheap and wide first, expensive and accurate second — is a general architectural pattern worth naming, and it explains a cost structure people otherwise find arbitrary.

**Point at the container in panel 4 and ask what happens when it is full.** Truncation policy is almost always undesigned. Ask which chunk gets dropped when eight are ranked and five fit, and whether anyone would know.

**Run the debugging drill.** This is the diagram's best use. Give the room a symptom — "the answer was fluent, confident, and missing a critical exception" — and ask which stage. Walk the diagnostic table with them. The key insight to extract: **each stage has an artefact you can inspect**, so debugging is a sequence of checks rather than a guess.

**Then tell them where to start.** Not stage 1. Start by asking whether the correct passage is in the index at all. Corwin & Blake spent two days on prompts for a problem that was an extraction bug three stages upstream.

**Make the point about silent failure.** Missing evidence does not produce an error. It produces a confident, plausible, incomplete answer. Ask the room how they would detect that in their own domain, and whether anyone except a domain expert could. In professional contexts the honest answer is usually no, which is the argument for retrieval-level evaluation.

**Timing.** Twenty-five minutes. Forty with the debugging drill, which is where the value is.

---

## Lab and checkpoint

**Lab:** Take one real RAG question-answer pair that went wrong. Walk it through the five stages of the answer pipeline and produce an artifact from each stage: the rewritten query, the scored candidate list, the reranked list with thresholds, the context container, and the final answer. Identify the first stage where the correct evidence was lost or the wrong evidence was included, and write the test that would catch it.

**Checkpoint:** Why should debugging start with whether the correct passage is in the index, not with the prompt?

**Answer:** Because a fluent, confident, wrong answer is usually caused by missing evidence, not by the prompt. If the correct passage was never retrieved, no amount of prompt engineering fixes the answer. Finding the missing evidence starts at the earliest retrieval stages.

## Glossary

- **Candidate** — a chunk retrieved as a possible answer source.
- **Context container** — the bounded set of chunks passed to the model for generation.
- **Query rewriting** — the stage that transforms the user's question into a search-friendly form.
- **Rerank** — the second scoring stage that uses a more accurate, often more expensive, model to order candidates.
- **Retrieval** — the first wide, cheap search that returns many candidates.
- **Score** — the similarity or relevance number attached to a candidate.
- **Threshold** — the cut-off score that decides which candidates are included or rejected.
- **Truncation policy** — the rule that decides which chunks to drop when the context container is full.

## Sources

- RAG answer pipeline and reranking patterns
- Dense retrieval and two-stage retrieval design
- Context-window management and truncation policies
