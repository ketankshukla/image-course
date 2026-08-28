import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { randomUUID } from 'node:crypto';
import { pathToFileURL } from 'node:url';
import { searchLessons, parseLimit } from './search.mjs';

export function makeServer(log = console.log) {
  return createServer(async (req, res) => {
    const url = new URL(req.url, 'http://127.0.0.1');
    if (req.method !== 'GET') { res.writeHead(405).end(); return; }
    if (url.pathname === '/') {
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.end(await readFile(new URL('./index.html', import.meta.url)));
      return;
    }
    if (url.pathname !== '/api/search') { res.writeHead(404).end(); return; }
    const requestId = randomUUID();
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Cache-Control', 'no-store');
    res.setHeader('X-Request-ID', requestId);
    try {
      const query = url.searchParams.get('q') ?? '';
      const limit = parseLimit(url.searchParams.get('limit'));
      const results = searchLessons(query, limit);
      log(JSON.stringify({ requestId, route: '/api/search', limit, count: results.length, status: 200 }));
      res.end(JSON.stringify({ requestId, results }));
    } catch (error) {
      log(JSON.stringify({ requestId, route: '/api/search', status: 400 }));
      res.writeHead(400).end(JSON.stringify({ requestId, error: error.message }));
    }
  });
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  makeServer().listen(4174, '127.0.0.1', () => console.log('Debug Lab: http://127.0.0.1:4174'));
}
