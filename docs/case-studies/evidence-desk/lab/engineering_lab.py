"""Offline teaching model: no LLM, network, durable storage, or production auth."""
from dataclasses import dataclass, replace
from decimal import Decimal
import unittest


@dataclass(frozen=True)
class Source:
    id: str
    workspace: str
    current: bool
    monthly_price: Decimal


SOURCES = (
    Source("P1", "northstar", False, Decimal("15")),
    Source("P2", "northstar", True, Decimal("20")),
    Source("X1", "finance", True, Decimal("9")),
)
PROMPT = "Draft only. Cite supplied evidence IDs. Mark absent evidence unknown."


def context(workspace):
    return [s for s in SOURCES if s.workspace == workspace and s.current]


def tool(name, seats, source):
    # Caller supplies only a source already admitted by the context layer.
    if name != "calculate_subscription":
        raise PermissionError("Tool not allowed")
    if type(seats) is not int or not 1 <= seats <= 1000:
        raise ValueError("Seats must be an integer between 1 and 1000")
    if source.monthly_price < 0:
        raise ValueError("Negative price")
    return source.monthly_price * seats * 12


def research(packet):
    # Sequential branches teach dependencies before introducing concurrency.
    if not packet:
        return None
    if len(packet) != 1:
        raise ValueError("Conflicting current price sources")
    cost = tool("calculate_subscription", 12, packet[0])
    capabilities = {"export": "unknown"}
    requirements = {"seats": 12, "export_required": True}
    return {"cost": cost, "capabilities": capabilities,
            "requirements": requirements, "source_id": packet[0].id}


def fake_writer(merged, bad=False):
    # PROMPT is recorded for illustration, not executed by an actual model.
    return {"prompt": PROMPT, "annual_cost": merged["cost"],
            "evidence_id": "P999" if bad else merged["source_id"],
            "export": merged["capabilities"]["export"]}


def check(draft, merged):
    return (draft["evidence_id"] == merged["source_id"]
            and draft["annual_cost"] == merged["cost"]
            and draft["export"] == "unknown")


def run(workspace="northstar", always_bad=False, cancelled=False):
    events = []
    if cancelled:
        return "cancelled", None, events
    packet = context(workspace)
    merged = research(packet)
    if merged is None:
        return "needs_evidence", None, events
    for attempt in range(3):  # initial draft plus two revisions
        draft = fake_writer(merged, bad=always_bad)
        events.append({"attempt": attempt + 1, "passed": check(draft, merged)})
        if events[-1]["passed"]:
            return "needs_review", draft, events
    return "exhausted", draft, events


class EngineeringTests(unittest.TestCase):
    def test_context_excludes_restricted_and_stale(self):
        self.assertEqual([s.id for s in context("northstar")], ["P2"])

    def test_cost(self):
        self.assertEqual(tool("calculate_subscription", 12, SOURCES[1]), Decimal("2880"))

    def test_forbidden_tool(self):
        with self.assertRaises(PermissionError):
            tool("publish_report", 12, SOURCES[1])

    def test_invalid_seats(self):
        for seats in (0, -1, True, 1.5, 1001):
            with self.assertRaises(ValueError):
                tool("calculate_subscription", seats, SOURCES[1])

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            tool("calculate_subscription", 12, replace(SOURCES[1], monthly_price=Decimal("-1")))

    def test_review_not_approval(self):
        state, draft, events = run()
        self.assertEqual(state, "needs_review")
        self.assertEqual(draft["export"], "unknown")
        self.assertEqual(len(events), 1)

    def test_bounded_failure(self):
        state, _, events = run(always_bad=True)
        self.assertEqual(state, "exhausted")
        self.assertEqual(len(events), 3)

    def test_cancel_before_work(self):
        self.assertEqual(run(cancelled=True), ("cancelled", None, []))

    def test_missing_evidence(self):
        self.assertEqual(run("unknown"), ("needs_evidence", None, []))

    def test_conflicting_sources(self):
        with self.assertRaises(ValueError):
            research([SOURCES[1], SOURCES[2]])

    def test_false_cost_rejected(self):
        merged = research(context("northstar"))
        draft = fake_writer(merged)
        draft["annual_cost"] = Decimal("1")
        self.assertFalse(check(draft, merged))


if __name__ == "__main__":
    unittest.main(verbosity=2)
