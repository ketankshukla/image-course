# Build FilePilot — Foundations and Your First Tests

## At a glance

Start with a program that cannot touch the filesystem at all. Its job is to determine whether a plan is unchanged, approved, and still eligible for execution. This exercise uses Python's standard library and synthetic identifiers. It is intentionally not a complete permission system or filesystem executor.

## What the diagram teaches

![Approval precedes prechecks and execution. A changed or ambiguous state must not be treated as verified completion.](../assets/recovery.svg)

Maya approves moving file F-001 into folder D-AGENT. Someone then changes the proposed destination to D-OTHER. The approval must no longer match. The exercise below captures that simple idea in a digest: a fingerprint of the exact plan fields.

The engine also observes a source revision just before execution. If that revision differs from the approved expectation, the plan is stale. These are separate checks: an unchanged plan can still refer to a changed file.

## 1. Create the smallest learning file

In a new empty application repository, create `foundation_exercise.py` and paste the complete block below. It performs no reads, writes, moves, or network requests. Run it with `python foundation_exercise.py` after installing a supported Python version. Expected result: five passing tests.

```python
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
import json
import unittest


@dataclass(frozen=True)
class Plan:
    root_id: str
    grant_version: int
    file_id: str
    expected_revision: str
    destination_id: str
    destination_name: str
    operation: str = "move"


def plan_digest(plan: Plan) -> str:
    payload = json.dumps(
        asdict(plan), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return sha256(payload).hexdigest()


def check_execution(plan, approved_digest, expires_at, now,
                    observed_revision, destination_exists, current_grant):
    if plan.operation != "move":
        raise ValueError("unsupported_operation")
    if current_grant != plan.grant_version:
        raise ValueError("grant_changed")
    if now >= expires_at:
        raise ValueError("approval_expired")
    if approved_digest != plan_digest(plan):
        raise ValueError("plan_changed")
    if observed_revision != plan.expected_revision:
        raise ValueError("source_changed")
    if destination_exists:
        raise ValueError("destination_occupied")
    return "eligible_for_adapter_checks"


class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.plan = Plan("ROOT-DEMO", 1, "F-001", "rev-a",
                         "D-AGENT", "agent-notes.txt")
        self.digest = plan_digest(self.plan)

    def check(self, **changes):
        args = dict(plan=self.plan, approved_digest=self.digest,
                    expires_at=200, now=100, observed_revision="rev-a",
                    destination_exists=False, current_grant=1)
        args.update(changes)
        return check_execution(**args)

    def test_matching_plan(self):
        self.assertEqual(self.check(), "eligible_for_adapter_checks")

    def test_changed_destination(self):
        with self.assertRaisesRegex(ValueError, "plan_changed"):
            self.check(plan=replace(self.plan, destination_id="D-OTHER"))

    def test_changed_source(self):
        with self.assertRaisesRegex(ValueError, "source_changed"):
            self.check(observed_revision="rev-b")

    def test_existing_destination(self):
        with self.assertRaisesRegex(ValueError, "destination_occupied"):
            self.check(destination_exists=True)

    def test_expiry_and_revocation(self):
        with self.assertRaisesRegex(ValueError, "approval_expired"):
            self.check(now=200)
        with self.assertRaisesRegex(ValueError, "grant_changed"):
            self.check(current_grant=2)


if __name__ == "__main__":
    unittest.main()
```

## 2. Understand every function

`Plan` names the expected operation. Its frozen dataclass prevents ordinary field assignment, but immutability here is a programming aid, not protection against a hostile caller. The authoritative persisted record still belongs on the server.

`plan_digest` produces stable bytes for this Python exercise. It is not automatically a cross-language canonicalization standard. `check_execution` examines conditions in a deliberate order and returns eligibility for more checks—not permission to perform arbitrary I/O.

The timestamps are synthetic integer values injected by tests. In the actual service, use a trusted clock and a consistent timezone-aware or epoch representation. Clients must not choose “now.” The observed revision, destination occupancy, and grant version must also come from trusted server-side observations rather than request fields.

## 3. Refactor only after the tests pass

Move `Plan` into `contracts.py`, the digest and execution rules into `approvals.py`, and the test class into `tests/unit/test_approvals.py`. Add a proper package layout and test command. Keep this pure logic independent of MCP, FastAPI, and any model SDK.

Then expand the contract with principal identity, root identity, operation IDs, plan revision, and allowed destination validation. Add tests for unsupported operations, malformed names, unknown fields, and mismatched principals. Those checks are deliberately absent from the minimal exercise and required before any write adapter is enabled.

## Acceptance gate

You can explain all five tests and add a sixth without asking a model to execute an operation. Passing them proves only the exercise's pure rules. It does not prove path containment, race resistance, operating-system semantics, or production safety.
