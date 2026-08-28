import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import sharp from 'sharp';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const folder = path.join(root, 'docs/training/coding-confidence');
const outline = await fs.readFile(path.join(folder, 'CODING-WITH-CONFIDENCE.md'), 'utf8');
assert.equal((outline.match(/^### Module \d+ /gm) || []).length, 15);
const example = outline.match(/```python\n([\s\S]*?)```/)[1];
const check = spawnSync('python', ['-c', example + '\nassert [proposed_folder(x) for x in ["invoice.pdf", "SCAN.PDF", "notes.txt", "   ", None, "report.pdf.exe"]] == ["documents", "documents", "needs-review", "needs-review", "needs-review", "needs-review"]'], {encoding:'utf8'});
assert.equal(check.status, 0, check.stderr || check.error?.message);
for (const stem of ['CODING-WITH-CONFIDENCE', 'VIDEO-FACT-CHECK']) {
  const source = await fs.readFile(path.join(folder, stem+'.md'), 'utf8');
  const html = await fs.readFile(path.join(folder, stem+'.html'), 'utf8');
  assert.equal((source.match(/^# /gm) || []).length, 1);
  assert(!html.includes('file:///') && !html.includes('C:\\Users\\'));
  for (const [, href] of source.matchAll(/\]\(([^)]+)\)/g)) {
    if (/^https?:/.test(href)) continue;
    await fs.access(path.resolve(folder, href.split('#')[0]));
  }
  const ids = new Set([...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]));
  for (const [, id] of html.matchAll(/href="#([^"]+)"/g)) assert(ids.has(id), id);
  for (const [, href] of html.matchAll(/href="([^"#]+\.html)"/g)) {
    if (!/^https?:/.test(href)) await fs.access(path.resolve(folder, href));
  }
  const images = [...html.matchAll(/<img[^>]+src="([^"]+)"/g)];
  assert.equal(images.length, stem==='CODING-WITH-CONFIDENCE' ? 4 : 0);
  for (const [, src] of images) assert(src.startsWith('data:'), 'HTML image must be embedded');
}
for (const name of await fs.readdir(path.join(folder,'assets'))) {
  const asset = path.join(folder,'assets',name);
  const metadata = await sharp(asset).metadata();
  assert.equal(metadata.width,1200);
  assert(metadata.height >= 800);
}
console.log('PASS: 15-module outline, 6 Python expectations, 2 HTML editions, 4 embedded diagrams, local links and HTML anchors.');
