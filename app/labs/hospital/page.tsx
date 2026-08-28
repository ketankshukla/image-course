import type { Metadata } from "next";
import HospitalCollection from "./HospitalCollection";
import "../filepilot/lab.css";
import "../filepilot/missions.css";

export const metadata: Metadata = { title: "HarborCare — 30 Hospital Privacy Labs | Visual Library", description: "Thirty fictional hospital privacy investigations using synthetic records, scoped access decisions, and reviewable sharing workflows." };
export default function Page() { return <HospitalCollection />; }
