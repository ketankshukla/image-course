# Diagram 160 — Secret Managers, Short-Lived Credentials, and Rotation

![On dark navy, an AGENT and a MODEL sit at the top with red X marks blocking their path to the SECRET VAULT. A WORKLOAD IDENTITY platform on the left sends cyan arrows labelled TARGET, PURPOSE, POLICY, and TTL to a CREDENTIAL BROKER. The broker fetches from the SECRET VAULT and sends a SHORT-LIVED HANDLE directly to a TOOL ADAPTER, which produces an ACCESS RECEIPT. Below, a coral flow shows ENV FILE, PROMPT, LOG, and ARTIFACT copies moving toward a QUARANTINE box.](../diagrams/160-secret-manager-short-lived-credentials.png)

**Module:** Capabilities, tools, policy, and secrets
**Role in the course:** how to keep secrets out of prompts, browser code, logs, queues, and artifacts while still letting approved tools authenticate
**Layout:** a workload identity requests a short-lived credential from a broker, the broker delivers it directly to a tool adapter, while the agent and model are explicitly blocked and exposure paths are quarantined

---

## At a glance

The **AGENT** and **MODEL** never reach the **SECRET VAULT**.

A **WORKLOAD IDENTITY** asks the **CREDENTIAL BROKER** for a credential, providing **TARGET, PURPOSE, POLICY,** and **TTL**.

The broker returns a **SHORT-LIVED HANDLE** directly to the **TOOL ADAPTER**.

The tool adapter produces an **ACCESS RECEIPT**.

**ENV FILE, PROMPT, LOG,** and **ARTIFACT** are the places where leaked secret material is quarantined.

A restaurant manager opens the safe and hands a temporary till key to the cashier; the customer ordering food never sees the key.

---

## What the diagram teaches

### 1. The model usually needs the result, not the credential

The diagram places the **AGENT** and **MODEL** at the top with red X marks. They do not need the payment API key, the database password, or the signing certificate. They need the result of calling a tool that uses the credential. The credential is not data for reasoning; it is a permission to act.

This boundary is the most common place where agent systems leak. A developer passes the secret into the model context so it can "understand the integration." A prompt includes the API key because a tool description needs it. A log captures the full tool call. The diagram says no. The model gets the tool result. The credential goes directly from protected storage to the narrow adapter that uses it.

### 2. A credential broker makes the credential purpose-bound and short-lived

The **WORKLOAD IDENTITY** does not read a secret from a file and hold it. It asks the **CREDENTIAL BROKER** for a credential, providing **TARGET, PURPOSE, POLICY,** and **TTL**. The broker decides whether the workload is allowed to have a credential for that target, for that purpose, under that policy, and for that time window.

The broker may fetch a secret from the **SECRET VAULT**, mint a short-lived token, or exchange a workload token for a target credential. In every case, the credential is bound to the workload identity, the target, the purpose, and the lifetime. It is not a reusable master key.

### 3. Direct handoff from broker to adapter keeps the secret out of general code

The **SHORT-LIVED HANDLE** goes directly to the **TOOL ADAPTER**. The tool adapter is the narrow code that knows how to call the payment provider, database, or signing service. The agent, the model, the prompt, and the browser never see the credential.

This direct handoff is the heart of the design. If the credential has to pass through the agent's memory, the model context, or the UI before it reaches the adapter, it can be logged, echoed, or exfiltrated. The broker must hand the credential to the adapter in the same way a cashier receives a key: directly and briefly.

### 4. Short-lived credentials reduce the value of a leak

Short-lived credentials expire quickly. A leaked credential captured in a log, a prompt, or a cache is only useful for a short window. The **TTL** in the request is a security control, not a convenience. A credential with a five-minute lifetime and a specific target is much less dangerous than a long-lived API key stored in an environment variable.

Short lifetimes also support rotation. A credential can be rotated without rewriting prompts or code because the broker mints or fetches a new one for each call.

### 5. Rotation is a control, not a quarterly chore

The **SECRET VAULT** has a rotation loop. Rotation changes or revokes credentials on a schedule or in response to an alert. The diagram shows the broker connected to the vault because the broker is where rotation is enforced. The tool adapter does not cache a key for the lifetime of the process. It asks for a fresh handle when it needs to act.

This makes incident response faster. If a credential is exposed, the team rotates the vault credential and the broker stops issuing the old one. No prompt, no model, and no tool adapter needs to change.

### 6. The quarantine path names the likely leaks

The bottom of the diagram shows a coral flow: **ENV FILE → PROMPT → LOG → ARTIFACT → QUARANTINE**. These are the places where secret material is most likely to escape.

- **ENV FILE** — a shared environment file checked into source control.
- **PROMPT** — the model context that includes a secret for "clarity."
- **LOG** — telemetry that captures the full tool call.
- **ARTIFACT** — a cache, queue, or downloadable file that preserves the credential.

The diagram does not say these are forbidden. It says they are the places to scan, redact, and quarantine. A secret stored safely in a vault but copied into a prompt or a log is no longer safely controlled.

### 7. Workload identity, not user identity, asks for the credential

The **WORKLOAD IDENTITY** is the identity of the running software, not the human user. The credential is requested by the workload, authorized by policy, and bound to the workload's identity. This is different from forwarding the user's session token to the payment provider.

The workload identity may be derived from a SPIFFE ID, a Kubernetes service account, an AWS IAM role, or an OAuth token exchange. The important thing is that the secret is not tied to a human session. It is tied to a specific, scoped, short-lived runtime identity.

### 8. Redaction and scanning are the last line of defense

Even with a direct handoff, secrets can leak through errors, exceptions, debug traces, or support views. The system must redact known formats and sensitive fields from telemetry. DLP scanning in logs and artifacts catches the cases where the broker handoff fails or where an exception dumps the credential.

Redaction is not a substitute for the direct handoff. It is a safety net. The first line is: the credential never enters the model context, the browser, the prompt, the queue, or the artifact. The second line is: if it does, redaction and quarantine catch it.

### 9. The previous lesson shows the capability that this secret enables

![On dark navy, a large coral key labeled ADMIN TOOL is shown on the left with a red X. To the right, four white capability cards sit on a cobalt platform: READ CASE, EXTRACT INVOICE, QUOTE REFUND, and ISSUE BOUND REFUND. Each card lists six fields. A CAPABILITY BROKER selects one card and hands it to an AGENT. POLICY and RECEIPT shields surround the high-impact tool.](../diagrams/157-least-privilege-capability-tools.png)

Diagram 157 defines a narrow capability card. Diagram 160 shows how that card gets the credential it needs to execute. A capability card such as **ISSUE BOUND REFUND** has a **DESTINATION** and a **LIMIT**. The credential broker issues a short-lived handle that can only be used for that destination and that limit. The two diagrams together describe a safe tool: one designs the capability; the other protects the secret that makes it real.

### 10. The Next.js map: server-only modules and no NEXT_PUBLIC secrets

In Next.js, secrets must be accessed only in server-only modules. They must not be placed in `NEXT_PUBLIC` variables or serialized props. External SDKs should be wrapped behind narrow adapters that receive a short-lived credential from a server-side broker. The React UI receives only the result and the access receipt.

Tokens, policy decisions, secrets, and privileged mutations stay in authenticated server code. The browser receives only the minimum display state. Typed request, decision, denial, approval, and receipt records let the React interface explain the security state without inventing it.

### 11. The Python map: dependency-injected provider clients and structured logging

In Python, secrets should be resolved inside dependency-injected provider clients. Prefer short-lived workload credentials over long-lived API keys. Use a credential broker or a secret manager that issues tokens bound to the workload identity. Structured logging should include field-level redaction so a credential or a token hash never appears in plain text.

Pydantic models plus explicit middleware keep identity, tenant, policy, data classification, and audit context separate. Tests should cover allow and deny paths with hostile synthetic fixtures. Test that a tool cannot be tricked into returning the secret, that a log does not capture the credential, and that a rotated secret stops working immediately.

### 12. A secret is a secret only as long as it stays in the vault

The safety rule is: secret material never enters model context, client bundles, general logs, durable queue payloads, downloadable artifacts, or cross-tenant caches. A secret manager is not enough if the secret is copied everywhere. The system must verify the relevant identity and tenant, evaluate narrow authority, constrain data and destinations, and preserve enough evidence to explain both allowed and denied outcomes.

---

## Case study — The vendor asks for the API key

A hostile vendor attachment tells the Acme agent to print the payment API key so the vendor can validate it.

### What the design does

1. The model has no tool that returns secret values. The available tools are **READ CASE**, **EXTRACT INVOICE**, **QUOTE REFUND**, and **ISSUE BOUND REFUND**.
2. When the refund tool runs, the payment adapter requests a short-lived credential through the workload identity.
3. The credential is injected directly into the provider client and discarded after the call.
4. The attempted request is logged in redacted form and linked to the attachment evidence.

### Result

The payment call succeeds without making the credential available to the agent or vendor. The vendor cannot validate a key it never sees.

### The danger

A secret stored safely but copied into prompts, exceptions, debug traces, environment dumps, or artifacts is no longer safely controlled. A shared `.env` file in a repository is not a secret manager. A log that captures the full HTTP request is a secret leak.

### The takeaway

Give the adapter a short-lived secret. Give the agent only the result.

---

## Composition

The diagram has a top half and a bottom half.

**Top half — the safe flow:**
- **AGENT** and **MODEL** at the top, blocked from the secret vault.
- **WORKLOAD IDENTITY** on the left, sending **TARGET, PURPOSE, POLICY,** and **TTL** to the **CREDENTIAL BROKER**.
- **CREDENTIAL BROKER** in the center, connected to the **SECRET VAULT** below.
- **SHORT-LIVED HANDLE** going from broker to **TOOL ADAPTER**.
- **ACCESS RECEIPT** on the right.

**Bottom half — the leak path:**
- **ENV FILE**, **PROMPT**, **LOG**, and **ARTIFACT** in coral, feeding **QUARANTINE**.

The flow reads from left to right at the top, while the bottom row shows the places where secret material is quarantined.

## Element by element

**AGENT** — the automated actor that plans and calls tools.

**MODEL** — the language model that reasons but does not receive credentials.

**WORKLOAD IDENTITY** — the runtime identity of the software that will use the credential.

**TARGET** — the intended resource or service for the credential.

**PURPOSE** — the reason the credential is being requested.

**POLICY** — the policy decision that authorizes the request.

**TTL** — the maximum lifetime of the credential.

**CREDENTIAL BROKER** — the service that issues or retrieves scoped, short-lived credentials.

**SECRET VAULT** — the protected store for credentials at rest.

**SHORT-LIVED HANDLE** — the temporary credential delivered directly to the tool adapter.

**TOOL ADAPTER** — the narrow code that uses the credential to call the target service.

**ACCESS RECEIPT** — the durable record of the credential request and use.

**ENV FILE** — a common source of leaked secrets in configuration files.

**PROMPT** — the model context, which must not include credentials.

**LOG** — telemetry that must redact or exclude secrets.

**ARTIFACT** — cache, queue, or file storage where secrets must not persist.

**QUARANTINE** — the control that isolates and removes exposed secret material.

## Colour and flow semantics

- **Cobalt platform** — a protected boundary or identity. The WORKLOAD IDENTITY, CREDENTIAL BROKER, SECRET VAULT, and TOOL ADAPTER are cobalt.
- **Cyan arrow** — a request or delegated authority. The arrows from workload to broker and broker to adapter are cyan.
- **Teal path** — a verified, safe, or receipt-producing path. The SHORT-LIVED HANDLE and ACCESS RECEIPT are teal.
- **Coral path** — an exposure, leak, or quarantine. The ENV FILE, PROMPT, LOG, and ARTIFACT flow is coral.
- **White card** — an identity, claim, policy, token, approval, artifact, or evidence record.
- **Red X** — a blocked path. The agent and model are blocked from the secret vault.

The safe flow runs from left to right across the top. The leak path runs from left to right across the bottom. The vertical separation makes the boundary clear.

## How to present it

**Ask the room where their secrets live.** Most will say a secret manager or environment variables. Then ask whether those secrets ever appear in logs, prompts, browser bundles, or cached tool calls.

**Point at the AGENT and MODEL.** They are at the top, blocked from the vault. Ask why. The answer is that the model does not need the credential; it needs the result.

**Trace the safe flow.** Workload identity sends target, purpose, policy, and TTL. The broker fetches from the vault. A short-lived handle goes directly to the tool adapter. The adapter produces a receipt. The agent and model never touch the credential.

**Emphasize the direct handoff.** The credential must not pass through the model, the prompt, the UI, or a shared queue. If it does, the system has failed at the most important boundary.

**Discuss short-lived credentials.** A credential with a five-minute lifetime and a single target is much less dangerous than a long-lived key. Ask what their credential lifetimes are.

**Discuss the quarantine path.** ENV FILE, PROMPT, LOG, ARTIFACT. These are not theoretical. They are the actual places where secrets leak. Ask for one real example from their system.

**Pair with Diagram 157.** A tool contract is only as safe as the credential that runs it. A narrow refund tool plus a short-lived, directly handed credential is a strong combination.

**Map to Next.js.** No `NEXT_PUBLIC` secrets. Server-only modules. Wrap SDKs behind narrow adapters. Pass only the result and receipt to the UI.

**Map to Python.** Dependency-injected provider clients. Short-lived workload credentials. Structured logging with redaction. Test that a tool cannot be asked to return the secret.

**Run the lab as an inventory.** Have the room list every Acme secret, its owner, storage, accessor identity, target audience, lifetime, rotation, redaction, revocation, and an exposure test.

**Ask the checkpoint.** "Does placing an API key in a server environment variable make it short-lived or least privilege?" The answer is no. It may keep it out of the browser, but scope, lifetime, rotation, accessor identity, and leakage paths still need design.

**Close on the standard.** Secret material never enters model context, client bundles, general logs, durable queue payloads, downloadable artifacts, or cross-tenant caches. The adapter gets a short-lived credential; the agent gets only the result.

**Timing.** Twenty to twenty-five minutes, plus five minutes for the lab inventory.

---

## Lab and checkpoint

**Lab:** Inventory every Acme secret. Record owner, storage, accessor identity, target audience, lifetime, rotation, redaction, revocation, and an exposure test.

**Checkpoint:** Does placing an API key in a server environment variable make it short-lived or least privilege?

**Answer:** No. It may keep it out of the browser, but scope, lifetime, rotation, accessor identity, and leakage paths still need design.

---

## Glossary

- **Secret manager** — a controlled store for credentials and other sensitive values.
- **Credential broker** — a service that issues or retrieves bounded, short-lived credentials for authenticated workloads.
- **Rotation** — the process of replacing a credential and retiring the old one.
- **Short-lived credential** — a credential with a limited lifetime, reducing the impact of a leak.
- **Quarantine** — the process of isolating and removing exposed secret material.

---

## Sources

- OWASP Secrets Management
- SPIFFE specifications
