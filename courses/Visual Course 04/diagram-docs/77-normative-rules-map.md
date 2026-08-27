# Diagram 77 — Normative Rules Versus Examples

![Three lanes on dark navy. SPECIFICATION on the left holds three white cards — MUST with a shield, SHOULD with a star, MAY with a question mark. CONFORMANCE TESTS in the centre holds three clipboard checklists, each fed by a cyan arrow from the spec cards. EXAMPLES AND IMPLEMENTATION CHOICES on the right holds code, gear, list, puzzle, slider and database icons, whose teal lines run leftward but are stopped by a vertical coral dashed divider labelled NOT A REQUIREMENT.](../diagrams/77-normative-rules-map.png)

**Module:** Reading a specification
**Role in the course:** the first diagram — what in a spec is binding and what is not
**Layout:** three lanes with a coral divider blocking the right lane from the centre

---

## At a glance

Three lanes. **SPECIFICATION** on the left, **CONFORMANCE TESTS** in the middle, **EXAMPLES AND IMPLEMENTATION CHOICES** on the right — and a **vertical coral dashed divider** between the right and the centre, labelled **NOT A REQUIREMENT**.

Cyan arrows cross freely from the left into the centre. Teal lines from the right run toward the centre and stop at the divider.

That asymmetry is the whole diagram. **Requirements generate tests. Examples do not.**

---

## What the diagram teaches

### 1. Three requirement words, three different obligations

**MUST** carries a **shield**. Binding. An implementation that does not do this is non-conformant. There is no discretion.

**SHOULD** carries a **star**. Strongly recommended. An implementation may deviate, but it needs a reason, and it needs to understand what it is giving up. In practice: do it unless you have written down why not.

**MAY** carries a **question mark**. Optional. Implementing it and not implementing it are both conformant. The question mark is apt — it marks something genuinely open.

The distinction matters because engineers reading a specification tend to flatten it. Everything becomes "the spec says," and then either everything is treated as mandatory (which makes conformance impossible) or nothing is (which makes it meaningless).

### 2. All three generate tests, and that is not obvious

Look carefully: **MUST, SHOULD and MAY each have a cyan arrow into their own conformance test.**

The instinct is that only MUST is testable. It is not.

**A MUST test** asserts the behaviour is present. Failure means non-conformance.

**A SHOULD test** asserts the behaviour is present *or* that a documented deviation exists. Failure means an undocumented deviation, which is a real finding.

**A MAY test** asserts that *if* the feature is implemented, it behaves as specified. An implementation that does not offer it passes trivially. One that offers it incorrectly fails.

That third case is the one teams miss most often, and it produces the worst interoperability failures: an optional feature implemented wrongly is worse than one not implemented at all, because clients discover it exists and depend on it.

Each of the three test lanes becomes a row in the inventory that tracks them:

![A five-column table headed REQUIREMENT, HAPPY PATH, NEGATIVE TEST, EVIDENCE and STATUS, with four rows showing PASS, PASS, FAIL and an amber NOT TESTED.](../diagrams/80-conformance-matrix.png)

The **NOT TESTED** status there is what an untested requirement looks like once you have a row for it. Without the requirement inventory, an untested MAY is simply absent.

### 3. The divider is coral, and it points the right way

The **NOT A REQUIREMENT** label runs vertically down a coral dashed line, and the teal lines from the right-hand lane terminate against it with arrowheads pointing *left* — toward the tests they are not allowed to reach.

Coral throughout this library marks risk and refusal. Here it marks a boundary that must not be crossed in one direction.

Note what the divider does *not* block: examples are still valuable. They clarify intent, they show idiomatic usage, they help you understand what a requirement means. The lines exist. They simply do not terminate in a test.

### 4. The right lane holds two different things, and both are non-normative

**EXAMPLES** — the code snippets, sample payloads and illustrative flows a specification includes to make requirements comprehensible.

**IMPLEMENTATION CHOICES** — the gear, the sliders, the database. Decisions a specification deliberately leaves to the implementer: what storage to use, what internal architecture, what performance characteristics.

They are grouped because they share a property: **testing them tests your reading of the document, not the document's requirements.**

An example showing a JSON payload with fields in a particular order does not make that order normative. A sample using a particular datastore does not make that datastore required.

### 5. The failure this prevents is over-constrained conformance

The specific damage: a conformance suite built from examples rejects implementations that are entirely valid.

An implementation that returns the same fields in a different order, or uses a different internal representation, or makes a different architectural choice, fails a test that was never testing a requirement.

That produces two bad outcomes. Valid implementations are told they are broken. And the suite's authority collapses — once a team knows some failures are spurious, they stop treating any failure as authoritative.

### 6. The under-constrained failure is the mirror image

Equally real and less discussed: a suite that only tests MUST misses the SHOULD deviations and the incorrectly-implemented MAY features.

Two implementations can both pass a MUST-only suite and fail to interoperate, because one deviated from every SHOULD and the other implemented an optional feature incorrectly.

The three test lanes exist because conformance is not a single bar.

---

## Case study — Ashgrove Interop, the suite that failed valid implementations

Ashgrove is a small consultancy that builds conformance suites for protocol working groups. They were commissioned to build a certification suite for an agent-interoperability protocol with about 190 numbered requirements.

Their first release was withdrawn after three weeks.

### What they built

A suite of 340 tests, derived by working through the specification section by section and writing a test for each observable behaviour.

It was thorough. It was also derived from the wrong material.

### The complaint that started the review

The third implementation to run the suite failed 31 tests. Its authors, an experienced team, disputed nearly all of them.

Ashgrove's initial position was that the tests reflected the specification. Working through the disputes one at a time took eleven days and produced an uncomfortable finding: **27 of the 31 were not testing requirements.**

### The four categories of bad test

**Field ordering — 9 tests.** The specification's example payloads listed fields in a consistent order. Ashgrove's tests asserted that order. Nothing in the specification required it, and JSON object member order is not significant.

**Sample values — 7 tests.** Examples used particular identifier formats — a specific prefix, a specific length. The tests asserted those formats. The specification said identifiers were opaque strings.

**Illustrative flow sequencing — 6 tests.** An example showed a client performing discovery before its first call. The specification required that a client not invoke an undiscovered capability; it did not require discovery to be the first operation. An implementation that discovered lazily, on first need, failed.

**Implementation choices — 5 tests.** The specification's non-normative guidance suggested a caching strategy. Ashgrove tested for it. Implementations with different, entirely valid caching behaviour failed.

The remaining 4 of the 31 were genuine requirement failures, and the implementation team fixed them without argument.

### The rebuild

They rewrote the suite from a **requirement inventory** rather than from the document's prose.

**Every requirement was extracted with its normative word.** 190 requirements: 118 MUST, 54 SHOULD, 18 MAY.

**Every test was traced to a requirement identifier.** A test with no requirement identifier could not enter the suite. This single rule eliminated every one of the 27.

**The three requirement classes got three test treatments.**

*MUST tests* assert behaviour. Failure is non-conformance.

*SHOULD tests* assert behaviour or an accompanying documented deviation. The suite accepts a machine-readable deviation declaration naming the requirement and the reason. Failure means an undeclared deviation.

*MAY tests* are conditional. The suite first asks whether the feature is offered. If not, the test is skipped and recorded as not-applicable. If offered, it is tested in full.

**Examples became documentation, not test sources.** The suite links to relevant examples in its failure messages — "R-047 failed; see specification example 12" — which turned out to be its most appreciated feature, because a failing test now explains itself.

### What the MAY handling found

The conditional MAY tests found the most serious interoperability problem in the programme.

Three implementations offered an optional extension. All three had implemented it differently — two had misread the same ambiguous sentence in opposite ways, and the third had implemented an earlier draft.

Under a MUST-only suite, all three passed. In the field, an orchestrator that discovered the extension on any of the three would have produced different behaviour against each.

The finding also improved the specification: the ambiguous sentence was rewritten.

### The numbers

- **Tests in the original suite:** 340, of which 27 tested non-requirements.
- **Tests in the rebuilt suite:** 296, every one traced to a requirement identifier.
- **Requirements with no test:** 0, down from 22 that had been missed while examples were being tested.
- **Implementations passing:** 2 of 6 initially, 6 of 6 after four months of coordinated fixes.

### The rule Ashgrove now applies to every commission

*A test with no requirement identifier does not go in the suite. If you cannot cite the requirement, you are testing the example.*

---

## Composition

Three vertical lanes with headers, arranged left to right.

**SPECIFICATION** (left): three white cards on blue platforms, each with a blue square icon and text lines — **MUST** (shield), **SHOULD** (star), **MAY** (question mark). Each sends a **cyan arrow** rightward.

**CONFORMANCE TESTS** (centre): three white cube-cards on blue platforms, each showing a clipboard with green-ticked checklist rows.

**EXAMPLES AND IMPLEMENTATION CHOICES** (right): three pairs of white cube-cards — a `</>` code tile with a **gear**, a list tile with a **puzzle piece**, a slider tile with a **database stack**.

**Between centre and right:** a **vertical coral dashed line**, with a coral rounded label reading **NOT A REQUIREMENT** rotated to run vertically. **Teal lines** from each right-hand pair curve leftward and terminate with arrowheads at the divider.

## Element by element

**MUST** — a white card with a blue shield containing a check. Binding.
**SHOULD** — a white card with a blue star. Recommended; deviation requires justification.
**MAY** — a white card with a blue question mark. Optional; conformant either way.

**The three test cubes** — identical white cubes showing clipboards with three green-ticked rows each, one per requirement class.

**The examples column** — `</>` and gear (code samples and implementation choices), list and puzzle (illustrative flows and optional structure), sliders and database (configuration and storage decisions).

**The divider** — a coral dashed vertical line the full height of the frame, carrying the vertical label **NOT A REQUIREMENT**.

## Colour and flow semantics

- **Cyan arrows** carry requirements into tests — the only flow that crosses into the centre lane.
- **Teal lines** from the examples lane run toward the centre and are stopped by the divider, arrowheads pointing at a boundary they do not cross.
- **Coral** marks the divider, consistent with coral meaning a refusal boundary throughout the library.
- The **three requirement icons** — shield, star, question mark — encode obligation strength without text.
- All three requirement classes are given **equal-sized test cubes**, asserting that all three are testable.

## How to present it

**Ask what a conformance suite should be built from.** Most answers are "the specification," which is right and insufficiently precise. Then show the divider.

**Read the three requirement words and ask which are testable.** Most rooms say only MUST. Then walk the three test treatments: assert; assert-or-documented-deviation; conditional-on-offered. The MAY case is the one that surprises people.

**Make the argument about optional features.** An optional feature implemented incorrectly is worse than one not implemented, because clients discover it and depend on it. Ashgrove's three-implementations-three-behaviours finding is the concrete version.

**Ask what happens when a suite tests examples.** Two failures: valid implementations are told they are broken, and the suite loses authority because some failures are known to be spurious.

**Walk Ashgrove's four categories.** Field ordering, sample values, illustrative sequencing, implementation choices. Ask the room which of the four they would have written. Field ordering catches almost everyone.

**Give them the traceability rule.** *A test with no requirement identifier does not go in the suite.* One rule, and it eliminated all 27 bad tests mechanically.

**Point out the under-constrained mirror.** A MUST-only suite lets two implementations both pass and fail to interoperate. Ask which failure mode their own testing has.

**Note what the divider does not block.** Examples still matter — they clarify intent and they make failure messages useful. Ashgrove's most appreciated feature was linking failures to examples. The examples are not the enemy; testing them is.

**Timing.** Twenty minutes. Thirty if you extract requirements from a real specification page and classify them, which reliably starts an argument about one sentence.

---

## Lab and checkpoint

**Lab:** Take one page from a specification you work with and classify every requirement as MUST, SHOULD, or MAY. For each, decide the correct test treatment: assert, assert-or-documented-deviation, or conditional-on-offered. Then identify any examples, sample values, or sequencing that should not become conformance tests.

**Checkpoint:** Why is an optional feature implemented incorrectly worse than one not implemented?

**Answer:** Because clients discover the optional feature and start to depend on it. If it is implemented incorrectly, two conformant-looking implementations can differ, and clients that rely on it break. Not implementing the feature at least makes the absence visible.

## Glossary

- **Conformance** — passing the suite of tests that a specification requires.
- **MAY** — an optional feature that must be conditional-on-offered if implemented.
- **MUST** — a mandatory requirement that the suite must assert.
- **Normative** — the part of a specification that creates obligations.
- **Optional feature** — something the specification permits but does not require.
- **SHOULD** — a recommended requirement that is asserted or a documented deviation is recorded.
- **Specification** — the source document from which tests are derived.
- **Test treatment** — the rule for how a requirement is tested.
- **Traceability** — the rule that every test must map to a requirement identifier.

## Sources

- RFC 2119 requirement levels: MUST, SHOULD, MAY
- Conformance testing and normative versus informative text
- Test traceability and implementation deviation documentation
