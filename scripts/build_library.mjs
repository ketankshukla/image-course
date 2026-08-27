// One reproducible Node-only build for local development and Vercel.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import MarkdownIt from 'markdown-it';
import sanitize from 'sanitize-html';
import sharp from 'sharp';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const publicDir = path.join(root, 'public');
const generated = path.join(publicDir, 'library');
const read = async p => (await fs.readFile(p, 'utf8')).replace(/^\uFEFF/, '');
const json = async p => JSON.parse(await read(p));
const hash = bytes => createHash('sha256').update(bytes).digest('hex').slice(0, 20);
const escape = s => s.replaceAll('&', '&amp;').replaceAll('"', '&quot;').replaceAll('<', '&lt;');
const slug = s => s.toLowerCase().replace(/[^\p{L}\p{N}\s-]/gu, '').trim().replace(/\s+/g, '-');
const relative = p => path.relative(root, p).split(path.sep).join('/');
function within(base, p) {
  const rel = path.relative(base, p);
  if (rel.startsWith('..') || path.isAbsolute(rel)) throw Error(`Path escapes content root: ${p}`);
  return p;
}
const icons = ['🧭', '🛠️', '🧠', '🤖', '🔄', '🎯', '🌐', '🔒', '📊', '🚀'];
const md = new MarkdownIt({ html: false, linkify: false });
const sources = new Map();
const assets = new Map();
const emitted = new Set();
const internalLinks = [];
let sourceImageBytes = 0;
let outputImageBytes = 0;

async function emit(name, bytes) {
  const out = within(generated, path.join(generated, name));
  await fs.mkdir(path.dirname(out), { recursive: true });
  await fs.writeFile(out, bytes);
  emitted.add(out);
  return `/library/${name}`;
}

async function imageAsset(source) {
  within(root, source);
  if (assets.has(source)) return assets.get(source);
  const bytes = await fs.readFile(source);
  // Flatten transparency; rasterize SVG before shipping. Originals are read-only.
  if (path.extname(source).toLowerCase() === '.svg' && /<(?:script|foreignObject)\b|(?:href|src)\s*=\s*["'](?:https?:|file:|\/\/)/i.test(bytes.toString())) {
    throw Error(`Unsafe external or active SVG content: ${relative(source)}`);
  }
  const key = hash(Buffer.concat([Buffer.from(`webp-q88-v1-${sharp.versions.sharp}`), bytes]));
  const filename = `images/${key}.webp`;
  const cached = path.join(generated, filename);
  let data;
  try { data = await fs.readFile(cached); } catch {
    data = await sharp(bytes, { density: 144 }).rotate().resize({ width: 2400, withoutEnlargement: true })
      .flatten({ background: '#ffffff' }).webp({ quality: 88, effort: 4 }).toBuffer();
  }
  const meta = await sharp(data).metadata();
  const result = { src: await emit(filename, data), width: meta.width, height: meta.height };
  sourceImageBytes += bytes.length;
  outputImageBytes += data.length;
  assets.set(source, result);
  return result;
}

async function render(source, body, collectionId, number) {
  const env = {};
  const tokens = md.parse(body, env);
  const toc = [];
  const ids = new Set();
  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i].type === 'heading_open') {
      const title = tokens[i + 1].content;
      const base = slug(title) || 'section';
      let id = base, suffix = 1;
      while (ids.has(id)) id = `${base}-${suffix++}`;
      ids.add(id);
      tokens[i].attrSet('id', id);
      if (tokens[i].tag === 'h2') toc.push({ id, title });
    }
  }
  async function walk(list) {
    for (const token of list) {
      if (token.type === 'image') {
        const target = token.attrGet('src');
        if (/^(?:[a-z]+:|\/\/)/i.test(target)) throw Error(`Images must be local: ${source}: ${target}`);
        const asset = await imageAsset(path.resolve(path.dirname(source), decodeURIComponent(target)));
        token.attrSet('src', asset.src);
        token.attrSet('width', String(asset.width));
        token.attrSet('height', String(asset.height));
        token.attrSet('loading', 'lazy');
        token.attrSet('decoding', 'async');
      }
      if (token.type === 'link_open') {
        const href = token.attrGet('href');
        if (/^https?:\/\//i.test(href)) {
          token.attrSet('rel', 'noopener noreferrer');
        } else if (href.startsWith('#course=')) {
          internalLinks.push(href);
        } else if (!/^mailto:/i.test(href)) {
          const [file, fragment] = href.split('#');
          const target = file ? sources.get(path.resolve(path.dirname(source), decodeURIComponent(file))) : { id: collectionId, number };
          if (!target) throw Error(`Unpublished local link in ${relative(source)}: ${href}`);
          const url = `#course=${target.id}&chapter=${target.number}${fragment ? `&anchor=${encodeURIComponent(decodeURIComponent(fragment))}` : ''}`;
          token.attrSet('href', url);
          internalLinks.push(url);
        }
      }
      if (token.children) await walk(token.children);
    }
  }
  await walk(tokens);
  const bodyHtml = sanitize(md.renderer.render(tokens, md.options, env), {
    allowedTags: [...sanitize.defaults.allowedTags, 'img'],
    allowedAttributes: { ...sanitize.defaults.allowedAttributes, '*': ['id'], img: ['src', 'alt', 'width', 'height', 'loading', 'decoding'], code: ['class'], a: ['href', 'rel'] },
    allowedSchemes: ['https', 'http', 'mailto'], allowProtocolRelative: false,
  });
  const plainText = sanitize(bodyHtml, { allowedTags: [], allowedAttributes: {} }).replace(/\s+/g, ' ').trim();
  return { body: bodyHtml, toc, plainText, readTime: Math.max(1, Math.round(plainText.split(/\s+/).length / 200)) };
}

const collections = [];
// Existing ten course contracts and chapter numbers remain intact.
for (const config of await json(path.join(root, 'data/courses.config.json'))) {
  const base = path.join(root, 'courses', config.source_dir);
  const overrides = new Map();
  if (config.content_json) {
    const contents = await json(path.join(base, config.content_json));
    const modules = new Map(contents.modules.map((m, i) => [m.id, { number: i + 1, title: m.title }]));
    for (const lesson of contents.lessons) overrides.set(lesson.id, modules.get(lesson.moduleId));
  }
  const entries = [];
  const names = (await fs.readdir(path.join(base, 'diagram-docs'))).filter(n => n.endsWith('.md')).sort((a, b) => Number(a.match(/\d+/)?.[0]) - Number(b.match(/\d+/)?.[0]));
  const moduleNames = new Map();
  for (const name of names) {
    const source = path.join(base, 'diagram-docs', name);
    const lines = (await read(source)).split(/\r?\n/);
    const match = lines[0].match(/^#\s*Diagram\s+(\d+)\s*[-–—]\s*(.*)/);
    if (!match) throw Error(`Invalid lesson title: ${source}`);
    const number = Number(match[1]), title = match[2].trim();
    const imageIndex = lines.findIndex(l => /^!\[/.test(l));
    const image = lines[imageIndex]?.match(/^!\[(.*)\]\(([^)]+)\)/);
    if (!image) throw Error(`Missing lesson image: ${source}`);
    const meta = {};
    let end = imageIndex + 1;
    for (; end < lines.length && lines[end].trim() !== '---'; end++) {
      const m = lines[end].match(/^\*\*([^*]+):\*\*\s*(.*)/);
      if (m) meta[m[1].trim().toLowerCase().replaceAll(' ', '_')] = m[2].trim();
    }
    if (end === lines.length) throw Error(`Missing metadata boundary: ${source}`);
    const moduleText = meta.module || '';
    const moduleMatch = moduleText.match(/^(\d+)\s*[-–—]\s*(.*)/);
    if (!moduleNames.has(moduleText)) moduleNames.set(moduleText, moduleNames.size + 1);
    const module = overrides.get(number) || { number: moduleMatch ? Number(moduleMatch[1]) : moduleNames.get(moduleText), title: moduleMatch ? moduleMatch[2].trim() : moduleText };
    entries.push({ source, number, title, fullTitle: `Diagram ${String(number).padStart(2, '0')} — ${title}`, slug: `diagram-${String(number).padStart(2, '0')}`, moduleNumber: module.number, moduleTitle: module.title, role: meta.role_in_the_course || '', layout: meta.layout || '', imageSource: path.resolve(path.dirname(source), image[2]), imageAlt: image[1], markdown: lines.slice(end + 1).join('\n') });
  }
  collections.push({ id: config.id, kind: 'course', title: config.title, subtitle: config.subtitle, icon: config.icon, slug: `visual-course-${config.id}`, entries });
}

// An explicit publication manifest prevents drafts/verification notes from leaking.
const caseRoot = path.join(root, 'docs/case-studies');
const configFiles = [];
for (const entry of await fs.readdir(caseRoot, { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const filename = path.join(caseRoot, entry.name, 'collection.json');
  try { await fs.access(filename); configFiles.push(filename); } catch { /* Unpublished folder. */ }
}
configFiles.push(path.join(root, 'docs/collection.json'));
const documentConfigs = await Promise.all(configFiles.map(async source => ({ source, config: await json(source) })));
documentConfigs.sort((a, b) => (a.config.order || 0) - (b.config.order || 0) || a.config.id.localeCompare(b.config.id));
for (const { source: configFile, config } of documentConfigs) {
  if (!/^[a-z][a-z0-9-]*$/.test(config.id) || !['case-study', 'guide'].includes(config.kind)) throw Error(`Invalid collection: ${configFile}`);
  const entries = [];
  const usedIds = new Set();
  for (const [i, section] of config.sections.entries()) for (const doc of section.documents) {
    if (!Number.isInteger(doc.id) || doc.id < 1 || usedIds.has(doc.id)) throw Error(`Invalid/duplicate document ID: ${configFile}`);
    usedIds.add(doc.id);
    const source = within(path.dirname(configFile), path.resolve(path.dirname(configFile), doc.file));
    if (!source.endsWith('.md')) throw Error(`Publish Markdown only: ${source}`);
    let markdown = await read(source);
    const heading = markdown.match(/^#\s+(.+)$/m);
    if (!heading) throw Error(`Missing document title: ${source}`);
    const title = doc.title || heading[1];
    markdown = markdown.replace(/^#\s+.+\r?\n/, '').replace(/\s*·\s*\[Markdown\]\([^)]+\)/g, '');
    entries.push({ source, number: doc.id, title, fullTitle: title, slug: slug(path.basename(source, '.md')), moduleNumber: i + 1, moduleTitle: section.title, role: '', layout: '', image: '', imageAlt: '', markdown });
  }
  collections.push({ id: config.id, kind: config.kind, title: config.title, subtitle: config.subtitle, icon: config.icon, slug: config.id, entries });
}

const collectionIds = new Set();
for (const collection of collections) {
  if (collectionIds.has(collection.id)) throw Error(`Duplicate collection ID: ${collection.id}`);
  collectionIds.add(collection.id);
  for (const chapter of collection.entries) {
    if (sources.has(chapter.source)) throw Error(`Document published twice: ${chapter.source}`);
    const target = { id: collection.id, number: chapter.number };
    sources.set(chapter.source, target);
    sources.set(chapter.source.replace(/\.md$/, '.html'), target);
  }
}

const manifest = { siteTitle: 'Visual Agent Learning Library', siteSubtitle: 'Learn the concepts. Explore complete case studies. Build your own agent systems.', courses: [] };
const search = [];
const renderedChapters = new Map();
for (const collection of collections) {
  const modules = new Map();
  for (const [i, entry] of collection.entries.entries()) {
    const { source, markdown, imageSource, ...chapter } = entry;
    Object.assign(chapter, await render(source, markdown, collection.id, chapter.number));
    if (imageSource) {
      const image = await imageAsset(imageSource);
      Object.assign(chapter, { image: image.src, imageWidth: image.width, imageHeight: image.height });
    }
    chapter.prev = collection.entries[i - 1]?.number ?? null;
    chapter.next = collection.entries[i + 1]?.number ?? null;
    search.push({ courseId: collection.id, courseTitle: collection.title, courseIcon: collection.icon, courseSubtitle: collection.subtitle, moduleTitle: chapter.moduleTitle, chapterNumber: chapter.number, chapterTitle: chapter.title, number: chapter.number, plainText: chapter.plainText, snippet: chapter.plainText.slice(0, 300) });
    delete chapter.plainText;
    if (!modules.has(chapter.moduleNumber)) modules.set(chapter.moduleNumber, { number: chapter.moduleNumber, title: chapter.moduleTitle, icon: icons[(chapter.moduleNumber - 1) % icons.length], chapters: [] });
    modules.get(chapter.moduleNumber).chapters.push(chapter);
    renderedChapters.set(`${collection.id}:${chapter.number}`, chapter);
  }
  const { entries, ...metadata } = collection;
  const full = { ...metadata, chaptersCount: entries.length, modules: [...modules.values()].sort((a, b) => a.number - b.number) };
  const bytes = JSON.stringify(full);
  const dataUrl = await emit(`collections/${collection.id}.${hash(bytes)}.json`, bytes);
  manifest.courses.push({ ...full, dataUrl, modules: full.modules.map(m => ({ ...m, chapters: m.chapters.map(({ number, title, slug }) => ({ number, title, slug })) })) });
  console.log(`${collection.kind}: ${collection.id} — ${entries.length} articles`);
}
for (const link of internalLinks) {
  const params = new URLSearchParams(link.slice(1));
  const chapter = renderedChapters.get(`${params.get('course')}:${params.get('chapter')}`);
  if (!chapter) throw Error(`Broken internal article link: ${link}`);
  const anchor = params.get('anchor');
  if (anchor && !chapter.body.includes(`id="${escape(anchor)}"`)) throw Error(`Broken section link: ${link}`);
}
const searchBytes = JSON.stringify(search);
manifest.searchUrl = await emit(`search.${hash(searchBytes)}.json`, searchBytes);
const manifestPath = path.join(root, 'data/manifest.json');
const manifestTemp = path.join(root, 'data/manifest.next.json');
await fs.writeFile(manifestTemp, JSON.stringify(manifest, null, 2));
await fs.rename(manifestTemp, manifestPath);

// Remove only obsolete files owned by this generator, never source or legacy assets.
async function prune(dir) {
  for (const entry of await fs.readdir(dir, { withFileTypes: true })) {
    const p = within(generated, path.join(dir, entry.name));
    if (entry.isDirectory()) await prune(p);
    else if (!emitted.has(p) && /\.(?:json|webp)$/.test(entry.name)) await fs.unlink(p);
  }
}
await prune(generated);
console.log(`Built ${collections.length} collections / ${search.length} articles / ${assets.size} unique source images.`);
console.log(`Image originals ${(sourceImageBytes / 1048576).toFixed(1)} MB → WebP ${(outputImageBytes / 1048576).toFixed(1)} MB. Manifest ${(JSON.stringify(manifest).length / 1024).toFixed(1)} KB.`);
