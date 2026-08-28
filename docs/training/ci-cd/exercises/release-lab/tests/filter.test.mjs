import test from 'node:test';
import assert from 'node:assert/strict';
import { filterLessons } from '../dist/filter.js';

const lessons = [
  { title: 'MCP foundations', category: 'course' },
  { title: 'FilePilot', category: 'case-study' },
  { title: 'HarborCare', category: 'case-study' }
];
test('all shows every lesson', () => {
  assert.deepEqual(filterLessons(lessons, 'all'), lessons);
});
test('case-study excludes courses', () => {
  assert.deepEqual(filterLessons(lessons, 'case-study').map(x => x.title), ['FilePilot', 'HarborCare']);
});
test('course excludes case studies', () => {
  assert.deepEqual(filterLessons(lessons, 'course').map(x => x.title), ['MCP foundations']);
});
test('empty input stays empty', () => {
  assert.deepEqual(filterLessons([], 'case-study'), []);
});
test('filtering does not change the original array', () => {
  const copy = structuredClone(lessons);
  filterLessons(copy, 'case-study');
  assert.deepEqual(copy, lessons);
});
