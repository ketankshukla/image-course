# Diagram 69 — Stage-by-Stage Quality Metrics

![A metrics breakdown on dark navy. At the top, a bordered panel reads END-TO-END SCORE with a teal gauge showing 87/100. Cyan arrows fan down to six numbered stages — UNDERSTAND, RETRIEVE, PLAN, TOOL, SYNTHESIZE, DELIVER — each with a white metric card beneath: ROUTE ACCURACY 85/100, RECALL AND PRECISION 82/100, PLAN VALIDITY 88/100, TOOL SUCCESS 83/100, GROUNDEDNESS 84/100, USER OUTCOME 90/100. Below each card a coral line drops to a red ✗ badge, and all six converge on a coral banner reading FINAL FAILURE.](../diagrams/69-stage-by-stage-quality-metrics.png)

**Module:** Evaluation and operations
**Role in the course:** why one score is not enough
**Layout:** a single end-to-end score fanning down to six stage metrics, each with a failure path converging on one outcome

---

## At a glance

One number at the top — **87/100** — and six numbers beneath it: **85, 82, 88, 83, 84, 90**.

Beneath those, six coral lines drop to red ✗ badges and converge on a single banner: **FINAL FAILURE**.

The composition makes an argument that a dashboard cannot. The 87 is an average of six things, **any one of which can produce a total failure on its own**. A respectable aggregate and a broken system are entirely compatible.

---

## What the diagram teaches

### 1. Six stages, six different metrics, and they are not interchangeable

Each stage gets a metric that measures **that stage's specific job**:

**1 UNDERSTAND → ROUTE ACCURACY.** Did the system correctly identify what kind of request this is and where it should go?

**2 RETRIEVE → RECALL AND PRECISION.** Did retrieval find what was needed, and was what it found relevant?

**3 PLAN → PLAN VALIDITY.** Is the decomposition sound? Right steps, right order, nothing missing.

**4 TOOL → TOOL SUCCESS.** Did the calls succeed, with the right arguments, returning usable results?

**5 SYNTHESIZE → GROUNDEDNESS.** Does the answer rest on what was retrieved and returned?

**6 DELIVER → USER OUTCOME.** Did the user get something they could act on?

These measure genuinely different properties. Route accuracy says nothing about groundedness. Tool success says nothing about plan validity. Averaging them produces a number that describes none of them.

### 2. The failure lines are the diagram's real content

Every metric card has a **coral line dropping to a red ✗**, and all six converge on **FINAL FAILURE**.

The claim: **a failure at any single stage produces a failed request**, regardless of how well the other five performed.

That is what makes an aggregate misleading. The stages are not additive — they are a chain. A request that routes perfectly, retrieves perfectly, plans perfectly, calls tools perfectly, and then produces an ungrounded answer has failed. The user does not receive 5/6 of an answer.

Drawing all six failure lines converging on one banner makes the chain structure visible in a way a scorecard does not.

### 3. The six numbers are deliberately similar, and that is the trap

85, 82, 88, 83, 84, 90. All respectable. All within eight points of each other.

That flatness is realistic and it is the reason stage metrics need thresholds rather than eyeballing. Nothing here looks alarming. The lowest is retrieval at 82 and it is not obviously a problem.

But if the six were multiplicative rather than averaged — which is closer to how a chain behaves — the compound figure would be far below 87.

The useful framing: **an aggregate tells you how the system is doing on average; stage metrics tell you where it is weakest.** Only the second is actionable.

### 4. The fan-out direction is from the aggregate to the stages

The cyan arrows run **downward from the 87** to the six stages, not upward from the stages to the 87.

That direction is a reading instruction: **start with the aggregate, then decompose.** The 87 is where you look first and it is not where you stop.

It also implies the correct diagnostic motion. A drop in the aggregate should immediately produce the question "which of the six moved?" — and the answer is one query, not a hunt.

### 5. Route accuracy is the metric most systems lack

Of the six, stage 1 is the one teams least often measure.

The others have obvious instrumentation: retrieval has known-correct passages, tools have success codes, groundedness has citations, user outcome has feedback. Routing — did we correctly work out what this request *is* — usually has nothing.

Its absence is costly, because a routing failure produces a downstream failure that looks like something else. A request routed to the wrong handler will show poor retrieval, an invalid plan, and a bad outcome, and none of those is the actual fault.

Measuring any of the six requires a set to measure against:

![A seven-stage loop from REAL CASES tagged NORMAL, EDGE, ADVERSARIAL and ABSTAIN, through REDACT AND CURATE, GOLDEN DATASET, RUN SYSTEM, SCORE OUTPUT, REVIEW FAILURES and ADD REGRESSION CASES, with a dashed IMPROVED CASES return.](../diagrams/68-golden-datasets-and-eval-harness.png)

Route accuracy in particular needs cases with a **human-assigned correct route**, which is an addition to the golden dataset rather than something derivable from existing cases.

### 6. User outcome is the only metric that is not about the system

Stage 6 measures whether the **user got something they could act on**.

That is a different kind of measurement from the other five. The first five are internal properties you can compute. User outcome requires evidence from outside the system: did they proceed, did they escalate, did they come back with the same question, did they say it helped.

Note that it scores **90 — the highest in the set**, above every internal metric. That combination is worth pointing at: users can be satisfied with a system that is internally mediocre, and internal excellence does not guarantee a satisfied user. Both directions occur.

---

## Case study — Wrenfield Legal Aid, the 87 that hid a routing collapse

Wrenfield operates a legal advice service for people who cannot afford solicitors — housing, welfare benefits, employment, and immigration. Their assistant helps advisers find applicable law and guidance, and is used by about 140 advisers across nine offices.

They measured a single quality score, computed weekly from a rubric applied to sampled outputs. It sat between 84 and 89 for eight months.

### What the score did not show

Housing advice quality had collapsed.

Specifically: questions about **disrepair claims** were being answered with material about **possession proceedings**. Both are housing law. Both involve tenants and landlords. Both draw on overlapping legislation.

An adviser asking about a tenant's rights when a landlord refuses to fix damp was receiving accurate, well-sourced, properly cited material about defending an eviction.

The answers were correct — about possession proceedings. They were grounded, complete and fluent. The rubric scored them well, because the rubric assessed the quality of the answer given, not whether it answered the question asked.

### The cause

A reindexing three months earlier had changed how housing content was chunked. Disrepair guidance and possession guidance, which had previously been separately retrievable, now shared enough vocabulary in their chunk boundaries that the router — which selected a specialist retrieval path based on question classification — was misclassifying disrepair questions as possession questions about 40% of the time.

Everything downstream then worked correctly on the wrong question.

### Why eight months

Two reasons, both instructive.

**The aggregate absorbed it.** Housing is one of four practice areas. A 40% failure rate in one sub-topic of one area moved the overall score by about two points, well inside its normal variation.

**No stage metric existed for routing.** They measured answer quality. A misrouted question produces a high-quality answer, so the metric was blind to it by construction.

Advisers had noticed, in the way people notice something slightly wrong without escalating it. Three had mentioned to colleagues that the assistant was "a bit off on damp cases." Nobody raised it formally because each individual answer looked competent.

### The rebuild

**Six stage metrics, matching the diagram.**

**Route accuracy** was the new one and the one that found the problem immediately. They built a set of 300 questions with human-assigned correct routes. First measurement: **overall 88%, housing 61%, disrepair sub-topic 58%.**

The number that had been invisible for eight months was visible in a day.

**Thresholds per stage, not per aggregate.** Each metric has a floor and an alerting threshold. The aggregate is still reported, and it is not what pages anyone.

**Per-topic breakdown within each stage.** This was the second important change. Route accuracy at 88% overall is fine. Route accuracy at 58% for one sub-topic is not, and only a breakdown shows it.

They now report every stage metric by practice area and by major sub-topic. It is more numbers, and the numbers are where the failures actually live.

**User outcome measured separately.** They added a lightweight adviser signal — did this answer the question, yes/no/partly — attached to each interaction.

It found something the internal metrics did not: **an answer could score well on all five internal dimensions and still be unusable**, because it addressed the law correctly at a level of generality that did not help with the specific case in front of the adviser.

Their groundedness was 89 and their user outcome was 71. The gap was the finding.

### The fix and the aftermath

The chunking change was reverted and redone with explicit topic boundaries. Route accuracy for disrepair went from 58% to 94%.

They also added a **routing confidence display**: where the router is not confident, the assistant tells the adviser which area it interpreted the question as, so a misroute is visible rather than silent.

That single interface change is what makes the residual 6% survivable.

### Results

- **Route accuracy, disrepair:** 58% → 94%.
- **Time to detect a stage-level regression:** eight months → under a day.
- **User outcome:** 71 → 86, after the generality problem was addressed separately.
- **Aggregate score:** moved from 87 to 89, which understates everything above.

That last figure is the argument for the whole diagram. The change that fixed a collapsed sub-topic and raised user outcome by fifteen points moved the headline number by two.

### The line in their quality documentation

*The aggregate is a summary for people who are not going to do anything. The stage metrics are for people who are.*

---

## Composition

A top-down fan-out with a bottom-up convergence.

**Top:** a bordered panel reading **END-TO-END SCORE** containing a **teal arc gauge** with **87** and **/100** beneath.

**Middle:** six **cyan arrows** fan downward to six numbered stages — **1 UNDERSTAND**, **2 RETRIEVE**, **3 PLAN**, **4 TOOL**, **5 SYNTHESIZE**, **6 DELIVER** — each a teal icon pair on a blue platform, connected left to right by small cyan arrows.

**Beneath each stage:** a white metric card with a teal circular icon, a metric name, a teal progress bar, and a score.

**Bottom:** from each card, a **coral line** descends to a **red circular ✗**, and all six converge into a **coral banner reading FINAL FAILURE**.

## Element by element

**END-TO-END SCORE** — a teal arc gauge reading **87/100**.

**1 UNDERSTAND** — a teal question bubble and a document. Metric: a brain icon, **ROUTE ACCURACY 85/100**.

**2 RETRIEVE** — teal database cylinders with a magnifier. Metric: a target icon, **RECALL AND PRECISION 82/100**.

**3 PLAN** — a card showing a branching path with ✗ markers. Metric: a clipboard icon, **PLAN VALIDITY 88/100**.

**4 TOOL** — a teal gear beside a `</>` card. Metric: a wrench icon, **TOOL SUCCESS 83/100**.

**5 SYNTHESIZE** — a document beside a teal cube. Metric: a chain-link icon, **GROUNDEDNESS 84/100**.

**6 DELIVER** — a teal person disc beside a checked card. Metric: a person icon, **USER OUTCOME 90/100**.

**FINAL FAILURE** — a coral rounded banner, fed by six converging coral lines.

## Colour and flow semantics

- **Cyan arrows** fan downward from the aggregate to the stages — a decomposition instruction.
- **Coral lines** rise from every metric to one banner — the chain structure made visible.
- **Teal** marks every stage icon, every metric icon and every progress bar.
- The **six similar scores** are deliberately flat, so nothing stands out by inspection.
- The aggregate sits **above** the stages rather than beside them, marking it as a summary of them.

## How to present it

**Show only the 87 first.** Ask whether this system is healthy. Most rooms say yes, or "reasonably." Then reveal the six stages and the six failure lines.

**Ask what the 87 is an average of.** Six different properties measuring six different things. Then ask what a 5-point drop in the aggregate tells you. Nothing about where.

**Point at the converging coral lines.** Any one stage failing produces a failed request. The stages are a chain, not a sum — the user does not receive five-sixths of an answer.

**Ask which of the six they measure.** Retrieval, tool success and sometimes groundedness are common. **Route accuracy** is the one almost nobody has, and its absence is diagnostic: a misroute produces a downstream failure that looks like something else.

**Tell the Wrenfield disrepair story.** Correct, grounded, well-cited answers about possession proceedings, delivered to advisers asking about damp. Eight months. The rubric measured answer quality, not whether it answered the question.

**Then give them the two reasons it hid.** The aggregate absorbed a 40% failure in one sub-topic as a two-point move. And no metric existed for the stage that had failed.

**Make the per-topic point.** Route accuracy at 88% overall, 58% for one sub-topic. Stage metrics without a breakdown hide the same way aggregates do, one level down.

**Ask about user outcome versus the internal five.** Wrenfield's groundedness was 89 and user outcome 71 — technically excellent answers pitched at a generality that did not help. Both directions occur, and only measuring the external signal shows it.

**Close on the aggregate movement.** The fix that repaired a collapsed sub-topic and raised user outcome fifteen points moved the headline from 87 to 89. Ask what the room's headline number would have done.

**Timing.** Twenty-five minutes. Thirty-five if you map the six metrics onto the room's own pipeline and identify which stage has none.

---

## Lab and checkpoint

**Lab:** Map the six stages of your own answer pipeline: understand, retrieve, plan, tool, synthesize, deliver. For each, define a metric and a per-topic breakdown. Then run a set of real cases and identify which stage has the worst score in one topic, even if the aggregate looks healthy.

**Checkpoint:** Why is an end-to-end score of 87 misleading?

**Answer:** Because it is an average of six different properties. A single bad stage can produce a failed answer, and the aggregate can hide a 40% failure in one sub-topic as a two-point move. Stages are a chain, not a sum.

## Glossary

- **Aggregate score** — the single overall number, such as 87/100, which hides per-stage variation.
- **Deliver** — the final stage that presents the answer to the user.
- **End-to-end score** — the headline metric summarising the whole pipeline.
- **Final failure** — the convergence point where any stage failure becomes a failed answer.
- **Groundedness** — the metric that checks answers are tied to sources.
- **Plan** — the stage that decides how to answer.
- **Recall and precision** — the retrieval metric.
- **Retrieve** — the stage that fetches evidence.
- **Route accuracy** — the metric that checks the system routed the question to the right topic.
- **Synthesize** — the stage that composes the answer from evidence.
- **Tool success** — the metric that checks tool calls worked.
- **Understand** — the first stage that interprets the user's question.
- **User outcome** — the external signal of whether the answer helped.

## Sources

- Stage-level evaluation and per-topic breakdowns
- Chain-of-quality metrics for agent pipelines
- User-outcome measurement beyond technical scores
