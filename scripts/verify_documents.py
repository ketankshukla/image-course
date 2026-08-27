"""Check authored editions without relying on external rendering resources."""
import ast
import base64
import io
import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
HOSPITAL = ROOT / "docs/case-studies/hospital"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.resources = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img" and attrs.get("id") != "diagram-large":
            assert attrs.get("alt"), "Missing image alternative text"
            self.images.append(attrs.get("src", ""))
        if tag in {"link", "script"}:
            self.resources.append(attrs.get("href", attrs.get("src", "")))


def main():
    sources = sorted(HOSPITAL.rglob("*.md"))
    assert len(sources) == 16, f"Expected 16 hospital guides, got {len(sources)}"
    filepilot = ROOT / "docs/case-studies/filepilot"
    filepilot_sources = sorted(filepilot.rglob("*.md"))
    assert len(filepilot_sources) == 16, f"Expected 16 FilePilot guides, got {len(filepilot_sources)}"
    sources.extend(filepilot_sources)
    sources.append(ROOT / "docs/FOLDER-STRUCTURE.md")
    sources.append(ROOT / "docs/PUBLISHING-CASE-STUDIES.md")
    image_count = 0
    for source in sources:
        page = Page()
        page.feed(source.with_suffix(".html").read_text(encoding="utf-8"))
        assert not any(r and not r.startswith("data:") for r in page.resources)
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path:
                assert (source.parent / unquote(parsed.path)).exists(), (source, link)
            elif parsed.fragment:
                assert unquote(parsed.fragment) in page.ids, (source, link)
        expected = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8"))
        assert len(page.images) == len(expected), source
        for original, embedded in zip(expected, page.images):
            assert embedded.startswith("data:image/svg+xml"), source
            header, payload = embedded.split(",", 1)
            data = base64.b64decode(payload) if ";base64" in header else unquote(payload).encode()
            assert data == (source.parent / original).read_bytes(), source
            ET.fromstring(data)
            image_count += 1
    # Execute only the self-contained foundational exercise in memory.
    lesson = (HOSPITAL / "manual-build/01-FOUNDATIONS.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```python\n(.*?)```", lesson, re.S)
    assert len(blocks) == 2
    namespace = {"__name__": "guide_exercise"}
    exec(compile(blocks[0], "foundation-policy", "exec"), namespace)
    tree = ast.parse(blocks[1])
    tree.body = [n for n in tree.body if not isinstance(n, ast.If)
                 and not (isinstance(n, ast.ImportFrom) and n.module == "backend.harborcare.policy")]
    exec(compile(tree, "foundation-tests", "exec"), namespace)
    result = unittest.TextTestRunner(stream=io.StringIO()).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(namespace["PickupPolicyTests"]))
    assert result.wasSuccessful(), result.errors + result.failures
    pilot_lesson = (filepilot / "manual-build/01-FOUNDATIONS.md").read_text(encoding="utf-8")
    pilot_blocks = re.findall(r"```python\n(.*?)```", pilot_lesson, re.S)
    assert len(pilot_blocks) == 1
    pilot_namespace = {"__name__": "filepilot_exercise"}
    exec(compile(pilot_blocks[0], "filepilot-foundations", "exec"), pilot_namespace)
    pilot_result = unittest.TextTestRunner(stream=io.StringIO()).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(pilot_namespace["ApprovalTests"]))
    assert pilot_result.wasSuccessful(), pilot_result.errors + pilot_result.failures
    # Course Markdown image references must still resolve after the move.
    course_images = 0
    for source in (ROOT / "courses").glob("*/diagram-docs/*.md"):
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", source.read_text(encoding="utf-8-sig")):
            if urlsplit(target).scheme:
                continue
            assert (source.parent / unquote(target)).exists(), (source, target)
            course_images += 1
    print(f"PASS: {len(sources)} HTML/Markdown pairs; {image_count} embedded diagrams; "
          f"{result.testsRun + pilot_result.testsRun} executable exercise tests; {course_images} course image references.")


if __name__ == "__main__":
    main()
