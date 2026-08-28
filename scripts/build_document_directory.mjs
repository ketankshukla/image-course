// Local-only catalogue: includes unpublished maintenance documents, not a publication allowlist.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import MarkdownIt from 'markdown-it';
import assert from 'node:assert/strict';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const docs = path.join(root, 'docs');
const md = new MarkdownIt({html: false});
const slash = p => p.split(path.sep).join('/');
const read = p => fs.readFile(p, 'utf8').then(s => s.replace(/^\uFEFF/, ''));
const exists = async p => { try { await fs.access(p); return true; } catch { return false; } };
const escape = s => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const clean = s => s.replace(/!\[[^\]]*\]\([^)]*\)/g, '').replace(/\[([^\]]+)\]\([^)]*\)/g, '$1').replace(/[*`_]/g, '').replace(/\s+/g, ' ').trim();
const shorten = (s, n = 400) => s.length <= n ? s : s.slice(0, n).replace(/\s+\S*$/, '') + '…';
const href = p => slash(path.relative(docs, p)).split('/').map(encodeURIComponent).join('/');
async function walk(dir) {
  const entries = await fs.readdir(dir, {withFileTypes:true});
  const out = [];
  for (const e of entries.sort((a,b) => a.name.localeCompare(b.name))) {
    if (e.name.startsWith('.') || e.name === '__pycache__') continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...await walk(p)); else out.push(p);
  }
  return out;
}
const published = new Map();
for (const file of (await walk(docs)).filter(p => path.basename(p) === 'collection.json')) {
  const c = JSON.parse(await read(file));
  for (const section of c.sections) for (const d of section.documents) {
    published.set(path.resolve(path.dirname(file), d.file), {id:c.id, number:d.id});
  }
}
const courseConfig = JSON.parse(await read(path.join(root, 'data/courses.config.json')));
const groups = [
  ['orientation', 'Start here — workspace guides', 'Understand the repository and how documents become website articles.'],
  ['training', 'Hands-on engineering workshops', 'Practice team workflows, acceptance testing, GitHub Actions, staging and controlled releases.'],
  ['acme', 'Acme — business operations', 'A coherent customer-service case: evidence, specialist agents, approvals and controlled actions.'],
  ['hospital', 'HarborCare — privacy-first coordination', 'A synthetic hospital discharge scenario with recipient-specific information sharing.'],
  ['filepilot', 'FilePilot — safe file automation', 'A proposed local assistant for finding and organizing files through approved, recoverable operations.'],
  ['evidence-desk', 'EvidenceDesk — five layers of AI engineering', 'Deep lessons in prompt, context, harness, loop and graph engineering, with a Next.js/Python capstone and manual build workbook.'],
  ['planning', 'Planning & reading-style references', 'Roadmaps, production plans and the blue reading-style sample. Historical plans are not current implementation status.'],
  ['maintenance', 'Authoring & verification references', 'Templates, prompt records and verification notes for maintaining the document collection.'],
  ...courseConfig.map(c => ['course-'+c.id, c.title, c.subtitle]),
  ['course-support', 'Course authoring & maintenance notes', 'Prompt libraries, roadmap notes and historical verification records accompanying the visual courses.']
].map(([id,title,description]) => ({id,title,description,items:[]}));
const groupMap = new Map(groups.map(g => [g.id,g]));
const overrides = {
  'Video Course Production Strategy.docx': ['Video Course Production Strategy', 'Plans a pilot-led route from visual teaching documents to video lessons, narration scripts, storyboards and presenter options. This is a historical planning document, not proof that videos were generated.', 'Plan a video-course pilot and distinguish production options from finished outputs.'],
  'Visual Agent Course - Volumes 1 to 10 Roadmap.docx': ['Volumes 1–10 — Complete Learning Roadmap', 'Maps the ten-volume learning progression from foundations through protocols, retrieval, security, operations and the final project blueprint. Its original completed/planned labels predate the current ten-course library.', 'Understand the curriculum sequence; use current course files for completion status.'],
  'Visual Agent Course - Volumes 4 to 10 Roadmap.docx': ['Volumes 4–10 — Future Learning Roadmap', 'The earlier proposal for seven continuation volumes covering protocols, knowledge, workflows, security, operations, product design and architecture.', 'Review the original continuation plan, not current delivery status.']
};
function purpose(p, title) {
  const s = (p+' '+title).toLowerCase();
  if (s.includes('evidence-desk/')) return 'Learn one part of the five-layer AI engineering course and apply it to the EvidenceDesk Next.js and Python capstone.';
  if (/coding-confidence\/video-fact-check/.test(s)) return 'Separate the supplied coding video\'s useful advice from factual errors, uncertain predictions, and unsupported generalizations.';
  if (/coding-confidence\/coding-with-confidence/.test(s)) return 'Plan a gradual return to coding through 12 core modules, 3 optional AI extensions, and a safe FilePilot Mini project.';
  if (/template\.html$/.test(s)) return 'Maintain HTML rendering layouts; this is a template, not a finished lesson.';
  if (/verification|verify\.md/.test(s)) return 'Review the checks and limitations recorded at authoring time; rerun current checks before release.';
  if (/prompt/.test(s)) return 'Maintain or reproduce diagram authoring; not the recommended learner starting point.';
  if (/website-roadmap/.test(s)) return 'Review a course-specific website plan; verify it against the current application before implementing.';
  if (/agents\.md/.test(s)) return 'Maintain the repository while preserving its content, build and publication rules.';
  if (/readme\.md/.test(s)) return 'Find the project overview and normal development commands.';
  if (/folder-structure/.test(s)) return 'Locate folders and understand which files belong together.';
  if (/publishing-case/.test(s)) return 'Add a case study to the website safely and verify its publication.';
  if (/reading-style/.test(s)) return 'Compare the approved blue palette, larger typography and reading treatments.';
  if (/strategy-response/.test(s)) return 'Review commentary on the original project strategy, rather than follow a build workbook.';
  if (/plain-english|legend/.test(s)) return 'Understand the end-to-end story and terminology before reading implementation details.';
  if (/manual-build.*00-start/.test(s)) return 'Choose the construction sequence and understand each workbook’s acceptance gate.';
  if (/foundations/.test(s)) return 'Begin implementation with small contracts, rules, fixtures and executable tests.';
  if (/manual-build.*mcp/.test(s)) return 'Build bounded tool interfaces and test authorization through the protocol adapter.';
  if (/manual-build.*rag/.test(s)) return 'Build document ingestion, authorized retrieval and evidence-backed answers.';
  if (/planner-and-a2a/.test(s)) return 'Implement validated organization proposals and optional specialist delegation.';
  if (/manual-build.*a2a/.test(s)) return 'Build specialist task coordination, artifact handling and failure behavior.';
  if (/manual-build.*(workflow|safe-operations)/.test(s)) return 'Implement approval-bound execution, durable records and crash recovery.';
  if (/manual-build.*(workspace|case-platform)/.test(s)) return 'Build the human-facing review interface and explain authoritative job state.';
  if (/manual-build.*production/.test(s)) return 'Prepare packaging, synthetic demonstrations, operational tests and release evidence.';
  if (/repositories|deployment/.test(s)) return 'Decide what lives in Git, what runs separately and what may be deployed.';
  if (/safety-policy|privacy-policy/.test(s)) return 'Define the safety boundary and adversarial tests before enabling consequential actions.';
  if (/hybrid/.test(s)) return 'Understand the Next.js interface and Python backend boundary.';
  if (/typescript/.test(s)) return 'Compare the alternative TypeScript implementation and its unchanged safety responsibilities.';
  if (/architecture/.test(s)) return 'Trace components, folders, ownership and calls before building the application.';
  if (/strategy/.test(s)) return 'Choose project scope, build order and the evidence a convincing demonstration needs.';
  if (/00-start-here/.test(s)) return 'Orient yourself to the case study and select the right next guide.';
  return 'Use this reference to understand the subject described below and its place in the collection.';
}
function describe(text) {
  const tokens = md.parse(text, {});
  const h1 = tokens.findIndex(t => t.type === 'heading_open' && t.tag === 'h1');
  const title = h1 >= 0 ? clean(tokens[h1+1].content) : '';
  let start = tokens.findIndex((t,i) => t.type === 'heading_open' && /at a glance/i.test(tokens[i+1]?.content || ''));
  if (start < 0) start = 0;
  let summary = '';
  for (let i=start;i<tokens.length;i++) {
    if (tokens[i].type !== 'paragraph_open') continue;
    const candidate = clean(tokens[i+1]?.content || '');
    if (candidate.length >= 90 && !/^(Module:|Role in the course:|Layout:)/.test(candidate)) { summary=shorten(candidate); break; }
  }
  const topics = tokens.filter((t,i) => i>0 && tokens[i-1].type==='heading_open' && tokens[i-1].tag!=='h1').map(t=>clean(t.content)).filter(s=>s&&!/^(At a glance|What the diagram teaches|Sources|How to present it)$/i.test(s)).slice(0,3);
  return {title, summary:summary || 'Reference material supporting the document collection.', topics};
}
const candidates = [
  ...(await walk(docs)).filter(p => /\.(md|html|docx|pdf)$/i.test(p) && !/MASTER-DOCUMENT-DIRECTORY\.(md|html)$/.test(p) && !/\/training\/[^/]+\/exercises\//.test(slash(p))),
  ...(await walk(path.join(root,'courses'))).filter(p => p.endsWith('.md')),
  path.join(root,'README.md'), path.join(root,'AGENTS.md')
];
for (const p of candidates) {
  if (p.endsWith('.html') && await exists(p.slice(0,-5)+'.md')) continue;
  const rel = slash(path.relative(root,p));
  const name = path.basename(p);
  let g = 'orientation';
  const course = courseConfig.find(c => rel.startsWith('courses/'+c.source_dir+'/'));
  if (course) g = rel.includes('/diagram-docs/') ? 'course-'+course.id : 'course-support';
  else if (/\/[^/]*assets\//.test(rel) || /\/assets\//.test(rel)) g='maintenance';
  else if (rel.includes('/case-studies/')) g = rel.split('/')[2];
  else if (rel.startsWith('docs/training/')) g = 'training';
  else if (/docs\/(general|design-samples)\//.test(rel)) g='planning';
  const item = p.endsWith('.md') ? describe(await read(p)) : {title:name,summary:'Reusable HTML layout containing placeholders and shared document structure.',topics:[]};
  item.title ||= name;
  item.purpose = purpose(rel,item.title);
  if (overrides[name]) [item.title,item.summary,item.purpose] = overrides[name];
  item.location=rel;
  item.kind=course?(g==='course-support'?'maintenance':'course'):g==='maintenance'?'maintenance':'guide';
  item.links=[{label:p.endsWith('.md')?'Markdown source':p.endsWith('.docx')?'Word document':p.endsWith('.html')?'HTML template':'PDF',url:href(p),file:p}];
  if(p.endsWith('.md') && await exists(p.slice(0,-3)+'.html')) item.links.unshift({label:'Read HTML',url:href(p.slice(0,-3)+'.html'),file:p.slice(0,-3)+'.html'});
  const pub=published.get(p);
  item.status=pub?'Published in website':course&&g!=='course-support'?'Published course lesson':'Local reference — not in website allowlist';
  if(pub) item.links.push({label:'Website reader',url:`https://course.ketanshukla.dev/#course=${pub.id}&chapter=${pub.number}`});
  if(course && g!=='course-support') {
    const number=Number(name.match(/^\d+/)?.[0]);
    assert(number, 'Missing lesson number: '+rel);
    item.links.push({label:'Website reader',url:`https://course.ketanshukla.dev/#course=${course.id}&chapter=${number}`});
    item.purpose='Study '+item.title.replace(/^Diagram\s+\d+\s*[—–-]\s*/i,'')+' through the diagram, its explanation and a worked teaching scenario.';
  }
  assert(groupMap.has(g),'Unclassified document: '+rel);
  groupMap.get(g).items.push(item);
}
groupMap.get('orientation').items.unshift({title:'Master Document Directory',summary:'The searchable local map of reading guides, course lessons, planning files and authoring references. Markdown/HTML pairs are grouped as one document.',purpose:'Find the document you need, see where it lives, and choose its reading or source edition.',location:'docs/MASTER-DOCUMENT-DIRECTORY.md',kind:'guide',status:'Local directory — not published',topics:[],links:[{label:'Read HTML',url:'MASTER-DOCUMENT-DIRECTORY.html'},{label:'Markdown source',url:'MASTER-DOCUMENT-DIRECTORY.md'}]});
const all=groups.flatMap(g=>g.items);
assert.equal(new Set(all.map(x=>x.location)).size,all.length,'Duplicate catalogue entry');
assert.equal(all.filter(x=>x.kind==='course').length,244,'Course lesson coverage');
for(const x of all) for(const link of x.links) if(link.file) assert(await exists(link.file),'Missing link '+link.file);
const counts={documents:all.length,lessons:all.filter(x=>x.kind==='course').length,other:all.filter(x=>x.kind!=='course').length};
const intro='Your blue-and-white map of the learning workspace: what each document explains, when to use it, and where to find it.';
const scope='Coverage: all Markdown documents under docs and courses; HTML reading editions paired with their Markdown sources; standalone HTML templates and Word/PDF files under docs; root README and AGENTS instructions. Course export bundles, images, code, JSON configuration and generated website files are not individual catalogue entries. This directory is local-only because it also links unpublished authoring notes. It does not publish those notes to the website.';
let markdown=`# Master Document Directory\n\n${intro}\n\n## At a glance\n\n${counts.documents} documents: ${counts.lessons} individual course lessons and ${counts.other} guides, planning documents and maintenance references. Matching HTML and Markdown files count as one document.\n\n${scope}\n\n## Choose your route\n\n- New to the workspace: start with the folder guide and the plain-English case-study explanations.\n- Ready to build: choose a case study, read its architecture, then follow its manual-build series.\n- Learning one concept: browse the numbered course sections below.\n- Maintaining content: use publishing instructions, templates and verification references.\n\nLocations below are relative to the image-course repository root. Links are relative to this document, so moving the entire repository preserves navigation. Historical roadmaps and verification notes are not claims about current implementation or deployment.\n\n## Directory sections\n\n${groups.map(g=>`- [${g.title}](#${g.id}) — ${g.items.length} documents`).join('\n')}\n`;
let htmlGroups='';
for(const g of groups) {
  markdown+=`\n<a id="${g.id}"></a>\n\n## ${g.title}\n\n${g.description}\n`;
  let cards='';
  for(const x of g.items) {
    markdown+=`\n### ${x.title}\n\n${x.summary}\n\n**Use it for:** ${x.purpose}\n\n**Location:** \`${x.location}\`\n\n**Availability:** ${x.status}\n\n${x.links.map(l=>`[${l.label}](${l.url})`).join(' · ')}\n`;
    if(x.topics.length) markdown+=`\n**Inside:** ${x.topics.join(' · ')}\n`;
    cards+=`<article class="document" data-kind="${x.kind}"><div class="eyebrow">${escape(x.status)}</div><h3>${escape(x.title)}</h3><p>${escape(x.summary)}</p><p class="purpose"><strong>Use it for</strong> ${escape(x.purpose)}</p>${x.topics.length?`<p class="topics"><strong>Inside</strong> ${escape(x.topics.join(' · '))}</p>`:''}<details class="location" open><summary>Location &amp; formats</summary><code>${escape(x.location)}</code><div class="links">${x.links.map(l=>`<a href="${escape(l.url)}">${escape(l.label)}</a>`).join('')}</div></details></article>`;
  }
  htmlGroups+=`<details class="collection" id="${g.id}"${g.id==='orientation'?' open':''}><summary><span>${escape(g.title)}</span><span class="count">${g.items.length} documents</span></summary><div class="collection-body"><p class="description">${escape(g.description)}</p>${cards}</div></details>`;
}
markdown+='\n## Keep this directory current\n\nRun `node scripts/build_document_directory.mjs` from the repository root after adding or moving documents. Run it with `--check` to verify coverage, links and that both editions match the current inventory. The directory reads source introductions and headings; it does not certify the correctness of every document. Its generated Markdown and HTML should be updated through the builder rather than edited separately.\n';
const css=await read(path.join(docs,'assets/directory.css'));
const html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Master Document Directory | Visual Learning Library</title><style>${css}</style></head><body><a class="skip" href="#content">Skip to directory</a><aside><a class="brand" href="#content">VISUAL LEARNING LIBRARY</a><h2>Your document<br>compass.</h2><p>One place to find the right guide.</p><nav aria-label="Directory sections">${groups.map(g=>`<a href="#${g.id}">${escape(g.title)} <span>${g.items.length}</span></a>`).join('')}</nav></aside><main id="content"><header><div class="eyebrow">THE MASTER DIRECTORY</div><h1>A place for every<br>document.</h1><p>${intro}</p><div class="stats"><div><strong>${counts.documents}</strong><span>documents catalogued</span></div><div><strong>10</strong><span>visual courses</span></div><div><strong>3</strong><span>practical case studies</span></div></div></header><section class="welcome"><h2>What do you want to do?</h2><div class="routes"><a href="#orientation"><strong>Find my way</strong><span>Folders, formats &amp; publishing</span></a><a href="#acme"><strong>Build a project</strong><span>Acme, HarborCare &amp; FilePilot</span></a><a href="#course-01"><strong>Learn a concept</strong><span>244 individual visual lessons</span></a></div><div class="key"><strong>One document. More than one format.</strong><p>Choose <b>Read HTML</b> for the designed reading edition, <b>Markdown source</b> to edit, or <b>Website reader</b> for a published article. Exact locations are shown relative to the repository root.</p></div></section><section class="finder" aria-label="Find a document"><label for="query">Find your next document</label><div class="fields"><input id="query" type="search" placeholder="Try privacy, FilePilot, MCP, architecture…"><select id="kind" aria-label="Document type"><option value="all">All document types</option><option value="guide">Guides &amp; planning</option><option value="course">Course lessons</option><option value="maintenance">Maintenance references</option></select><button id="clear" type="button">Clear</button></div><div class="actions"><p id="result" role="status" aria-live="polite">${counts.documents} documents available</p><button id="expand" type="button">Expand all</button><button id="collapse" type="button">Collapse all</button></div></section><p class="scope">${scope}</p><div id="catalogue">${htmlGroups}</div><p id="empty" hidden>No documents match. Try a broader topic or clear the filters.</p><footer><h2>Made to grow with your library.</h2><p>Refresh both editions with <code>node scripts/build_document_directory.mjs</code>. Check coverage and links with <code>node scripts/build_document_directory.mjs --check</code>.</p><p>Descriptions are drawn from source introductions and headings, with purpose notes. Historical planning and verification documents are not current implementation claims. Nothing is deployed by rebuilding this local directory.</p><a href="MASTER-DOCUMENT-DIRECTORY.md">Open the complete Markdown directory</a></footer></main><script>
const query=document.getElementById('query'),kind=document.getElementById('kind'),collections=[...document.querySelectorAll('.collection')],cards=[...document.querySelectorAll('.document')];
const searchText=new Map(cards.map(c=>[c,c.textContent.toLowerCase()]));
function filter(){const words=query.value.toLowerCase().trim().split(/\\s+/).filter(Boolean);let n=0;for(const c of cards){c.hidden=!(words.every(w=>searchText.get(c).includes(w))&&(kind.value==='all'||c.dataset.kind===kind.value));if(!c.hidden)n++;}for(const s of collections){s.hidden=![...s.querySelectorAll('.document')].some(c=>!c.hidden);s.open=(words.length>0||kind.value!=='all')?!s.hidden:s.id==='orientation';}document.getElementById('result').textContent=n+' of '+cards.length+' documents';document.getElementById('empty').hidden=n!==0;}
query.addEventListener('input',filter);kind.addEventListener('change',filter);document.getElementById('clear').addEventListener('click',()=>{query.value='';kind.value='all';filter();query.focus();});document.getElementById('expand').addEventListener('click',()=>collections.forEach(s=>{if(!s.hidden)s.open=true;}));document.getElementById('collapse').addEventListener('click',()=>collections.forEach(s=>s.open=false));
function reveal(){const s=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(s&&s.classList.contains('collection')){if(s.hidden){query.value='';kind.value='all';filter();}s.open=true;}}
document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{const s=document.getElementById(a.hash.slice(1));if(s&&s.classList.contains('collection')){if(s.hidden){query.value='';kind.value='all';filter();}s.open=true;}}));window.addEventListener('hashchange',reveal);reveal();
</script></body></html>`;
for(const [name,body] of [['MASTER-DOCUMENT-DIRECTORY.md',markdown],['MASTER-DOCUMENT-DIRECTORY.html',html]]) {
  const target=path.join(docs,name);
  if(process.argv.includes('--check')) assert.equal(await read(target),body,'Directory is stale: '+name);
  else {await fs.writeFile(target+'.next',body);await fs.rename(target+'.next',target);}
}
console.log(`PASS: ${counts.documents} documents, ${counts.lessons} course lessons, ${groups.length} sections; paired editions and local links verified.`);
