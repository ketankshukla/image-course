"use client";
import { useState } from "react";

type Summary = {slug:string;title:string;category:string;definition:string};
export default function WikiSearch({entries}:{entries:Summary[]}) {
  const [query,setQuery]=useState("");
  const [category,setCategory]=useState("All topics");
  const categories=["All topics",...new Set(entries.map(e=>e.category))];
  const visible=entries.filter(e=>(category==="All topics"||e.category===category)&&`${e.title} ${e.definition} ${e.category}`.toLowerCase().includes(query.trim().toLowerCase()));
  return <section aria-label="Find a wiki entry"><div className="wiki-search"><label htmlFor="wiki-query">Find a concept</label><input id="wiki-query" type="search" placeholder="Try retries, tools, evidence, or permissions…" value={query} onChange={e=>setQuery(e.target.value)}/><label htmlFor="wiki-category">Topic</label><select id="wiki-category" value={category} onChange={e=>setCategory(e.target.value)}>{categories.map(c=><option key={c}>{c}</option>)}</select></div><p role="status" className="wiki-count">{visible.length} {visible.length===1?"concept":"concepts"}{query ? ` matching “${query}”` : " to explore"}</p><div className="wiki-grid">{visible.map(e=><article className="wiki-card" key={e.slug}><p className="wiki-eyebrow">{e.category}</p><h2><a href={`/wiki/${e.slug}`}>{e.title}</a></h2><p>{e.definition}</p></article>)}</div>{visible.length===0?<div className="wiki-note"><p>No matching concepts. Try a shorter term or reset the filters.</p><button onClick={()=>{setQuery("");setCategory("All topics");}}>Show all concepts</button></div>:null}</section>;
}
