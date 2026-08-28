// Verify both intentional failure and corrected behavior without editing the starter.
import { mkdtemp, cp, readFile, writeFile, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import assert from 'node:assert/strict';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const starter = path.join(root, 'docs/training/ci-cd/exercises/release-lab');
const scratch = await mkdtemp(path.join(os.tmpdir(), 'cicd-training-'));
const compiler = path.join(root, 'node_modules/typescript/bin/tsc');
function run(args) {
  const result = spawnSync(process.execPath, args, { cwd: scratch, encoding: 'utf8' });
  if (result.error) throw result.error;
  return result;
}
try {
  for (const file of ['package.json', 'tsconfig.json', 'src', 'tests']) {
    await cp(path.join(starter, file), path.join(scratch, file), { recursive: true });
  }
  let build = run([compiler, '-p', 'tsconfig.json']);
  assert.equal(build.status, 0, build.stdout + build.stderr);
  let tests = run(['--test', '--test-reporter=tap', 'tests/filter.test.mjs']);
  assert.equal(tests.status, 1, tests.stdout + tests.stderr);
  assert.match(tests.stdout, /# pass 3/);
  assert.match(tests.stdout, /# fail 2/);
  console.log('BROKEN: compilation passed; exactly 2 acceptance tests failed, 3 passed.');
  const sourcePath = path.join(scratch, 'src/filter.ts');
  const source = await readFile(sourcePath, 'utf8');
  assert.equal(source.split('return lessons;').length, 2);
  await writeFile(sourcePath, source.replace('return lessons;', "if (category === 'all') return lessons;\n  return lessons.filter(lesson => lesson.category === category);"));
  build = run([compiler, '-p', 'tsconfig.json']);
  assert.equal(build.status, 0, build.stdout + build.stderr);
  tests = run(['--test', '--test-reporter=tap', 'tests/filter.test.mjs']);
  assert.equal(tests.status, 0, tests.stdout + tests.stderr);
  assert.match(tests.stdout, /# pass 5/);
  console.log('FIXED: compilation passed; all 5 acceptance tests passed.');
  assert.equal(await readFile(path.join(starter, 'src/filter.ts'), 'utf8'), source);
  console.log('Starter remains deliberately incomplete. No cloud deployment was attempted.');
} finally {
  // Only remove this invocation's newly created, OS-owned temporary directory.
  assert.equal(path.dirname(scratch), path.resolve(os.tmpdir()));
  assert.ok(path.basename(scratch).startsWith('cicd-training-'));
  await rm(scratch, { recursive: true, force: true });
}
