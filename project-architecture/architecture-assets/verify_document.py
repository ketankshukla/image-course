"""Check the generated document and its embedded images without a browser."""
from pathlib import Path
from html.parser import HTMLParser
import base64
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.ids = []
        self.anchors = []
        self.dependencies = []
        self.scripts = []
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'img' and 'src' in attrs:
            self.images.append(attrs)
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.anchors.append(attrs['href'][1:])
        if tag in {'script', 'link'}:
            url = attrs.get('src') or attrs.get('href')
            if url:
                self.dependencies.append(url)
        if tag == 'script':
            self.in_script = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False

    def handle_data(self, data):
        if self.in_script:
            self.scripts.append(data)

markdown = (ROOT / 'PROJECT-ARCHITECTURE.md').read_text(encoding='utf-8')
html = (ROOT / 'PROJECT-ARCHITECTURE.html').read_text(encoding='utf-8')
doc = Document()
doc.feed(html)
refs = re.findall(r'!\[[^\]]+\]\(([^)]+)\)', markdown)
assert len(refs) == len(doc.images) == 6, 'Expected six inline diagrams'
images = []
for ref, img in zip(refs, doc.images):
    source = ROOT / ref
    assert source.is_file(), f'Missing image: {ref}'
    assert img.get('alt'), 'Missing descriptive alt text'
    assert img['src'].startswith('data:image/png;base64,'), 'Image is not embedded'
    decoded = base64.b64decode(img['src'].split(',', 1)[1])
    original = source.read_bytes()
    assert decoded == original, f'Embedded image differs: {ref}'
    images.append({'name': source.name, 'sha256': hashlib.sha256(original).hexdigest()})
assert not doc.dependencies, 'Expected no external runtime dependencies'
assert len(doc.ids) == len(set(doc.ids)), 'Duplicate HTML IDs'
assert all(anchor in doc.ids for anchor in doc.anchors), 'Broken internal navigation'
assert markdown.count('```') % 2 == 0, 'Unclosed fenced code block'
assert len(re.findall(r'^## \d+\.', markdown, re.M)) == 19, 'Missing numbered chapter'
assert len(doc.scripts) == 1, 'Expected one self-contained enhancement script'
print(json.dumps({
    'status': 'PASS',
    'chapters': 19,
    'words': len(markdown.split()),
    'images': images,
    'html_bytes': (ROOT / 'PROJECT-ARCHITECTURE.html').stat().st_size,
    'internal_links': len(doc.anchors),
    'external_runtime_dependencies': doc.dependencies,
    'browser_visual_check': 'Not performed: local-file URL blocked by browser security policy'
}, indent=2))
