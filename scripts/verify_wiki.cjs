const fs = require('node:fs');
const assert = require('node:assert/strict');
const ts = require('typescript');
const {NextRequest} = require('next/server');
const entries = JSON.parse(fs.readFileSync('data/wiki.json','utf8'));
const ids = new Set(entries.map(e=>e.slug));
assert.equal(ids.size,entries.length);
assert.equal(entries.length,20);
for(const entry of entries){
  assert(/^[a-z0-9-]+$/.test(entry.slug));
  for(const field of ['title','category','definition','explanation','example','mistake','question','answer']) assert(entry[field]?.length > 3,field);
  assert.equal(entry.flow.length,3);
  for(const id of entry.related) assert(ids.has(id),id);
  for(const id of entry.projects) assert(['filepilot','acme','hospital'].includes(id));
  if(entry.source) assert.equal(new URL(entry.source).protocol,'https:');
}
const compiled=ts.transpileModule(fs.readFileSync('middleware.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS}}).outputText;
const mod={exports:{}};
new Function('require','module','exports',compiled)(require,mod,mod.exports);
const middleware=mod.exports.middleware;
const checks=[
 ['https://wiki.ketanshukla.dev/','x-middleware-rewrite','https://wiki.ketanshukla.dev/wiki'],
 ['https://wiki.ketanshukla.dev/rag?q=test','x-middleware-rewrite','https://wiki.ketanshukla.dev/wiki/rag?q=test'],
 ['https://wiki.ketanshukla.dev/wiki/rag?q=test','location','https://wiki.ketanshukla.dev/rag?q=test'],
 ['https://course.ketanshukla.dev/wiki','location','https://wiki.ketanshukla.dev/'],
 ['https://course.ketanshukla.dev/wiki/rag','location','https://wiki.ketanshukla.dev/rag'],
 ['https://wiki.ketanshukla.dev/how-to-use','location','https://course.ketanshukla.dev/how-to-use'],
 ['https://course.ketanshukla.dev/','x-middleware-next','1'],
 ['https://course.ketanshukla.dev/labs/filepilot','x-middleware-next','1'],
 ['https://ketanshukla.dev/','x-middleware-next','1'],
 ['http://localhost:3023/wiki/rag','x-middleware-next','1'],
 ['https://wiki.ketanshukla.dev.evil.example/','x-middleware-next','1'],
];
for(const [url,header,expected] of checks) assert.equal(middleware(new NextRequest(url)).headers.get(header),expected,url);
assert.equal(middleware(new NextRequest('http://localhost:3023/wiki/rag', {headers:{host:'course.ketanshukla.dev'}})).headers.get('location'),'https://wiki.ketanshukla.dev/rag');
const matcher=new RegExp('^'+mod.exports.config.matcher[0]+'$');
for(const path of ['/_next/static/test.js','/_next/image','/library/images/test.webp','/api/test','/favicon.ico']) assert(!matcher.test(path),path);
console.log('PASS: 20 entries, related links, case-study IDs, 11 routing cases, asset/API exclusions.');
