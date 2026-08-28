import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
const files = new Map([
  ['/', ['dist/index.html', 'text/html; charset=utf-8']],
  ['/app.js', ['dist/app.js', 'text/javascript; charset=utf-8']],
  ['/filter.js', ['dist/filter.js', 'text/javascript; charset=utf-8']]
]);
createServer(async (req, res) => {
  const entry = files.get(new URL(req.url, 'http://127.0.0.1').pathname);
  if (!entry) { res.writeHead(404).end('Not found'); return; }
  try {
    const body = await readFile(entry[0]);
    res.writeHead(200, { 'Content-Type': entry[1] }).end(body);
  } catch { res.writeHead(500).end('Run npm run build first.'); }
}).listen(4173, '127.0.0.1', () => console.log('Release Lab: http://127.0.0.1:4173'));
