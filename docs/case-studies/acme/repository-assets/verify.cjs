const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const stem = path.join(root, 'REPOSITORIES-AND-DEPLOYMENT');
const html = fs.readFileSync(stem + '.html', 'utf8');
const md = fs.readFileSync(stem + '.md', 'utf8');
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(x => x[1]);
if (ids.length !== new Set(ids).size) throw Error('Duplicate IDs');
for (const a of html.matchAll(/href="#([^"]+)"/g)) {
  if (!ids.includes(a[1])) throw Error('Missing anchor: ' + a[1]);
}
const images = [...html.matchAll(/<img[^>]*src="([^"]+)"/g)];
const sources = [...md.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)];
if (images.length !== 2 || sources.length !== 2) throw Error('Image count');
images.forEach((image, i) => {
  const src = image[1];
  if (!src.startsWith('data:image/svg+xml')) throw Error('Not embedded SVG');
  const comma = src.indexOf(',');
  const bytes = src.slice(0, comma).includes(';base64')
    ? Buffer.from(src.slice(comma + 1), 'base64')
    : Buffer.from(decodeURIComponent(src.slice(comma + 1)));
  if (!bytes.equals(fs.readFileSync(path.join(root, sources[i][1])))) throw Error('Image differs');
});
if (/<(?:script|link)[^>]*(?:src|href)=/i.test(html)) throw Error('External dependency');
for (const script of html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)) new vm.Script(script[1]);
if ([...md.matchAll(/^## \d+\./gm)].length !== 15) throw Error('Chapter count');
if ((md.match(/```/g) || []).length % 2) throw Error('Unclosed fence');
console.log('PASS: 15 chapters; 2 byte-identical embedded SVG diagrams; valid navigation; self-contained assets; valid script syntax; ' + md.split(/\s+/).length + ' words');
