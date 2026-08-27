# Workbook 4 — Build the A2A Specialist Network

## P3: delegate work without giving away business authority

**Outcome:** independent Policy and Finance services accept bounded tasks, persist their progress, return versioned artifacts, and recover after a restart. The coordinator talks to them through A2A rather than importing their private implementation functions.

Prerequisites: foundations, account-read contracts from P1, and evidence packs from P2. Use a small command-line coordinator for this workbook. P4 later embeds coordination in the durable case workflow.

## 1. At a glance

![A coordinator delegates bounded tasks to specialist agents, validates returned artifacts, and sends disagreements for review. Task completion does not itself authorize a credit.](../architecture-assets/04-a2a-delegation.png)

The picture includes a future Risk agent; implement only Policy and Finance first. Workflow owner, coordinator, and aggregation are logical responsibilities, not three extra services you must deploy.

An A2A task is an assignment: “Examine this evidence pack and return an eligibility finding.” It is not permission to manage the whole case. An artifact is the structured result of the assignment. The final execution approval remains outside both agents.

## 2. Create a shared task contract

Create `backend/src/acme/contracts/delegation.py`. Define `DelegationInput` with delegation ID, case ID, tenant, deadline, evidence-pack reference, allowed account context, and expected artifact type. Define separate `PolicyFinding` and `FinanceFinding` outputs.

Policy output contains eligibility, reason code, evidence references, policy version, and artifact revision. Finance output contains proposed amount, currency, calculation inputs, calculation-rule version, and revision. A free-text explanation can accompany each result but must not replace these fields.

Pass only the data each specialist needs. Finance does not need every uploaded document; Policy does not need a credential that can mutate the ledger. The service authenticates the coordinator and checks the tenant before accepting the assignment.

## 3. Create the files in order

| File under `backend/src/acme` | Functions to write | What they do |
|---|---|---|
| `agents/task_repository.py` | `accept_task`, `load_task`, `claim_task`, `complete_task` | Persist lifecycle and prevent duplicate acceptance |
| `agents/policy/rules.py` | `evaluate_policy(evidence, context)` | Produce a finding without network calls |
| `agents/finance/rules.py` | `calculate_credit(charge, cap, eligible)` | Calculate a permitted amount |
| `agents/policy/executor.py` | `execute_policy_task(task)` | Load evidence, evaluate, store artifact |
| `agents/finance/executor.py` | `execute_finance_task(task)` | Validate inputs, calculate, store artifact |
| `agents/policy/server.py` | `create_server(dependencies)` | Wire the official A2A server adapter |
| `agents/finance/server.py` | `create_server(dependencies)` | Independent Finance endpoint |
| `agents/client.py` | `submit_delegation`, `wait_for_result` | Protocol calls with deadlines and stable IDs |
| `lab/specialists.py` | `run_specialist_scenario` | Invoke both services and validate outputs |

Use a shared repository interface but separate database roles and ownership. Sharing Python code does not mean both agents should edit each other's tasks.

## 4. Write Finance before adding an LLM

Type this exercise into `agents/finance/rules.py`:

```python
def calculate_credit(charge_minor: int, cap_minor: int, eligible: bool) -> int:
    if type(eligible) is not bool:
        raise TypeError("Eligibility must be Boolean")
    if type(charge_minor) is not int or type(cap_minor) is not int:
        raise TypeError("Amounts must be integer minor units")
    if charge_minor < 0 or cap_minor < 0:
        raise ValueError("Amounts cannot be negative")
    if not eligible:
        return 0
    return min(charge_minor, cap_minor)
```

For the fictional rule, 12000 with a 7500 cap returns 7500. Ineligible returns zero. A charge of 5000 returns 5000, not 7500. Test those cases, plus negative and malformed inputs.

The function does not issue a credit. It returns a recommendation. A model may explain the result, but should not be the calculator for this deterministic rule.

## 5. Implement Policy as a traceable decision

Start with a fixture rule: a named policy version applies to the charge date and allows the exception when the fixture's eligibility conditions match. `evaluate_policy` returns an explicit reason code and the supporting evidence item IDs.

If the applicable source is absent, return an insufficiency finding. If two authoritative versions conflict, return review-required. Do not turn uncertainty into `eligible=True` because that makes the happy path easier.

When you later use a model, validate its structured finding against the contract and verify that cited evidence IDs exist in the supplied pack. Keep the deterministic amount calculation separate. Limit model calls and prevent the specialist from expanding its own task scope.

## 6. Make task acceptance durable

Create a task table with tenant, agent identity, delegation ID, input digest, protocol task ID, state, deadline, revision, and timestamps. Add a unique constraint on tenant/agent/delegation. Add artifact and task-outbox tables.

Implement `accept_task` in one transaction: check authorization, validate input, find an existing delegation, reject changed input under the same ID, or insert the new task and dispatch event together. Return the existing task for a matching retry.

Store accepted work before returning acceptance. Otherwise a successful-looking response can be followed by a lost task when the process stops. Do not rely on a module-level dictionary for task truth.

`complete_task` atomically stores the artifact and transitions the task using an expected revision. A stale executor cannot overwrite a newer result. A request for status reads persisted state and checks authorization every time.

## 7. Connect the A2A protocol

Use the official Python SDK's server, request-handler, executor, and task-store extension points for the version you pin. Implement the persistence adapter against those interfaces; the exact method signatures are version-sensitive. The protocol's lifecycle states and error codes come from that version's specification, not from invented endpoint names. [Official A2A Python SDK](https://github.com/a2aproject/a2a-python).

Create each agent's discovery metadata with its capability, input/output expectations, supported transport, and authentication requirements. Do not place secrets in public discovery metadata. The client should use configured, trusted agent destinations rather than fetch arbitrary user-provided agent URLs.

Start Policy and Finance as separate processes on separate configured ports. The lab client discovers or loads their known capabilities, submits assignments, persists returned task IDs, and retrieves results using the SDK. Test actual wire exchange; calling `evaluate_policy` directly does not prove A2A integration.

## 8. Implement the coordinator loop

`submit_delegation` derives a stable delegation ID for the case, purpose, and input revision. It saves intent before calling the remote endpoint. On an uncertain response, it retries the same delegation rather than creating a new one.

`wait_for_result` repeatedly reads the task state with bounded backoff until a terminal result, input-required state, or deadline. Make one bounded attempt in the initial runner; P4 supplies persisted scheduling. Avoid a forever-loop inside a public HTTP handler.

The coordinator validates artifact type, tenant, case reference, evidence bindings, and revision. It then combines the findings into a proposal candidate. If Policy approves but Finance uses the wrong currency, the result is invalid—not “mostly successful.”

For the initial fictional rule, Policy may complete before Finance so Finance receives an explicit eligibility finding. Later, independent preparatory tasks can run concurrently. Concurrency should follow actual dependencies rather than a blanket “run all agents at once.”

## 9. Restart, cancellation, and failure exercises

| Exercise | What you do | What must happen |
|---|---|---|
| Duplicate acceptance | Resend same delegation | Same task ID |
| Changed input | Reuse ID with different evidence pack | Conflict |
| Restart | Stop agent after acceptance, restart | Persisted task still visible and recoverable |
| Bad artifact | Return wrong case or missing citations | Coordinator rejects it |
| Deadline | Make agent exceed assignment deadline | Review/timeout outcome, no endless wait |
| Wrong tenant | Request another tenant's task | No status or artifact leakage |
| Cancellation race | Cancel as executor finishes | Consistent final state; no artifact overwrite |

Cancellation is a recorded request, not an assumption that remote execution has already stopped. Use revision checks to resolve races. If a task has completed, return its known state rather than pretending cancellation erased history.

## 10. TypeScript implementation path

Create `apps/policy-agent/src/rules.ts`, `executor.ts`, `server.ts`, and corresponding Finance files. Put shared wire contracts in `packages/contracts`, and persistence helpers behind per-service restricted connections.

Use the official JavaScript/TypeScript A2A SDK for server and client integration. Keep task acceptance short, with task-plus-outbox persistence. A bounded durable execution path processes the task; an in-memory promise started by a serverless request is not durable acceptance.

Translate the finance function with safe-integer checks. Run identical fixture contracts against both languages, then test a Python coordinator calling a TypeScript agent. Pin compatible protocol versions and transport explicitly; sharing the name A2A does not guarantee version compatibility.

## 11. Completion and presentation

P3 is complete when two independently running agents accept and recover tasks, return validated artifacts, and cannot write credits. Before production, configure task retention, per-tenant quotas, deadlines, trusted destinations, and authenticated status/artifact access.

Explain it aloud: **“I delegated a bounded question to each specialist, kept their task history, and validated their answers before using them.”**
