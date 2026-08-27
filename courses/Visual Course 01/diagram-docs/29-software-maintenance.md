# Diagram 29 — Software Maintenance

![Five stages across dark navy. ISSUE shows a dark card with a coral alert badge and a coral underline. RAG CODEBASE shows a code editor window with tiles labelled CODE and DOCS. MCP TOOLS shows a green toolbox with git branch, gear and terminal prompt tiles. A2A TEST AGENT shows a robot between two cards — BOUNDED TASK with two green ticks and a coral cross, and TEST RESULTS with two green ticks and a coral cross on a coral bar — with bidirectional arrows to the next stage. REVIEWED PATCH shows a code window with a green diff, a shield, a person reaching toward the screen, and a teal badge reading MERGE. A dashed cyan line returns along the bottom to the issue.](../diagrams/29-software-maintenance.png)

**Module:** 6 — End-to-end use cases
**Role in the course:** software-agent architecture
**Layout:** five stages with a test loop and a human-gated merge

---

## At a glance

A maintenance pipeline: **ISSUE → RAG CODEBASE → MCP TOOLS → A2A TEST AGENT → REVIEWED PATCH**, with a dashed return to the issue.

Two features distinguish it. The MCP toolbox carries **domain-specific tiles** — a git branch, a gear, a terminal prompt — rather than the generic plug/gear/database set used everywhere else in the library. And the test stage has **bidirectional arrows** to the patch stage, making it the only place in these use cases where a loop is drawn inside the pipeline rather than beneath it.

---

## What the diagram teaches

### 1. The toolbox changes, and the change is the point

Every other diagram in this library draws MCP as a toolbox with **plug, gear and database** tiles. This one draws **git branch, gear, and terminal prompt** `>_`.

Same object, different contents. Capabilities are domain-specific, and a software maintenance agent's toolbox is not a customer support agent's toolbox.

The three tiles map to what a maintenance agent actually needs:

- **Git branch** — version control operations. Read history, create branches, produce diffs, examine blame.
- **Gear** — build and configuration. Compile, lint, inspect dependencies.
- **Terminal** — execution. Run tests, run the thing, reproduce the bug.

That third one is the significant one. Most capability sets are reads and structured writes. A maintenance agent needs to **execute code**, which is a categorically larger permission and the one that requires the most careful bounding.

### 2. The codebase is a RAG lane, and it holds two kinds of thing

Stage 2 shows a code editor with two tiles beneath: **CODE** and **DOCS**.

Both belong in the retrieval lane, and they behave differently.

**Code** is structured text where chunking on arbitrary boundaries is destructive. A half-function is not evidence of anything. Chunking must follow structure — function, class, module — which is exactly the case the chunk-size diagram identifies as needing structure-aware treatment:

![Three panels comparing TOO SMALL with fragments funnelling into a bin, JUST RIGHT with one coherent document and overlap regions, and TOO LARGE crammed with unrelated blocks.](../diagrams/15-rag-chunk-size.png)

**Docs** are prose — README files, architecture decisions, runbooks, comments. They explain intent, which code does not. A maintenance agent that has read only the code knows what the system does and not why.

The pairing matters because most bugs live in the gap between the two: the code does what it says, and what it says is not what was intended.

### 3. Bounded task and test results are the same shape, and that is deliberate

The A2A stage shows a robot between two cards, and they mirror each other.

**BOUNDED TASK** *(above)* — two green ticks and one coral ✗.
**TEST RESULTS** *(below)* — two green ticks and one coral ✗ on a coral bar.

The visual rhyme says: the task specified what should pass, and the results report what did. The failing item is drawn in coral in both.

This is the artifact-validation relationship made concrete. The task declared the shape of an acceptable answer; the artifact reports against that shape. You can compare them mechanically, which is what makes a test agent's output checkable rather than merely informative.

### 4. The failing test is coral and inside the loop, which reframes it

A coral ✗ appears in the test results, and the arrows between the test stage and the patch stage run **both ways**.

Failure here is not an exception route dropping out of the pipeline. It is a normal state of a cycle. The patch is proposed, tested, found wanting, revised, tested again.

That is a meaningfully different treatment from the failure paths elsewhere in this library, where coral usually means rejected and discarded. Here it means *not yet*, and the loop is how you get from not-yet to done.

The design consequence: the agent must be able to act on a failure. A test result that says "3 failed" is not actionable; one that says which tests, with what assertions, at what lines, is. The specificity of the failure determines whether the loop converges.

### 5. The merge is separate, teal, and touched by a human

Stage 5 shows a code window with a **green diff** — `+` lines added — a shield, a person reaching toward the screen, and a **separate teal badge reading ✓ MERGE**.

The merge badge is drawn as its own object below the platform, not as part of the patch. Two distinct things: a patch exists, and a patch is merged.

The person is physically reaching toward the screen. Same posture as the confirm stage of the safe side-effect pipeline, and the same meaning:

![Four numbered panels — CONFIRM, AUTHORIZE, IDEMPOTENCY KEY, CHANGE + RECEIPT — with a SAFE RETRY loop through a rejected duplicate write.](../diagrams/02-safe-side-effect.png)

Merging is the side effect. Everything before it — reading, reasoning, patching, testing — is reversible and contained. Merging puts code into a branch other people build on, and it is the point at which an agent's work becomes the organisation's problem.

### 6. The return path goes to the issue, and it closes the record

A dashed cyan line runs from the patch stage all the way back to **ISSUE**.

The issue is where the work started and it is where the outcome belongs: what was changed, why, which tests now cover it, and which commit carries it. Not just "closed."

For maintenance work this is more than audit hygiene. The issue is the artefact a future engineer will find when the bug recurs or when they are trying to understand why the code looks the way it does. An issue closed with no linkage is a dead end six months later.

---

## Case study — Ferrous, the platform team's triage backlog

Ferrous runs an internal developer platform for a company of about 1,400 engineers. Their team of nine maintains build tooling, CI infrastructure, service scaffolding and a set of shared libraries.

Their problem was not building things. It was the backlog: around 240 open issues against their libraries, mostly small — a broken edge case, an unclear error message, a dependency needing a bump, a flaky test. Each one takes an engineer twenty minutes to an hour, and nine people could not get to them.

They built a maintenance assistant to work the tail.

### What it was allowed to touch

The scope was drawn narrowly and deliberately:

- **Their own libraries only.** Not application code, not infrastructure.
- **Issues labelled `triage-eligible`** — applied by a human, never by the assistant.
- **No production access.** Nothing the assistant can do touches a running system.
- **No merge authority.** Ever.

That last constraint was non-negotiable from the outset, and it is the thing that made the project acceptable to the wider engineering organisation.

### Stage 1 — Issue

A representative one: *"`retry_with_backoff` throws on the first attempt when `max_attempts=1` instead of executing once. Expected: executes once, no retry."*

Small, specific, reproducible. Exactly the kind of thing that sits in a backlog for months because it is nobody's priority and takes an hour.

### Stage 2 — RAG Codebase

The index covers their nine libraries: source chunked by function and class, plus docs, ADRs, runbooks and the changelog.

For this issue, retrieval surfaces the `retry_with_backoff` implementation, its tests, the ADR explaining why the retry policy was designed as it was, and two prior issues touching the same function.

The ADR turned out to matter. It documented that `max_attempts` was intentionally defined as the number of *retries* rather than total attempts in an early version, then changed to total attempts, and that the loop condition was not updated in the same commit. The bug had a documented history that the code alone did not carry.

This is the code/docs pairing earning its place. An agent with only the source would have seen a boundary condition and guessed at intent.

### Stage 3 — MCP Tools

Their gateway exposes exactly the three categories the diagram's tiles depict:

**Version control** — `get_file`, `get_history`, `get_blame`, `create_branch`, `write_file`, `create_pull_request`. Note that `create_pull_request` is the terminal write; there is no merge.

**Build and config** — `build`, `lint`, `check_dependencies`.

**Execution** — `run_tests(scope)`, in an ephemeral sandboxed container with no network egress and no credentials. This is the most tightly bounded capability they expose, and it took the longest to get approved.

The sandbox constraints came from a security review that asked what happens if the agent writes and executes malicious code — either through a compromised dependency or through a prompt-injection path in an issue description. The answer had to be "nothing, it runs in a container with no network and no secrets and is destroyed afterwards."

### Stage 4 — A2A Test Agent

Ferrous's QA tooling team owns the test agent. The separation is real: the thing that writes the patch should not be the thing that decides whether the patch is correct.

The **bounded task** sent to it declares what must hold:

- Existing tests for `retry_with_backoff` continue to pass.
- New tests cover `max_attempts=1`, `max_attempts=0`, and the normal multi-attempt path.
- Coverage of the modified function does not decrease.
- No change to the public signature.

The **test results** come back in the same shape. On the first iteration:

- ✓ Existing tests pass
- ✓ Coverage maintained
- ✗ **`max_attempts=0` raises `ValueError`; task required defined behaviour**

The patch had handled `1` and not `0`. The failure was specific — which case, which exception, which assertion — so the assistant could act on it.

Second iteration: `max_attempts=0` returns without executing, matching the documented contract. All checks pass.

Two iterations. Their median is 1.8.

### Stage 5 — Reviewed patch

A pull request is opened. It contains the diff, the new tests, a summary of the change, a link to the ADR that explained the original intent, the test agent's results for both iterations, and a reference to the issue.

A human platform engineer reviews it.

They merge, or they do not. Approximately **73% are merged**, most with no changes. About 18% are merged after modification. About 9% are closed unmerged — usually because the reviewer decides the fix is right but the underlying design is wrong, and the issue deserves a larger change.

That 9% is not a failure rate. It is the review stage working: an agent that fixes the reported symptom correctly may still be papering over something that needs a human decision.

### The return path

On merge, the issue is closed with the pull request, the commit, the tests added, and the test agent's results attached.

Ferrous cared about this more than expected. Six months in, an engineer investigating a related problem found one of these closed issues and had, immediately, the ADR link, the reasoning, and the tests — a better record than most of their human-closed issues from the same period, because the assistant is consistent about linkage in a way tired engineers are not.

### Results after ten months

- **Backlog** from 240 to 71 open issues.
- **Throughput** around 14 triage-eligible issues resolved per week, against a prior rate of 3 to 4.
- **Reviewer time** averaging 9 minutes per pull request, against 35–50 minutes to fix such an issue by hand.
- **Regressions traced to assistant-authored patches**: two in ten months. Both were caught in staging. Both were cases where the test agent's bounded task had not specified a condition that mattered.

Those two regressions produced their most useful process change: **the bounded task specification is now itself reviewed** by the human reviewer, not just the patch. A patch that satisfies an incomplete specification is a patch that passes its tests and is wrong.

### What they will not do

They have been asked repeatedly to enable auto-merge for high-confidence patches. They have declined every time, and their reasoning is worth repeating.

The value of the assistant is that it converts an hour of engineering into nine minutes of review. Auto-merge would convert nine minutes into zero, saving 9 minutes and removing the only step that catches the 9% where the fix is right and the design is wrong.

The marginal saving is small. The marginal risk is the entire safety property of the system.

---

## Composition

Five stages run left to right, headed by white uppercase labels. Cyan arrows connect stages 1 through 4; between stages 4 and 5 the arrows run in **both directions**. A dashed cyan line runs along the bottom from the final stage back to the first.

**ISSUE → RAG CODEBASE → MCP TOOLS → A2A TEST AGENT ⇄ REVIEWED PATCH**

## Element by element

**ISSUE**
A dark upright card carrying a **coral circular alert badge** with an exclamation, three grey text lines, and a **coral underline** on the final line. A reported problem.

**RAG CODEBASE**
A blue code editor window showing `</>` and lines of code in blue and teal. In front, two tiles: a **teal tile with `</>` labelled CODE**, and a **white document tile labelled DOCS**.

**MCP TOOLS**
The green toolbox with a dark handle and latch, carrying three dark tiles: a **git branch glyph**, a **gear**, and a **terminal prompt `>_`**. Domain-specific rather than the library's generic set.

**A2A TEST AGENT**
A blue cube robot on a glowing teal disc at centre, with a card above and below. Above: a dark card headed **BOUNDED TASK** in teal, listing two green-ticked rows and one **coral ✗** row. Below: a dark card headed **TEST RESULTS**, listing two green-ticked rows and one **coral ✗** row on a **coral bar**. Curved cyan arrows run to and from the next stage.

**REVIEWED PATCH**
A code window with a teal title bar showing a **green diff** — a column of `+` marks with added lines. A **green shield with a white check** sits at the left, and a person seated at the right is **reaching toward the screen**. Below the platform, a separate dark badge carries a **teal check and the word MERGE**.

**The return path**
A dashed cyan line from beneath the patch stage, running the width of the frame, turning up into the issue.

## Colour and flow semantics

- **Cyan arrows** carry the pipeline forward; the **bidirectional arrows** between stages 4 and 5 mark the test/revise cycle.
- **Coral** appears three times: the issue's alert, the bounded task's unmet condition, and the failing test result. In this diagram coral means *not yet satisfied* rather than *rejected*.
- **Green** marks the passing checks, the diff, and the review shield.
- **Teal** marks the merge badge — the committed, human-authorised outcome.
- The **merge badge sits outside the patch platform**, separating "a patch exists" from "a patch is merged."

## How to present it

**Point at the toolbox first.** Ask what is different about it. Git, gear, terminal — not plug, gear, database. Capabilities are domain-specific, and the diagram bothers to redraw them. Then ask which of the three is the dangerous one. The terminal, because executing code is categorically larger than reading or writing structured data.

**Ask how they would bound execution.** Push for specifics: sandbox, no network, no credentials, ephemeral, destroyed after. Then ask the security review's question — what happens if the agent runs malicious code, whether from a dependency or from an issue description someone wrote. Prompt injection through an issue title is a real path and most rooms have not considered it.

**Ask why CODE and DOCS are separate tiles.** Code says what; docs say why. Then use Ferrous's ADR — the bug had a documented history the source did not carry. An agent with only code guesses at intent.

**Point at the two mirrored cards.** Bounded task above, test results below, same shape. Ask what that says. The task declared what an acceptable answer looks like; the artifact reports against it. Mechanically comparable, which is what makes it checkable.

**Ask what the coral ✗ means here versus elsewhere.** In most of the library coral means rejected. Here it means not yet, and the loop is how you resolve it. Then ask what makes a loop converge — the specificity of the failure. "3 tests failed" is not actionable; "`max_attempts=0` raises ValueError at line 47" is.

**Ask about the 9%.** Patches closed unmerged because the fix was right and the design was wrong. Ask what would catch that if there were no human review. Nothing would — the tests pass. This is the argument against auto-merge in one number.

**Run the auto-merge debate.** Someone will propose it for high-confidence patches. Give them Ferrous's arithmetic: the assistant already converted an hour into nine minutes. Auto-merge saves nine minutes and removes the only step that catches the 9%. Marginal saving, total loss of the safety property.

**Close on the regression finding.** Two regressions in ten months, both because the bounded task was incomplete. The fix was to review the specification, not just the patch. A patch that satisfies an incomplete spec passes its tests and is wrong — which generalises well beyond software.

**Timing.** Thirty minutes. Forty with the auto-merge debate, which engineering audiences engage with strongly.

---

## Lab and checkpoint

**Lab:** Take one real bug from your issue tracker and write a bounded task specification for an agent to fix it. Include the code context, the docs context, the test criteria, and the execution bounds. Then run the agent, inspect the returned patch, and decide whether the failure mode "patch is right but design is wrong" is detectable from the test criteria alone.

**Checkpoint:** Why is auto-merge a bad trade for this workflow?

**Answer:** Because the agent already converts an hour of work into nine minutes. Auto-merge saves the remaining nine minutes but removes the human review step that catches the 9% of patches that are correct against the spec but wrong in design. Marginal time saving, total loss of the safety property.

## Glossary

- **Artifact** — the returned result, such as a patch, that is compared against the bounded task.
- **Bounded task** — the specification that declares what an acceptable result looks like.
- **Coral ✗** — the "not yet" marker that the patch has failed a test and must be refined.
- **Git** — the source-of-truth for code and change history.
- **Sandbox** — the restricted execution environment for the agent's code execution.
- **Terminal** — the tool that executes commands and is therefore the most dangerous capability.
- **Test results** — the artifact that reports whether the patch meets the bounded task.

## Sources

- Agent-assisted software maintenance and patch generation
- Bounded task specification and test-driven agent workflows
- Sandboxed code execution and auto-merge safety
