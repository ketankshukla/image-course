import { mkdtemp, cp, readFile, writeFile, rm } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const source = path.join(root, 'docs/training/testing/exercises/testing-lab');
const temp = await mkdtemp(path.join(os.tmpdir(), 'testing-training-'));
function run(file) {
  return spawnSync(process.execPath, ['--test', '--test-reporter=tap', file], { cwd: temp, encoding: 'utf8' });
}
function strong(pass, fail) {
  const r = run('tests/policy.test.mjs');
  assert.equal(r.status, fail ? 1 : 0, r.stdout + r.stderr);
  assert.match(r.stdout, new RegExp('# pass ' + pass + '\\b'));
  assert.match(r.stdout, new RegExp('# fail ' + fail + '\\b'));
}
try {
  await cp(source, temp, { recursive: true });
  const target = path.join(temp, 'policy.mjs');
  const original = await readFile(target, 'utf8');
  assert.equal(run('tests/weak.example.mjs').status, 0);
  strong(8, 3);
  console.log('Starter: weak test passes; meaningful suite has 8 passes and 3 failures.');
  const fixA = original.replace('approval.approved &&', 'approval.approved === true &&');
  await writeFile(target, fixA);
  strong(10, 1);
  const fixed = fixA.replace('approval.expiresAt >= now', 'approval.expiresAt > now');
  await writeFile(target, fixed);
  strong(11, 0);
  console.log('After fixes: 10/1 then 11/0, as documented.');
  for (const [label, from, to] of [
    ['truthy approval', 'approval.approved === true &&', 'approval.approved &&'],
    ['inclusive expiry', 'approval.expiresAt > now', 'approval.expiresAt >= now'],
    ['wrong plan accepted', 'approval.planId === plan.id &&', 'true &&']
  ]) {
    assert.ok(fixed.includes(from));
    await writeFile(target, fixed.replace(from, to));
    const result = run('tests/policy.test.mjs');
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.match(result.stdout, /not ok/);
    console.log('Meaningful suite detects deliberate mutation: ' + label);
  }
  assert.equal(await readFile(path.join(source, 'policy.mjs'), 'utf8'), original);
  console.log('Original lab remains intentionally broken. No real file operations performed by the lab.');
} finally {
  assert.equal(path.dirname(temp), path.resolve(os.tmpdir()));
  assert.ok(path.basename(temp).startsWith('testing-training-'));
  await rm(temp, { recursive: true, force: true });
}
