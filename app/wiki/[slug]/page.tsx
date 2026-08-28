import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { wikiEntries, wikiPath, wikiUrl, courseUrl } from "@/lib/wiki";

export const dynamicParams = false;
export function generateStaticParams() { return wikiEntries.map(e=>({slug:e.slug})); }
type Props={params:Promise<{slug:string}>};
export async function generateMetadata({params}:Props):Promise<Metadata> {
  const {slug}=await params;
  const entry=wikiEntries.find(e=>e.slug===slug);
  if(!entry) return {};
  return {title:entry.title,description:entry.definition,alternates:{canonical:wikiUrl(slug)}};
}
export default async function WikiArticle({params}:Props) {
  const {slug}=await params;
  const entry=wikiEntries.find(e=>e.slug===slug);
  if(!entry) notFound();
  return <main id="wiki-content" className="wiki-main wiki-article"><nav aria-label="Breadcrumb"><a href={wikiPath()}>All concepts</a><span> / {entry.category}</span></nav><p className="wiki-eyebrow">{entry.category}</p><h1>{entry.title}</h1><section className="wiki-note"><h2>At a glance</h2><p>{entry.definition}</p></section><h2>What this means</h2><p>{entry.explanation}</p><h2>Follow the idea</h2><ol className="wiki-flow" aria-label={`${entry.title}: illustrative flow`}>{entry.flow.map((step,i)=><li key={step}><span>{String(i+1).padStart(2,"0")}</span>{step}</li>)}</ol><p className="wiki-caption">A simplified teaching flow—not a complete protocol specification.</p><h2>A practical example</h2><p>{entry.example}</p><div className="wiki-note"><h2>A mistake to avoid</h2><p>{entry.mistake}</p></div><h2>Check your understanding</h2><p>{entry.question}</p><details><summary>Show an explanation</summary><p>{entry.answer}</p></details><h2>Connect it to your projects</h2><p>Explore these fictional case studies and their mission exercises. The connections below are learning suggestions, not claims that the labs run real agents or integrations.</p><div className="wiki-grid">{entry.projects.map(id=><div className="wiki-card" key={id}><h3>{id==="filepilot"?"FilePilot":id==="acme"?"Acme":"Hospital / HarborCare"}</h3><p><a href={`${courseUrl}/#course=${id}&chapter=1`}>Read the case study ↗</a></p><a href={`${courseUrl}/labs/${id}`}>Explore its mission labs ↗</a></div>)}</div><h2>Related concepts</h2><div className="wiki-related">{entry.related.map(id=>{const related=wikiEntries.find(e=>e.slug===id)!;return <a href={wikiPath(id)} key={id}>{related.title} →</a>;})}</div>{entry.source?<p className="wiki-caption">Further reading: <a href={entry.source}>Original documentation ↗</a>. Protocol details can change; check the applicable version before implementing.</p>:null}<p className="wiki-caption">Reference edition · reviewed 27 August 2026</p><a href={wikiPath()}>← Back to all concepts</a></main>;
}
