import { Chapter, Module } from "./types";

export function chapterByNumber(modules: Module[]): Map<number, Chapter> {
  const map = new Map<number, Chapter>();
  modules.forEach((m) => m.chapters.forEach((c) => map.set(c.number, c)));
  return map;
}

export function cn(...classes: (string | false | null | undefined)[]) {
  return classes.filter(Boolean).join(" ");
}

export interface FuzzyMatch {
  score: number;
  indices: number[];
}

export function fuzzyMatch(query: string, text: string): FuzzyMatch | null {
  if (!query || !text) return null;
  const q = query.toLowerCase().trim();
  const t = text.toLowerCase();
  if (q === t)
    return { score: 1000 + t.length, indices: Array.from({ length: t.length }, (_, i) => i) };
  if (t.startsWith(q))
    return { score: 500, indices: Array.from({ length: q.length }, (_, i) => i) };

  const indices: number[] = [];
  let score = 0;
  let textIndex = 0;
  let prevIndex = -1;
  let firstIndex = -1;

  for (let qi = 0; qi < q.length; qi++) {
    const ch = q[qi];
    const idx = t.indexOf(ch, textIndex);
    if (idx === -1) return null;

    indices.push(idx);
    if (firstIndex === -1) firstIndex = idx;

    if (prevIndex === -1) {
      if (idx === 0) score += 3;
      else if (isWordBoundary(t[idx - 1])) score += 1;
    } else {
      if (idx === prevIndex + 1) score += 4;
      else if (isWordBoundary(t[idx - 1])) score += 2;
    }

    score += 1;
    textIndex = idx + 1;
    prevIndex = idx;
  }

  const span = prevIndex - firstIndex + 1;
  score -= (span - q.length) * 0.3;
  score -= t.length * 0.05;
  return { score: Math.max(score, 0.1), indices };
}

export function fuzzyScore(query: string, text: string): number {
  return fuzzyMatch(query, text)?.score ?? 0;
}

export function escapeHtml(text: string): string {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function escapeRegExp(text: string): string {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

export function highlightInHtml(
  html: string,
  query: string,
  markClass = "search-highlight"
): { highlightedHtml: string; matchCount: number } {
  const q = query.trim().toLowerCase();
  if (!q) return { highlightedHtml: html, matchCount: 0 };

  const skipTags = new Set(["pre", "code", "script", "style", "mark"]);
  let inSkip = 0;
  let count = 0;
  const re = new RegExp(`(${escapeRegExp(q)})`, "gi");

  const parts = html.split(/(<[^>]+>)/g);
  for (let i = 0; i < parts.length; i++) {
    const part = parts[i];
    if (!part) continue;

    if (part[0] === "<") {
      const start = part.match(/^<(pre|code|script|style|mark)(?:\s|\/?>|>)/i);
      if (start && skipTags.has(start[1].toLowerCase())) inSkip++;

      const end = part.match(/^<\/(pre|code|script|style|mark)>/i);
      if (end && skipTags.has(end[1].toLowerCase())) {
        inSkip = Math.max(0, inSkip - 1);
      }
      continue;
    }

    if (inSkip === 0) {
      const highlighted = part.replace(re, (match) => {
        count++;
        return `<mark class="${markClass}">${match}</mark>`;
      });
      parts[i] = highlighted;
    }
  }

  return { highlightedHtml: parts.join(""), matchCount: count };
}

export function highlightMatches(
  text: string,
  query: string,
  markClass = "bg-yellow-200 rounded px-0.5"
): string {
  const q = query.trim().toLowerCase();
  if (!q) return escapeHtml(text);

  // Exact matches first.
  const t = text.toLowerCase();
  const matches: { start: number; end: number }[] = [];
  let pos = t.indexOf(q);
  while (pos !== -1) {
    matches.push({ start: pos, end: pos + q.length });
    pos = t.indexOf(q, pos + q.length);
  }

  if (matches.length > 0) {
    let html = "";
    let last = 0;
    for (const { start, end } of matches) {
      html += escapeHtml(text.slice(last, start));
      html += `<mark class="${markClass}">${escapeHtml(text.slice(start, end))}</mark>`;
      last = end;
    }
    html += escapeHtml(text.slice(last));
    return html;
  }

  // Fuzzy fallback: only highlight if the match is a single, close span so
  // we don’t end up with scattered letters across a sentence.
  const match = fuzzyMatch(query, text);
  if (!match) return escapeHtml(text);
  const span = match.indices[match.indices.length - 1] - match.indices[0] + 1;
  if (span > q.length * 2 + 4) return escapeHtml(text);

  const first = match.indices[0];
  const last = match.indices[match.indices.length - 1];
  let html = escapeHtml(text.slice(0, first));
  html += `<mark class="${markClass}">${escapeHtml(text.slice(first, last + 1))}</mark>`;
  html += escapeHtml(text.slice(last + 1));
  return html;
}

export function buildSnippet(
  plainText: string,
  query: string,
  radius = 100,
  maxLength = 280
): string {
  if (!query) {
    const prefix = escapeHtml(plainText.slice(0, maxLength));
    return prefix + (plainText.length > maxLength ? "…" : "");
  }

  const q = query.trim().toLowerCase();
  const t = plainText.toLowerCase();

  // Only build a highlighted snippet around an exact phrase match.
  const exact = t.indexOf(q);
  if (exact === -1) {
    const prefix = escapeHtml(plainText.slice(0, maxLength));
    return prefix + (plainText.length > maxLength ? "…" : "");
  }

  const first = exact;
  const last = exact + q.length - 1;

  let start = Math.max(0, first - radius);
  let end = Math.min(plainText.length, last + radius);

  // Extend to word boundaries so we don’t chop words.
  start = findWordBoundaryBefore(plainText, start, 0);
  end = findWordBoundaryAfter(plainText, end, plainText.length);

  const snippet = plainText.slice(start, end);
  const prefix = start > 0 ? "…" : "";
  const suffix = end < plainText.length ? "…" : "";
  return prefix + highlightMatches(snippet, query) + suffix;
}

function findWordBoundaryBefore(text: string, index: number, fallback: number): number {
  for (let i = index; i > fallback; i--) {
    if (/\s/.test(text[i - 1])) return i;
  }
  return fallback;
}

function findWordBoundaryAfter(text: string, index: number, fallback: number): number {
  for (let i = index; i < fallback; i++) {
    if (/\s/.test(text[i])) return i;
  }
  return fallback;
}

function isWordBoundary(ch: string): boolean {
  return ch === " " || ch === "-" || ch === "_" || ch === "/" || ch === ":";
}
