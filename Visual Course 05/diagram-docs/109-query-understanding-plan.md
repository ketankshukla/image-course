# Diagram 109 — Query Understanding and Plan

![A USER QUESTION banner on dark navy feeds a wide QUERY UNDERSTANDING bar. Five white cards descend from it — INTENT with a target, ENTITIES with a database and person, FILTERS with a funnel, TIME with a calendar and clock, AMBIGUITY with a question mark. Teal lines from these feed four action platforms — DIRECT QUERY with a magnifier, REWRITE with a pencil, DECOMPOSE with cubes, CLARIFY with a speech bubble — which converge on a teal ORIGINAL QUESTION platform. A coral dashed line runs right from query understanding to UNSAFE ASSUMPTION, a red warning tile, and on to BLOCKED.](../diagrams/109-query-understanding-plan.png)

**Module:** Query and retrieval
**Role in the course:** what to extract from a question before searching
**Layout:** one question into five extractions, producing one of four actions, with an unsafe-assumption block

---

## At a glance

A question is decomposed into five things — **INTENT, ENTITIES, FILTERS, TIME, AMBIGUITY** — and those five determine which of four actions to take: **DIRECT QUERY, REWRITE, DECOMPOSE, CLARIFY**.

All four converge on a teal **ORIGINAL QUESTION** platform.

And a coral path leads from query understanding to **UNSAFE ASSUMPTION** and then **BLOCKED**.

Two claims worth arriving at. The original question is retained regardless of what the system does to it. And filling an ambiguity with an assumption is a blocked outcome, not a fallback.

---

## What the diagram teaches

### 1. Five extractions, and each one changes what you search for

**INTENT** — a target. What kind of answer is wanted. A definition, a procedure, a value, a comparison, a decision. Intent determines which sources are relevant before any matching happens.

**ENTITIES** — a database with a person. The specific things named. A customer, a product, a policy, a case reference. Entities are what filters get built from.

**FILTERS** — a funnel with list rows. Constraints narrowing the search. Document type, jurisdiction, status, category.

**TIME** — a calendar with a clock. When. This is the extraction most systems omit entirely, and the temporal retrieval diagram later in the volume is entirely about what it enables.

**AMBIGUITY** — a question mark. What is unclear. Not an absence of information; a positive finding that something could mean more than one thing.

The fifth is the one that makes the others safe. Extracting intent, entities, filters and time without noticing ambiguity produces a confident search for the wrong thing.

### 2. TIME is a first-class extraction, and its presence here is unusual

Most query-understanding designs extract intent and entities and stop.

Time appears as its own card because a question frequently carries a temporal qualifier that changes the answer entirely: *"what was the rate last April"*, *"under the previous policy"*, *"as things stood when the claim was made."*

A system that ignores it answers with current content, which is a different question.

The card's calendar-and-clock pairing hints at the distinction the temporal diagram develops: business time versus record time.

### 3. Four actions, and they are responses to different findings

**DIRECT QUERY** — the question is clear and searchable as asked. Proceed.

**REWRITE** — the question is clear but its vocabulary does not match the corpus. Translate it. *"Time off"* becomes *"annual leave."*

**DECOMPOSE** — the question contains several distinct questions. Split it. One retrieval cannot serve a compound question well.

**CLARIFY** — the question is ambiguous in a way that matters. Ask.

Note the escalation. Direct query does nothing. Rewrite changes the words. Decompose changes the structure. Clarify involves the user.

### 4. The four actions converge on ORIGINAL QUESTION, and that is the diagram's quiet centrepiece

All four teal lines meet at a platform holding a document glyph, labelled **ORIGINAL QUESTION**, rendered in teal.

Whatever the system did — rewrote the terms, split it into three, asked a clarifying question — the question as the user asked it is preserved.

Three reasons that matters.

**Verification.** An answer must be checkable against what was actually asked, not against the system's reformulation.

**Debugging.** When an answer is wrong, you need to see both the original and the transformation to know which was at fault.

**Trust.** Showing a user "you asked X; I searched for Y" is the difference between a system that helps and one that quietly substitutes.

### 5. UNSAFE ASSUMPTION is a blocked outcome, and the pairing is the point

The coral path runs **QUERY UNDERSTANDING → UNSAFE ASSUMPTION → BLOCKED**.

An unsafe assumption is what happens when the system resolves an ambiguity by picking. The user said "the policy"; there are three; the system chose the most recently updated one and proceeded.

That is not an error. It produces an answer. The answer is about a policy the user may not have meant, and nothing indicates the choice was made.

Drawing it as **BLOCKED** rather than as a warning is the strong position: where an ambiguity is material, the system does not guess. It clarifies, or it stops.

### 6. AMBIGUITY feeding CLARIFY is the only extraction with a dedicated action

Trace the teal lines. Intent, entities, filters and time all contribute to direct query, rewrite and decompose.

Ambiguity is what drives clarify.

That is the structural relationship: four extractions tell you *what* to search for; the fifth tells you whether you can search at all.

### 7. Not every ambiguity is material, and the diagram does not say which

An honest gap.

*"What's the refund policy"* is ambiguous — which product line, which region, which customer tier — and frequently the answer is the same regardless.

*"What's the contribution rate"* is ambiguous in a way that changes the answer entirely.

The distinction is domain knowledge, and getting it wrong in either direction is bad: clarifying everything makes the system exhausting, and clarifying nothing produces confident wrong answers.

Which of the two errors you prefer depends on what a wrong answer costs.

**DECOMPOSE** is the action with the largest downstream consequence, because a decomposed question becomes a sequence of retrievals:

![A question fanning to HOP 1 FIND POLICY, HOP 2 FIND PRODUCT CLASS and HOP 3 VERIFY PURCHASE, each producing evidence and a next query, feeding a STOP GATE listing ANSWERABLE, MAX 3 HOPS, BUDGET and NO NEW EVIDENCE, with a coral LOOP BLOCKED return.](../diagrams/113-bounded-multihop-retrieval.png)

The named hops there are what a decomposition produces. A decompose action with no stop gate is how a query-understanding stage turns into an unbounded loop.

---

## Case study — Kirkham Occupational Pensions, the scheme nobody named

Kirkham administers occupational pension schemes for 240 employers, covering about 190,000 members. Their assistant supports administrators answering member queries.

The corpus is scheme-specific: 240 sets of rules, many of which have several sections and most of which have changed over time.

### The problem their questions have

An administrator handling a member call asks a question in the context of that member's scheme, and does not say which scheme it is — because they are looking at it on another screen.

*"What's the normal retirement age?"*

There are 240 answers.

### What the first version did

It searched, found the most relevant match across the whole corpus, and answered.

The most relevant match was usually the scheme whose rules were most clearly written, most recently ingested, or most frequently retrieved — none of which correlates with the scheme the administrator was asking about.

### The audit

They sampled 500 queries and had administrators assess whether the answer applied to the scheme they had been working on.

**On 34% of queries, the answer came from a different scheme.**

Most were caught. Administrators know their schemes and noticed when a figure looked wrong.

**On roughly 4%, it was not caught** — cases where the wrong scheme's answer was plausible for the right scheme.

Kirkham identified eleven instances over eighteen months where a member had been given incorrect information. Two had made decisions on it: one member had deferred taking benefits based on an incorrect normal retirement age.

### The rebuild around query understanding

**Five extractions, with entities carrying scheme identity.**

The critical change: **scheme identity is not extracted from the question.** It is taken from the administrator's session context — which member's record they have open.

That is a server-trusted value in the same sense as the tenant identity in the previous diagram. It cannot be wrong because the administrator did not have to state it.

Where no member record is open, the scheme becomes an ambiguity.

**Ambiguity classified by materiality.** Kirkham's rules team classified their question types into three groups:

*Scheme-invariant* — the answer is the same across all schemes. Statutory minimums, HMRC limits, general process. About 20% of questions. No clarification needed.

*Scheme-specific* — the answer depends entirely on the scheme. Retirement ages, accrual rates, contribution levels, benefit structures. About 65%. Clarification mandatory if the scheme is unknown.

*Scheme-specific-but-usually-aligned* — the answer usually matches across schemes but not always. About 15%. This was the hard category.

For the third group they answer with the scheme identified where known, and where unknown they answer with an explicit statement of which scheme's rules the answer draws on and a prompt to confirm.

**Time extraction added.** A member asking about their entitlement is asking under the rules in force when they accrued it, which may be three scheme versions ago.

Their assistant now extracts temporal qualifiers and, where absent for a benefit question, asks. *"Are you asking about current rules, or the rules that applied when the member joined?"*

That question turned out to be one administrators frequently needed prompting to consider themselves.

**The original question is retained and displayed.** The interface shows what was asked and what was searched:

> You asked: *What's the normal retirement age?*
> Searched: normal retirement age · Scheme: Harwood Engineering Pension Scheme · Rules version effective 2019-04-06

Administrators check that line. It is where they catch the scheme being wrong.

**Unsafe assumptions block.** Where the scheme is unknown and the question is scheme-specific, the assistant does not answer. It asks.

That produces about 90 clarification prompts a day across their administration team. Their operations manager regards it as the correct cost.

### The finding they had not anticipated

Displaying the searched-for interpretation caught a category of error that had nothing to do with schemes.

Administrators noticed the assistant searching for a rules version that was not the one they expected — cases where a scheme had a recent amendment the administrator had not been aware of.

That prompted a change to how amendments are communicated internally. The assistant had become a channel for surfacing rule changes to the people who needed to know about them.

### Results

- **Answers from the wrong scheme:** 34% → under 1%.
- **Uncaught wrong-scheme answers:** ~4% → 0 known.
- **Clarification prompts:** ~90/day, accepted as correct.
- **Members given incorrect information:** 11 over eighteen months → 0 in the following year.
- **Rule amendments surfaced to administrators via the searched-for line:** an unplanned benefit, now a deliberate one.

### The line in their operations manual

*If you did not tell it which scheme, and the answer depends on the scheme, it will ask. That prompt is the system working.*

---

## Composition

A vertical flow from question through extraction to action, with a coral block to the right.

**Top:** **USER QUESTION** — a blue banner with a person glyph.

**Second:** a wide blue **QUERY UNDERSTANDING** bar.

**Third:** five **cyan arrows** descend to five white cards — **INTENT** (blue target), **ENTITIES** (database with a person), **FILTERS** (funnel with list rows), **TIME** (calendar with a clock), **AMBIGUITY** (question mark).

**Fourth:** **teal lines** from the five cards converge and fan to four blue action platforms — **DIRECT QUERY** (magnifier), **REWRITE** (pencil), **DECOMPOSE** (cubes), **CLARIFY** (speech bubble).

**Fifth:** **teal lines** from all four converge on **ORIGINAL QUESTION** — a teal platform with a document glyph.

**Right:** a **coral dashed line** from the query understanding bar to **UNSAFE ASSUMPTION** — a red tile with a warning triangle — then a coral arrow down to **BLOCKED**, a red tile with a prohibition sign.

## Element by element

**INTENT** — a target. What kind of answer is wanted.
**ENTITIES** — a database with a person. What is named.
**FILTERS** — a funnel. What narrows the search.
**TIME** — a calendar with a clock. When.
**AMBIGUITY** — a question mark. What is unclear.

**DIRECT QUERY** — proceed as asked.
**REWRITE** — translate the vocabulary.
**DECOMPOSE** — split a compound question.
**CLARIFY** — ask the user.

**ORIGINAL QUESTION** — a teal platform retaining what was asked.

**UNSAFE ASSUMPTION → BLOCKED** — the coral path.

## Colour and flow semantics

- **Cyan arrows** carry the decomposition from the question into the five extractions.
- **Teal lines** carry the extractions into actions and all actions back to the original question.
- **Coral** marks the unsafe-assumption path and its blocked terminal.
- **ORIGINAL QUESTION is rendered in teal**, marking it as verified and retained rather than as a processing stage.
- The five extraction cards are **white and identically sized**, presenting them as equal-weight findings.

## How to present it

**Read the five extractions and ask which their system does.** Intent and entities are common. Filters sometimes. **Time** is usually absent. **Ambiguity** almost always is.

**Ask what ambiguity extraction is for.** It is a positive finding, not an absence. Then note that it is the only extraction with a dedicated action.

**Walk the four actions as an escalation.** Do nothing, change the words, change the structure, involve the user.

**Point at the convergence on ORIGINAL QUESTION.** Whatever was done, the question as asked is retained. Then give the three reasons: verification, debugging, trust.

**Ask what BLOCKED means here.** Where an ambiguity is material, the system does not guess. Then contrast with what guessing produces — an answer about something the user may not have meant, with nothing indicating a choice was made.

**Tell the Kirkham scheme problem.** 240 schemes, administrators who do not name theirs because it is on another screen, and 34% of answers coming from a different scheme.

**Give them the server-trusted resolution.** Scheme identity comes from the open member record, not from the question. The administrator did not have to state it, so it cannot be wrong.

**Introduce materiality classification.** Scheme-invariant, scheme-specific, and scheme-specific-but-usually-aligned. Ask the room to classify their own question types. The third category is the hard one.

**Read the searched-for line aloud.** *You asked X. Searched: Y, scheme Z, rules version W.* Then note that administrators check that line and it is where they catch errors.

**Tell the unplanned finding.** Displaying the interpretation surfaced rule amendments administrators had not known about. A transparency feature became a communication channel.

**Ask about the clarification cost.** 90 prompts a day. Whether that is acceptable depends on what a wrong answer costs, and Kirkham's cost was a member deferring benefits on incorrect information.

**Timing.** Twenty-five minutes. Thirty-five if you classify the room's question types by materiality, which is the exercise that determines their clarification threshold.

---

## Lab and checkpoint

**Lab:** Pick five real questions from your users. Extract intent, entities, filters, time, and ambiguity for each. Classify the ambiguity as material or not. For each, choose one of the four actions: do nothing, rewrite query, rewrite plan, or ask for clarification. Then write the "searched-for" line that shows the original question, the resolved scheme, and the version.

**Checkpoint:** Why is ambiguity the only extraction with a dedicated action?

**Answer:** Because ambiguity is a finding that requires a decision. It is not a missing piece that can be filled by default. The other extractions affect how the query is run, but ambiguity may require the system to stop and ask the user what they mean.

## Glossary

- **Ambiguity** — a query whose meaning is not clear enough to answer.
- **Clarify** — the action of asking the user to resolve an ambiguity.
- **Entities** — the specific objects named in the query.
- **Extraction** — the process of pulling structured information from a question.
- **Filters** — the constraints the user applies, such as time or document type.
- **Intent** — what the user wants the system to do.
- **Material** — an ambiguity that changes the answer.
- **Query plan** — the sequence of searches and tools used to answer the question.
- **Rewrite query** — changing the words of the query to match the corpus.
- **Rewrite plan** — changing the search strategy.
- **Time** — a first-class extraction for temporal constraints.
- **Unsafe assumption** — a query the system will not answer because it would require guessing.

## Sources

- Query understanding and entity extraction
- Query planning and ambiguity detection
- Materiality and clarification in conversational search
