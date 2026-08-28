"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import MissionScenario from "@/app/components/MissionScenario";
import { acmeMissions } from "@/lib/acme-missions";

export default function AcmeCollection() {
  const [selected, setSelected] = useState(1);
  useEffect(() => {
    const read = () => { const n = Number(new URLSearchParams(location.hash.slice(1)).get("mission")); setSelected(acmeMissions.some(m => m.id === n) ? n : 1); };
    read(); window.addEventListener("hashchange", read);
    return () => window.removeEventListener("hashchange", read);
  }, []);
  const mission = acmeMissions.find(m => m.id === selected) ?? acmeMissions[0];
  return <>
    <nav className="fp-mission-nav" aria-label="Acme missions"><div><strong>Acme · 30 business-agent mission labs</strong><p>Inspect evidence, choose a strategy, and compare the consequences. These are fictional simulations, not live agents. Switching missions resets the exercise; no persistent progress is tracked.</p><p><Link href="/labs/filepilot">Explore FilePilot’s file-automation missions →</Link></p>{["01–10 · Trustworthy answers", "11–20 · Reliable agent teamwork", "21–30 · Safe operation & releases"].map((label, group) => <details key={label} open={Math.floor((selected - 1) / 10) === group} className="fp-mission-group"><summary>{label}</summary><div className="fp-mission-links">{acmeMissions.filter(m => Math.floor((m.id - 1) / 10) === group).map(m => <a key={m.id} href={`#mission=${m.id}`} aria-current={selected === m.id ? "page" : undefined}>{String(m.id).padStart(2, "0")} · {m.title}</a>)}</div></details>)}</div></nav>
    <MissionScenario key={mission.id} mission={mission} collectionTitle="Acme" caseStudyId="acme" total={acmeMissions.length} />
  </>;
}
