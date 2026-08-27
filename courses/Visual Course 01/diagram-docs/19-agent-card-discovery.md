# Diagram 19 — Agent Card Discovery

![Four numbered stages on dark navy. DISCOVER CARD shows a robot on a disc labelled SPECIALIST AGENT emitting sparkles toward a white PUBLIC AGENT CARD with a blue verified badge. CHECK INTERFACE shows a white card with CAPABILITIES and COMPATIBILITY sections, every row green-ticked. CHECK SECURITY shows a teal shield with a padlock beside three green-ticked rows and a plaque reading AUTHENTICATED VERIFIED SIGNED. TRUST DECISION shows a teal gate labelled ALLOWLIST splitting into a teal route to an APPROVED robot and a coral route to a striped barrier marked BLOCKED.](../diagrams/19-agent-card-discovery.png)

**Module:** 4 — A2A collaboration
**Role in the course:** discovery and trust review
**Layout:** four stages ending in a two-way branch

---

## At a glance

Four stages: find the card, check what it can do, check who it is, decide whether to trust it. The fourth stage is a gate labelled **ALLOWLIST** that splits into two visibly different outcomes — a teal route to an approved agent, and a coral route to a barricade marked **BLOCKED**.

The single claim is that **discovery is not trust**. Finding an agent, reading its card, and confirming its identity are three separate things, and none of them means you should send it work.

---

## What the diagram teaches

### 1. The card is published by the agent, which makes it a claim

Stage 1 shows the specialist agent **emitting** its card — sparkles travelling from the robot toward a document reading **PUBLIC AGENT CARD**.

The direction matters. The agent produces this. It is a self-description: here is what I am, here is what I can do, here is how to reach me. The blue verified badge in the corner says something has been attested, but the *content* is the agent's own account of itself.

That makes the card a claim rather than a fact. Everything downstream exists to evaluate the claim. A card asserting an agent can adjudicate credit decisions is a statement that must be checked, not a capability you have acquired.

This is the same relationship a client has with a capability catalogue, but with a crucial difference in stakes:

![Four numbered panels — CLIENT, SERVER/DISCOVER, CAPABILITY CATALOG, CALL — with a catalogue card travelling back along the bottom to the client.](../diagrams/07-mcp-capability-discovery.png)

There, the catalogue describes tools you will call inside a boundary you control. Here, the card describes an actor you will hand work to, outside your boundary. The verification burden is correspondingly higher.

### 2. Interface and security are separate checks, and both are necessary

Stages 2 and 3 could have been one panel. They are two because they answer different questions and either can fail independently.

**CHECK INTERFACE — can we work together?** The panel shows two sections: **CAPABILITIES** (plug, gear, database) and **COMPATIBILITY** (puzzle piece, code), every row green-ticked. Does it do what we need, does it speak a protocol version we speak, do the task and artifact shapes line up.

An agent can be entirely trustworthy and interface-incompatible. That is a failure, and it is a *cheap* failure — you find out before you have sent anything.

**CHECK SECURITY — is it who it says it is?** The panel shows a teal shield with a padlock, three green-ticked rows (a **fingerprint**, a **certificate**, a **clock**), and a plaque reading **AUTHENTICATED / VERIFIED / SIGNED**.

Those three rows are three distinct checks. The fingerprint is identity — is this the agent it claims to be. The certificate is attestation — has someone credible vouched for it. The clock is validity — is that attestation current, or expired.

An agent can be perfectly interface-compatible and have an expired certificate. Also a failure, and a more serious one.

The plaque's three words are worth separating. **Authenticated** means it proved its identity. **Verified** means its claims were checked. **Signed** means the card itself is tamper-evident. Passing one is not passing the others.

### 3. The allowlist is the decision, and it is a human one

Stage 4 shows a **gate structure labelled ALLOWLIST** with a check in the centre. This is where the three preceding stages become an outcome.

The word choice is deliberate. Not "trust score." Not "risk assessment." An **allowlist** — an explicit enumeration of agents you have decided to work with.

That means default-deny. An agent that passes every check in stages 1 through 3 and is not on the list does not get work. Passing the checks makes an agent *eligible* for the decision, not the beneficiary of it.

The reason to insist on this: stages 1 through 3 are all evaluations of the agent's own claims and credentials. None of them evaluates whether *you want to depend on this party*. That question involves things no card carries — contractual relationships, operational track record, data-handling agreements, what happens when they have an outage, who is liable when they are wrong.

### 4. Both outcomes are drawn, and the blocked one is drawn fully

The gate splits. A **teal arrow** rises to an approved robot with a green check. A **coral arrow** descends to a striped construction barrier with red ✗ signs and a card reading **BLOCKED**.

Most trust diagrams show only the happy path. Drawing the blocked route at equal weight makes two points.

**Rejection is a normal outcome.** Not an error, not an exception. Some agents should not be trusted, and a discovery process that never blocks anything is not evaluating anything.

**The block must be enforced, not advisory.** A barricade, not a warning sign. An agent that fails the trust decision cannot be reached — the block is a runtime control, not a note in a review document.

### 5. Discovery is not one-time

The clock in the security panel implies what the diagram's linear layout does not: **trust decisions expire**.

Certificates lapse. Agents change what they do. An agent that adjudicated credit decisions six months ago may now do something broader. The organisation behind it may have been acquired. The card is a live document and the checks against it are perishable.

Practical consequence: re-verify on a schedule, and re-verify when the card changes. An agent whose card has changed since approval should return to the gate, not continue on a decision made about a different description.

### 6. This is the first gate; it is not the whole security model

Passing this diagram means an agent is on your allowlist. It does not mean work sent to it is safe.

Everything about *what you send*, *how it is bounded*, *what comes back*, and *what happens before anything takes effect* is a separate pipeline:

![Five stages — MINIMIZE CONTEXT, ALLOWLIST AGENT, BIND TASK, VALIDATE ARTIFACT, LOCAL APPROVAL — with coral reject paths dropping into bins and a final teal SIDE EFFECT ALLOWED badge.](../diagrams/23-a2a-security-gates.png)

Note that the entire content of this diagram appears there as **one stage of five** — "allowlist agent." Discovery and trust is the second gate of a longer pipeline, and treating it as the whole security story is the most common mistake teams make with A2A.

---

## Case study — Meridian Procure, onboarding vendor agents

Meridian Procure runs a procurement platform used by about six hundred corporate buyers. Their roadmap included letting supplier organisations connect their own agents — so a buyer's agent could negotiate lead times, request quotes, or check compliance documentation directly with a supplier's agent rather than going through email.

The commercial case was strong. The trust problem was the entire project.

### What they were being asked to allow

A supplier agent would receive: the buyer's identity, the products in scope, quantities, delivery requirements, and sometimes contract terms. It would return quotes, availability, or compliance attestations that would then influence purchasing decisions worth, in some cases, seven figures.

The security team's initial position was that this was not possible. The compromise that made it work was building the four stages as a formal onboarding process.

### Stage 1 — Discover card

Supplier organisations publish an agent card at a well-known location on a domain they control. The card declares organisation identity, what the agent does, which protocol versions it speaks, task and artifact schemas, endpoints, and its security posture.

Meridian did not build a directory or a marketplace. A buyer cannot browse available supplier agents — Meridian fetches cards only for suppliers already in a commercial relationship with that buyer. **Discovery is scoped by an existing relationship**, which eliminated an entire class of problem before it started.

### Stage 2 — Check interface

Automated. The card's declarations are checked against what Meridian's platform can work with:

- Protocol version within the supported range.
- Task schema matching one of five supported interaction types (quote request, availability check, lead time query, compliance document request, order status).
- Artifact schema parseable and matching the declared type.
- Declared error behaviours present.

About 30% of supplier agents failed this on first submission, almost always on artifact schema — suppliers returning free-form text where a structured quote was expected. Meridian publishes the schemas and a validator, and most suppliers resolve it within a week.

Cheap failure, caught before anything was sent.

### Stage 3 — Check security

Three checks, mapping to the three rows in the diagram's panel.

**Identity.** The agent endpoint presents a certificate for a domain matching the supplier's registered organisation domain. This binds the agent to a legal entity Meridian already has a contract with.

**Attestation.** The card is signed with a key whose certificate chains to a CA Meridian accepts. The signature covers the card's content, so a modified card fails.

**Validity.** Certificate not expired, signature current, card carrying a freshness timestamp within thirty days. This last one exists because Meridian found early on that some suppliers published a card once and never touched it, including one whose declared endpoint had been decommissioned four months earlier.

### Stage 4 — Trust decision

This is where it stops being automated.

An agent passing stages 2 and 3 becomes **eligible**. Adding it to a buyer's allowlist requires a human decision by the buyer's procurement lead, who sees the card's contents, the check results, and — importantly — a plain statement of what data would be sent to this agent.

The buyer decides. Meridian does not decide on their behalf, because Meridian is not the party whose commercial data is at stake.

Allowlist entries are per buyer-supplier pair and carry a scope: which of the five interaction types are permitted. A supplier trusted for availability checks is not automatically trusted for quote negotiation.

### What the blocked route actually does

A supplier agent not on a buyer's allowlist cannot be reached from that buyer's context. Enforced at the platform's outbound gateway, which checks the allowlist before any task is dispatched. Not a UI restriction — a network-level control.

They also implemented an automatic block. An agent whose card changes materially — new capabilities, changed endpoint, changed schema — is **suspended pending re-approval**. The buyer is notified and must re-approve.

This fired in earnest once. A supplier expanded their agent from availability checks to accepting orders, which would have let it receive purchase commitments from buyers who had approved it for a read-only interaction. Every affected allowlist entry suspended automatically. Four buyers re-approved with the expanded scope; eleven did not.

### The re-verification schedule

- Cards re-fetched and re-checked **daily**. Failures suspend the entry.
- Certificate expiry monitored, with warnings at thirty and seven days.
- Human re-approval required **annually**, or on material card change.

Daily re-fetching catches decommissioned endpoints and expired certificates before a buyer discovers them mid-transaction.

### What they learned

Two things went into their internal guidance.

**The interface check is not security and should not be conflated with it.** Their first design had one combined validation step. Suppliers failing on artifact schema were being reported to buyers as "security check failed," which was inaccurate and caused unnecessary alarm. Separating the two — as the diagram does — made the failures legible.

**The allowlist decision cannot be automated, because it is not a technical question.** Everything stages 2 and 3 check is verifiable. Whether a buyer wants their pricing requirements visible to a particular supplier's automated system is a commercial judgement. The team's attempt to build a scoring model for it was abandoned; a person looks at the card and decides.

---

## Composition

Four stages run left to right, each headed by a blue numbered circle and a white uppercase label:

**1 DISCOVER CARD → 2 CHECK INTERFACE → 3 CHECK SECURITY → 4 TRUST DECISION**

Small teal arrows connect the stages. The fourth stage splits into two divergent routes — one rising in teal, one descending in coral.

## Element by element

**1 DISCOVER CARD**
A blue cube robot on a glowing disc, with a plaque reading **SPECIALIST AGENT**. Teal sparkles travel from the robot to the right, toward a large white document headed **PUBLIC AGENT CARD** showing an avatar tile, capability rows with plug, gear and database icons, and a **blue verified badge** at its lower right.

**2 CHECK INTERFACE**
A white card divided into two labelled sections. **CAPABILITIES** lists three rows with plug, gear and database icons. **COMPATIBILITY** lists two rows with a puzzle piece and a `</>` code icon. Every row carries a **green check** on the right.

**3 CHECK SECURITY**
A **teal shield bearing a white padlock** on a blue plinth. To its right, a dark panel with three green-ticked rows showing a **fingerprint**, a **certificate with a ribbon**, and a **clock**. A green padlock sits to the right, and a dark plaque on the platform reads **AUTHENTICATED / VERIFIED / SIGNED**.

**4 TRUST DECISION**
A teal gate structure with vertical bars and a lintel reading **ALLOWLIST**, with a large teal check disc at its centre. Two routes leave it: a **teal arrow rising to the right** toward a teal robot on a disc with a green check badge and an **APPROVED** card; and a **coral arrow descending to the right** toward a striped construction barrier carrying two red ✗ signs, beside a **BLOCKED** card with a red ✗.

## Colour and flow semantics

- **Teal** marks the approved route and the security shield, consistent with teal meaning verified and committed throughout the library.
- **Coral** marks the blocked route, the only coral in the diagram, appearing exactly at the point of refusal.
- **Green checks** appear at row level in stages 2 and 3, marking individual passed checks rather than overall verdicts.
- The two outcome routes are drawn at **equal visual weight**, with the blocked path given a full barricade rather than a small warning.
- The gate structure in stage 4 is the only object in the diagram rendered as **architecture** rather than as a document or device — it is a physical checkpoint.

## How to present it

**Ask what makes an agent trustworthy.** Before showing the diagram. Rooms typically offer authentication and a valid certificate. Then reveal the fourth stage and ask why, if the first three all passed, there is still a decision to make. The answer — the checks verify claims, they do not establish that you want to depend on this party — is the session's core.

**Separate the three security rows.** Point at the fingerprint, the certificate and the clock and ask what each proves. Identity, attestation, validity. Then ask which of the three their current process checks. The clock is usually missing, and expired attestations are a real and common gap.

**Ask why interface and security are two panels.** The answer — an agent can be trustworthy and incompatible, or compatible and untrustworthy — matters practically, because conflating them makes failures illegible. Meridian's supplier reported as "security check failed" for a schema mismatch is a good illustration.

**Dwell on the word "allowlist."** Ask what it implies. Default-deny, explicit enumeration, and a decision that someone owns. Then ask who in their organisation would sign it. If the answer is "nobody, it would be automatic," ask what a scoring model would use for inputs that a card does not carry.

**Point at the barricade and ask whether it is real.** Is a blocked agent unreachable, or merely not recommended? A UI restriction is not a control. Meridian's outbound gateway check is the shape of the real answer.

**Raise the expiry question.** The clock icon is the prompt. Ask what happens when an approved agent changes what it does. Meridian's automatic suspension on material card change — and the supplier who added order acceptance to a read-only agent — makes it concrete.

**End by shrinking the diagram.** Show the delegation security pipeline and point out that this entire four-stage process is *one of its five gates*. Teams that treat discovery as their A2A security model have built one fifth of it. That reframing is the most useful thing to leave the room with.

**Timing.** Twenty minutes. Thirty if you work through what their own allowlist decision would require, which tends to surface that nobody currently owns it.

---

## Lab and checkpoint

**Lab:** Create an agent card review checklist for one external or internal agent your system depends on. Verify its identity claim, attestation, and validity. Then write the allowlist criteria that would let it be used and the owner who would sign it. If the agent's card changes materially, write the rule that decides whether it is suspended, re-verified, or allowed to continue.

**Checkpoint:** Why is an interface check not the same as a trust check?

**Answer:** Because an agent can be trustworthy and incompatible, or compatible and untrustworthy. The interface check confirms the agent speaks the right protocol. The trust check confirms that the agent is from an approved party, its attestation is valid, and you are willing to depend on it. These are separate gates.

## Glossary

- **Agent card** — a discoverable identity and capability record for an agent.
- **Allowlist** — an explicit list of approved agents, maintained with default-deny and an owning decision-maker.
- **Attestation** — a signed or verified statement about the agent's identity or behaviour.
- **Certificate** — the cryptographic credential that authenticates the agent.
- **Expiry** — the point after which an attestation or certificate is no longer valid.
- **Fingerprint** — a unique identifier that proves the agent's identity.
- **Interface check** — the verification that the agent speaks the correct protocol and schema.
- **Trust check** — the decision that the agent is from a party you are willing to depend on.

## Sources

- A2A Agent Card discovery and verification model
- Allowlisting and default-deny security patterns
- Attestation, certificate, and expiry management in agent systems
