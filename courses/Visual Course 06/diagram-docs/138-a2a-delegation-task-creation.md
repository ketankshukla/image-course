# Diagram 138 — A2A Discovery, Delegation, and Task Creation

![On dark navy, a CLIENT AGENT on a blue platform resolves an AGENT CARD, then sends a MESSAGE carrying CONTEXT ID and REQUEST ID through an A2A INTERFACE into a REMOTE AGENT. The remote agent returns a TASK ID and WORKING STATUS, then later sends STATUS UPDATE and ARTIFACT. A red coral dashed path at the bottom labelled VERSION FALLBACK is blocked by a red X and a forbidden sign. Labels include A2A-VERSION 1.0 and ID badges on each message.](../diagrams/138-a2a-delegation-task-creation.png)

**Module:** Multi-agent collaboration, delegation, and A2A
**Role in the course:** the A2A protocol in action — from message to durable task to artifact
**Layout:** a left-to-right message flow with a version-fallback blocked path below

---

## At a glance

**CLIENT AGENT** resolves an **AGENT CARD**, then sends a **MESSAGE** with **CONTEXT ID** and **REQUEST ID** through the **A2A INTERFACE** to a **REMOTE AGENT**.

The remote agent returns a **TASK ID** and **WORKING STATUS**.

Later it sends **STATUS UPDATE** and **ARTIFACT**.

A coral dashed path at the bottom is **VERSION FALLBACK** — blocked.

The label at the top: **A2A-VERSION 1.0**.

A2A is not a chat. It is a versioned contract that creates a durable task and returns a durable artifact.

---

## What the diagram teaches

### 1. Resolve the card first

The first box on the left is **1. RESOLVE AGENT CARD**. Before any message is sent, the client agent must have a valid, policy-filtered Agent Card from the previous diagram.

That resolution is a separate step because the card is the contract. The client must know the supported A2A version, the security requirements, the input and output modes, and the available skills before it can compose a valid message.

Skipping this step and hard-coding a URL is the common beginner mistake. The URL is not the contract. The card is.

### 2. A message is the request, not the work

The **2. SEND MESSAGE** box carries **CONTEXT ID** and **REQUEST ID**. The message is the envelope that starts the work.

The message is not the task. It is not the artifact. It is the request. The remote agent accepts the message and creates a **TASK** in response.

That distinction matters because messages can be lost, retried, and clarified. A task is durable. A message is ephemeral. The client must not treat a sent message as proof that the work was accepted.

### 3. Task ID is the durable identity of the remote work

The remote agent returns **TASK ID** and **WORKING STATUS**. The client must persist that task ID before it does anything else.

The task ID is the handle. It is how the client asks for status later, how it reconnects after a crash, and how it proves which remote work belongs to which local workflow.

Without the task ID, the client has no durable relationship with the remote agent. It has only a message and a hope.

### 4. Status updates are progress, not results

The remote agent sends **STATUS UPDATE**. It is a notification that the work is progressing. It may say `WORKING`, `INPUT REQUIRED`, `COMPLETED`, or `FAILED`.

A status update is not the artifact. It is not proof that the side effect happened. It is the remote agent's statement about its own state.

The client should record status updates, but it should not update its own business record based on a status alone. The business record changes only when the artifact has been validated.

### 5. The artifact is the durable output

**ARTIFACT** is the final card on the lower path. It is the completed output of the task. In A2A, artifacts are typed, versioned, and associated with the task.

The artifact is the durable business evidence. It is what the client can store, hash, and correlate with its own case record. A status of `COMPLETED` without an artifact is a chat message, not a result.

### 6. Version fallback is blocked

The **VERSION FALLBACK** path is drawn in coral and blocked by a red X.

This is the diagram's security rule. The client and remote agent agreed on A2A version 1.0 when the card was resolved and the message was sent. If the remote agent tries to fall back to an older version during the conversation, the client must reject it.

Version fallback can silently remove guarantees. A feature present in 1.0 may not exist in 0.9. The contract is pinned at the start.

### 7. Context ID and request ID are different things

The message carries both **CONTEXT ID** and **REQUEST ID**.

**Context ID** groups related tasks and messages. It is the conversation. It may be reused across multiple messages and tasks.

**Request ID** identifies this specific message. It is used for idempotency and correlation. Two messages with the same request ID in the same context are the same request.

The task ID is created by the remote agent. The request ID is created by the client. The context ID is agreed or created by the client. All three are needed to trace one delegation.

### 8. Persist the delegation record before you trust the stream

The task ID is not enough. The client must also keep a local **delegation record** that ties the remote task to its own workflow before it subscribes to updates or refreshes a UI. That record should include the workflow identity, the remote agent, the **Agent Card** hash or version, the selected interface, the pinned **A2A-VERSION 1.0**, the **CONTEXT ID**, the **TASK ID**, the current status, the deadline, and the expected artifact contract.

This record is the authoritative boundary between the client and the remote agent. It is what makes a reconnect possible after a client crash. It is what stops a retried message from becoming a second task. And it is what lets an auditor prove which version of the contract produced a given result.

The protocol can retry, the worker can disappear, and the remote agent can revise its proposal, but the delegation record must stay stable. A restart must never change the business meaning of the delegated work. If the record is only in memory or only in the last streamed message, the relationship is still fragile.

### 9. Keep messages bounded, updates idempotent, and business truth separate

The **MESSAGE** in the second box is deliberately bounded: it carries the requested A2A version, the context, the request, and nothing else. Do not stuff the message with extra state, prompts, or business assumptions. The remote agent will create its own task from that envelope, so the message should not leak internal reasoning or unnecessary data.

Status updates and artifact messages must be received idempotently. The same update arriving twice because of a retry should not change the client's record the second time. The client verifies the task identity on every update before it acts, and it treats an artifact update as a typed, versioned delta to an existing task, not as a brand-new outcome.

Most importantly, the client must not confuse protocol truth with business truth. A transport can retry, a queue can redeliver, a model can change its reasoning, and an agent can send a new proposal. The durable business record is what the client stores, validates, and accepts. The A2A interface is a contract, not hidden framework behavior.

Creating a task is only the start. The next diagram shows what ownership of the parent case and the delegated task looks like:

![On dark navy, a PARENT WORKFLOW on a blue platform owns a CASE record. It sends a cyan arrow through a HANDOFF LEDGER with columns FROM, TO, SCOPE, and DEADLINE to a FINANCE AGENT, which receives an INPUT ARTIFACT and an ACCEPTANCE CONTRACT. The finance task moves through SUBMITTED, WORKING, INPUT REQUIRED, and COMPLETED status, returning an OUTPUT ARTIFACT. The parent workflow's CASE ownership never leaves the parent.](../diagrams/139-ownership-handoff-artifact-status.png)

The parent workflow owns the case and never loses it. The finance agent owns the task for a bounded scope and deadline. The handoff ledger records the contract. That is the real shape of A2A delegation: the client creates a task, but the parent remains the owner of the customer outcome.

---

## Case study — Aldermoor Analytics, the report that arrived twice

Aldermoor uses a remote analytics agent to generate risk reports for mortgage applications. The client agent is part of their mortgage workflow.

### What they had

The client sent a message to the analytics agent and waited for a response. The agent returned a report in the response body. The client stored the report and moved the case forward.

There was no task ID. There was no artifact. The report was treated as the response to a request.

### The incident

A network timeout caused the client to retry the message. The analytics agent received the same request twice. It generated two reports, each with a different report ID, because each request was new.

The client received the first report and used it. The second report arrived later and overwrote the first in the case record. The two reports had slightly different calculations because market data had changed between them.

The case record showed the second report, but the underwriting decision had been made on the first. A week later, a reviewer noticed the mismatch and the case had to be re-underwritten.

### The A2A design

The client resolves the analytics agent card, validates the A2A 1.0 interface, and sends a message with a **REQUEST ID**.

The remote agent creates a **TASK** and returns a **TASK ID** and **WORKING STATUS**. The client stores the task ID in the mortgage workflow.

If the client retries because of a network timeout, it sends the same message with the same **REQUEST ID**. The remote agent's deduplication checks the request ID and returns the existing task ID.

The remote agent sends **STATUS UPDATE** messages as the report is generated. When the report is ready, it sends an **ARTIFACT**. The artifact is checked against the expected output contract: a typed report with named fields, not free text.

The client validates the artifact against the expected output contract, records it, and moves the case forward. The artifact includes a content hash, a version, and a correlation to the task and context, so the client can prove which report belongs to which application.

### Results

- **Duplicate reports from retried requests:** 2 per week → 0.
- **Report mismatches between request and stored record:** 1 per month → 0.
- **Time to reconnect after client crash:** unknown, because there was no task handle → immediate, by task ID.
- **Reports accepted as final before validation:** any → 0, because the client now validates the artifact contract.

### The line in their engineering standard

*A message starts a task, a task ID is the handle, and an artifact is the only durable result. Do not treat a status update or a chat response as the final output.*

---

## Composition

A left-to-right protocol flow with a blocked version fallback path below.

**Left:** **CLIENT AGENT** on a blue platform with a robot and an Agent Card icon.

**Two white boxes on the left:**
- **1. RESOLVE AGENT CARD** — person icon with card.
- **2. SEND MESSAGE** — message icon with **CONTEXT ID** and **REQUEST ID** badges.

**Centre:** **A2A INTERFACE** — a blue platform with a network icon. Above it, a cyan banner reads **A2A-VERSION 1.0**.

**Cyan arrow** from SEND MESSAGE through the A2A INTERFACE to the REMOTE AGENT.

**Right:** **REMOTE AGENT** on a blue platform with a robot and a gear card.

**Three white boxes on the right, stacked vertically:**
- **3. RETURN TASK ID, WORKING STATUS** — ID badge and gear.
- **4. SEND STATUS UPDATE** — graph icon.
- **5. SEND ARTIFACT** — document icon.

**Arrows returning left:** teal arrows from each right-side box back to the A2A INTERFACE, then teal arrows from the interface to the client.

**Bottom:** a **coral dashed path** from left to right, with a red X and **VERSION FALLBACK** box, ending at **BLOCKED**.

## Element by element

**CLIENT AGENT / REMOTE AGENT** — the two A2A participants.
**AGENT CARD** — the discoverable contract.
**MESSAGE** — the request envelope.
**CONTEXT ID** — the group identity for related work.
**REQUEST ID** — the idempotent message identity.

**A2A INTERFACE** — the protocol boundary.
**A2A-VERSION 1.0** — the pinned version.

**TASK ID / WORKING STATUS** — the durable remote work identity and its state.
**A2A Task** — stateful remote unit of work.
**STATUS UPDATE** — progress notification.
**ARTIFACT** — the durable output.

**VERSION FALLBACK / BLOCKED** — the rejected silent downgrade.

## Colour and flow semantics

- **Cyan arrows** carry commands and forward work: resolve, send message, version banner.
- **Teal arrows** carry durable state back to the client: task ID, status, artifact.
- **Coral dashed** marks the version fallback path — a failure because the contract is pinned.
- The **ID badges** on every card show that identity is tracked at every step.
- The **A2A-VERSION 1.0 banner** is at the top because version is the umbrella contract.

## How to present it

**Start with the resolve step.** A message is not the beginning. The client must have a valid, policy-filtered card first.

**Point at the message and ask what it is.** Is it the work? Is it the result? It is neither. It is a request that creates a task.

**Trace the task ID.** The client must store it before it does anything else. Ask where their system stores remote task IDs. If the answer is "in the response object," the relationship is not durable.

**Distinguish status update from artifact.** A status is progress. An artifact is output. Do not move a business record on a status.

**Point at VERSION FALLBACK BLOCKED.** The version is agreed at the start. If the remote agent tries to change it, the client refuses. This prevents silent loss of guarantees.

**Tell the Aldermoor story.** A retried request produced two reports. No task ID, no artifact, no deduplication. The fix: request ID, task ID, status updates, artifact validation.

**Ask what happens after a client crash.** If there is no stored task ID, the work is orphaned. With A2A, the client reconnects by task ID.

**Point at the version fallback path and ask why it is blocked.** A silent protocol downgrade can remove security or idempotency guarantees. The client and agent agreed on 1.0 at the start; that is the contract.

**Close on the standard.** *A message starts a task, a task ID is the handle, and an artifact is the only durable result. Do not treat a status update or a chat response as the final output.*

**Run the checkpoint.** Ask: Should an A2A Message carry the final report? Let the room argue, then confirm that messages support initiation, clarification, status, and interaction, while results belong in artifacts associated with a task.

**Put the delegation record on the board.** Ask the room to list the fields a local record needs before it can safely subscribe to updates. Prompt for workflow, remote agent, card version, interface, protocol version, context, task, status, deadline, and artifact contract.

**Show the implementation frame.** In a Next.js system, call remote A2A interfaces only from protected server code and project task states into the local case timeline through a typed adapter. In Python, use the current A2A SDK behind a narrow client adapter, persist the local-to-remote task correlation before subscribing, and treat artifact updates as idempotent deltas.

**Cite the sources.** This diagram follows the A2A Protocol 1.0 specification and the A2A key concepts.

**Timing.** Twenty minutes. Thirty if the room maps one real integration to message, task, status, and artifact, which usually exposes that it is currently message-and-response only.

---

## Lab and checkpoint

**Lab:** Pick one real integration and re-map it to A2A: resolve the agent card, send a message that creates a task, store the task ID, subscribe to status updates, and receive the artifact. Persist the delegation record with workflow, agent, card version, protocol version, context, task, and artifact contract. Then ensure version fallback is blocked.

**Checkpoint:** Why must a client persist the delegation record before it subscribes to updates?

**Answer:** Because a client that crashes before storing the task ID and delegation record can lose the relationship to the remote work. When it recovers, it has no handle to reconnect, continue, or verify the artifact. Persisting first makes the local-to-remote task correlation durable.

## Glossary

- **Artifact** — the durable output of an A2A task.
- **Context ID** — the identifier that groups related tasks across the workflow.
- **Delegation record** — the durable local record of a delegated A2A task.
- **Message** — the request that creates or interacts with a task.
- **Request ID** — the identifier for the local request that sent the message.
- **Resolve** — the step that validates the agent card before delegating.
- **Status update** — a progress notification, not a result.
- **Task** — the remote work identified by a task ID.
- **Task ID** — the durable handle for a remote task.
- **Version fallback** — the blocked path that would silently downgrade the protocol.

## Sources

- A2A Protocol 1.0 and task lifecycle
- A2A message, status, and artifact
- Delegation record and durable remote work
