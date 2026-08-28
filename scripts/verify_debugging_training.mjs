import { mkdtemp, cp, readFile, writeFile, rm } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const source = path.join(root, 'docs/training/debugging/exercises/debug-lab');
const temp = await mkdtemp(path.join(os.tmpdir(), 'debugging-training-'));
try {
  await cp(source, temp, { recursive: true });
  const original = await readFile(path.join(temp, 'search.mjs'), 'utf8');
  function check(pass, fail) {
    const result = spawnSync(process.execPath, ['--test', '--test-reporter=tap', 'tests.mjs'], { cwd: temp, encoding: 'utf8' });
    assert.equal(result.status, fail ? 1 : 0, result.stdout + result.stderr);
    assert.match(result.stdout, new RegExp('# pass ' + pass));
    assert.match(result.stdout, new RegExp('# fail ' + fail));
    console.log(`Verified ${pass} passing / ${fail} failing tests, including HTTP integration.`);
  }
  check(5, 3);
  const firstFix = original.replace('query.trim();', 'query.trim().toLowerCase();');
  await writeFile(path.join(temp, 'search.mjs'), firstFix);
  check(6, 2);
  await writeFile(path.join(temp, 'search.mjs'), firstFix.replace('return value || 10;', 'return value;'));
  check(8, 0);
  assert.equal(await readFile(path.join(source, 'search.mjs'), 'utf8'), original);
  console.log('Starter preserved. The independent empty-limit challenge is intentionally unsolved.');
} finally {
  assert.equal(path.dirname(temp), path.resolve(os.tmpdir()));
  assert.ok(path.basename(temp).startsWith('debugging-training-'));
  await rm(temp, { recursive: true, force: true });
}
