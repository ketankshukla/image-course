import type { Metadata } from "next";
import MissionCollection from "./MissionCollection";
import "./lab.css";
import "./missions.css";

export const metadata: Metadata = { title: "FilePilot — 10 Mission Labs | Visual Library", description: "Ten safe simulations covering file organization, RAG, privacy, recovery, MCP permissions, and agent teamwork." };
export default function Page() { return <MissionCollection />; }
