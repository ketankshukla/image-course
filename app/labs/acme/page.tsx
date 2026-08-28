import type { Metadata } from "next";
import AcmeCollection from "./AcmeCollection";
import "../filepilot/lab.css";
import "../filepilot/missions.css";

export const metadata: Metadata = { title: "Acme — 30 Agent Mission Labs | Visual Library", description: "Practise trustworthy answers, reliable agent coordination, and safe operation through thirty fictional business-agent investigations." };
export default function Page() { return <AcmeCollection />; }
