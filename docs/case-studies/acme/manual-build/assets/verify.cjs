const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const files = fs.readdirSync(root).filter(n => /^\d\d-.*\.md$/.test(n));
if (files.length !== 8) throw Error('Expected index plus seven workbooks');
let words = 0;
for (const file of files) {
  const md = fs.readFileSync(path.join(root, file), 'utf8');
  const html = fs.readFileSync(path.join(root, file.replace(/\.md$/, '.html')), 'utf8');
  const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(x => x[1]);
  if (new Set(ids).size !== ids.length) throw Error(file + ': duplicate IDs');
  for (const a of html.matchAll(/href="([^"]+)"/g)) {
    const href = a[1];
    if (href.startsWith('#') && !ids.includes(href.slice(1))) throw Error('Missing anchor ' + href);
    if (!/^(https?:|#|data:)/.test(href) && !fs.existsSync(path.resolve(root, href))) throw Error('Missing link ' + href);
  }
  const sources = [...md.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)];
  const images = [...html.matchAll(/<img[^>]*src="([^"]+)"/g)];
  if (sources.length !== images.length || !images.length) throw Error('Image count');
  images.forEach((image, i) => {
    const src = image[1], comma = src.indexOf(',');
    if (!src.startsWith('data:image/')) throw Error('Nonembedded image');
    const bytes = src.slice(0, comma).includes(';base64') ? Buffer.from(src.slice(comma + 1), 'base64') : Buffer.from(decodeURIComponent(src.slice(comma + 1)));
    if (!bytes.equals(fs.readFileSync(path.resolve(root, sources[i][1])))) throw Error('Image mismatch');
  });
  if (/<(?:script|link)[^>]*(?:src|href)=/i.test(html)) throw Error('External render dependency');
  for (const script of html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)) new vm.Script(script[1]);
  if ((md.match(/```/g) || []).length % 2) throw Error('Unclosed code fence');
  const count = md.split(/\s+/).length;
  words += count;
  console.log(file + ': PASS; ' + count + ' words; ' + images.length + ' embedded diagram');
}
const ts = require('typescript');
const web = fs.readFileSync(path.join(root, '06-CASE-PLATFORM.md'), 'utf8');
const code = web.match(/```typescript\n([\s\S]*?)```/)[1];
const js = ts.transpileModule(code, {compilerOptions: {module: ts.ModuleKind.CommonJS}}).outputText;
const context = {exports: {}, Intl, Number, TypeError};
vm.runInNewContext(js, context);
if (context.exports.formatUsdMinor(7500) !== '$75.00' || context.exports.formatUsdMinor(0) !== '$0.00') throw Error('Money formatting failed');
for (const invalid of [1.5, Number.MAX_SAFE_INTEGER + 1]) {
  let rejected = false;
  try { context.exports.formatUsdMinor(invalid); } catch { rejected = true; }
  if (!rejected) throw Error('Invalid formatting input accepted');
}
console.log('TypeScript formatting exercise: PASS');
console.log('TOTAL WORDS: ' + words);
