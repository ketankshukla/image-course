"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import MissionScenario from "@/app/components/MissionScenario";
import { hospitalMissions } from "@/lib/hospital-missions";

export default function HospitalCollection() {
  const [selected, setSelected] = useState(1);
  useEffect(() => {
    const read = () => { const n = Number(new URLSearchParams(location.hash.slice(1)).get("mission")); setSelected(hospitalMissions.some(m => m.id === n) ? n : 1); };
    read(); window.addEventListener("hashchange", read);
    return () => window.removeEventListener("hashchange", read);
  }, []);
  const mission = hospitalMissions.find(m => m.id === selected) ?? hospitalMissions[0];
  return <>
    <nav className="fp-mission-nav" aria-label="Hospital missions"><div><strong>HarborCare · 30 hospital privacy mission labs</strong><p>Synthetic records and fictional policies only. These exercises do not provide clinical or legal advice, establish compliance, or govern real patient care. No real records or services are connected. Switching missions resets the exercise; no persistent progress is tracked.</p><p><Link href="/labs/acme">Acme agent labs</Link> · <Link href="/labs/filepilot">FilePilot automation labs</Link></p>{["01–10 · Establish access", "11–20 · Difficult sharing decisions", "21–30 · Investigate, recover & review"].map((label, group) => <details key={label} open={Math.floor((selected - 1) / 10) === group} className="fp-mission-group"><summary>{label}</summary><div className="fp-mission-links">{hospitalMissions.filter(m => Math.floor((m.id - 1) / 10) === group).map(m => <a key={m.id} href={`#mission=${m.id}`} aria-current={selected === m.id ? "page" : undefined}>{String(m.id).padStart(2, "0")} · {m.title}</a>)}</div></details>)}</div></nav>
    <MissionScenario key={mission.id} mission={mission} collectionTitle="HarborCare" caseStudyId="hospital" total={hospitalMissions.length} />
  </>;
}
