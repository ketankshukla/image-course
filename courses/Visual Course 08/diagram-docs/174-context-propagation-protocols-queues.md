# Diagram 174 — Context propagation across MCP, A2A, AG-UI, HTTP, and queues

![A W3C trace context is injected and extracted across browser, Next.js, FastAPI, MCP, A2A, and queue boundaries while business IDs remain separate and asynchronous work uses span links.](../diagrams/174-context-propagation-protocols-queues.png)

**Module:** Telemetry and correlation
**Role in the course:** Follow one business request across every service and protocol while keeping telemetry useful, versioned, and privacy-safe.
**Layout:** The diagram shows one TRACEPARENT ribbon flowing from BROWSER to NEXT.JS to FASTAPI, then branching to MCP CALL, A2A TASK, and QUEUE MESSAGE before joining an ARTIFACT; it also places separate BUSINESS ID cards labeled REQUEST ID, TASK ID, CONTEXT ID, ARTIFACT ID.

---

## At a glance

**Preserve one explainable evidence chain across protocol and asynchronous boundaries without confusing trace identity with business identity.**

- Create one trace at the trusted entry point or validate and continue an acceptable incoming context.
- Extract before work begins, create a correctly parented span, and inject before every supported outbound boundary.
- Record MCP request, A2A task and context, run, message, and artifact IDs as separate correlation attributes.
- A BROKEN CONTEXT path shows the failure the design must catch before it reaches the user.

---

## What the diagram teaches

### 1. Preserve one evidence chain across protocols and time

Context propagation carries the small identifiers needed to connect work performed by different components. For HTTP, the stable baseline is the W3C traceparent header and optional tracestate. The receiving service extracts that context, creates a child span, and injects the updated context into the next outbound call. Queues require the same inject-and-extract idea using message properties; delayed, batched, retried, or fan-out work may be better represented with span links rather than pretending every operation is one simple parent-child chain. MCP request metadata, A2A task and context identifiers, AG-UI run or event identifiers, application request IDs, and artifact IDs are useful business correlation fields, but none is automatically a distributed trace ID. The diagram exists so the team can preserve one explainable evidence chain across protocol and asynchronous boundaries without confusing trace identity with business identity.

### 2. Create one trace at the trusted entry point or validate

Create one trace at the trusted entry point or validate and continue an acceptable incoming context. Queues require the same inject-and-extract idea using message properties; delayed, batched, retried, or fan-out work may be better represented with span links r. Trust boundaries matter: validate incoming propagation fields, do not put personal data or authorization in trace headers. In the diagram, this is represented by **TRACEPARENT** and **CONTEXT ID**, near **BROKEN CONTEXT**. The case study where Maya's support request starts in the browser, triggers a FastAPI workflow, delegates policy research to another agent, and resumes from a queue five minutes later makes the risk concrete: using a customer email, access token, prompt, or full task payload as baggage or tracestate spreads sensitive data to every downstream service and telemetry backend. When this step is done well, an operator can move from Maya's artifact to the workflow, task, message attempt, and trace without overloading any one identifier.

### 3. Extract before work begins, create a correctly parented span,

In the diagram, this is represented by **INJECT** and **EXTRACT**. Extract before work begins, create a correctly parented span, and inject before every supported outbound boundary. The receiving service extracts that context, creates a child span, and injects the updated context into the next outbound call. Queues require the same inject-and-extract idea using message properties; delayed, batched, retried, or fan-out work may be better represented with span links r. The case study where Maya's support request starts in the browser, triggers a FastAPI workflow, delegates policy research to another agent, and resumes from a queue five minutes later shows the value: an operator can move from Maya's artifact to the workflow, task, message attempt, and trace without overloading any one identifier. Skip it, and using a customer email, access token, prompt, or full task payload as baggage or tracestate spreads sensitive data to every downstream service and telemetry backend. The takeaway is clear: propagate trace context; correlate business IDs; never confuse either with authority.

### 4. Record MCP request, A2A task and context, run, message,

MCP request metadata, A2A task and context identifiers, AG-UI run or event identifiers, application request IDs, and artifact IDs are useful business correlation fields. This is why the step is non-negotiable: record MCP request, A2A task and context, run, message, and artifact IDs as separate correlation attributes. Keep these identities separate and record their relationships. In the diagram, this is represented by **A2A TASK** and **ARTIFACT**, near **ARTIFACT ID**. The case study where Maya's support request starts in the browser, triggers a FastAPI workflow, delegates policy research to another agent, and resumes from a queue five minutes later proves it: an operator can move from Maya's artifact to the workflow, task, message attempt, and trace without overloading any one identifier. If the team omits this, using a customer email, access token, prompt, or full task payload as baggage or tracestate spreads sensitive data to every downstream service and telemetry backend.

### 5. Use span links for fan-out, retries, batches, and work

Use span links for fan-out, retries, batches, and work that begins long after the initiating request ends. The receiving service extracts that context, creates a child span, and injects the updated context into the next outbound call. Queues require the same inject-and-extract idea using message properties; delayed, batched, retried, or fan-out work may be better represented with span links r. In the diagram, this is represented by **SPAN LINK**. The case study where Maya's support request starts in the browser, triggers a FastAPI workflow, delegates policy research to another agent, and resumes from a queue five minutes later makes the risk concrete: using a customer email, access token, prompt, or full task payload as baggage or tracestate spreads sensitive data to every downstream service and telemetry backend. When this step is done well, an operator can move from Maya's artifact to the workflow, task, message attempt, and trace without overloading any one identifier.

### 6. Test missing, malformed, duplicated, stale, and attacker-controlled context so

In the diagram, this is represented by **BUSINESS ID** and **CONTEXT ID**, near **BROKEN CONTEXT**. Test missing, malformed, duplicated, stale, and attacker-controlled context so a broken header never breaks the business operation. MCP request metadata, A2A task and context identifiers, AG-UI run or event identifiers, application request IDs, and artifact IDs are useful business correlation fields. The receiving service extracts that context, creates a child span, and injects the updated context into the next outbound call. The case study where Maya's support request starts in the browser, triggers a FastAPI workflow, delegates policy research to another agent, and resumes from a queue five minutes later shows the value: an operator can move from Maya's artifact to the workflow, task, message attempt, and trace without overloading any one identifier. Skip it, and using a customer email, access token, prompt, or full task payload as baggage or tracestate spreads sensitive data to every downstream service and telemetry backend. The takeaway is clear: propagate trace context; correlate business IDs; never confuse either with authority.

### 7. Putting it together

Taken together, these steps turn the objective "preserve one explainable evidence chain across protocol and asynchronous boundaries without confusing trace identity with business identity" into an operating contract. Create one trace at the trusted entry point or validate and continue an acceptable incoming context; Extract before work begins, create a correctly parented span, and inject before every supported outbound boundary; Record MCP request, A2A task and context, run, message, and artifact IDs as separate correlation attributes. The remaining steps extend this: Use span links for fan-out, retries, batches, and work that begins long after the initiating request ends; Test missing, malformed, duplicated, stale, and attacker-controlled context so a broken header never breaks the business operation. The case of Maya's support request starts in the browser, triggers a FastAPI workflow, delegates policy research to another agent, and resumes from a queue five minutes later shows how quickly using a customer email, access token, prompt, or full task payload as baggage or tracestate spreads sensitive data to every downstream service and telemetry backend. The durable lesson is propagate trace context; correlate business IDs; never confuse either with authority.

### Analogy

A train ticket, a parcel tracking number, and a hotel booking number can belong to one holiday, but they are different identifiers. The itinerary records the relationship without pretending they are interchangeable.

### The Next.js surface

In the Next.js surface, the same contract appears through framework-specific patterns. Use AsyncLocalStorage or the OpenTelemetry context manager to keep trace context attached to the current server request and outbound fetch calls. Translate browser run IDs and server request IDs into span attributes, but let the tracing SDK own trace and span identifier format. When creating queue messages or MCP/A2A requests, inject trace context through a typed carrier adapter and add business IDs in their defined metadata fields.

### The Python surface

In the Python surface, the same contract is enforced with typed models and tests. Use FastAPI middleware for inbound extraction and ContextVar-backed context for asynchronous request and worker code. Instrument HTTP clients and queue producers and consumers; add span links when a consumer handles retried or batched work with more than one cause. Write contract tests that assert continuity, valid parentage, business-ID correlation, and graceful behavior when propagation is absent or invalid.
![One user outcome connects to a distributed trace made of spans, correlated logs, aggregate metrics, timestamped events, and resource identity such as service and version.](../diagrams/173-traces-spans-logs-metrics-events-resources.png)

Diagram 173 — *Traces, spans, logs, metrics, events, and resources* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

---

## Case study — Maya's multi-protocol support request

Maya's support request starts in the browser, triggers a FastAPI workflow, delegates policy research to another agent, and resumes from a queue five minutes later.

### The walkthrough

1. The browser run ID remains a product identifier while the server creates the trusted trace.
2. Next.js and FastAPI propagate trace context and record the A2A context ID and task ID on delegation spans.
3. The queue message carries injected trace context plus a durable workflow ID, attempt number, and idempotency key.
4. The resumed worker links its span to the earlier work and records the final artifact ID and user-visible receipt.

### The result

An operator can move from Maya's artifact to the workflow, task, message attempt, and trace without overloading any one identifier.

### The danger

Using a customer email, access token, prompt, or full task payload as baggage or tracestate spreads sensitive data to every downstream service and telemetry backend.

### The takeaway

Propagate trace context; correlate business IDs; never confuse either with authority.

---

## Composition

A single cyan TRACEPARENT ribbon enters from the left at BROWSER, flows right through NEXT.JS and FASTAPI, then branches into three cyan paths: an MCP CALL, an A2A TASK, and a QUEUE MESSAGE. These converge again on an ARTIFACT near the right. Along the ribbon, INJECT and EXTRACT gates mark where context crosses boundaries. Four separate BUSINESS ID cards—REQUEST ID, TASK ID, CONTEXT ID, and ARTIFACT ID—float above the flow to show that business identity is not the same as trace identity. A SPAN LINK curves toward asynchronous work. Near the bottom, one coral BROKEN CONTEXT gap interrupts the ribbon, showing a missing or malformed trace context. The composition reads left to right like a map of a single request traveling across protocols and time.

## Element by element

- **TRACEPARENT** — The **TRACEPARENT** is a ribbon flowing from BROWSER to NEXT.JS to FASTAPI,.
- **BROWSER** — The **BROWSER** is a cyan request or propagation path that one TRACEPARENT ribbon flowing from to NEXT.JS to FASTAPI,.
- **NEXT.JS** — The **NEXT.JS** is the TypeScript/React application that receives user-facing requests and continues telemetry context on the server.
- **FASTAPI** — The **FASTAPI** is the Python backend service that processes requests, enforces policy, and emits durable business records.
- **MCP CALL** — The **MCP CALL** is a cyan request or propagation path that then branching to ,.
- **A2A TASK** — The **A2A TASK** is a cyan request or propagation path.
- **QUEUE MESSAGE** — The **QUEUE MESSAGE** is a ARTIFACT .
- **ARTIFACT** — The **ARTIFACT** is iD.
- **BUSINESS ID** — The **BUSINESS ID** is the set of identifiers that separate business identity from trace identity.
- **REQUEST ID** — The **REQUEST ID** is the protocol or application identifier for the user request, separate from the trace identity.
- **TASK ID** — The **TASK ID** is the A2A task identifier used to delegate and track work.
- **CONTEXT ID** — The **CONTEXT ID** is the A2A context identifier used to correlate related tasks and artifacts.
- **ARTIFACT ID** — The **ARTIFACT ID** is the durable identifier for an output artifact produced by the workflow.
- **INJECT** — The **INJECT** is and EXTRACT gates,.
- **EXTRACT** — The **EXTRACT** is a cyan request or propagation path that iNJECT and gates,.
- **SPAN LINK** — The **SPAN LINK** is the non-parent relationship that connects asynchronous work to a causal span.
- **BROKEN CONTEXT** — The **BROKEN CONTEXT** is a coral failure, risk, or incident path that one coral gap.

---

## Colour and flow semantics

- **Cyan arrow** — a request, propagated context, telemetry signal, evaluation flow, or candidate release path. In this diagram it appears on **TRACEPARENT**, **BROWSER**, **NEXT.JS**, **FASTAPI**, **MCP CALL**, **A2A TASK**, **QUEUE MESSAGE**, **INJECT** and others.
- **Coral path** — a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path. In this diagram it appears on **BROKEN CONTEXT**.
- **White card** — a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record. In this diagram it appears on **ARTIFACT**, **BUSINESS ID**, **REQUEST ID**, **TASK ID**, **CONTEXT ID**, **ARTIFACT ID**, **SPAN LINK**.

The overall flow moves from the inputs on the left through the telemetry and correlation stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.

---

## How to present it

- Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it.
- Ask the room what the team would need to know before approving the next release. Point at **TRACEPARENT** and **CONTEXT ID** and ask what would change if this step were skipped? Use the case study to make the failure concrete.
- Have the group list the operational decisions this stage informs. Highlight **INJECT** and **EXTRACT** and ask what real decision does this evidence support? Use the case study to make the failure concrete.
- Ask what evidence would change the route a support ticket takes. Trace with your finger **A2A TASK** and **ARTIFACT** and ask what would a missing or corrupted value look like here? Use the case study to make the failure concrete.
- Get the room to name the owner who would need this evidence in an incident. Put a marker on **SPAN LINK** and ask who owns the evidence produced at this step? Use the case study to make the failure concrete.
- Ask what would need to be true for the team to skip this stage safely. Ask the room to locate **BUSINESS ID** and **CONTEXT ID** and ask which downstream stage would fail if this step were wrong? Use the case study to make the failure concrete.
- Use the analogy. A train ticket, a parcel tracking number, and a hotel booking number can belong to one holiday, but they are different identifiers. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.
- Tell the case study — Maya's multi-protocol support request. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.
- Run the lab. Create a carrier matrix for HTTP, MCP, A2A, AG-UI, and one queue. For each boundary, specify inject, extract, continue, link, restart, validation, missing-context behavior, and the separate business identifiers recorded. Have each group label the fields that are captured, hashed, redacted, or omitted.
- Pose the checkpoint. Is an A2A task ID a replacement for a W3C trace ID? Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.
- Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.
- Close on the contract. Propagate trace context; correlate business IDs; never confuse either with authority. Make the group write one sentence that ties the lesson to their own system.

---

## Lab and checkpoint

**Lab:** Create a carrier matrix for HTTP, MCP, A2A, AG-UI, and one queue. For each boundary, specify inject, extract, continue, link, restart, validation, missing-context behavior, and the separate business identifiers recorded.

**Checkpoint:** Is an A2A task ID a replacement for a W3C trace ID?

**Answer:** No. The task ID identifies protocol-level business work. Trace context connects observability operations across services. Record the relationship between them.

---

## Glossary

- **Propagation** — carrying context across a boundary
- **Carrier** — headers or message properties that transport context
- **Span link** — a non-parent relationship to one or more causal spans

---

## Sources

- [W3C Trace Context](https://www.w3.org/TR/trace-context/)
- [W3C Baggage](https://www.w3.org/TR/baggage/)
- [A2A Protocol 1.0 specification](https://a2a-protocol.org/latest/specification/)
- [OpenTelemetry messaging semantic conventions](https://opentelemetry.io/docs/specs/semconv/messaging/)

---

## Related lessons

- Diagram 173 — Traces, spans, logs, metrics, events, and resources
- Diagram 176 — Business outcomes, artifacts, receipts, and trace references
- Diagram 193 — Alerts, ownership, triage, and runbooks

---
