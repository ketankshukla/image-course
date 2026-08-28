import test from 'node:test';
import assert from 'node:assert/strict';
import { mayExecute, executePlan } from '../policy.mjs';
import { fixture } from './fixtures.mjs';

test('valid approval permits this plan before expiry', () => {
  const { plan, approval, now } = fixture();
  assert.equal(mayExecute(plan, approval, now), true);
});
test('boolean false denies execution', () => {
  const { plan, approval, now } = fixture();
  approval.approved = false;
  assert.equal(mayExecute(plan, approval, now), false);
});
test('text false is not approval', () => {
  const { plan, approval, now } = fixture();
  approval.approved = 'false';
  assert.equal(mayExecute(plan, approval, now), false);
});
test('missing approval denies execution', () => {
  const { plan, now } = fixture();
  assert.equal(mayExecute(plan, null, now), false);
});
test('approval for another plan is rejected', () => {
  const { plan, approval, now } = fixture();
  approval.planId = 'another-plan';
  assert.equal(mayExecute(plan, approval, now), false);
});
test('past expiry is rejected', () => {
  const { plan, approval } = fixture();
  assert.equal(mayExecute(plan, approval, 2001), false);
});
test('exact expiry is rejected', () => {
  const { plan, approval } = fixture();
  assert.equal(mayExecute(plan, approval, 2000), false);
});
test('denied text approval never calls the move adapter', async () => {
  const { plan, approval, now } = fixture();
  approval.approved = 'false';
  const calls = [];
  const result = await executePlan(plan, approval, { now, move: async (...args) => calls.push(args) });
  assert.deepEqual({ result, calls }, { result: { status: 'denied' }, calls: [] });
});
test('adapter failure is not reported as completion', async () => {
  const { plan, approval, now } = fixture();
  await assert.rejects(executePlan(plan, approval, {
    now, move: async () => { throw new Error('simulated adapter failure'); }
  }), /simulated adapter failure/);
});
test('permission check does not mutate its inputs', () => {
  const { plan, approval, now } = fixture();
  const before = structuredClone({ plan, approval });
  mayExecute(plan, approval, now);
  assert.deepEqual({ plan, approval }, before);
});
test('service and in-memory adapter transfer the expected content', async () => {
  const { plan, approval, now } = fixture();
  const files = new Map([[plan.source, 'synthetic lesson notes']]);
  const calls = [];
  const move = async (source, destination) => {
    calls.push([source, destination]);
    if (!files.has(source) || files.has(destination)) throw new Error('invalid fake move');
    files.set(destination, files.get(source));
    files.delete(source);
  };
  const result = await executePlan(plan, approval, { now, move });
  assert.deepEqual(result, { status: 'completed' });
  assert.deepEqual(calls, [[plan.source, plan.destination]]);
  assert.equal(files.has(plan.source), false);
  assert.equal(files.get(plan.destination), 'synthetic lesson notes');
});
