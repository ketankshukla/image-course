import type { Mission } from "./mission-types";

type Strategy = { label: string; review: string; plan: string[]; result: string[]; tradeoff: string };
type Investigation = {
  id: number; title: string; topic: string; brief: string;
  clues: { title: string; text: string }[];
  shortcut: string; rejection: string; rejectedEvidence: string[];
  strategies: [Strategy, Strategy]; lesson: string;
};

export function investigation(config: Investigation): Mission {
  const [a, b] = config.strategies;
  const choice = (label: string, next: string) => ({ label, next });
  return {
    id: config.id, title: config.title, topic: config.topic, brief: config.brief,
    boundary: "This investigation uses fixed fictional evidence and predefined outcomes. It does not inspect files, run tools, or contact external services.",
    clues: config.clues.map((c, i) => ({ ...c, id: `clue-${i + 1}` })),
    comparison: config.strategies.map(s => ({ title: s.label, explanation: s.tradeoff })),
    steps: {
      start: { title: "Inspect the case before choosing", explanation: "Open each evidence card. Compare what the task asks for with the observed state; do not assume a filename or a success message tells the whole story.", evidence: [config.brief, "No operation has been authorized or executed."], actions: [choice("Compare the available strategies", "decision")] },
      decision: { title: "Choose your response", explanation: "There are two defensible strategies here, with different costs. A third option skips an important check. Pick a response and inspect its consequences before approving anything.", evidence: config.clues.map(c => `${c.title}: ${c.text}`), actions: [choice(a.label, "review-a"), choice(config.shortcut, "blocked"), choice(b.label, "review-b")] },
      blocked: { title: "That shortcut does not satisfy the policy", explanation: config.rejection, evidence: config.rejectedEvidence, blocked: true, actions: [choice("Reconsider using the evidence", "decision")] },
      "review-a": { title: "Review strategy A", explanation: a.review, evidence: a.plan, actions: [choice("Choose a different strategy", "decision"), choice("Approve this exact strategy", "result-a")] },
      "review-b": { title: "Review strategy B", explanation: b.review, evidence: b.plan, actions: [choice("Choose a different strategy", "decision"), choice("Approve this exact strategy", "result-b")] },
      "result-a": { title: "Inspect the result of strategy A", explanation: a.tradeoff, evidence: a.result, actions: [choice("Review the lesson and compare alternatives", "done")] },
      "result-b": { title: "Inspect the result of strategy B", explanation: b.tradeoff, evidence: b.result, actions: [choice("Review the lesson and compare alternatives", "done")] },
      done: { title: "Investigation debrief", explanation: config.lesson, evidence: ["Your decision trail records the strategy you actually selected and its simulated result.", "The alternatives below explain what a different choice would trade off; they were not both executed.", "Explain which assumption failed and what you would verify in a real implementation."], complete: true, actions: [] }
    }
  };
}
