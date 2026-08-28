import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dir = path.join(root, 'docs/case-studies/evidence-desk');
const manifest = JSON.parse(await fs.readFile(path.join(dir, 'collection.json'), 'utf8'));
const documents = manifest.sections.flatMap(s => s.documents);
assert.equal(documents.length, 11);
const images = new Set();
let words = 0;
for (const entry of documents) {
  const md = await fs.readFile(path.join(dir, entry.file), 'utf8');
  const html = await fs.readFile(path.join(dir, entry.file.replace('.md', '.html')), 'utf8');
  assert.equal((md.match(/^# /gm) || []).length, 1, entry.file);
  assert(md.includes('## At a glance'), entry.file);
  assert(md.includes('## What the diagram teaches'), entry.file);
  assert(md.includes('## How to present'), entry.file);
  assert(html.includes('data:image/svg+xml'), 'Missing embedded diagram: '+entry.file);
  assert(!/href="[^"#]*\.md(?:#|"|\?)/.test(html), 'Unconverted reading link');
  for (const match of md.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)) {
    await fs.access(path.join(dir, match[1])); images.add(match[1]);
  }
  words += md.split(/\s+/).length;
}
assert.equal(images.size, 9);
assert(words > 7000, 'Unexpectedly incomplete course');
// Scan current source/reading editions and generated website assets, not Git history.
const forbidden = /aish\s+reganti|aishwara\s+ganti|aishwarya\s+reganti/iu;
async function scan(folder) {
  for (const entry of await fs.readdir(folder, {withFileTypes:true})) {
    const full = path.join(folder, entry.name);
    if (entry.isDirectory()) { if (!entry.name.startsWith('.')) await scan(full); }
    else if (/\.(md|html|json|tsx?|jsx?)$/.test(entry.name)) {
      assert(!forbidden.test(await fs.readFile(full, 'utf8')), 'Named reference remains: '+full);
    }
  }
}
for (const folder of ['docs','app','data','public/library']) await scan(path.join(root, folder));
console.log(`PASS: ${documents.length} paired chapters, ${images.size} diagrams, ${words} words, no named references in current publication sources/assets.`);
