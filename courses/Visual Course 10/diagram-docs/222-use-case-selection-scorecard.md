# Diagram 222 — Use-case selection, value, frequency, uncertainty, and reversibility

![Candidate use cases pass through a scorecard for value, frequency, uncertainty, reversibility, data, and evidence; policy review becomes a pilot while high-harm irreversible work stays human-controlled.](../diagrams/222-use-case-selection-scorecard.png)

**Module:** Choose the right problem
**Role in the course:** Rank candidate agent use cases using user value and risk-shaped evidence instead of novelty or an impressive demo.
**Layout:** POLICY REVIEW begins on the left and the diagram flows toward POLICY REVIEW; a teal **POLICY REVIEW** path is the desired route and a coral **HIGH HARM LOW REVERSIBILITY** path is blocked or contained.

---

## At a glance

**Use-case selection, value, frequency, uncertainty, and reversibility** — Rank candidate agent use cases using user value and risk-shaped evidence instead of novelty or an impressive demo.

- The central takeaway is: Choose the use case you can value, bound, evaluate, and safely reverse—not the one with the flashiest demo.
- The visual begins with **POLICY REVIEW** and ends with the diagram's outcome, not a technology name.
- The safe or selected path is marked **teal**: POLICY REVIEW moves to PILOT.
- The blocked or dangerous path is marked **coral**: HIGH HARM LOW REVERSIBILITY moves to HUMAN ONLY.
- The analogy is: A hospital does not buy equipment because its screen looks advanced. It asks which patient problem it solves, how often it occurs, what happens when it is wrong, and whether staff can verify and reverse the result.

---

## What the diagram teaches

### 1. Use-case selection, value, frequency, uncertainty, and reversibility

A frequent low-value nuisance may not deserve an elaborate platform. High uncertainty plus low reversibility usually demands stronger human authority, staged rollout, or a narrower use case. In the diagram, **HIGH HARM LOW REVERSIBILITY**, **VALUE**, **FREQUENCY** appear at the left, turning this idea into something a reviewer can point at.

### 2. Name Candidate Outcomes in User Language and Remove Duplicate Technology Ideas.

A useful candidate occurs often enough to matter, creates a clear user outcome, and contains uncertainty that language, retrieval, or adaptive planning can genuinely reduce. The visual places **POLICY REVIEW**, **REFUND COMMIT**, **ACCOUNT DELETE** at the center; the arrows between them are the physical expression of this principle. If this is skipped, a weighted total can disguise one unacceptable outcome, borrowed data, or a score invented to justify a preferred technology.

### 3. Define Value, Frequency, Uncertainty, Reversibility, Data, and Evidence Scales.

Frequency affects learning and operating cost. Uncertainty asks whether inputs, evidence, or paths vary. Data sensitivity, tool power, evidence availability, latency tolerance, and failure visibility change the ranking. The trace asks the team to define value, frequency, uncertainty, reversibility, data, and evidence scales. Look at **HIGH HARM LOW REVERSIBILITY**, **VALUE**, **FREQUENCY** on the top: the diagram uses those elements to show where this decision lives.

### 4. Evaluate with Stakeholders and Attach the Reason and Source Behind Every Score.

A rare scenario may still matter, but it needs a stronger reason and enough safe examples to evaluate. The scorecard is a conversation aid, not a magic formula. Write definitions before scores, mark every sample number illustrative, document who supplied the evidence, and let an unacceptable outcome override a high total. The picture shows **SCORECARD** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: Maya defines each outcome and scores evidence availability, uncertainty, reversibility, sensitivity, and tool power.

### 5. Apply Hard Exclusions for Unacceptable Harm, Missing Authority, or Untestable Behavior.

Reversibility asks whether a mistaken action can be undone. To put this into practice, the team should apply hard exclusions for unacceptable harm, missing authority, or untestable behavior. At the bottom, **HIGH HARM LOW REVERSIBILITY** is the element that makes this concept concrete before any code is written.

### 6. Turn the Strongest Candidate Into a Bounded Pilot with Stop and Rollback Rules.

Selection ends with a pilot hypothesis: named users, one bounded workflow, expected behavior, excluded behavior, evaluation set, stop rule, owner, and an inexpensive way to return to the old process. In the diagram, **PILOT** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, a weighted total can disguise one unacceptable outcome, borrowed data, or a score invented to justify a preferred technology.
![A user problem is matched to the smallest sufficient solution among documentation, workflow, assistant, agent, and automation while human judgment and the authoritative system remain visible.](../diagrams/221-automation-boundary-map.png)

Diagram 221 — *Problem, workflow, assistant, agent, and automation boundaries* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 7. Choose the use case you can value, bound, evaluate

Value must be stated for a person and a business process, not as a vague claim that AI saves time. A use case with no trustworthy ground truth may be impossible to evaluate even if the demo looks fluent. The visual places **VALUE** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A hospital does not buy equipment because its screen looks advanced. It asks which patient problem it solves, how often it occurs, what happens when it is wrong, and whether staff can verify and reverse the result. Look at **POLICY REVIEW**, **REFUND COMMIT**, **ACCOUNT DELETE** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: Acme has four ideas: answer FAQs, review policies, issue refunds, and delete accounts. Leadership wants the most dramatic demonstration first.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Build the future scorecard as a transparent review form whose scale definitions, evidence notes, exclusions, and owner are stored with each assessment.
- Render illustrative values with a visible scenario badge so no portfolio viewer mistakes them for measured product results.
- Generate a pilot brief page from approved scorecard data, including excluded actions, evaluation cases, stop rules, and rollback path.

Together these choices prevent the mistakes in the Acme case—Acme has four ideas: answer FAQs, review policies, issue refunds, and delete accounts. Leadership wants the most dramatic demonstration first.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Define typed score dimensions and validation rules; keep hard exclusions separate from weighted totals.
- Store assessment versions and evidence references so a later change in policy or workload can trigger reassessment.
- Test deterministic ranking and make the API return reasons, not only a number, so reviewers can challenge the decision.

These boundaries make the Acme case—Acme has four ideas: answer FAQs, review policies, issue refunds, and delete accounts. Leadership wants the most dramatic demonstration first.—testable and replaceable.

---

## Case study — Acme has four ideas

Acme has four ideas: answer FAQs, review policies, issue refunds, and delete accounts. Leadership wants the most dramatic demonstration first.

### The walkthrough

1. Maya defines each outcome and scores evidence availability, uncertainty, reversibility, sensitivity, and tool power.
2. FAQ answers are easy but lower value; account deletion is valuable but highly consequential and poorly reversible.
3. Policy review has useful uncertainty, versioned evidence, visible human review, and no direct irreversible effect.
4. Acme selects policy review as the pilot and keeps refund commits and deletion behind separate human-controlled services.

### The result

The first project demonstrates real agent value while keeping risk and evaluation manageable.

### The danger

A weighted total can disguise one unacceptable outcome, borrowed data, or a score invented to justify a preferred technology.

### The takeaway

Choose the use case you can value, bound, evaluate, and safely reverse—not the one with the flashiest demo.

---

## Composition

The picture is a scorecard at the center of the scene. From the left, four candidate cards—**FAQ**, **POLICY REVIEW**, **REFUND COMMIT**, **ACCOUNT DELETE**—enter the **SCORECARD**. Inside the scorecard, six white cards—**VALUE**, **FREQUENCY**, **UNCERTAINTY**, **REVERSIBILITY**, **DATA**, **EVIDENCE**—represent the dimensions. A teal **POLICY REVIEW** arrow moves toward a **PILOT** card on the right. Below, a coral **HIGH HARM LOW REVERSIBILITY** arrow points to **HUMAN ONLY**. The bottom of the scorecard marks the sample scores **ILLUSTRATIVE**. The whole composition shows a decision funnel, not a calculator.

## Element by element

- **POLICY REVIEW** — Policy review has useful uncertainty, versioned evidence, visible human review, and no direct irreversible effect.
- **REFUND COMMIT** — the REFUND COMMIT card shown in this diagram; it is one of the labeled elements the architecture uses.
- **ACCOUNT DELETE** — a labeled visual element in this diagram; the prompt shows it as ACCOUNT DELETE entering a SCORECARD with VALUE.
- **HIGH HARM LOW REVERSIBILITY** — ability to restore a safe prior state.
- **HUMAN ONLY** — High uncertainty plus low reversibility usually demands stronger human authority, staged rollout, or a narrower use case.
- **FAQ** — FAQ answers are easy but lower value; account deletion is valuable but highly consequential and poorly reversible.
- **SCORECARD** — The scorecard is a conversation aid, not a magic formula.
- **VALUE** — Value must be stated for a person and a business process, not as a vague claim that AI saves time.
- **FREQUENCY** — Frequency affects learning and operating cost.
- **UNCERTAINTY** — A useful candidate occurs often enough to matter, creates a clear user outcome, and contains uncertainty that language, retrieval, or adaptive planning can genuinely reduce.
- **REVERSIBILITY** — Reversibility asks whether a mistaken action can be undone.
- **DATA** — Data sensitivity, tool power, evidence availability, latency tolerance, and failure visibility change the ranking.
- **EVIDENCE** — Uncertainty asks whether inputs, evidence, or paths vary.
- **PILOT** — Selection ends with a pilot hypothesis: named users, one bounded workflow, expected behavior, excluded behavior, evaluation set, stop rule, owner, and an inexpensive way to return to the old process.
- **ILLUSTRATIVE** — Write definitions before scores, mark every sample number illustrative, document who supplied the evidence, and let an unacceptable outcome override a high total.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **REFUND COMMIT**, **ACCOUNT DELETE**, **FAQ**, **SCORECARD**, **VALUE**, **FREQUENCY** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **REFUND COMMIT**, **ACCOUNT DELETE**, **FAQ**, **SCORECARD** carry the forward motion of the architecture.
- **Teal arrow** — an authoritative decision, verified contract, passing gate, safe release, or recovered service. The teal elements **POLICY REVIEW**, **PILOT** show the path the design wants to keep open.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **HIGH HARM LOW REVERSIBILITY**, **HUMAN ONLY** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **REFUND COMMIT**, **ACCOUNT DELETE**, **FAQ**, **SCORECARD**, **VALUE**, **FREQUENCY**, **UNCERTAINTY**, **REVERSIBILITY** are the readable records the diagram communicates.

---

## How to present it

- Point to **POLICY REVIEW** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **REFUND COMMIT** and ask what would have to change for the team to list candidate outcomes in user language and remove duplicate technology ideas, and who would own that change.
- Point to **HIGH HARM LOW REVERSIBILITY** and ask what evidence would show the team has already define value, frequency, uncertainty, reversibility, data, and evidence scales, and what test would fail first if it is missing.
- Point to **SCORECARD** and ask who else in the room must agree before the team can score with stakeholders and attach the reason and source behind every score, and what would change their mind.
- Point to **HIGH HARM LOW REVERSIBILITY** and ask what the smallest version of apply hard exclusions for unacceptable harm, missing authority, or untestable behavior looks like, and what would be left out of that version.
- Point to **PILOT** and ask what would have to change for the team to turn the strongest candidate into a bounded pilot with stop and rollback rules, and who would own that change.
- Trace the **teal** path (POLICY REVIEW moves to PILOT) and ask what evidence would prove the real system follows it, who collects that evidence, and how often it is refreshed.
- Show the **coral** path (HIGH HARM LOW REVERSIBILITY moves to HUMAN ONLY) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Point to **POLICY REVIEW** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Use the analogy: A hospital does not buy equipment because its screen looks advanced. It asks which patient problem it solves, how often it occurs, what happens when it is wrong, and whether staff can verify and reverse the result. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Create a six-dimension scorecard for five candidate use cases. Define each scale, attach evidence notes, mark sample values illustrative, add three hard exclusions, and write a pilot hypothesis plus rollback path for the selected case.
- Pose the checkpoint: *Should the candidate with the highest weighted score always win?*

---

## Lab and checkpoint

**Lab:** Create a six-dimension scorecard for five candidate use cases. Define each scale, attach evidence notes, mark sample values illustrative, add three hard exclusions, and write a pilot hypothesis plus rollback path for the selected case.

**Checkpoint:** Should the candidate with the highest weighted score always win?

**Answer:** No. A hard risk exclusion, missing ground truth, unclear ownership, or unacceptable outcome can disqualify it regardless of the total.

---

## Glossary

- **Reversibility** — ability to restore a safe prior state
- **Ground truth** — trusted evidence used to judge correctness
- **Pilot** — limited real-world trial with explicit safeguards

---

## Sources

- NIST AI Risk Management Framework
- NIST AI RMF Playbook
- NIST Generative AI Profile

---

## Related lessons

- **Lesson 221** — Problem, workflow, assistant, agent, and automation boundaries (`automation-boundary-map`)
- **Lesson 223** — Risk classification, human authority, and unacceptable outcomes (`risk-authority-unacceptable-outcomes`)
- **Lesson 224** — Success criteria, exit criteria, and evidence requirements (`success-exit-evidence-contract`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Use-case selection, value, frequency, uncertainty, and reversibility until the diagram is legible to every reviewer. Rank candidate agent use cases using user value and risk-shaped evidence instead of novelty or an impressive demo. The trace moves through 5 decisions: List candidate outcomes in user language and remove duplicate technology ideas.; Define value, frequency, uncertainty, reversibility, data, and evidence scales.; Score with stakeholders and attach the reason and source behind every score.; Apply hard exclusions for unacceptable harm, missing authority, or untestable behavior.; Turn the strongest candidate into a bounded pilot with stop and rollback rules.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—Acme has four ideas: answer FAQs, review policies, issue refunds, and delete accounts. Leadership wants the most dramatic demonstration first.—shows that Choose the use case you can value, bound, evaluate, and safely reverse—not the one with the flashiest demo. If the team skips this, A weighted total can disguise one unacceptable outcome, borrowed data, or a score invented to justify a preferred technology. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.