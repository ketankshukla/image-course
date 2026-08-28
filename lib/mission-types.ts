export type MissionAction = { label: string; next: string };
export type MissionStep = { title: string; explanation: string; evidence: string[]; actions: MissionAction[]; complete?: boolean; blocked?: boolean };
export type Mission = { id: number; title: string; topic: string; brief: string; boundary: string; steps: Record<string, MissionStep>; clues?: { id: string; title: string; text: string }[]; comparison?: { title: string; explanation: string }[] };

export function advanceMission(mission: Mission, current: string, target: string, inspected: string[] = []): string {
  if (current === "start" && mission.clues?.some(c => !inspected.includes(c.id))) throw new Error("Inspect every evidence card before choosing a strategy.");
  if (!mission.steps[current]?.actions.some(a => a.next === target) || !mission.steps[target]) throw new Error("That transition is not available from the current step.");
  return target;
}
