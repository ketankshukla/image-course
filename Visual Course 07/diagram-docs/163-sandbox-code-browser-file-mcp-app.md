# Diagram 163 — Sandboxed Code, Browser, File, and MCP App Execution

![On dark navy, INPUT enters SCAN and CLASSIFY on the left. From there, four separate blue sandbox boxes run in parallel: CODE VM, BROWSER SESSION, FILE WORKSPACE, and MCP APP IFRAME. Each box lists CPU, MEMORY, TIME, FILE, NETWORK, ORIGIN, and PERMISSION limits. In the center, four coral blocks labelled HOST FILE, LOCAL CREDENTIAL, TOP NAVIGATION, and ARBITRARY NETWORK are blocked by red X marks. On the right, OUTPUT leaves each sandbox through VALIDATE and DLP.](../diagrams/163-sandbox-code-browser-file-mcp-app.png)

**Module:** Tenant isolation and runtime boundaries
**Role in the course:** how to contain executable or interactive agent work so one malicious input cannot reach the host, credentials, other tenants, or unrestricted network
**Layout:** four sandboxes for code, browser, file, and MCP App, with input scanning, resource and permission limits, blocked host-level paths, and output validation

---

## At a glance

Four **sandboxes** run side by side: **CODE VM**, **BROWSER SESSION**, **FILE WORKSPACE**, and **MCP APP IFRAME**.

Each sandbox has **CPU, MEMORY, TIME, FILE, NETWORK, ORIGIN,** and **PERMISSION** limits.

**INPUT** passes through **SCAN** and **CLASSIFY** before entering any sandbox.

Coral attempts to touch the **HOST FILE, LOCAL CREDENTIAL, TOP NAVIGATION,** or **ARBITRARY NETWORK** are blocked.

**OUTPUT** leaves through **VALIDATE** and **DLP** before it can be used.

A chemistry experiment happens in a fume hood with measured ingredients, limited tools, a timer, and controlled waste—not on the office kitchen table.

---

## What the diagram teaches

### 1. A sandbox is a restricted execution environment, not just a container

The diagram shows four different kinds of sandboxes because "sandbox" means different things for different work. A **CODE VM** constrains a process and its resources. A **BROWSER SESSION** isolates origins, downloads, and navigation. A **FILE WORKSPACE** provides temporary, scoped storage. An **MCP APP IFRAME** renders a remote UI with declared permissions and content security policy.

The common idea is the same: the execution receives only explicit inputs and capabilities, has bounded resources and lifetime, and releases only validated outputs. The boundary is the wall between the untrusted or semi-trusted work and the host, tenant data, secrets, identity session, and network.

### 2. Input must be scanned and classified before execution

The first two boxes are **SCAN** and **CLASSIFY**. Before any code, browser, file, or MCP App runs, the system must know what kind of input it is and what the smallest appropriate execution profile is. A PDF is not the same as a Python script. An MCP App is not the same as a generic web page.

Classification also drives the limits. A code sandbox for a refund calculation needs a different profile from a code sandbox that converts a file format. A browser preview of an MCP App needs stricter origin and navigation limits than a browser session used to fetch a static page.

### 3. Each sandbox carries the same seven limits

The diagram lists **CPU, MEMORY, TIME, FILE, NETWORK, ORIGIN,** and **PERMISSION** for every sandbox. These are not optional extras. They are the control surface.

- **CPU** and **MEMORY** prevent a runaway process from starving the host.
- **TIME** enforces a maximum lifetime and kills stuck work.
- **FILE** limits which files the sandbox can see and write.
- **NETWORK** controls whether and where the sandbox can make outbound calls.
- **ORIGIN** restricts browser and MCP App navigation and resource loading.
- **PERMISSION** lists the specific capabilities the sandbox is allowed to request.

A sandbox without one of these limits is not a sandbox; it is a slower process.

### 4. The sandbox must not inherit ambient host credentials

The central coral block **LOCAL CREDENTIAL** is blocked. Ambient credentials are secrets that the host process, browser, or file system would make available automatically. A sandbox that can read `~/.aws/credentials`, `~/.kube/config`, or the browser's cookies is not isolated.

Creating an ephemeral sandbox means it starts with nothing. No host files, no local credentials, no default network access, no pre-approved permissions. Everything it has must be granted explicitly.

### 5. Code sandboxes need real process and resource isolation

The **CODE VM** is not `eval` in the same process. It is an external sandbox service, a VM, a container with a strict seccomp profile, or a WebAssembly runtime with no host access. The diagram uses the term **CODE VM** to emphasize that the code runs in its own virtualized environment.

The sandbox has its own CPU and memory limits, a bounded file system, no network by default, and a short time limit. The input is scanned and classified. The output is validated and scanned. The environment is destroyed after the run, and cleanup is verified.

### 6. Browser sandboxes isolate the origin and navigation surface

The **BROWSER SESSION** sandbox is for web pages or web-based tools. Its **ORIGIN** and **PERMISSION** limits prevent a page from navigating to a different origin, opening a top-level window, accessing local storage, or requesting camera or microphone access. The **TOP NAVIGATION** block means the sandboxed page cannot redirect the top-level browser.

This is important for agents that fetch or render web content. A malicious page could try to phish the user, exfiltrate data, or abuse browser permissions. The sandbox treats the page as untrusted even if the user asked for the summary.

### 7. File workspaces provide temporary, scoped storage

The **FILE WORKSPACE** is a sandbox for file processing. It gives the agent a place to write intermediate files, but the workspace is scoped to the tenant and task. It cannot read the host file system, and files cannot stay there forever.

The diagram shows **HOST FILE** as a blocked path. A sandboxed file processor must not be able to read `/etc/passwd`, the host's source code, or another tenant's workspace. It can only see the files explicitly mounted into the workspace.

### 8. MCP Apps are sandboxed iframes with declared permissions

The **MCP APP IFRAME** is the newest surface. MCP Apps render in a sandboxed iframe and declare UI permissions and a content security policy. But the diagram warns that the host must still enforce capabilities and validate messages. An iframe is not authorization.

The MCP App can ask for permissions, but the host independently decides whether to grant them. The host validates every JSON-RPC message, checks the origin, and never lets the iframe directly call payment or secret tools. The permission declared by the app is a request, not a right.

### 9. Arbitrary network is the wrong default

The coral block **ARBITRARY NETWORK** is blocked for every sandbox. A sandbox should not be able to reach any URL it wants. Network access, if needed at all, is through a brokered, allowlisted, audited adapter. The previous diagram on egress control applies here.

![Central trusted tenant context scopes cache keys, vector namespaces, queue envelopes, artifact paths, traces, metrics, and logs while unscoped keys, shared results, guessable URLs, and raw logs are blocked.](../diagrams/162-cache-index-queue-artifact-telemetry-isolation.png)

Diagram 162 shows how tenant context must scope every cache, index, queue, artifact, and telemetry signal. A sandboxed tool that can write to an unscoped cache or an unguessed URL bypasses isolation. The two diagrams together say: the sandbox is only as strong as the tenant and egress boundaries around it.

### 10. Output must be validated and scanned before release

After the sandbox finishes, its **OUTPUT** must pass through **VALIDATE** and **DLP** before it can be shown to the user, stored in a cache, or used as a tool argument. The output could contain secrets, personal data, malicious links, or instructions that try to escape the sandbox.

Validation also includes making sure the sandbox did not leave behind files, processes, or network connections. Cleanup is part of the lifecycle.

### 11. The Next.js map: configure the iframe and keep privileged mediation on the server

In Next.js, MCP Apps should run in a sandboxed iframe with a strict content security policy. The JSON-RPC channel must be validated. Privileged host actions must stay behind authenticated server mediation. The React UI should not expose raw host capabilities to the iframe.

Tokens, policy decisions, secrets, and privileged mutations stay in authenticated server code. Typed request, decision, denial, approval, and receipt records let the interface explain the security state without inventing it. The browser can render the sandboxed app, but it cannot authorize it.

### 12. The Python map: external sandbox services and no eval

In Python, untrusted code or files must run in an external sandbox service with an explicit profile. `eval`, `exec`, and normal worker processes are not containment. The sandbox service should enforce CPU, memory, time, file, network, origin, and permission limits. Pydantic models and explicit service boundaries keep identity, tenant, policy, data classification, and audit context separate.

Tests should cover allow and deny paths with hostile fixtures. Test that a sandbox cannot read a host file, access the network, escape its time limit, or leave files behind after destruction.

---

## Case study — The vendor attachment with an MCP App preview

A vendor attachment contains an embedded script and offers a rich MCP App preview. The preview asks for filesystem and navigation access.

### What the design does

1. **Static scanning and classification** prevent automatic host execution. The attachment is classified as an untrusted interactive document.
2. **The preview runs in a sandboxed iframe** with declared minimal permissions and a content security policy.
3. **Host messages are validated** and cannot directly call payment capabilities. The host mediates every privileged action.
4. **Any generated file** passes output scanning and tenant-safe storage before Maya can download it.

### Result

Maya can inspect safe content without granting the attachment a path to host files, browser identity, or payment authority.

### The danger

A container, iframe, or temporary folder is not automatically a secure sandbox. Defaults, mounts, credentials, origins, and network access determine the real boundary. A default Docker container with the host network and all volumes mounted is not a sandbox.

### The takeaway

Give untrusted execution an empty room, a short tool list, and a guarded exit.

---

## Composition

The diagram is a four-quadrant layout with a shared input and output pipeline.

**Input pipeline (left):**
- **INPUT** enters **SCAN** then **CLASSIFY**.

**Four sandboxes (center):**
- **CODE VM** — for code execution.
- **BROWSER SESSION** — for web rendering and interaction.
- **FILE WORKSPACE** — for file processing.
- **MCP APP IFRAME** — for MCP App UI.

Each sandbox lists the same seven limits:
- **CPU**
- **MEMORY**
- **TIME**
- **FILE**
- **NETWORK**
- **ORIGIN**
- **PERMISSION**

**Blocked paths (center, coral):**
- **HOST FILE**
- **LOCAL CREDENTIAL**
- **TOP NAVIGATION**
- **ARBITRARY NETWORK**

**Output pipeline (right):**
- **OUTPUT** passes through **VALIDATE** and **DLP**.

## Element by element

**INPUT** — the code, page, file, or app to be sandboxed.

**SCAN** — the first check for known malicious or unsafe patterns.

**CLASSIFY** — the step that selects the smallest appropriate execution profile.

**CODE VM** — a virtualized or containerized environment for code.

**BROWSER SESSION** — an isolated browser context for web content.

**FILE WORKSPACE** — a temporary, scoped file storage area.

**MCP APP IFRAME** — a sandboxed iframe for MCP App user interfaces.

**CPU** — the maximum processor share.

**MEMORY** — the maximum memory.

**TIME** — the maximum lifetime.

**FILE** — the allowed file access.

**NETWORK** — the allowed outbound network access.

**ORIGIN** — the allowed web origins.

**PERMISSION** — the allowed browser or app capabilities.

**HOST FILE** — files on the host system, blocked.

**LOCAL CREDENTIAL** — ambient credentials, blocked.

**TOP NAVIGATION** — top-level browser navigation, blocked.

**ARBITRARY NETWORK** — uncontrolled outbound traffic, blocked.

**OUTPUT** — the result from the sandbox.

**VALIDATE** — the check that the output is safe and expected.

**DLP** — data loss prevention, which scans output for sensitive data.

## Colour and flow semantics

- **Cobalt platform with blue neon border** — a sandbox boundary. The four sandbox boxes are cobalt.
- **Cyan arrow** — a request, input, or allowed data path. INPUT, the sandbox entry, and OUTPUT are cyan.
- **Teal arrow** — a verified or safe result. OUTPUT after VALIDATE is teal.
- **Coral block** — a blocked or dangerous path. HOST FILE, LOCAL CREDENTIAL, TOP NAVIGATION, and ARBITRARY NETWORK are coral.
- **White card** — a limit, permission, or record. CPU, MEMORY, TIME, FILE, NETWORK, ORIGIN, and PERMISSION are white cards inside each sandbox.

The flow is: INPUT → SCAN → CLASSIFY → sandbox → OUTPUT → VALIDATE → DLP. The blocked paths are shown in the center, between the sandboxes, as common escape routes.

## How to present it

**Ask what "sandboxed" means in the room.** Many will say Docker, iframe, or temporary folder. The diagram says those are tools, not guarantees. The guarantee is the set of limits.

**Point at the four sandboxes.** Code, browser, file, and MCP App each need a different profile. Ask what kind of untrusted execution their system runs today.

**List the seven limits for each.** CPU, memory, time, file, network, origin, permission. Ask which limits are missing in their current setup. A missing network limit is a common gap.

**Emphasize ambient credentials.** A sandbox that can read the host's AWS credentials or browser cookies is not a sandbox. Ask what credentials are mounted into their containers.

**Show the blocked paths.** HOST FILE, LOCAL CREDENTIAL, TOP NAVIGATION, ARBITRARY NETWORK. These are the escape routes. Ask which ones are open today.

**Explain MCP App iframes.** The iframe is a rendering surface. The host still validates messages and independently authorizes privileged capabilities. A sandboxed UI is not authority.

**Pair with Diagram 162.** A sandboxed tool that writes to an unscoped cache or an unguessed URL bypasses isolation. The sandbox is only as strong as the tenant and egress boundaries around it.

**Map to Next.js.** Configure iframe sandbox, CSP, and JSON-RPC validation. Keep privileged actions behind authenticated server mediation. The React UI renders the app but does not authorize it.

**Map to Python.** Use an external sandbox service. No `eval`. Enforce CPU, memory, time, file, network, origin, and permission limits. Test escape paths.

**Run the lab as a profile design.** Have the room create four profiles for code, browser, file, and MCP App. For each, specify input scan, identity, tenant, resources, mounts, permissions, origins, network, outputs, evidence, lifetime, and cleanup test.

**Ask the checkpoint.** "Does iframe sandboxing authorize an MCP App to invoke host tools?" The answer is no. It constrains browser behavior; the host still validates messages and independently authorizes every privileged capability.

**Close on the standard.** Sandboxed work receives only explicit inputs and capabilities, has bounded resources and lifetime, and releases only validated outputs.

**Timing.** Twenty to twenty-five minutes, plus ten minutes for the lab profile design.

---

## Lab and checkpoint

**Lab:** Create four profiles—code, browser, file, MCP App. Specify input scan, identity, tenant, resources, mounts, permissions, origins, network, outputs, evidence, lifetime, and cleanup test.

**Checkpoint:** Does iframe sandboxing authorize an MCP App to invoke host tools?

**Answer:** No. It constrains browser behavior; the host still validates messages and independently authorizes every privileged capability.

---

## Glossary

- **Sandbox** — a restricted execution environment.
- **CSP** — Content Security Policy, a browser policy limiting loaded and contacted origins.
- **Ambient credential** — a credential automatically available without an explicit grant.
- **MCP App** — an application that extends an MCP server with a sandboxed user interface.
- **Origin** — the scheme, host, and port of a web resource.

---

## Sources

- MCP Apps overview
- MCP Apps CSP and CORS
- MCP security best practices
- OWASP Agentic Top 10 2026
