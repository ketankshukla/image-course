export const lessons = [
  { title: 'MCP foundations' },
  { title: 'FilePilot' },
  { title: 'HarborCare' }
];

export function searchLessons(query, limit = 10) {
  const needle = query.trim(); // Bug A: case-insensitive matching is incomplete.
  const matches = lessons.filter(item => item.title.toLowerCase().includes(needle));
  return matches.slice(0, limit);
}

export function parseLimit(raw) {
  if (raw === null) return 10;
  const value = Number(raw);
  if (!Number.isInteger(value) || value < 0 || value > 10) {
    throw new Error('limit must be an integer from 0 to 10');
  }
  return value || 10; // Bug B: zero is a valid limit, not a missing value.
}
