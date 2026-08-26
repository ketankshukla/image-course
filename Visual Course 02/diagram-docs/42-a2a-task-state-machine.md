# Diagram 42 — A2A Task State Machine

![A state diagram on dark navy. SUBMITTED holds a white card reading TASK-1024 with a green check. A cyan arrow leads to WORKING, showing a teal gear and the same TASK-1024 card. From WORKING, a cyan arrow curves up to INPUT REQUIRED with a teal question bubble and the TASK-1024 card, with a second cyan arrow curving back down to WORKING. A long cyan arrow runs right to COMPLETED, showing a large teal check and the TASK-1024 card. Two coral arrows drop from WORKING to FAILED, a red warning triangle with the card, and CANCELED, a red cross with the card.](../diagrams/42-a2a-task-state-machine.png)

**Module:** Agent behaviour
**Role in the course:** what happens to delegated work over time
**Layout:** a state machine with one card moving through five states

---

## At a glance

Five states, and **the same card — TASK-1024 — appears in every one of them**.

That repetition is the diagram's method. It is not showing five different things; it is showing one thing at five moments. The task has an identity that persists across every state change, which is precisely what makes work that takes time possible to manage.

Three of the five states are terminal. Two of those three are failures, drawn in coral, at equal weight to the success.

---

## What the diagram teaches

### 1. The card is the same card, and that is the whole idea

**TASK-1024** appears five times. Same identifier, same card shape, different badge in each state — a green check when submitted, a gear when working, a question mark when input is required, a warning when failed, a cross when cancelled, a large check when completed.

A task is not a message that gets sent and answered. It is an **object with an identity that outlives any single request**. That identity is what lets you:

- Ask about it later, from a different session, after a restart.
- Attach a result to it when the result eventually exists.
- Report on how many are in flight and in what states.
- Audit what happened to a specific piece of work.

Without the identifier, none of those are possible, and work that takes longer than one request cannot be managed at all.

### 2. Five states, and two of them are failures

**SUBMITTED** — accepted, not yet started. Distinguishing this from working matters more than it seems: a task queued behind others is not stuck, and a caller needs to be able to tell the difference.

**WORKING** — in progress. The gear conveys ongoing activity.

**INPUT REQUIRED** — paused, waiting on the caller. Not failed; blocked on someone else.

**COMPLETED** — finished successfully, result available.

**FAILED** — could not be completed.

**CANCELED** — stopped deliberately.

Drawing failed and cancelled at the same size and prominence as completed is the diagram refusing to treat them as edge cases. In any real system, a meaningful share of tasks end in one of those two states, and a caller has to be able to handle all three terminal outcomes.

### 3. Failed and cancelled are different, and conflating them loses information

Both are coral, both are terminal, and they mean different things.

**FAILED** — the work was attempted and could not be completed. Something went wrong: bad input, an unavailable dependency, an impossible request. There is a reason, and the reason is diagnostic.

**CANCELED** — a decision was made to stop. Nothing went wrong; someone changed their mind, or the work became unnecessary, or a timeout policy ended it.

A system that reports both as "failed" makes its own metrics meaningless. A rising failure rate is a signal to investigate; a rising cancellation rate is usually a signal about user behaviour or upstream changes. Merging them hides both.

### 4. Input required is the state beginners never build, and it is the most useful one

A **teal question bubble**, reached from working and returning to working.

This is the state that lets a task ask a question. Without it, an agent that encounters ambiguity has exactly two options: guess, or fail. Both are bad, and both are avoidable.

Three properties make it work:

**It is not terminal.** The task is alive, holding its context, waiting. When the answer arrives it resumes from where it paused rather than restarting.

**It returns to working, not to submitted.** The curved arrow back down is explicit about this. Everything established before the question stays established.

**It is a normal state, not an error.** It appears in cyan alongside the success path, not in coral with the failures. A task waiting for input is a healthy task.

This mirrors the **ASK HUMAN** branch of the agent decision loop earlier in the volume:

![A circular loop of five platforms — OBSERVE, PLAN, CHOOSE, ACT, CHECK — with a cyan exit to STOP, a dashed return to PLAN, and a coral branch down to ASK HUMAN.](../diagrams/39-agent-decision-loop.png)

Same idea, expressed differently. There it is a momentary detour from the check stage; here it is a **persistent state** the task can sit in for minutes or days. The difference matters: a detour needs someone waiting, a state does not.

### 5. Everything branches from working, and nothing branches from submitted

Look at where the arrows leave from. **WORKING** has four outgoing paths: to input required, to completed, to failed, to cancelled. **SUBMITTED** has one.

That asymmetry is accurate. A submitted task has not been attempted, so it cannot have succeeded or failed, and it has not encountered anything it needs to ask about. All the interesting transitions happen once work has begun.

It also means **WORKING is where your monitoring belongs**. A task in working for far longer than expected is the signature of almost every operational problem — a stuck dependency, an infinite loop, a lost worker.

### 6. Three terminal states means callers need three handlers

A practical consequence worth making explicit for beginners.

Code that delegates a task and waits for a result usually handles one outcome: the result arrives. This diagram says there are three ways a task can end, and only one of them produces a result.

Handling only the success path produces a caller that hangs forever on a failed task, or treats a cancellation as a timeout, or has no path for a task that needs an answer before it can continue.

---

## Case study — Alder Print, the artwork check that waited three weeks

Alder is a commercial printer producing packaging and labels for food and drink brands. Before anything goes to press, artwork must be checked: colour profiles, bleed, barcode integrity, legal text placement, and — for food packaging — allergen declaration formatting.

They delegate the check to a prepress specialist agent that their studio team built and maintain separately.

### The first version — three states

Their initial implementation had `pending`, `done`, and `error`.

It worked for straightforward jobs. Roughly a quarter of jobs are not straightforward.

### What went wrong

**Ambiguity became failure.** Artwork arrived where the barcode was placed over a fold. Whether that is acceptable depends on the substrate and the folding method — information the prepress agent did not have and could not obtain.

With only three states, the agent had to choose: guess (and risk a print run with an unscannable barcode) or return `error`.

It returned `error`. The job appeared in the studio's queue as a failed check with a message about barcode placement. An operator read "error," assumed a system fault, and re-submitted the identical file. It failed again. This happened four times over three weeks before someone read the message properly and realised it was a **question**, not a fault.

The job was three weeks late. The client moved two subsequent orders elsewhere.

**Cancellations polluted the failure rate.** Clients pull jobs — a recipe changes, a launch is delayed, a design is revised. Those jobs were being cancelled mid-check and recorded as `error`.

Their failure rate read as 19%. The studio manager spent a fortnight investigating what was wrong with the prepress agent. Actual failure rate was about 6%; the other 13 points were cancellations.

**Queued was invisible.** During busy periods, jobs waited hours before the check started. Both queued and in-progress jobs showed as `pending`, so operators could not tell whether a job was waiting or being worked on. They chased the studio team about jobs that were simply in a queue.

### The rebuild — five states plus queued

They implemented the diagram's five states, plus a separate queued state distinct from submitted.

**INPUT REQUIRED** was the change that mattered most. The barcode case now looks like this:

> TASK-4471 · Input required · Barcode placed across fold at 14mm from spine. Acceptable on 300gsm folding boxboard with score-and-fold; not acceptable on corrugated. Confirm substrate and fold method, or approve repositioning.

An operator answers that in under a minute. The task resumes with the answer; it does not restart, and everything the agent had already checked stays checked.

**FAILED and CANCELED separated.** Failure rate immediately read as 6%, and the studio manager stopped investigating a problem that did not exist. Cancellation rate became its own number, which turned out to be useful for a different reason — a spike in cancellations traced to a client whose design approval process had changed, which prompted a conversation and a process fix.

**Queued distinguished from working.** Operators can see whether a job is waiting or being processed. Chasing dropped substantially.

**Working became the monitored state.** Any task in working for more than twice its expected duration raises an alert. This has caught three genuine stalls — twice a dependency on their colour-profile service, once a malformed PDF that put the parser into a loop.

### The measured effect

- **Jobs stuck in a misread error state:** effectively zero. About 22% of jobs now pass through input required, and median time spent there is around four minutes.
- **Failure rate:** reported accurately at 6%, from an apparent 19%.
- **Average check turnaround:** from 3.1 hours to 40 minutes, almost entirely because ambiguous jobs stopped being re-submitted repeatedly.
- **Operator chase messages to the studio team:** down about 70%.

### What the studio lead said

*We thought we had three states because we thought there were three things that could happen. There were six, and the two we were missing were the two that happened most often.*

---

## Composition

A state diagram reading left to right, with branches above and below the main line.

**SUBMITTED** (left) → **WORKING** (centre-left) → **COMPLETED** (right), connected by cyan arrows.

From **WORKING**, a cyan arrow curves upward to **INPUT REQUIRED** (upper centre-right), with a second cyan arrow curving back down to **WORKING**.

Two **coral arrows** drop from **WORKING** to **FAILED** (lower centre-right) and **CANCELED** (lower right).

Every state platform carries a white card reading **TASK-1024**.

## Element by element

**SUBMITTED**
A white card reading **TASK-1024** with a **green check disc**, seated in a raised blue cradle. Accepted, not yet started.

**WORKING**
A large **teal gear** beside the **TASK-1024** card, which carries a small gear badge. Active processing.

**INPUT REQUIRED**
A **teal speech bubble containing a question mark**, beside the **TASK-1024** card carrying a question-mark badge. Paused, awaiting an answer. Reached and left by cyan arrows.

**COMPLETED**
A large **teal check disc** beside the **TASK-1024** card carrying a small check badge. Successful terminal state.

**FAILED**
A **red warning triangle** with an exclamation, beside the **TASK-1024** card carrying a red exclamation badge. Terminal.

**CANCELED**
A **red circular cross**, beside the **TASK-1024** card carrying a red cross badge. Terminal.

## Colour and flow semantics

- **Cyan arrows** carry every non-failure transition, including both directions of the input-required detour.
- **Coral arrows** carry the two failure transitions, and only those.
- **Teal** marks the active and successful states — the gear, the question bubble, the completion check.
- **Red badges** distinguish the two terminal failures from each other by shape: a triangle for failed, a circle-cross for cancelled.
- The **persistent TASK-1024 card** in every state is the diagram's central device.
- **WORKING is the only state with multiple outgoing transitions** — four of them.

## How to present it

**Ask what is the same in all five panels.** The card. Then ask why that matters. A task is an object with an identity that outlives a request, and that identity is what makes everything else possible — asking about it, attaching a result, reporting on it, auditing it.

**Count the terminal states.** Three. Then ask how many their code handles. Usually one. A caller that only handles success hangs on failure and has nowhere to put a task that needs an answer.

**Ask the difference between failed and cancelled.** Something went wrong versus someone decided to stop. Then tell the Alder metric story — a 19% failure rate that was actually 6%, and a fortnight spent investigating a problem that did not exist. Merging the two makes your own numbers lie to you.

**Spend the most time on input required.** Ask what an agent does when it hits genuine ambiguity and has only success and failure available. Guess or fail. Both are bad.

**Then tell the barcode story.** Three weeks, four identical re-submissions, because a question was reported as an error and an operator read the label rather than the message. This is the most vivid illustration in the volume of why the state matters more than the message.

**Ask why the return arrow goes to working and not to submitted.** Because the task resumes rather than restarting. Everything already established stays established. This is the same reasoning as the human's answer returning to ACT in the agent decision loop.

**Point out that input required is cyan, not coral.** A task waiting for input is healthy. Presenting it as an error is what caused Alder's three-week delay.

**Ask where the arrows leave from.** All four branches come out of working. Then make the operational point: working is where monitoring belongs, because a task in working for too long is the signature of nearly every operational problem.

**Ask about queued.** The diagram does not have it, and Alder needed it. Whether submitted and queued are distinct depends on whether your callers need to tell waiting from working. Worth asking rather than assuming.

**Timing.** Twenty minutes. Thirty if you have the room enumerate the states for a real piece of delegated work, which is where the missing ones surface.

---

## Lab and checkpoint

**Lab:** Enumerate the states for one real piece of delegated work in your system. Start with submitted, working, input-required, completed, failed, and cancelled. Then add queued if callers need to tell waiting from working. Draw the transitions and identify where a task in working for too long becomes an operational problem.

**Checkpoint:** What is the difference between failed and cancelled?

**Answer:** Failed means something went wrong and the task could not complete. Cancelled means someone decided to stop the task before it completed. Merging them makes your own numbers lie to you, and it hides the cause of a stopped task.

## Glossary

- **Cancelled** — a terminal state where the caller or operator ended the task before completion.
- **Completed** — the terminal state where the task finished successfully.
- **Failed** — a terminal state where the task could not complete due to an error.
- **Input-required** — a healthy state where the specialist needs clarification before continuing.
- **State machine** — the defined set of states and the permitted transitions between them.
- **Submitted** — the initial state where the task has been accepted.
- **Task** — the managed object with an identity that outlives any single request.
- **Terminal state** — a state with no further transitions.
- **Working** — the state where the specialist is actively working on the task.

## Sources

- A2A task lifecycle and state-machine documentation
- Long-running task monitoring and operational alerts
- Task state design and terminal-state distinction
