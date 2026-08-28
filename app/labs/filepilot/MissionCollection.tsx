"use client";

import { useEffect, useState } from "react";
import FilePilotLab from "./FilePilotLab";
import { missions } from "@/lib/filepilot-missions";
import MissionScenario from "@/app/components/MissionScenario";

export default function MissionCollection() {
  const [selected, setSelected] = useState(1);
  useEffect(() => {
    const read = () => { const n = Number(new URLSearchParams(location.hash.slice(1)).get("mission")); setSelected(n === 1 || missions.some(m => m.id === n) ? n : 1); };
    read(); window.addEventListener("hashchange", read);
    return () => window.removeEventListener("hashchange", read);
  }, []);
  const mission = missions.find(m => m.id === selected);
  return <>
    <nav className="fp-mission-nav" aria-label="FilePilot missions"><div><strong>FilePilot · {missions.length + 1} mission labs</strong><p>Choose a mission. Switching missions resets its exercise; no real files or services are connected.</p>{["01–10 · Foundations", "11–20 · Filesystem investigations", "21–30 · Advanced automation"].map((label, group) => <details key={label} open={Math.floor((selected - 1) / 10) === group} className="fp-mission-group"><summary>{label}</summary><div className="fp-mission-links">{[{ id: 1, title: "A tidy folder. Nothing lost." }, ...missions].filter(m => Math.floor((m.id - 1) / 10) === group).map(m => <a key={m.id} href={`#mission=${m.id}`} aria-current={selected === m.id ? "page" : undefined}>{String(m.id).padStart(2, "0")} · {m.title}</a>)}</div></details>)}</div></nav>
    {mission ? <MissionScenario key={mission.id} mission={mission} collectionTitle="FilePilot" caseStudyId="filepilot" total={missions.length + 1} /> : <FilePilotLab />}
  </>;
}
