import type { Metadata } from "next";
import FilePilotLab from "./FilePilotLab";
import "./lab.css";

export const metadata: Metadata = { title: "FilePilot Mission Lab | Visual Library", description: "Practise planning, approving and undoing safe file organization in a fictional sandbox." };
export default function Page() { return <FilePilotLab />; }
