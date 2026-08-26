# Diagram 88 — MCP Apps, Sandbox, and Consent

![A flow on dark navy. HOST, a dark monitor, sends HOST PREFETCH AND REVIEW to a green-ticked checklist card, then to SANDBOXED IFRAME, a browser window containing a blue cube inside a dashed boundary, then to USER CONSENT GATE, a green shield with a person, then to TOOL ACTION, a wrench. Two coral dashed arrows drop from tool action to SECRETS, a database with a red padlock, and NETWORK, a globe. A teal arrow runs left from secrets to HOST AUDIT, a clipboard with a shield, which branches to DATA and UI TEMPLATE cards and returns up to the host.](../diagrams/88-mcp-apps-sandbox-consent.png)

**Module:** MCP at scale
**Role in the course:** running third-party interface code safely
**Layout:** a left-to-right containment pipeline with two blocked reach paths and an audited return

---

## At a glance

A host prefetches and reviews something, runs it in a **sandboxed iframe**, gates its actions behind **user consent**, and lets it perform a **tool action** — while two **coral dashed arrows** run from that action toward **SECRETS** and **NETWORK**.

Everything the app produces returns through **HOST AUDIT** and comes back as **DATA** and a **UI TEMPLATE**.

The subject is third-party interface code. An MCP server can supply not just capabilities but the interface for using them — which means running someone else's code in your host, and the entire diagram is about the containment that makes that acceptable.

---

## What the diagram teaches

### 1. Prefetch and review happens before anything runs

The first arrow is labelled **HOST PREFETCH AND REVIEW**, terminating at a green-ticked checklist.

The host fetches the app's content and inspects it **before** rendering. Not while rendering, not after.

That ordering is what makes review meaningful. Content examined as it executes has already had the opportunity to act.

What review covers in practice: does the content match its declared shape, does it reference only permitted resources, does it request only permitted capabilities, does it exceed size or complexity limits.

### 2. The sandbox is drawn as a dashed boundary inside a browser window

The **SANDBOXED IFRAME** shows a blue cube inside a **dashed rectangle** inside a browser chrome.

Three nested things, and the dashing is the containment. The app is a real thing running in a real frame, and the boundary around it is enforced rather than assumed.

The properties a sandbox provides: no access to the host document, no access to host storage, no ability to navigate the host, and no ambient credentials.

The last is the one that matters most. An app running with the host's cookies or tokens is not sandboxed in any useful sense, however restricted its DOM access.

### 3. User consent is a gate between the sandbox and any action

**USER CONSENT GATE** — a green shield with a person — sits between the iframe and the tool action.

The app can render. It cannot act without the user agreeing.

That separation is the important one. Rendering is low-risk: the app draws an interface inside a sandbox. Acting is not: a tool action has effects outside the sandbox.

Putting the gate between them means an app can present itself fully, and the user can see what it proposes, before anything happens.

The person glyph inside the shield says the gate is a human decision, not a policy evaluation.

### 4. The two coral arrows are the reach paths that must not exist

**SECRETS** — a database with a **red padlock**. **NETWORK** — a globe.

Both are reached by **coral dashed arrows** from **TOOL ACTION**.

These are drawn to be denied. An app performing a tool action must not thereby gain access to the host's credentials or the ability to make arbitrary outbound requests.

**Secrets.** The app invokes a capability; the host supplies the credentials to the capability server. The app never holds them. An app that could read the host's secret store could use every capability the host can, regardless of what the user consented to.

**Network.** Arbitrary outbound access is the exfiltration path. An app that can render an interface, obtain data through a consented tool action, and then make an unrestricted network request can send that data anywhere.

Denying both means an app's reach is exactly what it was granted and nothing more.

### 5. Everything returns through host audit

The teal arrow from the secrets area runs left to **HOST AUDIT** — a clipboard with a shield — before anything reaches the host.

The audit stage records what the app did: which capabilities it invoked, what the user consented to, what data came back, what it rendered.

Its position on the return path rather than as a side observer means the app's output is **audited before it is used**, not logged after the fact.

### 6. The app returns two things, and separating them is deliberate

**DATA** (a bar-chart card) and **UI TEMPLATE** (a browser-layout card), both feeding back to the host.

An MCP app supplies content and presentation as separate artefacts.

That separation lets the host treat them differently. Data is validated against a schema. A template is rendered under host-controlled constraints — sanitised, style-bounded, and unable to introduce script.

An app that returned a single blob of renderable content would give the host no way to distinguish what to validate from what to render.

### 7. The whole shape is defence in depth, and each layer assumes the previous may fail

Five controls in series: review, sandbox, consent, denied reach, audit.

Each is meaningful alone and the design assumes each may be bypassed.

Review may miss something, so the sandbox contains it. The sandbox may have a gap, so consent gates the action. Consent may be granted wrongly, so reach is denied. Everything may go right and still need explaining, so it is audited.

The consent gate here is the same control as the approval contract in the AG-UI model:

![A run finishing with an OUTCOME INTERRUPT, producing interrupt cards that compose into an amber DRAFT CONTRACT, reviewed by a human and resumed as a new run carrying a PARENT RUN ID.](../diagrams/95-agui-interrupt-approval-steering.png)

Both put a human decision between a proposal and an effect. The difference is scope: that one gates an agent's proposed action, this one gates third-party code running inside your host.

---

## Case study — Fernwood Health Records, the app that asked for the whole chart

Fernwood provides electronic health records to about 60 clinics. They introduced MCP app support so that specialist tool vendors — imaging, prescribing, referral management — could supply interfaces that run inside the clinician's Fernwood workspace rather than requiring a separate system.

Fourteen vendors registered apps in the first year.

### What the review stage caught

Their prefetch-and-review stage rejects apps at registration and re-checks on every update.

**Size and complexity limits** rejected two apps outright. One was a full single-page application weighing 4 MB that attempted to reimplement a large part of Fernwood's own interface inside a frame.

**Declared-capability mismatch** rejected four. An app requesting capabilities beyond what its vendor's registration permitted — in three cases through carelessness, in one case an app requesting a prescribing capability when the vendor was registered only for imaging.

**Resource references** rejected one app that loaded a script from a third-party CDN. Fernwood's policy is that app content must be self-contained; an app that fetches code at render time cannot be reviewed, because what was reviewed is not what runs.

That last rejection was the most contested and the most important. The vendor argued the CDN was reputable. Fernwood's position was that review of content that changes after review is not review.

### The consent gate finding

Their initial consent implementation asked once, at app installation: *allow this app to access patient records?*

A clinician approved it once and the app could act on any record thereafter.

Their clinical governance review rejected this. The consent was too broad in two dimensions — it covered all records rather than the record in context, and it was permanent rather than per-action.

**The rebuild:** consent is per action and scoped to the record currently open.

> **Imaging Assistant** requests: retrieve imaging studies for **this patient** (NHS 000 000 0000, currently open). Allow once / Allow for this session / Deny.

Three options rather than two. Session-scoped consent covers the common case of a clinician working through one patient's record with an app open, without granting standing access.

Consent volume was a concern. In practice, session-scoped consent means about 2.4 prompts per clinical session, which their clinicians reported as acceptable.

### The secrets and network finding

A security assessment tested both denied paths.

**Secrets.** A test app attempted to read the host's storage and to enumerate the credentials the host used for its own capability calls. Both blocked by the sandbox.

The assessment then tested something subtler: the app invoked a consented capability and inspected the *response* for anything credential-shaped. Nothing was, because Fernwood's capability layer strips authorisation material from responses before they reach an app.

That stripping had been implemented for an unrelated reason — response size — and turned out to be a security control nobody had classified as one.

**Network.** The test app attempted an outbound request to an external host. Blocked by the sandbox's content policy.

It then attempted the subtler version: constructing an image URL with patient data encoded in the query string, on the assumption that image loading might not be covered.

**It was not covered.** The image loaded, and the data left.

Fernwood's content policy had restricted script and fetch and had not restricted image sources. Closing it required an explicit allowlist covering every subresource type, not just the obvious ones.

That finding is the reason this diagram draws the network arrow at all. Exfiltration paths are rarely the obvious ones.

### The data and template separation

Fernwood validates returned data against a per-capability schema and renders returned templates through a sanitiser that permits a bounded set of elements and no script.

The separation caught a real problem: an app returning what it called data, containing markup, on the assumption the host would render it. Under the separation, the data failed schema validation and the app was told to use the template channel.

Had the two been one channel, that markup would have been rendered.

### Results

- **Apps rejected at review:** 7 of 21 submissions, on size, capability mismatch and external resource loading.
- **Consent model:** once-per-install → per-action, record-scoped, with a session option.
- **Exfiltration paths found:** 1 (image subresource), closed by an explicit allowlist.
- **Markup-in-data attempts:** 1, caught by schema validation.
- **Credential exposure:** none, partly by design and partly by an accidental control.

### The line in their vendor guidance

*Your app runs in our workspace, in front of a clinician, with a patient's record open. Everything it can reach, it can reach because we decided it could.*

---

## Composition

An upper left-to-right pipeline with a lower return path.

**Upper:** **HOST** (dark monitor on a blue platform) → labelled arrow **HOST PREFETCH AND REVIEW** → a white card with three **green ticks** → cyan arrow → **SANDBOXED IFRAME** (browser window containing a blue cube inside a **dashed boundary**) → cyan arrow → **USER CONSENT GATE** (green shield with a white person) → cyan arrow → **TOOL ACTION** (blue wrench).

**Two coral dashed arrows** drop from **TOOL ACTION** to **SECRETS** (dark database with a **red padlock**) and **NETWORK** (blue wireframe globe).

**Lower return:** a **teal arrow** runs left from the secrets platform to **HOST AUDIT** (dark clipboard with a blue shield), which branches with **teal arrows** to two white cards — **DATA** (blue bar chart) and **UI TEMPLATE** (browser layout) — and then rises with a teal arrow back into **HOST**.

## Element by element

**HOST** — a dark monitor showing content blocks. The environment the app runs inside.

**Prefetch and review card** — a white card with three green tick rows.

**SANDBOXED IFRAME** — a browser window with coloured chrome dots, containing a **dashed rectangle** enclosing a blue cube.

**USER CONSENT GATE** — a green shield containing a white person glyph.

**TOOL ACTION** — a blue wrench.

**SECRETS** — a dark database stack with a **red padlock**.

**NETWORK** — a blue wireframe globe.

**HOST AUDIT** — a dark clipboard with checked rows and a blue shield.

**DATA** — a white card with a blue bar chart.
**UI TEMPLATE** — a white card with a browser layout.

## Colour and flow semantics

- **Cyan arrows** carry the containment pipeline left to right.
- **Coral dashed arrows** mark the two reach paths that must be denied — drawn so they can be seen and refused.
- **Teal arrows** carry the audited return of data and template to the host.
- **Green** marks the review ticks and the consent shield — the two human-verified stages.
- **Red** appears once, on the secrets padlock.
- The **dashed sandbox boundary** is the only enclosing boundary in the frame.

## How to present it

**Establish what is being run.** Somebody else's interface code, inside your host, in front of your user. Ask what would have to be true for that to be acceptable.

**Ask why review comes before render.** Content examined as it executes has already had its chance. Then give the Fernwood CDN rejection: review of content that changes after review is not review.

**Ask what a sandbox actually denies.** Push past DOM access to **ambient credentials**. An app running with the host's tokens is not sandboxed in any useful sense.

**Point at the consent gate's position.** Between rendering and acting. Rendering is contained; acting has effects outside. An app can present itself fully before anything happens.

**Tell the Fernwood consent rebuild.** Once-per-install covering all records → per-action, record-scoped, with a session option. Then give the number: 2.4 prompts per session, which clinicians accepted.

**Walk both coral arrows.** Secrets — an app that could read them could use every capability the host can. Network — an app that can render, obtain consented data, and make arbitrary requests can send that data anywhere.

**Tell the image-subresource finding.** Script and fetch restricted; image sources not. Patient data encoded in a query string, and the image loaded. Ask the room which subresource types their own content policy covers.

**Ask why data and template return separately.** One is validated against a schema; the other is rendered under host constraints. Then give the markup-in-data attempt that schema validation caught.

**Note the accidental control.** Fernwood stripped authorisation material from responses for size reasons and discovered it was a security control. Worth asking what unclassified controls the room already has.

**Close on the vendor line.** *Everything it can reach, it can reach because we decided it could.*

**Timing.** Twenty-five minutes. Thirty-five if you work through what a review stage would check for the room's own app surface.

---

## Lab and checkpoint

**Lab:** Design an MCP app sandbox and consent flow for one third-party app your system could host. Write the review checklist, the sandbox boundary, the consent gate that is per-action and record-scoped, the blocked reach paths for secrets and network, and the host audit log. Then define the data and template separation rule.

**Checkpoint:** Why must review happen before render?

**Answer:** Because content that is reviewed as it executes has already had its chance to do something. Review must happen before the app runs or renders in the user's context, or the review is not a security gate.

## Glossary

- **Consent gate** — the point where the user approves a specific action before it runs.
- **Host** — the application that embeds the MCP app.
- **Host audit** — the log of what the app did through the host.
- **MCP app** — the third-party interface code running inside the host.
- **Prefetch and review** — the stage where the app's code is examined before it runs.
- **Sandbox** — the constrained environment that limits what the app can do.
- **Schema validation** — the check that returned data matches an expected shape before rendering.
- **Secrets** — credentials or tokens the app must not be able to read.
- **Subresource** — an image, script, or fetch target loaded by the app.
- **Template** — the presentation layer returned separately from data.

## Sources

- MCP app sandboxing and consent
- Third-party UI embedding and content review
- Content-security policy and ambient credential isolation
