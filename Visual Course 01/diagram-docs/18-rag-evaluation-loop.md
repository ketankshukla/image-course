# Diagram 18 — RAG Evaluation Loop

![Five panels arranged in a circle on dark navy, connected by curved cyan arrows running clockwise — RETRIEVAL showing a database and magnifier with a results list carrying one green tick and one red cross, FAITHFULNESS showing a robot beside a document with a green tick and a red cross, COVERAGE showing a checklist and a donut chart with an amber warning triangle, LATENCY showing a speedometer nearing red and a rising trend chart with an amber warning, and IMPROVE showing a toolbox with a wrench and screwdriver.](../diagrams/18-rag-evaluation-loop.png)

**Module:** 3 — RAG evidence
**Role in the course:** evaluation and regression testing
**Layout:** closed circular loop of five stages

---

## At a glance

Four measurements and one action, arranged as a circle that never terminates: **RETRIEVAL → FAITHFULNESS → COVERAGE → LATENCY → IMPROVE →** back to the start.

This is the only closed loop in the library, and the closure is the argument. A RAG system is not tuned once and finished. The corpus changes, the questions change, the model changes, and each of those degrades quality in ways that are invisible without measurement.

---

## What the diagram teaches

### 1. Four metrics, because one number cannot see all four failures

The four measurement panels exist because a RAG system fails in four independent ways, and a single quality score conflates them into something undiagnosable.

**RETRIEVAL — did we find the right evidence?** Measured independently of what the answer said. Given a question with a known-correct source passage, was that passage in the retrieved set?

This is the metric teams most often lack and it is the most diagnostic. Retrieval failure is unrecoverable — nothing downstream can use a passage that was never retrieved — so measuring it separately tells you whether to work on ingestion and search or on everything else.

**FAITHFULNESS — does the answer match the evidence?** Every claim traceable to something retrieved, with no unsupported assertions. The panel shows a robot beside a document carrying **one green tick and one red cross**: claim-level checking, exactly as the grounding diagram requires.

![Four panels — EVIDENCE, ANSWER, CITATIONS, VERIFY — with four colour-coded sources threaded through each stage and a dashed return path through an amber shield.](../diagrams/17-grounded-citations.png)

Faithfulness is the metric that catches the fluent-and-unsupported failure, which no retrieval metric can see.

**COVERAGE — did we answer the whole question?** The panel shows a checklist beside a **donut chart with an amber warning triangle** — a partial answer. Some of what was asked is addressed; some is not.

Coverage failures are silent. An answer addressing three of four parts of a question reads as complete, because nothing signals the missing part. This is the metric that surfaces corpus gaps, and it distinguishes "we do not have this information" from "we retrieved the wrong thing."

**LATENCY — is it fast enough to be used?** A speedometer with the needle **nearing the red**, and a rising trend chart with an amber warning. Two separate signals: current latency, and the trend.

The trend is the part usually omitted. Latency degrades gradually as the corpus grows, and a system that was fast at launch becomes unusable over a year without any single change causing it.

### 2. Latency is a quality metric, not an infrastructure metric

Its inclusion alongside three correctness measures is a deliberate claim: **an accurate answer that arrives too late is not a good answer.**

The threshold is behavioural rather than technical. Past a certain wait, people stop using the system, or they start doing something else and lose the thread. A correctness improvement that doubles latency may be a net loss, and without measuring both you cannot see the trade.

Placing it in the loop makes those trades explicit. Adding a reranker improves retrieval and costs latency. Retrieving more chunks improves coverage and costs latency. Every quality lever in a RAG system has a latency price, and the loop is where you decide whether to pay it.

### 3. Green, red and amber mean different things

The four measurement panels use their colours precisely.

**RETRIEVAL and FAITHFULNESS** carry **green ticks and red crosses**. Binary per case: the passage was retrieved or it was not; the claim was supported or it was not. These are pass/fail measurements over a test set.

**COVERAGE and LATENCY** carry **amber warnings**. Degradation rather than failure. A partially covered question is not wrong. A response taking four seconds is not broken. Both are getting worse in a way that needs attention before it becomes failure.

The distinction affects how you act on them. Red is a bug to fix. Amber is a trend to watch and a budget to manage.

### 4. Improve is a stage, and it has a toolbox for a reason

The fifth panel shows the green MCP toolbox with a **wrench and screwdriver** added and a teal cube beside it.

Making it a stage rather than an outcome asserts that measurement without a change process is theatre. Plenty of teams build dashboards, look at them weekly, and change nothing, because there is no defined step where measurement becomes work.

The toolbox and hand tools carry a second meaning: improvement is *manual intervention*, not automatic. Somebody decides what to change based on what the numbers said. The four measurements tell you which of several very different actions to take:

- Poor retrieval → chunking, cleaning, or search configuration.
- Poor faithfulness → context assembly, prompt structure, or claim attribution.
- Poor coverage → the corpus itself; the content may not exist.
- Poor latency → retrieval depth, reranking cost, or infrastructure.

Four metrics, four distinct remedies. That is the payoff for measuring them separately.

### 5. The circle closes, and the closure is the point

Every other diagram in this library is a line. This one is a ring, and it is the only place where the course commits to a process rather than an architecture.

Three things guarantee that a system measured once will drift:

**The corpus changes.** Documents are added, revised, superseded. New content can change retrieval behaviour for existing questions by crowding results.

**The questions change.** Users learn what the system is good at and ask more of that, then start asking adjacent things it was never evaluated on.

**The components change.** A new embedding model, a reranker upgrade, a prompt revision, a chunking tweak. Each is an improvement in isolation and each can regress something else.

That third case is what makes this a **regression** loop rather than a tuning exercise. Without a test set that runs on every change, improvements are indistinguishable from lateral moves, and a fix for one class of question quietly breaks another.

### 6. Build the test set from real questions, and the loop needs it first

The diagram shows four measurements and does not show what they are measured against. The unstated prerequisite is a test set: real questions, with known-correct source passages, ideally with known-good answers.

Synthetic questions generated from the corpus are the common shortcut and they are misleading, because they are phrased in the corpus's vocabulary. Real users do not use the corpus's vocabulary — that mismatch is precisely the retrieval problem you are trying to measure.

---

## Case study — Lumen Support, the eight-month drift

Lumen sells a project management product to about eleven thousand business customers. Their support assistant answers customer questions from a knowledge base of roughly 900 articles plus release notes.

It launched well. Support ticket deflection was around 34% in the first quarter, which beat the target. Then nobody measured anything for eight months.

### What they found when they finally measured

Deflection had fallen to 19%. Nobody had noticed, because it declined a little each month and there was no baseline to compare against — the 34% was a launch number in a slide deck, not a tracked metric.

They built a test set of 200 real questions drawn from support tickets, each with a support engineer identifying the correct knowledge base article and, where relevant, the specific section. Then they measured all four dimensions.

### Retrieval — 71%, and falling for a specific reason

Correct passage in the top five for 71% of the test set. At launch, spot checks had suggested around 90%.

The cause was corpus growth. The knowledge base had grown from 900 to about 1,600 articles, and much of the growth was near-duplicate content — separate articles for each product tier describing nearly identical features with small differences.

A question about a feature now retrieved five articles about that feature across five tiers, one of which was correct for the asking customer. Retrieval was finding the right *topic* and the wrong *variant*.

**The fix** was not a search change. It was corpus hygiene: tier-specific articles were consolidated into single articles with tier-conditional sections, cutting the article count to about 1,100. Retrieval recovered to 88%.

The diagnostic value of measuring retrieval separately is what made this findable. An answer-quality metric would have scored these responses as plausible — they described a real feature accurately, just the wrong tier's version.

### Faithfulness — 94%, and the 6% mattered

Claim-level checking on a sample found 94% of claims traceable to retrieved content.

The 6% clustered. Almost all were in answers about features that had changed recently. The knowledge base had the current behaviour; the model's parameters had the old behaviour from training data; and when retrieved content was thin, the model filled gaps from what it knew.

The most serious instance involved a feature whose default had been inverted in a release. The assistant described the old default, confidently, in an answer that also contained correct retrieved claims.

**The fix** was context assembly plus a prompt change: when retrieved content for a question is below a confidence threshold, the assistant says the knowledge base does not clearly cover it rather than answering. Faithfulness went to 99%; the number of answered questions fell about 7%.

Support leadership regarded that trade as obviously correct. A wrong answer generates a ticket *and* destroys trust; a "not covered" answer generates a ticket.

### Coverage — 62%, and this was the real finding

Only 62% of test questions were fully answered. Nearly a third received partial answers that addressed some of what was asked.

Analysis of the gaps found that the missing content was concentrated: integration configuration, permissions and roles, and anything involving the API. Three areas where the knowledge base was genuinely thin, because they were the areas the documentation team found hardest to write.

**The fix** was not technical at all. The coverage report went to the documentation team as a prioritised backlog of what customers were asking that the corpus could not answer. Forty new articles over a quarter, targeted at measured gaps rather than guessed ones.

Coverage went to 84%. This is the metric that produced the largest business impact and it required no engineering.

### Latency — median 3.1s, p95 8.4s, and trending badly

Median had been about 1.4 seconds at launch. The trend chart was the alarming part: latency was rising roughly 8% per month, tracking corpus growth.

The cause was retrieval depth. As the corpus grew and retrieval quality dropped, an earlier engineer had increased the number of retrieved chunks from 5 to 20 to compensate — which improved recall slightly and increased reranking cost fourfold.

**The fix** followed from fixing retrieval properly. With the corpus consolidated and retrieval back at 88%, depth was returned to 8. Median dropped to 1.7 seconds.

This is the clearest illustration of why the four metrics belong in one loop: a latency problem was caused by a compensation for a retrieval problem that was caused by a corpus problem. Measuring any one of them in isolation would have led to the wrong fix.

### The loop they run now

- **Nightly:** the full 200-question test set, retrieval and latency measured automatically. Any regression beyond threshold blocks the next deploy.
- **Weekly:** faithfulness sampled on 50 real production answers, checked by a support engineer.
- **Monthly:** coverage recomputed, with the gap report going to the documentation team.
- **Quarterly:** the test set is refreshed with 40 new questions from recent tickets, so it tracks what customers are actually asking rather than what they asked a year ago.

That last practice is the one they consider most important. A static test set becomes a measurement of a system's performance on historical questions, which drifts away from reality at exactly the rate the product changes.

### Where they ended

Deflection recovered to 41% — above the launch figure. The team's own account of why is worth quoting in spirit: the system was never actually good, it was only ever *unmeasured*. The 34% launch figure was a spot check on a small corpus with early adopters asking simple questions.

---

## Composition

Five panels are arranged in a ring around an empty centre, connected by **curved cyan arrows running clockwise**:

**RETRIEVAL** (top) **→ FAITHFULNESS** (right) **→ COVERAGE** (lower right) **→ LATENCY** (lower left) **→ IMPROVE** (left) **→** back to RETRIEVAL.

Each panel sits on an angled blue platform with a white uppercase heading. The empty centre and the unbroken ring make the closure unmistakable.

## Element by element

**RETRIEVAL**
A blue database stack with a **teal magnifying glass**, beside a results list of three cards — one marked with a **green check**, one with a **red ✗**. Pass/fail per case.

**FAITHFULNESS**
A blue cube robot on a glowing disc, beside a white document with text lines carrying a **green check** and a **red ✗**. Claim-level verification against retrieved evidence.

**COVERAGE**
A white checklist with teal bullet rows, beside a **donut chart** segmented in teal, blue and dark blue, carrying an **amber warning triangle**. Partial completion.

**LATENCY**
A **speedometer** with a teal-to-red arc and the needle approaching red, beside a dark panel showing a **rising trend line** with an **amber warning triangle**. Current value and direction of travel.

**IMPROVE**
The green MCP toolbox with database, gear and **wrench** tiles, accompanied by a large grey **wrench and screwdriver** and a teal cube. Hand tools — manual intervention.

## Colour and flow semantics

- **Curved cyan arrows** run clockwise with no exit. The ring never terminates.
- **Green ticks and red crosses** appear in the two binary metrics — retrieval and faithfulness.
- **Amber warning triangles** appear in the two degradation metrics — coverage and latency — marking trends rather than failures.
- **IMPROVE is the only panel with no measurement iconography.** It is the action stage, and it is drawn with tools rather than indicators.
- The empty centre is compositionally deliberate: there is no single quality score at the middle of these four metrics.

## How to present it

**Ask what their RAG quality metric is.** Most rooms have one number or none. Then show four panels and ask which failure each one catches. The realisation that a single score cannot distinguish "we did not find it" from "we found it and misused it" is the session's opening.

**Ask specifically whether they measure retrieval separately from answers.** This is the highest-value question in the whole RAG module. Most do not. Then give them the Corwin & Blake case — sixty missing provisions, invisible for five months, because every answer scored well while omitting content that had never been retrievable.

**Ask what an amber triangle means versus a red cross.** Push until the room separates failure from degradation. Coverage and latency degrade; retrieval and faithfulness fail. The two need different responses and different thresholds.

**Argue about latency being in the list.** Someone usually objects that it is an infrastructure concern. The counter is a question: would you take a five-point accuracy improvement for three extra seconds? Then: how would you know if you had already made that trade accidentally? Lumen made it without deciding to.

**Point at the toolbox and ask who does that.** Measurement with no owner of the improvement stage is a dashboard nobody acts on. Ask what happens when a number goes red — is there a defined step, or a conversation?

**Trace the Lumen causal chain.** Corpus growth → retrieval degraded → someone increased depth to compensate → latency degraded. Ask which metric they would have been looking at, and what they would have fixed. Most rooms say latency, and would have optimised infrastructure for a corpus problem two steps upstream. This is the clearest argument for measuring all four together.

**Ask where their test set comes from.** If the answer is generated from the corpus, explain the vocabulary trap: synthetic questions use the corpus's language, real users do not, and that gap is the thing you are trying to measure. Then ask how often it is refreshed. Static test sets measure last year's system.

**Close on the circle.** Ask what happens if you stop. Lumen's answer — eight months, deflection halved, nobody noticed — is the whole case for closure.

**Timing.** Twenty-five minutes. Forty if you audit which of the four they currently measure, which usually produces an uncomfortable and useful table.

---

## Lab and checkpoint

**Lab:** Audit your own RAG system against the four metrics in the diagram — retrieval, faithfulness, coverage, and latency — and write what you currently measure, what tool or dashboard owns it, and who acts when it degrades. For any metric that is missing or unowned, design the smallest test that would add it and the threshold that would trigger improvement.

**Checkpoint:** Why is a single quality score not enough for a RAG system?

**Answer:** Because one score cannot distinguish "we did not find the evidence" from "we found it but misused it." Retrieval and faithfulness are binary failures; coverage and latency are degradations. They need different thresholds and different responses, so they must be measured separately.

## Glossary

- **Coverage** — the metric that tracks how much of the relevant corpus the system can retrieve.
- **Faithfulness** — the metric that checks whether the answer uses retrieved evidence correctly.
- **Improvement** — the action stage where a person or team changes the system based on metrics.
- **Latency** — the time it takes to produce an answer.
- **Metric** — a measured property of the RAG pipeline.
- **Retrieval** — the metric that checks whether the correct evidence is found.
- **Test set** — the set of questions and expected answers used to evaluate the system.
- **Vocabulary trap** — the problem where synthetic test questions use the corpus's language and fail to match real user phrasing.

## Sources

- RAG evaluation and retrieval-versus-generation metrics
- Faithfulness and coverage measurement in generation systems
- Continuous evaluation and test-set refresh practices
