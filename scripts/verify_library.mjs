import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const readJson = async p => JSON.parse(await fs.readFile(p, 'utf8'));
const manifest = await readJson(path.join(root, 'data/manifest.json'));
const publicPath = url => {
  assert.match(url, /^\/library\/[a-z0-9/.-]+$/);
  return path.join(root, 'public', url);
};
const seen = new Set();
const images = new Set();
const articles = new Map();
let total = 0;
for (const summary of manifest.courses) {
  assert(!seen.has(summary.id)); seen.add(summary.id);
  assert(['course', 'case-study', 'guide'].includes(summary.kind));
  assert.match(summary.dataUrl, /\.[a-f0-9]{20}\.json$/);
  const data = await readJson(publicPath(summary.dataUrl));
  assert.equal(data.id, summary.id);
  const chapters = data.modules.flatMap(m => m.chapters);
  assert.equal(chapters.length, summary.chaptersCount);
  assert.equal(new Set(chapters.map(c => c.number)).size, chapters.length);
  assert(summary.modules.every(m => m.chapters.every(c => !('body' in c))));
  for (const [i, chapter] of chapters.entries()) {
    assert.equal(chapter.prev, chapters[i - 1]?.number ?? null);
    assert.equal(chapter.next, chapters[i + 1]?.number ?? null);
    assert(chapter.body.length > 100, `Empty content: ${summary.id}:${chapter.number}`);
    assert(!/(?:src|href)="(?:data:|file:|[A-Z]:)/i.test(chapter.body));
    for (const link of chapter.body.matchAll(/href="([^"]+)"/g)) assert(/^(?:#course=|https?:\/\/|mailto:)/.test(link[1]), `Local file link: ${link[1]}`);
    assert(!/<(?:script|iframe|svg)\b/i.test(chapter.body));
    const ids = [...chapter.body.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]);
    assert.equal(new Set(ids).size, ids.length);
    for (const entry of chapter.toc) assert(ids.includes(entry.id));
    if (chapter.image) { images.add(chapter.image); assert(chapter.imageWidth > 0 && chapter.imageHeight > 0); }
    for (const match of chapter.body.matchAll(/<img\b[^>]*>/g)) {
      assert.match(match[0], /width="\d+"/); assert.match(match[0], /height="\d+"/);
      assert.match(match[0], /loading="lazy"/);
      images.add(match[0].match(/src="([^"]+)"/)[1]);
    }
    articles.set(`${summary.id}:${chapter.number}`, chapter);
  }
  if (summary.kind === 'course') {
    // Compare preserved historical course contracts when available locally.
    try {
      const old = await readJson(path.join(root, 'public/courses', `${summary.id}.json`));
      const oldChapters = old.modules.flatMap(m => m.chapters);
      assert.deepEqual(chapters.map(c => [c.number, c.title, c.moduleNumber]), oldChapters.map(c => [c.number, c.title, c.moduleNumber]));
      for (const chapter of chapters) {
        const previous = oldChapters.find(c => c.number === chapter.number);
        assert(chapter.body.length > previous.body.length * .8, `Possible truncated lesson: ${summary.id}:${chapter.number}`);
      }
    } catch (error) { if (error.code !== 'ENOENT') throw error; }
  }
  total += chapters.length;
}
for (const chapter of articles.values()) for (const match of chapter.body.matchAll(/href="#course=([^" ]+)"/g)) {
  const params = new URLSearchParams(`course=${match[1].replaceAll('&amp;', '&')}`);
  const target = articles.get(`${params.get('course')}:${params.get('chapter')}`);
  assert(target, `Broken link ${match[1]}`);
  if (params.get('anchor')) assert(target.body.includes(`id="${params.get('anchor')}"`));
}
for (const url of images) {
  assert.match(url, /\/[a-f0-9]{20}\.webp$/);
  const meta = await sharp(publicPath(url)).metadata();
  assert.equal(meta.format, 'webp'); assert.equal(meta.hasAlpha, false);
}
const search = await readJson(publicPath(manifest.searchUrl));
assert.equal(search.length, total);
assert.equal(new Set(search.map(s => `${s.courseId}:${s.chapterNumber}`)).size, total);
for (const entry of search) assert(articles.has(`${entry.courseId}:${entry.chapterNumber}`));
assert(search.some(s => s.courseId === 'hospital' && s.plainText.includes('ORG-T99')));
console.log(`PASS: ${seen.size} collections, ${total} articles, ${images.size} flattened images, search coverage, anchors, stable course contracts and lazy image dimensions.`);
