export type DemoFile = { id: string; path: string; content: string };
export type Move = { id: string; from: string; to: string };
export const seedFiles: DemoFile[] = [
  { id: "1", path: "Inbox/project-notes.txt", content: "Fictional project notes: prepare a learning demo." },
  { id: "2", path: "Inbox/budget.csv", content: "item,amount\nDemo hosting,10" },
  { id: "3", path: "Inbox/team-photo.png", content: "Synthetic image placeholder; no real photograph." },
  { id: "4", path: "Inbox/meeting.txt", content: "Fictional meeting: review the plan before applying it." },
  { id: "5", path: "Inbox/archive.zip", content: "Synthetic archive placeholder; never opened or executed." },
];
export function makePlan(files: DemoFile[]): Move[] {
  return files.filter(f => f.path.startsWith("Inbox/")).flatMap(f => {
    const name = f.path.slice(6);
    const folder = name.endsWith(".txt") ? "Documents" : name.endsWith(".csv") ? "Spreadsheets" : name.endsWith(".png") ? "Images" : null;
    return folder ? [{ id: f.id, from: f.path, to: `${folder}/${name}` }] : [];
  });
}
export function planErrors(files: DemoFile[], plan: Move[]): string[] {
  const errors: string[] = [];
  const destinations = new Set<string>();
  const ids = new Set<string>();
  for (const move of plan) {
    if (ids.has(move.id)) errors.push("The same file appears twice in the plan.");
    ids.add(move.id);
    if (!files.some(f => f.id === move.id && f.path === move.from)) errors.push(`Source changed: ${move.from}`);
    if (!/^(Documents|Spreadsheets|Images)\/[^/\\]+$/.test(move.to) || move.to.includes("..")) errors.push(`Destination is outside the allowed folders: ${move.to}`);
    const key = move.to.toLowerCase();
    if (destinations.has(key) || files.some(f => f.path.toLowerCase() === key)) errors.push(`Would overwrite an existing file: ${move.to}`);
    destinations.add(key);
  }
  if (!plan.length) errors.push("There are no supported files to move.");
  return errors;
}
export function applyPlan(files: DemoFile[], plan: Move[], approved: boolean): DemoFile[] {
  if (!approved) throw new Error("Review and explicitly approve the plan first.");
  const errors = planErrors(files, plan);
  if (errors.length) throw new Error(errors.join(" "));
  return files.map(f => ({ ...f, path: plan.find(m => m.id === f.id)?.to ?? f.path }));
}
