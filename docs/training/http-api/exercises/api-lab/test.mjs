import test from 'node:test';
import assert from 'node:assert/strict';
import {once} from 'node:events';
import {makeServer} from './server.mjs';
test('HTTP contract across seven request scenarios',async()=>{
  const s=makeServer(); s.listen(0,'127.0.0.1'); await once(s,'listening');
  const base=`http://127.0.0.1:${s.address().port}`;
  try {
    let r=await fetch(base+'/lessons?limit=1'); assert.equal(r.status,200); assert.equal((await r.json()).items.length,1);
    r=await fetch(base+'/lessons?limit=0'); assert.equal(r.status,400);
    r=await fetch(base+'/lessons',{method:'POST',body:'plain'}); assert.equal(r.status,415);
    const post=body=>fetch(base+'/lessons',{method:'POST',headers:{'Content-Type':'application/json'},body});
    r=await post('{'); assert.equal(r.status,400);
    r=await post(JSON.stringify({title:'FilePilot'})); assert.equal(r.status,201); assert.equal((await r.json()).title,'FilePilot');
    r=await post(JSON.stringify({title:'FilePilot'})); assert.equal(r.status,409);
    r=await fetch(base+'/lessons',{method:'DELETE'}); assert.equal(r.status,405); assert.equal(r.headers.get('allow'),'GET, POST');
  } finally {s.closeAllConnections();await new Promise(resolve=>s.close(resolve));}
});
