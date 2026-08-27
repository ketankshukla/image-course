# Diagram 63 — Least-Privilege Tools

![A comparison on dark navy. On the left, DO EVERYTHING shows a large coral toolbox marked READ, WRITE, DELETE and ADMIN. A cyan arrow leads right to NARROW TOOLS, a platform carrying four teal tiles labelled TENANT, RESOURCE, ACTION and LIMITS. Dashed arrows descend to four white cards — GET REFUND STATUS, REQUEST REVIEW, ADD CASE NOTE and CLOSE OWN TICKET. Beneath them, a band reads AGENT RECEIVES ONLY ALLOWED TOOLS, and dashed arrows lead to two surviving cards, GET REFUND STATUS and REQUEST REVIEW, flanking a teal check.](../diagrams/63-least-privilege-tools.png)

**Module:** Security
**Role in the course:** from one powerful tool to several narrow ones
**Layout:** a coral do-everything toolbox contrasted with a four-dimension narrowing that filters to an allowed set

---

## At a glance

On the left, one tool that can do anything — **READ, WRITE, DELETE, ADMIN** — rendered in **coral**, the library's colour for risk.

On the right, the alternative: capabilities narrowed along **four dimensions** (**TENANT, RESOURCE, ACTION, LIMITS**) into specific named tools, and then filtered again so the **agent receives only the two it is allowed**.

Two separate ideas. Narrow the tools you define. Then give each agent only the subset it needs.

---

## What the diagram teaches

### 1. The do-everything toolbox is coral, and its labels are the diagnosis

**READ, WRITE, DELETE, ADMIN** on one box.

That is the shape of a capability defined around a *system* rather than around a *task*. `manage_tickets` with an action parameter. `database_query` that takes arbitrary SQL. `admin_api` with a method argument.

They are attractive because they are few and flexible. One tool covers everything, and adding a use case requires no new capability.

The cost is that the tool's power is the union of everything anyone might need, and every caller gets all of it. There is no way to grant someone the read without the delete, because they are the same tool.

Coral is the correct colour. This is not a bad tool; it is a risk-carrying one.

### 2. Four dimensions, and each answers a different narrowing question

The teal tiles across the top of the right side: **TENANT, RESOURCE, ACTION, LIMITS**.

**TENANT** — whose data? In a multi-tenant system this is the first and most consequential boundary. A tool scoped to a tenant cannot reach another's data by construction.

**RESOURCE** — which objects? Not all tickets — this user's tickets. Not all accounts — the account in scope.

**ACTION** — what operation? Read, or write, or close — one of them, not a parameter selecting between them.

**LIMITS** — how much, how often, how large? Rate, batch size, value ceiling. The dimension teams most often omit, and the one that bounds damage when something goes wrong within permitted scope.

Applying all four turns one broad tool into several narrow ones. The four cards beneath — **GET REFUND STATUS**, **REQUEST REVIEW**, **ADD CASE NOTE**, **CLOSE OWN TICKET** — are what comes out.

### 3. The tool names are the design, and they read as tasks

Look at the four names. Every one is a **verb plus a specific object**, and several encode a constraint in the name itself.

**CLOSE OWN TICKET** — the word *own* is a scope boundary written into the capability. There is no `close_any_ticket`, so there is nothing to accidentally grant.

**REQUEST REVIEW** — not `approve`. The agent can request; approving is someone else's capability.

**GET REFUND STATUS** — read only. There is no refund-issuing tool in this set at all.

Naming capabilities after tasks rather than after systems is what makes the narrowing durable. A tool called `manage_tickets` will accrete parameters. A tool called `close_own_ticket` cannot.

### 4. The second filter is the diagram's real subject

Beneath the four narrow tools, a band reads **AGENT RECEIVES ONLY ALLOWED TOOLS**, and dashed arrows lead to **two** surviving cards.

Four tools were defined. This agent gets two.

That is a separate decision from narrowing. Narrow tools are a *catalogue* property; the allowed subset is a *per-agent, per-context* property.

The consequence is important and often missed: **the agent cannot plan around a tool it never received.** This is stronger than refusing the call at execution time. An agent that can see `add_case_note` will propose using it and be refused; an agent that never received it will not consider it.

Restricting at discovery rather than only at execution removes a whole class of wasted planning, confusing refusals, and information leakage about what exists.

### 5. Limits are the dimension that bounds damage inside permitted scope

Worth separating because the other three are about *what* and this one is about *how much*.

Tenant, resource and action all define a boundary. Limits define behaviour within it.

An agent with correct scope, correct resource and correct action can still cause harm at volume — 400 case notes in a minute, a batch operation across every ticket it legitimately owns, a refund status query loop that exhausts a downstream API.

Limits are what turn "permitted" into "permitted, in reasonable quantity."

### 6. This composes with the identity model rather than replacing it

The narrowing here is about the tool catalogue. The token model is about the credential each call carries.

![A five-column token flow showing per-hop tokens stamped AUDIENCE MCP SERVER and AUDIENCE DOWNSTREAM API, with a VALIDATES panel and a red NO TOKEN PASSTHROUGH path along the base.](../diagrams/62-identity-and-token-flow.png)

Narrow tools mean the agent can only ask for a small set of things. Scoped tokens mean each of those requests carries only the authority it needs. Both are required — a narrow tool executing with a wide credential is still a wide capability.

---

## Case study — Ashcombe Utilities, the tool that could do everything

Ashcombe supplies water to about 300,000 households. Their customer service assistant helps advisers handle billing queries, meter readings, payment arrangements and complaints.

The first version exposed six tools. One of them was `customer_action`.

### What customer_action did

It took a customer reference, an action name, and a parameters object. The action name could be any of 31 values: reading account details, updating contact preferences, adjusting bills, applying credits, closing accounts, changing payment plans, writing off balances.

It had been built that way for a good reason. Their customer system exposed one API with a method parameter, and wrapping it as one tool was a two-day job. Wrapping 31 separate capabilities would have taken weeks.

### The incident

An adviser asked the assistant to "clear the balance" on an account where a customer had been incorrectly billed for a period they had not occupied the property.

The correct action was to raise a billing adjustment for the specific period, which requires a supervisor's approval above £200.

The assistant called `customer_action` with action `write_off_balance`. The balance was £1,840 and it was written off entirely — including £610 of legitimate charges from before the disputed period.

No approval was required because `write_off_balance` was reachable through the same tool as `get_account_details`, and the tool as a whole was permitted for advisers.

### Why the phrase mattered

"Clear the balance" is genuinely ambiguous. It could mean adjust the disputed portion or write off the lot. The assistant chose the interpretation that most directly matched the instruction.

The failure was not that the assistant misread it. It was that **a misreading could reach a write-off at all**. A narrow tool set would have had no `write_off_balance` available to an adviser context, and the misreading would have produced either the correct adjustment or a refusal.

### The rebuild

**Thirty-one actions became nineteen narrow tools.** Not one per action — some collapsed, some split, and eight actions were removed from the assistant's reach entirely.

The four dimensions were applied explicitly:

**Tenant** — not relevant here; single-tenant system.

**Resource** — every tool is scoped to the account in the current case context. There is no tool that takes an arbitrary account reference. This eliminated a category of error where the assistant operated on a similar account number.

**Action** — one operation per tool. `get_account_balance`, `raise_billing_adjustment`, `record_meter_reading`, `add_payment_arrangement`, `add_case_note`.

**Limits** — value ceilings and rate caps. `raise_billing_adjustment` is capped at £200; above that it becomes `request_billing_adjustment`, which creates an approval task rather than acting.

**Eight actions removed from the catalogue.** Account closure, write-off, payment plan restructuring above a threshold, and five others are not available to the assistant at all. They exist in the customer system and are performed by humans through their own interface.

The reasoning: these are the actions where a misreading is expensive and where the volume is low enough that automation saves little.

**Per-context allowed sets.** An adviser in the billing queue receives nine tools. An adviser in the complaints queue receives eleven, with three that the billing set does not include. A supervisor receives fifteen.

The assistant does not know the others exist. It cannot propose them, and it does not produce plans that require them.

### The measurable effect

**Refusals dropped sharply.** Before, the assistant would propose actions the adviser could not perform, and the adviser would receive a permission error. About 4% of interactions. After, the assistant only plans with what it has: refusals fell to under 0.3%, and those are limit breaches rather than permission errors.

That was an unexpected user-experience benefit of restricting at discovery rather than at execution.

**Approval routing became visible.** The `request_billing_adjustment` path creates an explicit task. In the first year it created about 1,400 approval requests, of which supervisors declined 90. Those 90 are adjustments that would previously have gone through automatically under the old tool.

**The rebuild cost.** Six weeks, against the two days the original tool took. Their engineering lead's assessment was that the two days had been borrowed rather than saved.

### Results

- **Write-offs by the assistant:** possible before, structurally impossible after.
- **Permission-error refusals:** 4% → under 0.3%.
- **Approval requests created:** ~1,400/year, 90 declined.
- **Tools in the catalogue:** 6 broad → 19 narrow, with 8 actions removed entirely.

### Their rule for new capabilities

*If the name needs an "action" parameter, it is not one tool.*

---

## Composition

A left-right comparison with a two-stage narrowing on the right.

**Left:** a large **coral toolbox** labelled **DO EVERYTHING**, carrying four white icon-and-label pairs: **READ**, **WRITE**, **DELETE**, **ADMIN**.

A single **cyan arrow** crosses to the right.

**Right, upper:** a blue platform headed **NARROW TOOLS** carrying four **teal tiles** — **TENANT** (building), **RESOURCE** (database), **ACTION** (gear), **LIMITS** (gauge) — connected by a teal line.

**Right, middle:** four **dashed cyan arrows** descend to four white cards: **GET REFUND STATUS** (magnifier), **REQUEST REVIEW** (message bubble), **ADD CASE NOTE** (document with pencil), **CLOSE OWN TICKET** (✗).

**Right, lower:** a band reading **AGENT RECEIVES ONLY ALLOWED TOOLS**, with dashed cyan arrows descending to **two** cards — **GET REFUND STATUS** and **REQUEST REVIEW** — flanking a **teal check disc**.

## Element by element

**DO EVERYTHING**
A large **coral toolbox** with a dark handle and latch, its front face carrying four white icons with labels: a book (**READ**), a pencil (**WRITE**), a bin (**DELETE**), a person-shield (**ADMIN**).

**The four dimension tiles**
Teal rounded tiles with white glyphs: an institution (**TENANT**), a database (**RESOURCE**), a gear (**ACTION**), a gauge (**LIMITS**).

**The four narrow tools**
White cards, each with a teal circular icon: a magnifier — **GET REFUND STATUS**; a message bubble — **REQUEST REVIEW**; a document with pencil — **ADD CASE NOTE**; a cross — **CLOSE OWN TICKET**.

**The allowed set**
Two of the four cards repeated below the band, with a **teal check disc** between them.

## Colour and flow semantics

- **Coral** marks the do-everything toolbox — risk, not error.
- **Teal** marks every narrowing dimension, every narrow tool icon, and the final approval check.
- **Solid cyan** carries the single transition from broad to narrow; **dashed cyan** carries the two filtering steps.
- The **reduction from four cards to two** is the composition's second argument, visually distinct from the first.

## How to present it

**Ask the room to name their broadest tool.** There is always one. Then ask what a caller who only needs one of its functions receives — all of it.

**Read the four coral labels.** Read, write, delete, admin on one box. Ask how you grant read without delete. You cannot; they are the same tool.

**Walk the four dimensions and ask which they apply.** Tenant, resource, action, limits. Most teams apply action and sometimes resource. **Limits** is the one almost nobody has, and it is the one that bounds damage inside permitted scope.

**Read the tool names aloud and ask what "own" is doing in CLOSE OWN TICKET.** A scope boundary written into the capability. There is no `close_any_ticket` to accidentally grant.

**Give them the naming rule.** *If the name needs an action parameter, it is not one tool.* Then ask how many of their capabilities would fail that test.

**Tell the Ashcombe write-off.** "Clear the balance" was genuinely ambiguous, the assistant chose a defensible reading, and £1,840 went including £610 of legitimate charges. Then make the point: the failure was not the misreading, it was that a misreading could reach a write-off at all.

**Ask about the two-stage narrowing.** Defining narrow tools is a catalogue decision. Giving an agent a subset is a per-context decision. Both are needed.

**Ask why restricting at discovery beats refusing at execution.** An agent that can see a tool will plan with it and be refused; an agent that never received it will not consider it. Then give them Ashcombe's number: permission-error refusals fell from 4% to 0.3%, and the assistant stopped proposing things advisers could not do.

**Address the effort objection.** Ashcombe's broad tool took two days; the rebuild took six weeks. Their lead called the two days borrowed rather than saved. That framing usually lands.

**Timing.** Twenty-five minutes. Thirty-five if you narrow one of the room's own broad tools along all four dimensions, which typically produces five or six capabilities from one.

---

## Lab and checkpoint

**Lab:** Pick the broadest tool in your system. Narrow it along the four dimensions: tenant, resource, action, and limits. Rewrite it as a set of named, single-purpose tools. For each new tool, define its allowed caller, what it can act on, the exact action, and any limit. Then write the discovery rule that gives an agent only the tools it may actually use.

**Checkpoint:** Why is restricting at discovery better than refusing at execution?

**Answer:** Because an agent that discovers a tool will plan with it and then be refused at execution, which wastes calls and confuses users. An agent that never receives a tool will not consider it. Discovery filtering makes the agent's plan match its permissions from the start.

## Glossary

- **Action** — the dimension that narrows what a tool does.
- **Allowed tool set** — the subset of tools an agent receives in a context.
- **Broad tool** — a tool that does many things and cannot be granted narrowly.
- **Discovery** — the stage where the agent learns which tools are available.
- **Least privilege** — the principle that an agent should get the minimum tools it needs.
- **Limits** — the dimension that bounds how much or how often a tool may be used.
- **Narrow tool** — a tool with a specific, bounded purpose.
- **Resource** — the dimension that narrows what the tool acts on.
- **Tenant** — the dimension that narrows which organisation the tool applies to.

## Sources

- Least-privilege capability design
- MCP tool discovery and catalogue filtering
- Action/resource/tenant/limits scoping in APIs
