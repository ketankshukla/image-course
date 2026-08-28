import test from 'node:test';
import assert from 'node:assert/strict';
import { mayExecute } from '../policy.mjs';
import { fixture } from './fixtures.mjs';
test('WEAK: permission function returns a boolean', () => {
  const { plan, approval, now } = fixture();
  approval.approved = 'false';
  assert.equal(typeof mayExecute(plan, approval, now), 'boolean');
});
