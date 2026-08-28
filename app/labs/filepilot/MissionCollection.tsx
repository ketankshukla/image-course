"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import FilePilotLab from "./FilePilotLab";
import { advanceMission, missions, type Mission } from "@/lib/filepilot-missions";

export default function MissionCollection() {
  const [selected, setSelected] = useState(1);
  useEffect(() => {
    const read = () => { const n = Number(new URLSearchParams(location.hash.slice(1)).get("mission")); setSelected(Number.isInteger(n) && n >= 1 && n <= 10 ? n : 1); };
    read(); window.addEventListener("hashchange", read);
    return () => window.removeEventListener("hashchange", read);
  }, []);
  const mission = missions.find(m => m.id === selected);
  return <>
    <nav className="fp-mission-nav" aria-label="FilePilot missions"><div><strong>FilePilot · 10 mission labs</strong><p>Choose a mission. Switching missions resets its exercise; no real files or services are connected.</p><div className="fp-mission-links">{[{ id: 1, title: "A tidy folder. Nothing lost." }, ...missions].map(m => <a key={m.id} href={`#mission=${m.id}`} aria-current={selected === m.id ? "page" : undefined}>{String(m.id).padStart(2, "0")} · {m.title}</a>)}</div></div></nav>
    {mission ? <Scenario key={mission.id} mission={mission} /> : <FilePilotLab />}
  </>;
}

function Scenario({ mission }: { mission: Mission }) {
  const [current, setCurrent] = useState("start");
  const [trail, setTrail] = useState<{ title: string; evidence: string[] }[]>([]);
  const state = mission.steps[current];
  function choose(target: string, label: string) {
    const next = advanceMission(mission, current, target);
    setTrail(old => [...old, { title: `${state.title} → ${label}`, evidence: state.evidence }]);
    setCurrent(next);
  }
  function restart() { setCurrent("start"); setTrail([]); }
  return <div className="fp-lab"><header className="fp-top"><Link href="/">← Learning library</Link><span>MISSION {String(mission.id).padStart(2, "0")} / 10</span><Link href="/#course=filepilot&chapter=1">FilePilot case study</Link></header><main>
    <section className="fp-hero"><p className="fp-eyebrow">{mission.topic}</p><h1>{mission.title}</h1><p className="fp-lead">{mission.brief}</p><div className="fp-badge">Guided simulation · Fictional data · No live AI or filesystem access</div><p className="fp-small">{mission.boundary} Your choices reveal predefined outcomes so you can practise the decision process. Session evidence is lost when you refresh or switch missions.</p></section>
    <section className="fp-card"><h2>How this mission works</h2><ol className="fp-flow"><li><span>1</span>Read the task</li><li><span>2</span>Inspect evidence</li><li><span>3</span>Choose an action</li><li><span>4</span>Explain the outcome</li></ol><p>Try an unsafe choice if you want to see why it fails. A blocked action changes no real files. You can return to the safe path without restarting.</p></section>
    <section className="fp-card" aria-label="Active mission step"><p className="fp-eyebrow">{state.complete ? "COMPLETED" : state.blocked ? "SAFETY BOUNDARY" : "YOUR NEXT DECISION"}</p><div aria-live="polite" aria-atomic="true"><h2>{state.title}</h2><p>{state.explanation}</p></div><div className="fp-preview"><h3>Evidence you can inspect</h3><ul className="fp-evidence">{state.evidence.map((line, i) => <li key={i}>{line}</li>)}</ul></div><div className="fp-actions">{state.actions.map(a => <button key={a.label} className="fp-primary" onClick={() => choose(a.next, a.label)}>{a.label}</button>)}</div>{state.complete && <div className="fp-status"><strong>You completed mission {mission.id}.</strong> Explain the outcome in your own words: what was permitted, what was rejected, and which evidence justified the decision?{mission.id < 10 && <p><a href={`#mission=${mission.id + 1}`}>Continue to mission {mission.id + 1} →</a></p>}</div>}<button onClick={restart}>Restart this mission</button></section>
    <section className="fp-card"><h2>Your decision trail</h2><p className="fp-small">This is an educational session record, not a production audit log. It includes unsafe choices as well as successful ones.</p>{trail.length ? <ol className="fp-events">{trail.map((entry, i) => <li key={i}><details><summary>{entry.title}</summary><ul>{entry.evidence.map((line, n) => <li key={n}>{line}</li>)}</ul></details></li>)}</ol> : <p>No actions yet. Inspect the evidence above and choose your first action.</p>}</section>
  </main><footer>FilePilot · Safe practice before real automation</footer></div>;
}
