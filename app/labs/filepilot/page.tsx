import type { Metadata } from "next";
import MissionCollection from "./MissionCollection";
import "./lab.css";
import "./missions.css";

export const metadata: Metadata = { title: "FilePilot — 30 Mission Labs | Visual Library", description: "Thirty safe simulations and investigations covering file organization, RAG, privacy, recovery, MCP permissions, and agent teamwork." };
export default function Page() { return <MissionCollection />; }
