# Diagram 39 — Agent Decision Loop

![A circular layout on dark navy. Five platforms form a ring connected by cyan arrows running clockwise — OBSERVE with a teal eye, PLAN with a folded map showing a dashed route, CHOOSE with three teal branching arrows, ACT with a hand holding a wrench, and CHECK with a magnifier over a teal check. From CHECK a cyan arrow leads left to STOP, a chequered flag, which returns up to OBSERVE. A dashed teal arrow runs from CHECK up to PLAN. A coral arrow drops from CHECK to ASK HUMAN, a person figure, with a dashed teal arrow returning up to ACT.](../diagrams/39-agent-decision-loop.png)

**Module:** Agent behaviour
**Role in the course:** what an agent actually does, step by step
**Layout:** a closed clockwise loop with three exits from the check stage

---

## At a glance

Five stages in a ring — **OBSERVE → PLAN → CHOOSE → ACT → CHECK** — and then three different things can happen from **CHECK**: loop back to plan, stop, or ask a human.

This is the first diagram in the volume about the agent itself rather than the infrastructure around it. Everything interesting is in the check stage, because that is where an agent decides whether to keep going — and an agent that cannot decide to stop is the single most common failure a beginner builds.

---

## What the diagram teaches

### 1. Five stages, and choose is separate from plan

The stage most people would omit is **CHOOSE**, drawn as three teal arrows branching upward from a single point.

Plan and choose are different operations. **Planning** produces options — here are the things that might work. **Choosing** commits to one. Separating them makes visible something that is otherwise hidden inside a single "decide" step: an agent that plans well and chooses badly, or one that generates only one option and therefore never really chooses at all.

For beginners the practical version is that these two stages fail differently and are debugged differently. A bad plan means the agent misunderstood the goal. A bad choice means it understood and picked wrong. The fixes are not the same.

### 2. Act is a hand holding a tool, and that is the only stage that touches the world

**ACT** shows a teal hand gripping a wrench. Four stages of thinking, one of doing.

The hand is the tell. This is where the agent's reasoning becomes something that happens — a tool call, a write, a message sent. Everything before it is reversible; this stage is where consequences begin.

That single platform expands into a whole diagram of its own:

![Five numbered stages — MODEL PROPOSES, CLIENT VALIDATES, SERVER AUTHORIZES, DOMAIN EXECUTES, RESULT + RECEIPT — with red octagonal STOP signs hanging beneath the two checking stages.](../diagrams/40-tool-call-lifecycle.png)

Reading the two together is worth doing explicitly: everything between the agent wanting something and it happening lives inside this one stage.

The proportions carry the same message as the request pipeline earlier in the volume: most of what a system does is establishing the conditions under which the action is safe, and the action itself is one small step.

### 3. Check has three exits, and that is the diagram's content

**CHECK** — a magnifier over a teal check disc — is the only stage with more than one outgoing path.

**Exit 1: the dashed teal arrow up to PLAN.** The action happened, the result was not sufficient, and the agent re-plans with what it now knows. This is the iteration loop and it is the normal case.

**Exit 2: the cyan arrow left to STOP.** Drawn as a **chequered flag** — a finish line. The goal is met, and the agent stops.

**Exit 3: the coral arrow down to ASK HUMAN.** Something needs a person. A dashed teal arrow returns from the human up to **ACT**, which is worth noticing: the human's answer feeds back into acting, not into planning. The plan was fine; the agent needed permission or information to proceed.

Three exits, three genuinely different situations. An agent implementation that only has the first one loops forever.

### 4. STOP is a stage, and giving it a platform is the point

Beginners building their first agent almost never build a stop condition. The loop runs, produces something, runs again, and the only thing that ends it is a maximum-iterations counter or a person killing the process.

The chequered flag says stopping is a **destination**, not a failure to continue. An agent needs an explicit answer to "how do I know I am done," and that answer has to be checkable at the check stage.

Note also that STOP flows back to OBSERVE. The ring is closed. This reads as: the agent finishes this piece of work and returns to watching for the next thing. Stopping ends a task, not the agent.

### 5. Ask human is coral, and coral means the same thing it always does

The only coral element in the diagram is the branch to the human.

Throughout both volumes, coral marks risk, refusal, and human-control paths. Its use here says that escalating to a person is in the same family as a gate refusing — it is a point where the automated flow stops and something else decides.

Two design questions follow, and neither is answered by the picture:

**What triggers it?** Low confidence, a consequential action, an ambiguity the agent cannot resolve, a policy rule, or a threshold being crossed. This has to be defined; an agent that never asks is as broken as one that asks constantly.

**What does the human see?** A question they can actually answer, with the context needed to answer it. "Should I proceed?" is not a question. "The address on this order does not match the account address — use the order address, the account address, or hold?" is.

### 6. The return from the human goes to ACT, not to PLAN

Easy to miss, and it is a considered choice.

If the human's input returned to planning, it would mean the agent re-thinks the whole approach after every consultation. Returning to **ACT** means the plan stands and the human supplied what was missing — a decision, a permission, a piece of information — so the agent can now proceed with the action it was about to take.

That models the common case correctly. Most human escalations are not "your whole approach is wrong"; they are "yes, go ahead" or "use this value."

---

## Case study — Bramble Home Services, the agent that would not stop

Bramble is a home maintenance company — plumbing, electrical, general repairs — running about 120 jobs a week across a team of thirty engineers. They built their first agent to handle job scheduling: a customer describes a problem, the agent works out what kind of job it is, how long it will take, which engineer has the right skills, and offers appointment slots.

It was built by two developers, neither of whom had built an agent before. It worked in testing and behaved very strangely in its first week of real use.

### Symptom one — the agent that ran for nine minutes

A customer described a problem that was genuinely ambiguous: *"there's water coming through the kitchen ceiling and the bathroom's above it."*

Could be a leaking pipe, a failed seal around the bath, a blocked overflow, or a shower tray. Different jobs, different durations, different skills.

The agent observed, planned, chose an approach, acted by querying the job-type catalogue, checked whether it had enough to schedule, decided it did not, re-planned, queried again with a slightly different framing, checked, re-planned…

It ran for nine minutes and 47 tool calls before an operator noticed and killed it. It had made no progress after roughly the fourth iteration — it was re-querying the same catalogue with slightly different phrasings, each time finding the same four candidate job types, each time deciding that was insufficient.

**Diagnosis:** the check stage had exactly one exit. It could route back to plan. It could not stop and it could not ask.

### Symptom two — the agent that stopped too early

A different customer: *"boiler making a noise."*

The agent observed, planned, chose, queried the catalogue, found "boiler service — 60 minutes," checked, and stopped. It scheduled a standard service.

The noise was a failing pump. The engineer arrived with a service kit and no pump, and the job had to be rebooked — a wasted visit, an unhappy customer, and a second appointment three days later.

**Diagnosis:** the check stage's stop condition was "did I produce a schedule," not "do I have enough to produce a *correct* schedule."

Both symptoms are the same defect from opposite directions. The check stage had no well-defined notion of sufficiency.

### What they built

**A real stop condition.** Not "did I produce an answer" but a checklist the agent evaluates: is the job type determined, is the duration known, are the required skills identified, is the confidence above threshold, are there no unresolved ambiguities. All five, or it is not done.

**An iteration limit with a purpose.** Three planning cycles. Not as a safety net that silently truncates — reaching it *routes to the human*, carrying what the agent has established and what it is stuck on. The difference between a limit that gives up and a limit that escalates is the difference between a dropped job and a coordinator getting a well-framed question.

**Explicit ask-human triggers.** Four of them:
- Confidence below threshold on job type.
- Two or more candidate job types with materially different durations.
- Any job involving gas, electrical work above a certain scope, or a vulnerable-customer flag on the account.
- Iteration limit reached.

The third trigger is not about the agent's uncertainty at all — it is a policy rule. Some categories go to a person regardless of how confident the agent is. That distinction mattered to their compliance position and it is worth separating: **escalation is sometimes about capability and sometimes about authority.**

**A question format.** The human sees what the agent established, what it could not resolve, and a specific choice. For the ceiling-leak case:

> Water through kitchen ceiling, bathroom above. Candidates: bath seal failure (60 min, general), pipe leak (90 min, plumber), shower tray (120 min, plumber + tiler). Cannot distinguish from description. Ask customer whether the leak worsens when the bath or shower is used?

A coordinator answers that in fifteen seconds. The agent then acts — which is why the return arrow goes to ACT.

### The results

- **Runaway loops:** eliminated. The three-cycle limit routes to a person instead of spinning.
- **Escalation rate:** about 18% of jobs, which the operations manager considered roughly right — they had estimated 15–20% of enquiries were genuinely ambiguous before the agent existed.
- **Wasted visits from wrong job types:** from 11 in the first week to under 1 a week.
- **Median time to schedule:** 40 seconds for the 82% the agent handles alone.

### What the developers said afterwards

Their retrospective note is the reason this diagram is drawn with three exits: *we built the loop and forgot to build the ways out of it. The loop was the easy part.*

---

## Composition

Five platforms arranged in a ring, connected by **curved cyan arrows running clockwise**: **OBSERVE** (upper left) → **PLAN** (top) → **CHOOSE** (upper right) → **ACT** (lower right) → **CHECK** (bottom centre).

From CHECK, three paths leave:
- A **cyan arrow left to STOP** (lower left), which then curves upward with a cyan arrow back to OBSERVE, closing the ring.
- A **dashed teal arrow upward to PLAN**, running through the centre of the ring.
- A **coral arrow downward to ASK HUMAN**, below the ring, with a **dashed teal arrow** curving up and right from the human back to ACT.

## Element by element

**OBSERVE**
A large **teal and white eye** on a blue platform. Taking in the current state.

**PLAN**
A **folded teal map** showing a dashed route with a start point and an ✗ destination. Options and a path.

**CHOOSE**
Three **teal arrows** branching upward and outward from a single teal base disc. Commitment to one option.

**ACT**
A **teal hand gripping a grey wrench**. The only stage that touches the world.

**CHECK**
A **teal magnifying glass** over a **teal check disc**. Assessing whether the result is sufficient.

**STOP**
A **chequered flag** on a teal pole. A finish line, given its own platform.

**ASK HUMAN**
A person figure in a teal top on a blue platform, labelled in **coral** capitals.

## Colour and flow semantics

- **Solid cyan arrows** carry the main loop clockwise and the exit to STOP.
- **Dashed teal arrows** carry the two return paths — check back to plan, and human back to act. Dashed marks a return rather than forward progress.
- **Coral** appears once, on the escalation branch, consistent with coral marking human-control paths throughout the library.
- **Teal** dominates every stage icon, marking the agent's own working machinery.
- The ring is **closed** — STOP returns to OBSERVE, so ending a task does not end the agent.

## How to present it

**Ask what an agent does, in five words.** Let the room try. Then reveal the ring. Most attempts produce three or four of the five and merge plan with choose.

**Ask why plan and choose are separate.** Planning produces options; choosing commits. Then ask what it means if an agent generates one option — it never really chooses, and its "decision" is whatever occurred to it first.

**Count the exits from check.** Three. Then ask what happens to an agent that has only one. It loops. Tell the Bramble nine-minute story with the 47 tool calls, and note that it had stopped making progress after four.

**Then tell the second symptom immediately.** The boiler that stopped too early. Same defect, opposite direction — no definition of sufficiency. This pairing is the most efficient way to teach that a stop condition is a *specification*, not a counter.

**Ask what their stop condition would be.** For an agent the room is building or imagining. Push for a checklist rather than "when it has an answer." Bramble's five items are a good model.

**Separate the two kinds of escalation.** Capability — the agent is not confident. Authority — the agent is not permitted, regardless of confidence. Bramble's gas and vulnerable-customer rules are the second kind, and beginners rarely think of it.

**Ask what a good question to a human looks like.** "Should I proceed?" versus a framed choice with context. Read the ceiling-leak escalation aloud. A coordinator answers it in fifteen seconds; a bare "should I proceed" produces a coordinator who has to do the whole investigation themselves.

**Point at where the human's answer returns.** To ACT, not to PLAN. Ask why. Because the plan was fine — what was missing was a decision or a piece of information, so the agent proceeds with the action it was already about to take.

**Ask why STOP loops back to OBSERVE.** Finishing a task is not finishing. The ring is closed because the agent goes back to watching.

**Timing.** Twenty-five minutes. Thirty-five if you have the room define a stop condition and escalation triggers for a real agent idea, which is the exercise that prevents the runaway loop.

---

## Lab and checkpoint

**Lab:** Design a stop condition and two escalation triggers for one agent your team is building or imagining. The stop condition should be a checklist, not a counter. One escalation should be for capability uncertainty and one for authority. Write the exact question the agent would ask a human and what it would do after receiving the answer.

**Checkpoint:** Why are plan and choose separate stages?

**Answer:** Because planning produces options and choosing commits to one. If an agent generates only one option, it never really chooses; its "decision" is whatever occurred to it first. Separating the two makes the agent evaluate alternatives before committing.

## Glossary

- **Act** — the stage that executes the chosen action.
- **Check** — the stage that evaluates the result against the stop condition.
- **Choose** — the stage that commits to one of the planned options.
- **Escalation** — the path to a human when the agent lacks capability or authority.
- **Human in the loop** — the person who receives a framed question and returns an answer.
- **Observe** — the stage that watches for the next situation.
- **Plan** — the stage that generates options for how to proceed.
- **Stop condition** — the checklist that decides when the task is finished.

## Sources

- Agent decision loops and stop-condition design
- Human-in-the-loop escalation and authority boundaries
- Planning, choosing, and acting in autonomous systems
