"""Check self-contained companion reading editions without browser execution."""
from pathlib import Path
from html.parser import HTMLParser
import base64
import re

ROOT = Path(__file__).resolve().parent.parent

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.dependencies = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'img' and attrs.get('src'):
            self.images.append(attrs)
        if tag in ('script', 'link'):
            dependency = attrs.get('src') or attrs.get('href')
            if dependency:
                self.dependencies.append(dependency)

for edition, chapters in [('HYBRID', 15), ('TYPESCRIPT', 17)]:
    markdown = (ROOT / f'{edition}-ARCHITECTURE.md').read_text(encoding='utf-8')
    html = (ROOT / f'{edition}-ARCHITECTURE.html').read_text(encoding='utf-8')
    doc = Document()
    doc.feed(html)
    sources = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', markdown)
    assert len(sources) == len(doc.images) == 4, (edition, 'image count')
    for source, embedded in zip(sources, doc.images):
        assert embedded.get('alt'), source
        assert embedded['src'].startswith('data:image/png;base64,'), source
        assert base64.b64decode(embedded['src'].split(',', 1)[1]) == (ROOT / source).read_bytes(), source
    assert len(doc.ids) == len(set(doc.ids)), 'Duplicate IDs'
    for link in doc.links:
        if link.startswith('#'):
            assert link[1:] in doc.ids, link
    assert not doc.dependencies, doc.dependencies
    assert len(re.findall(r'^## \d+\.', markdown, re.M)) == chapters
    assert markdown.count('```') % 2 == 0
    assert not re.search(r'[A-Z]:[\\/]', markdown), 'Machine path in reading content'
    assert '$body$' not in html and '$toc$' not in html
    print(f'{edition}: {len(markdown.split()):,} words; {chapters} chapters; 4 byte-identical embedded images; valid internal links; no external rendering dependencies; {len(html.encode()):,} HTML bytes')
