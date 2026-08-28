const assert = require('node:assert/strict');
const fs = require('node:fs');
const ts = require('typescript');
const Module = require('node:module');
const path = require('node:path');
const filename = path.resolve(__dirname, '../lib/filepilot-missions.ts');
const output = ts.transpileModule(fs.readFileSync(filename, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS } });
const loaded = new Module(filename, module);
loaded._compile(output.outputText, filename);
const { missions, advanceMission } = loaded.exports;
assert.deepEqual(missions.map(m => m.id), [2,3,4,5,6,7,8,9,10]);
let total = 0;
for (const mission of missions) {
  const visited = new Set();
  const queue = ['start'];
  while (queue.length) {
    const key = queue.shift();
    if (visited.has(key)) continue;
    visited.add(key);
    const state = mission.steps[key];
    assert.ok(state, `${mission.id}: missing ${key}`);
    assert.ok(state.evidence.length && state.explanation);
    assert.equal(new Set(state.actions.map(a=>a.label)).size, state.actions.length);
    if (state.complete) assert.equal(state.actions.length, 0);
    else assert.ok(state.actions.length);
    for (const a of state.actions) {
      assert.equal(advanceMission(mission, key, a.next), a.next);
      queue.push(a.next);
    }
  }
  assert.equal(visited.size, Object.keys(mission.steps).length, 'Unreachable state');
  assert.ok(visited.has('done'));
  assert.throws(() => advanceMission(mission, 'start', 'done'));
  assert.throws(() => advanceMission(mission, 'done', 'start'));
  // Every state must have a path to completion, including blocked choices.
  for (const origin of visited) {
    const pending = [origin], seen = new Set();
    while (pending.length) {
      const key = pending.shift();
      if (seen.has(key)) continue;
      seen.add(key);
      pending.push(...mission.steps[key].actions.map(a=>a.next));
    }
    assert.ok(seen.has('done'), `${mission.id}/${origin} is a dead end`);
  }
  total += visited.size;
}
console.log(`PASS: ${missions.length} missions, ${total} states, all branches reachable and recoverable; completion cannot be skipped from start.`);
