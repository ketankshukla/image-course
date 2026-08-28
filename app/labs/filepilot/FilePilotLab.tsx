"use client";

import Link from "next/link";
import { useState } from "react";
import { applyPlan, makePlan, planErrors, seedFiles, type DemoFile, type Move } from "@/lib/filepilot-lab";

export default function FilePilotLab() {
  const [files, setFiles] = useState<DemoFile[]>(seedFiles);
  const [plan, setPlan] = useState<Move[] | null>(null);
  const [approved, setApproved] = useState(false);
  const [snapshot, setSnapshot] = useState<DemoFile[] | null>(null);
  const [stage, setStage] = useState(0);
  const [events, setEvents] = useState<string[]>(["Sandbox ready. Five fictional files; nothing has moved."]);
  const [notice, setNotice] = useState("Start by generating a plan. This only proposes changes.");
  const [selected, setSelected] = useState("1");
  const [challenge, setChallenge] = useState(false);
  const [recovered, setRecovered] = useState(false);
  const [answer, setAnswer] = useState("");
  const errors = plan ? planErrors(files, plan) : [];
  const preview = files.find(f => f.id === selected);
  function record(message: string) { setEvents(old => [...old, message]); setNotice(message); }
  function reset() {
    setFiles(seedFiles); setPlan(null); setApproved(false); setSnapshot(null); setStage(0);
    setChallenge(false); setRecovered(false); setAnswer(""); setSelected("1");
    setEvents(["Sandbox reset to five fictional files."]); setNotice("Ready for a fresh mission.");
  }
  function generate() {
    setPlan(makePlan(files)); setApproved(false); setStage(1);
    record("Plan generated: four proposed moves. The ZIP stays in Inbox. No files changed.");
  }
  function injectConflict() {
    setFiles(old => [...old, { id: "conflict", path: "Documents/meeting.txt", content: "An existing fictional document. Do not overwrite me." }]);
    setChallenge(true); setApproved(false);
    record("Challenge added: Documents/meeting.txt already exists. Approval is blocked until the plan is safe.");
  }
  function resolve() {
    setPlan(old => old?.map(m => m.id === "4" ? { ...m, to: "Documents/meeting-from-inbox.txt" } : m) ?? null);
    setApproved(false); record("Plan revised to use meeting-from-inbox.txt. Review it again; the existing file will be preserved.");
  }
  function execute() {
    try {
      const next = applyPlan(files, plan ?? [], approved);
      setSnapshot(files); setFiles(next); setStage(2); setApproved(false);
      record("Applied four moves in the simulation. Contents and file count are unchanged. Undo is available.");
    } catch (error) { record(error instanceof Error ? error.message : "Operation blocked."); }
  }
  function undo() {
    if (!snapshot) return;
    setFiles(snapshot); setSnapshot(null); setPlan(null); setApproved(false); setStage(3); setRecovered(true);
    record("Undo complete: the exact pre-approval sandbox state has been restored, including any existing conflict file.");
  }
  return <div className="fp-lab">
    <header className="fp-top"><Link href="/">← Learning library</Link><span>MISSION LAB / 01</span><Link href="/#course=filepilot&chapter=1">Read the FilePilot case study</Link></header>
    <main id="lab-main">
      <section className="fp-hero"><p className="fp-eyebrow">FILEPILOT · LEARN BY DOING</p><h1>A tidy folder.<br />Nothing lost.</h1><p className="fp-lead">Your mission: organize a messy project folder, approve every move, and prove you can undo the operation.</p><div className="fp-badge">Safe simulation · Fictional files only · No account needed</div><p className="fp-small">Everything runs in this browser tab. No files are uploaded, read from your computer, or written to disk. Refreshing clears the mission. This version uses fixed rules—not live AI, MCP, RAG, or A2A services.</p></section>
      <section className="fp-card"><h2>Your flight plan</h2><ol className="fp-flow" aria-label="Mission stages">{["Inspect & plan", "Review & approve", "Apply safely", "Undo & explain"].map((label, i) => <li key={label} aria-current={stage === i ? "step" : undefined}><span>{i + 1}</span>{label}{stage === i && <small>Current step</small>}</li>)}</ol><p>Planning is a suggestion. Approval is permission. Execution is a change. Keeping them separate gives you a chance to catch a mistake before it matters.</p></section>
      <div className="fp-workspace">
        <section className="fp-card"><h2>1. Inspect the sandbox</h2><p className="fp-small">Select a file to inspect its fictional contents. Paths below belong only to this demonstration.</p><ul className="fp-files">{files.map(file => <li key={file.id}><button onClick={() => setSelected(file.id)} aria-pressed={selected === file.id}>{file.path}</button></li>)}</ul><div className="fp-preview"><h3>File preview</h3><pre>{preview?.content}</pre></div><p className="fp-small">{files.length} files · Text → Documents · CSV → Spreadsheets · PNG → Images. Unknown types stay put.</p></section>
        <section className="fp-card"><h2>2. Review the proposed moves</h2><p>Generate a plan before making changes. Read both sides of every move.</p><button className="fp-primary" onClick={generate} disabled={stage === 2}>Generate plan</button>
          {plan && <><div className="fp-table"><table><caption>Proposed moves—not changes already made</caption><thead><tr><th>From</th><th>To</th></tr></thead><tbody>{plan.map(m => <tr key={m.id}><td>{m.from}</td><td>{m.to}</td></tr>)}</tbody></table></div><p className="fp-small">Leave unchanged: Inbox/archive.zip. The planner has no rule for archives.</p>
          {stage !== 2 && <><div className="fp-policy"><h3>Safety check</h3>{errors.length ? <ul>{errors.map((e, i) => <li key={i}>{e}</li>)}</ul> : <p>Passed: sources exist, destinations are allowed, and no existing file will be overwritten.</p>}</div>
          <label className="fp-approval"><input type="checkbox" checked={approved} disabled={!!errors.length} onChange={e => setApproved(e.target.checked)} />I reviewed these exact moves and approve this plan.</label><button className="fp-primary" disabled={!approved || !!errors.length} onClick={execute}>Apply approved plan</button></>}
          </>}
        </section>
      </div>
      <section className="fp-card fp-challenge"><div><p className="fp-eyebrow">BREAK IT ON PURPOSE</p><h2>What if the filename already exists?</h2><p>Add an existing meeting document after generating a plan. A safe executor must check the current state, not blindly trust an earlier preview.</p></div><div className="fp-actions"><button onClick={injectConflict} disabled={!plan || challenge || stage === 2}>Introduce a filename conflict</button><button onClick={resolve} disabled={!challenge || !plan || !errors.length || stage === 2}>Revise plan: use a new filename</button></div><p className="fp-small">Revising a plan clears its approval. The original destination file remains untouched.</p></section>
      <section className="fp-card"><h2>3. Check the result and recover</h2><p role="status" aria-live="polite" className="fp-status">{notice}</p><div className="fp-actions"><button className="fp-primary" disabled={!snapshot} onClick={undo}>Undo last operation</button><button onClick={reset}>Reset sandbox</button></div><p className="fp-small">Undo restores a snapshot in browser memory. Real filesystem recovery needs a durable journal and checks for files changed by other programs; this simulation does not implement those protections.</p><details open><summary>Operation evidence · {events.length} events</summary><ol className="fp-events">{events.map((event, i) => <li key={i}>{event}</li>)}</ol></details></section>
      <section className="fp-card"><h2>4. Explain what you learned</h2><p>Why should changing a destination filename clear the approval?</p><div className="fp-actions"><button onClick={() => setAnswer("retry")}>Because renaming is always dangerous</button><button onClick={() => setAnswer("correct")}>Because approval belongs to the exact reviewed plan</button></div><p role="status">{answer === "correct" ? "Exactly. Permission for one plan must not silently authorize a different plan." : answer === "retry" ? "Try again. A rename can be safe; the issue is whether this specific change was reviewed." : "Choose an explanation to check your understanding."}</p>{recovered && answer === "correct" && <div className="fp-status"><strong>Mission complete.</strong> You planned, approved, executed, recovered, and explained the approval boundary. {challenge ? "You also explored a collision challenge." : "Try again with the filename conflict for an extra challenge."}</div>}</section>
      <section className="fp-card"><h2>Where the real technologies fit</h2><p>In a future Python implementation, an MCP server could expose narrowly scoped file tools. RAG could help find relevant document passages. A2A could let specialist agents collaborate on a proposal. None of them replaces explicit permission, destination checks, or a recovery record.</p><p>This lab teaches that safety boundary without connecting an agent to your actual files.</p><Link href="/#course=filepilot&chapter=4">Explore the FilePilot safety policy →</Link></section>
    </main><footer>FilePilot Mission Lab · A practical companion to the Visual Library</footer>
  </div>;
}
