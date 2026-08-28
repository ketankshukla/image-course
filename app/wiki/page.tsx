import type { Metadata } from "next";
import Link from "next/link";
import { wikiEntries, wikiUrl } from "@/lib/wiki";
import WikiSearch from "./WikiSearch";

export const metadata: Metadata = { alternates: { canonical: wikiUrl() } };

export default function WikiHome() {
  return <main id="wiki-content" className="wiki-main"><p className="wiki-eyebrow">YOUR CONNECTED REFERENCE SHELF</p><h1>One idea. Many places it fits.</h1><p className="wiki-lead">Understand a term, follow its visual flow, then recognize it in a real project design.</p><div className="wiki-note"><strong>New here?</strong> Courses teach in sequence. Case studies connect the pieces. Labs let you practise. This wiki helps you understand an unfamiliar idea without starting another course.</div><WikiSearch entries={wikiEntries.map(({slug,title,category,definition})=>({slug,title,category,definition}))}/><section className="wiki-note"><h2>Three ways to explore</h2><p>Start with <Link prefetch={false} href="/wiki/mcp">MCP</Link>, <Link prefetch={false} href="/wiki/rag">RAG</Link>, and <Link prefetch={false} href="/wiki/a2a">A2A</Link> to distinguish tools, evidence, and teamwork. Follow the related concepts on any entry, or use the search above to find a particular problem.</p><p>The search on this page covers wiki entries. The <a href="https://course.ketanshukla.dev">library search</a> covers course and guide articles. They are separate indexes.</p></section></main>;
}
