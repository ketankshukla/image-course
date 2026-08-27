# Build FilePilot — Organization Planning and Optional A2A

## At a glance

Build a deterministic planner first. It takes an inventory snapshot, allowed destinations, and optional evidence, then returns proposed operations. Later, a model or separate classifier can suggest categories. Neither gets filesystem write access or approval authority.

## What the diagram teaches

![Explorer and finder supply evidence to planning. The coordinator persists proposals; only the operations engine can cross the write boundary after approval.](../assets/architecture.svg)

Maya's notes mention both “agents” and “hospital.” A classifier might suggest Hospital Study with moderate confidence. That is not enough to move the file automatically. The planner records its suggestion, the evidence supporting it, and an uncertainty reason. The UI presents the ambiguity rather than concealing it behind a confidence percentage.

For release one, a rule such as an explicit synthetic project tag is easier to audit. Add a model only after you have a labelled fixture collection and a baseline to compare it against. A refusal to classify ambiguous content can be the correct result.

## 1. Create the plan contract

Implement `propose_plan(scan_id, destination_ids)` and `validate_plan(plan)` in `planner.py`. Each operation contains a stable operation ID, source file ID, expected revision, destination folder ID, destination name, operation type, and evidence references. Keep explanatory text separate from executable fields.

Validate destination names, root scope, unique targets, source uniqueness, allowed operations, and the absence of cycles or chained dependencies. The first planner moves files only into already registered destination folders and rejects directory creation, swaps, case-only renames, and plans in which one operation depends on another's newly created path. This simplifies review and partial failure.

## 2. Make uncertainty a first-class result

Return classifications such as `proposed`, `needs_review`, or `unchanged`, with reasons. A number like 0.93 is not a permission level and may not be a calibrated probability. Use held-out synthetic examples to evaluate grouping quality, and report errors by category rather than hiding them in one aggregate score.

Exact duplicate detection is separate from semantic classification. A model should not decide that two files are byte-identical. It can explain the deterministic duplicate result, but the evidence must come from the explorer's comparisons.

## 3. Add an A2A specialist only when it has a real boundary

Create `adapters/classifier_a2a.py` only when the classifier needs its own lifecycle or deployment. The coordinator requests a bounded classification task containing permitted excerpts and destination categories. The specialist returns a structured artifact referencing the input scan revision. It cannot request arbitrary additional paths or submit approval records.

Use an allowlisted specialist registry and authenticated endpoints. An Agent Card describes capabilities; it does not by itself establish trust or grant file access. Pin the selected SDK and protocol together. The [A2A task lifecycle reference](https://a2a-protocol.org/dev/topics/life-of-a-task/) explains why work may return a task with progress and terminal outcomes rather than one immediate answer.

## 4. Handle late and repeated responses

Persist the local request ID, specialist task ID, scan revision, and artifact schema version. If Maya rescans while the specialist is working, its old result is stale. Reject or mark it for review rather than silently attaching it to a new plan, even if the specialist reports success.

Cancellation means stop accepting further work for that request; it does not erase any data already disclosed to a remote specialist. Initial A2A experiments should run locally with synthetic excerpts. Retries must deduplicate by the local task request and cannot create multiple competing plan revisions without explicit tracking.

## 5. Tests and acceptance gate

Test an unknown destination, an absolute path disguised as a name, duplicate target names, a missing source revision, an artifact from an unapproved specialist, a response after cancellation, and an output containing a shell command. All must be rejected or held for review before approval is possible.

Compare the rule-based and model-assisted planner using the same fixture set. Demonstrate that either can be replaced by a deliberately bad fake without gaining the ability to write files. A2A is valuable when it clarifies a genuine specialist boundary; a direct function call is better when no such boundary exists.

## How to present it

Show a classifier suggestion beside the validated plan and the approval record. Ask which of the three is allowed to authorize a move. The answer is the authenticated approval process, and even that remains subject to execution-time checks.
