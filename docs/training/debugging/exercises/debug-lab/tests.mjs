import test from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { searchLessons, parseLimit } from './search.mjs';
import { makeServer } from './server.mjs';

test('lowercase query finds FilePilot', () => assert.equal(searchLessons('filepilot')[0].title, 'FilePilot'));
test('mixed-case query finds FilePilot', () => assert.equal(searchLessons('FilePilot').length, 1));
test('surrounding spaces are ignored', () => assert.equal(searchLessons(' filepilot ').length, 1));
test('unknown title returns no results', () => assert.deepEqual(searchLessons('not-a-lesson'), []));
test('absent limit defaults to ten', () => assert.equal(parseLimit(null), 10));
test('zero limit remains zero', () => assert.equal(parseLimit('0'), 0));
test('negative limit is rejected', () => assert.throws(() => parseLimit('-1')));
test('HTTP preserves case-insensitive search and zero limit', async () => {
  const server = makeServer(() => {});
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  try {
    const base = `http://127.0.0.1:${server.address().port}`;
    const a = await fetch(base + '/api/search?q=FilePilot&limit=10');
    assert.equal(a.status, 200);
    const data = await a.json();
    assert.equal(data.requestId, a.headers.get('x-request-id'));
    assert.equal(data.results.length, 1);
    const b = await fetch(base + '/api/search?q=filepilot&limit=0');
    assert.deepEqual((await b.json()).results, []);
    const bad = await fetch(base + '/api/search?limit=-1');
    assert.equal(bad.status, 400);
  } finally {
    server.closeAllConnections();
    await new Promise(resolve => server.close(resolve));
  }
});
