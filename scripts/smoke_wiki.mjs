import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import http from 'node:http';
const entries=JSON.parse(await fs.readFile(new URL('../data/wiki.json',import.meta.url),'utf8'));
const origin=process.argv[2] || 'http://localhost:3023';
const live=origin==='https://wiki.ketanshukla.dev';
const prefix=live?'':'/wiki';
// Node fetch can normalize Host. Use HTTP for explicit local hostname simulation.
const get=(path,host)=>host?new Promise((resolve,reject)=>{
  const request=http.get(origin+path,{headers:{host}},response=>{
    let body='';response.setEncoding('utf8');response.on('data',chunk=>body+=chunk);
    response.on('end',()=>resolve({status:response.statusCode,headers:{get:name=>response.headers[name]},text:async()=>body}));
  });
  request.setTimeout(20000,()=>request.destroy(new Error('Request timed out')));
  request.on('error',reject);
}):fetch(origin+path,{redirect:'manual',signal:AbortSignal.timeout(20000)});
let home=await get(prefix || '/');
assert.equal(home.status,200);
assert((await home.text()).includes('One idea. Many places it fits.'));
for(const entry of entries){
  const response=await get(`${prefix}/${entry.slug}`);
  assert.equal(response.status,200,entry.slug);
  const html=await response.text();
  assert(html.includes(`href="https://wiki.ketanshukla.dev/${entry.slug}"`),`${entry.slug} canonical`);
  assert(html.includes('Check your understanding'),entry.slug);
  assert(html.includes('Follow the idea'),entry.slug);
}
assert.equal((await get(`${prefix}/not-a-real-concept`)).status,404);
const redirect=live?await get('/wiki/rag?q=test'):await get('/wiki/rag?q=test','course.ketanshukla.dev');
assert.equal(redirect.status,308);
assert.equal(new URL(redirect.headers.get('location'),live?origin:'https://wiki.ketanshukla.dev').href,'https://wiki.ketanshukla.dev/rag?q=test');
if(!live){
  const rewrite=await get('/rag','wiki.ketanshukla.dev');
  assert.equal(rewrite.status,200);
  assert((await rewrite.text()).includes('RAG — Retrieval-Augmented Generation'));
  const course=await get('/','course.ketanshukla.dev');
  assert.equal(course.status,200);
  assert((await course.text()).includes('Visual Agent Learning Library'));
}
console.log(`PASS: ${origin}: home, 20 entries, canonicals, missing-entry 404, canonical redirect${live?'':', host rewrite and course isolation'}.`);
