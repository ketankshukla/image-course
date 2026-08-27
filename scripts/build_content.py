#!/usr/bin/env python3
"""Build course content and compress diagram images for all configured courses."""

import html
import json
import re
from pathlib import Path

import markdown as md
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
COURSE_ROOT = ROOT / "courses"
OUT_DATA = ROOT / "data"
OUT_COURSES = ROOT / "public" / "courses"
OUT_IMAGES = ROOT / "public" / "images"
OUT_SEARCH = ROOT / "public"

OUT_DATA.mkdir(parents=True, exist_ok=True)
OUT_COURSES.mkdir(parents=True, exist_ok=True)
OUT_IMAGES.mkdir(parents=True, exist_ok=True)
OUT_SEARCH.mkdir(parents=True, exist_ok=True)

COURSES = [
    {
        "id": "01",
        "source_dir": "Visual Course 01",
        "title": "Visual Course Volume 1 — MCP, ACP, A2A and RAG",
        "subtitle": "A visual course on modern agent architecture, capabilities, collaboration, and retrieval.",
        "icon": "🎨",
    },
    {
        "id": "02",
        "source_dir": "Visual Course 02",
        "title": "Visual Course Volume 2 — Build Your First Agent System",
        "subtitle": "The implementation bridge from web basics to MCP, RAG, A2A, reliability, and deployment.",
        "icon": "🛠️",
    },
    {
        "id": "03",
        "source_dir": "Visual Course 03",
        "title": "Visual Course Volume 3 — Production Agent Systems",
        "subtitle": "Turn a working agent demo into a durable, secure, measurable system.",
        "icon": "🚀",
    },
    {
        "id": "04",
        "source_dir": "Visual Course 04",
        "title": "Visual Course Volume 4 — Protocol Engineering and Interoperability",
        "subtitle": "Read, test, connect, and safely evolve MCP, A2A, and AG-UI systems.",
        "icon": "🔗",
        "content_json": "Volume 4 Course Content.json",
    },
    {
        "id": "05",
        "source_dir": "Visual Course 05",
        "title": "Visual Course Volume 5 — Knowledge Systems and Advanced RAG",
        "subtitle": "Build permission-aware, fresh, explainable, and measurable evidence systems.",
        "icon": "🔍",
        "content_json": "Volume 5 Course Content.json",
    },
    {
        "id": "06",
        "source_dir": "Visual Course 06",
        "title": "Visual Course Volume 6 — Durable Orchestration and Multi-Agent Workflows",
        "subtitle": "Design queues, sagas, A2A delegation, and recovery so agent work survives failure.",
        "icon": "🎓",
        "content_json": "Volume 6 Course Content.json",
    },
    {
        "id": "07",
        "source_dir": "Visual Course 07",
        "title": "Visual Course Volume 7 — Agent Identity, Security, and Governance",
        "subtitle": "Protect every identity, capability, data path, tenant, and consequential action.",
        "icon": "🔒",
        "content_json": "Volume 7 Course Content.json",
    },
    {
        "id": "08",
        "source_dir": "Visual Course 08",
        "title": "Visual Course Volume 8 — Evaluation, Observability, and AgentOps",
        "subtitle": "Prove quality, safety, latency, cost, and recovery before and after release.",
        "icon": "📊",
        "content_json": "Volume 8 Course Content.json",
    },
    {
        "id": "09",
        "source_dir": "Visual Course 09",
        "title": "Visual Course Volume 9 — Agentic Product Design and Human Control",
        "subtitle": "Turn complex agent work into an understandable, accessible, and recoverable human experience.",
        "icon": "🧑‍💻",
        "content_json": "Volume 9 Course Content.json",
    },
    {
        "id": "10",
        "source_dir": "Visual Course 10",
        "title": "Visual Course Volume 10 — Enterprise Architecture and Dual-Stack Project Blueprint",
        "subtitle": "Assemble the architecture, contracts, delivery, and operational handoff for a real agent platform.",
        "icon": "🏛️",
        "content_json": "Volume 10 Course Content.json",
    },
]

# A palette of module icons we cycle through within each course.
MODULE_ICONS = ["🧭", "🛠️", "🧠", "🤖", "🔄", "🎯", "🌐", "🔒", "📊", "🚀", "📦", "🎓"]


def to_webp_name(png_path: str) -> str:
    return Path(png_path).stem + ".webp"


def parse_meta(lines: list[str], start: int) -> tuple[dict[str, str], int]:
    meta: dict[str, str] = {}
    i = start
    while i < len(lines):
        line = lines[i].strip()
        if line == "---":
            break
        m = re.match(r"^\*\*([^*]+):\*\*\s*(.*)", line)
        if m:
            key = m.group(1).strip().lower().replace(" ", "_")
            meta[key] = m.group(2).strip()
        i += 1
    return meta, i


def transform_image_refs(body: str, image_map: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        alt = m.group(1)
        src = m.group(2).strip()
        new_src = image_map.get(src, src)
        return f"![{alt}]({new_src})"

    return re.sub(r"!\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^)]+)\)", repl, body)


def md_to_html(text: str) -> str:
    if not text:
        return ""
    return md.markdown(str(text), extensions=["tables", "fenced_code"])


def build_json_lesson_body(lesson: dict, course_id: str, related_map: dict[int, dict]) -> str:
    parts: list[str] = []

    if lesson.get("outcome") or lesson.get("explanation"):
        parts.append("<h2>At a glance</h2>")
        if lesson.get("outcome"):
            parts.append(md_to_html(lesson["outcome"]))
        if lesson.get("explanation"):
            parts.append(md_to_html(lesson["explanation"]))

    if lesson.get("trace"):
        parts.append("<h2>What the diagram teaches</h2>")
        parts.append("<h3>Trace the visual</h3>")
        parts.append("<ol>")
        for item in lesson["trace"]:
            parts.append(f"<li>{html.escape(str(item))}</li>")
        parts.append("</ol>")

    if lesson.get("analogy"):
        parts.append("<h3>Analogy</h3>")
        parts.append(md_to_html(lesson["analogy"]))

    case = lesson.get("caseStudy")
    if case:
        parts.append("<h2>Case study</h2>")
        if case.get("situation"):
            parts.append("<h3>Situation</h3>")
            parts.append(md_to_html(case["situation"]))
        if case.get("walkthrough"):
            parts.append("<ol>")
            for item in case["walkthrough"]:
                parts.append(f"<li>{html.escape(str(item))}</li>")
            parts.append("</ol>")
        for label, key in [("Result", "result"), ("Danger", "danger"), ("Takeaway", "takeaway")]:
            if case.get(key):
                parts.append(f"<h3>{label}</h3>")
                parts.append(md_to_html(case[key]))

    if lesson.get("nextjs"):
        parts.append("<h2>Next.js map</h2>")
        parts.append("<ul>")
        for item in lesson["nextjs"]:
            parts.append(f"<li>{html.escape(str(item))}</li>")
        parts.append("</ul>")

    if lesson.get("python"):
        parts.append("<h2>Python map</h2>")
        parts.append("<ul>")
        for item in lesson["python"]:
            parts.append(f"<li>{html.escape(str(item))}</li>")
        parts.append("</ul>")

    if lesson.get("lab"):
        parts.append("<h2>Mini lab</h2>")
        parts.append(md_to_html(lesson["lab"]))

    if lesson.get("checkpoint"):
        parts.append("<h2>Checkpoint</h2>")
        parts.append(f"<p><strong>Question:</strong> {html.escape(str(lesson['checkpoint']))}</p>")
        if lesson.get("answer"):
            parts.append(f"<p><strong>Answer:</strong> {html.escape(str(lesson['answer']))}</p>")

    if lesson.get("glossary"):
        parts.append("<h2>Glossary</h2>")
        parts.append("<ul>")
        for item in lesson["glossary"]:
            parts.append(f"<li>{html.escape(str(item))}</li>")
        parts.append("</ul>")

    if lesson.get("related"):
        parts.append("<h2>Related lessons</h2>")
        parts.append("<ul>")
        for rid in lesson["related"]:
            related = related_map.get(rid)
            if related:
                parts.append(
                    f'<li><a href="#course={course_id}&chapter={rid}">'
                    f"{html.escape(related['title'])}</a></li>"
                )
            else:
                parts.append(f"<li>{html.escape(str(rid))}</li>")
        parts.append("</ul>")

    return "\n".join(parts)


def process_course_from_json(config: dict) -> tuple[dict, dict, set[str]]:
    course_id = config["id"]
    source_dir = COURSE_ROOT / config["source_dir"]
    json_path = source_dir / config["content_json"]
    source_img = source_dir / "diagrams"

    if not json_path.exists():
        print(f"  Skipping {config['source_dir']}: {json_path.name} not found")
        return {}, {}, set()

    data = json.loads(json_path.read_text(encoding="utf-8"))
    modules_raw = data.get("modules", [])
    lessons = data.get("lessons", [])

    module_map: dict[str, dict] = {
        m["id"]: {"number": i + 1, "title": m.get("title", "").strip()}
        for i, m in enumerate(modules_raw)
    }

    related_map: dict[int, dict] = {l["id"]: l for l in lessons}

    chapters: list[dict] = []
    image_sources: set[str] = set()

    for lesson in lessons:
        number = int(lesson["id"])
        title = str(lesson.get("title", "")).strip()
        module_id = lesson.get("moduleId", "")
        module = module_map.get(module_id, {"number": 0, "title": ""})

        diagram_rel = str(lesson.get("diagram", "")).strip()
        diagram_basename = Path(diagram_rel).name
        image_src = source_img / diagram_basename
        image_sources.add(str(image_src))
        image_webp = f"/images/{to_webp_name(diagram_basename)}"

        body_html = build_json_lesson_body(lesson, course_id, related_map)
        plain_text = re.sub(r"<[^>]+>", " ", body_html)
        plain_text = re.sub(r"\s+", " ", plain_text).strip()
        words = len(re.findall(r"\w+", plain_text))
        read_time = max(1, round(words / 200))

        chapters.append(
            {
                "number": number,
                "slug": lesson.get("slug", f"diagram-{number:02d}"),
                "title": title,
                "fullTitle": f"Diagram {number:02d} — {title}",
                "image": image_webp,
                "imageAlt": str(lesson.get("alt", "")).strip(),
                "moduleNumber": module["number"],
                "moduleTitle": module["title"],
                "role": str(lesson.get("stability", "")).strip(),
                "layout": "",
                "readTime": read_time,
                "body": body_html,
            }
        )

    chapters.sort(key=lambda c: c["number"])
    for i, c in enumerate(chapters):
        c["prev"] = chapters[i - 1]["number"] if i > 0 else None
        c["next"] = chapters[i + 1]["number"] if i < len(chapters) - 1 else None

    modules_dict: dict[int, dict] = {}
    for c in chapters:
        mn = c["moduleNumber"]
        if mn not in modules_dict:
            modules_dict[mn] = {
                "number": mn,
                "title": c["moduleTitle"],
                "chapters": [],
            }
        modules_dict[mn]["chapters"].append(c)

    modules = [modules_dict[k] for k in sorted(modules_dict)]
    for i, m in enumerate(modules):
        m["icon"] = MODULE_ICONS[i % len(MODULE_ICONS)]

    course_data = {
        "id": course_id,
        "slug": f"visual-course-{course_id}",
        "title": config["title"],
        "subtitle": config["subtitle"],
        "modules": modules,
        "chaptersCount": len(chapters),
    }

    manifest_entry = {
        "id": course_id,
        "slug": f"visual-course-{course_id}",
        "title": config["title"],
        "subtitle": config["subtitle"],
        "icon": config.get("icon", "📚"),
        "chaptersCount": len(chapters),
        "modules": [
            {
                "number": m["number"],
                "title": m["title"],
                "icon": m["icon"],
                "chapters": [
                    {
                        "number": c["number"],
                        "slug": c["slug"],
                        "title": c["title"],
                    }
                    for c in m["chapters"]
                ],
            }
            for m in modules
        ],
    }

    return course_data, manifest_entry, image_sources


def process_course(config: dict) -> tuple[dict, dict, set[str]]:
    source_dir = COURSE_ROOT / config["source_dir"]
    source_md = source_dir / "diagram-docs"
    source_img = source_dir / "diagrams"
    course_id = config["id"]

    # Optional JSON with the intended module/lesson mapping.
    module_override: dict[int, dict[str, int | str]] = {}
    content_json_name = config.get("content_json")
    if content_json_name:
        json_path = source_dir / content_json_name
        if json_path.exists():
            data = json.loads(json_path.read_text(encoding="utf-8"))
            modules_raw = data.get("modules", [])
            module_id_to_num: dict[str, dict[str, int | str]] = {
                m["id"]: {"number": i + 1, "title": m.get("title", "").strip()}
                for i, m in enumerate(modules_raw)
            }
            for lesson in data.get("lessons", []):
                module = module_id_to_num.get(lesson.get("moduleId", ""), {"number": 0, "title": ""})
                module_override[int(lesson["id"])] = {
                    "number": int(module["number"]),
                    "title": str(module["title"]),
                }

    chapters: list[dict] = []
    image_sources: set[str] = set()
    module_index_map: dict[str, int] = {}
    next_module_index = 1

    if not source_md.exists():
        print(f"  Skipping {config['source_dir']}: no diagram-docs folder")
        return {}, {}, set()

    def _diagram_number(p: Path) -> int:
        m = re.search(r"\d+", p.name)
        return int(m.group()) if m else 0

    for md_path in sorted(source_md.glob("*.md"), key=_diagram_number):
        text = md_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines:
            continue

        title_match = re.match(r"^#\s*Diagram\s+(\d+)\s*[-–—]\s*(.*)", lines[0])
        if not title_match:
            print(f"  Skipping {md_path.name}: could not parse title")
            continue

        number = int(title_match.group(1))
        title = title_match.group(2).strip()

        img_line_idx = -1
        img_match: re.Match[str] | None = None
        for idx, line in enumerate(lines[1:], start=1):
            m = re.match(r"!\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^)]+)\)", line)
            if m:
                img_match = m
                img_line_idx = idx
                break

        if not img_match:
            print(f"  Skipping {md_path.name}: no image found")
            continue

        image_alt = img_match.group(1).strip()
        image_src = img_match.group(2).strip()
        image_basename = Path(image_src).name
        image_sources.add(str(source_img / image_basename))

        image_map: dict[str, str] = {
            image_src: f"/images/{to_webp_name(image_basename)}"
        }

        meta, meta_end = parse_meta(lines, img_line_idx + 1)

        # Use an optional course JSON to set the module number and title.
        override = module_override.get(number)
        if override:
            module_number = int(override["number"])
            module_title = str(override["title"])
        else:
            module_raw = meta.get("module", "")
            module_match = re.match(r"^(\d+)\s*[-–—]\s*(.*)", module_raw)
            if module_match:
                module_number = int(module_match.group(1))
                module_title = module_match.group(2).strip()
            else:
                if module_raw not in module_index_map:
                    module_index_map[module_raw] = next_module_index
                    next_module_index += 1
                module_number = module_index_map[module_raw]
                module_title = module_raw

        role = meta.get("role_in_the_course", "")
        layout = meta.get("layout", "")

        body_start = meta_end + 1
        while body_start < len(lines) and lines[body_start].strip() == "":
            body_start += 1

        body_md = "\n".join(lines[body_start:])

        for m in re.finditer(r"!\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^)]+)\)", body_md):
            src = m.group(2).strip()
            if src.startswith("../diagrams/") and src.endswith(".png"):
                basename = Path(src).name
                image_sources.add(str(source_img / basename))
                image_map[src] = f"/images/{to_webp_name(basename)}"

        body_md = transform_image_refs(body_md, image_map)
        body_html = md.markdown(body_md, extensions=["tables", "fenced_code"])

        plain_text = re.sub(r"<[^>]+>", " ", body_html)
        plain_text = re.sub(r"\s+", " ", plain_text).strip()
        words = len(re.findall(r"\w+", plain_text))
        read_time = max(1, round(words / 200))

        chapters.append(
            {
                "number": number,
                "slug": f"diagram-{number:02d}",
                "title": title,
                "fullTitle": f"Diagram {number:02d} — {title}",
                "image": image_map[image_src],
                "imageAlt": image_alt,
                "moduleNumber": module_number,
                "moduleTitle": module_title,
                "role": role,
                "layout": layout,
                "readTime": read_time,
                "body": body_html,
            }
        )

    chapters.sort(key=lambda c: c["number"])
    for i, c in enumerate(chapters):
        c["prev"] = chapters[i - 1]["number"] if i > 0 else None
        c["next"] = chapters[i + 1]["number"] if i < len(chapters) - 1 else None

    # Group chapters into modules.
    modules_dict: dict[int, dict] = {}
    for c in chapters:
        mn = c["moduleNumber"]
        if mn not in modules_dict:
            modules_dict[mn] = {
                "number": mn,
                "title": c["moduleTitle"],
                "chapters": [],
            }
        modules_dict[mn]["chapters"].append(c)

    modules = [modules_dict[k] for k in sorted(modules_dict)]
    for i, m in enumerate(modules):
        m["icon"] = MODULE_ICONS[i % len(MODULE_ICONS)]

    course_data = {
        "id": course_id,
        "slug": f"visual-course-{course_id}",
        "title": config["title"],
        "subtitle": config["subtitle"],
        "modules": modules,
        "chaptersCount": len(chapters),
    }

    manifest_entry = {
        "id": course_id,
        "slug": f"visual-course-{course_id}",
        "title": config["title"],
        "subtitle": config["subtitle"],
        "icon": config.get("icon", "📚"),
        "chaptersCount": len(chapters),
        "modules": [
            {
                "number": m["number"],
                "title": m["title"],
                "icon": m["icon"],
                "chapters": [
                    {
                        "number": c["number"],
                        "slug": c["slug"],
                        "title": c["title"],
                    }
                    for c in m["chapters"]
                ],
            }
            for m in modules
        ],
    }

    return course_data, manifest_entry, image_sources


def main() -> None:
    all_image_sources: set[str] = set()
    manifest_courses: list[dict] = []
    search_index: list[dict] = []

    for config in COURSES:
        print(f"Processing {config['source_dir']}...")
        course_data, manifest_entry, image_sources = process_course(config)
        if not course_data:
            continue

        all_image_sources.update(image_sources)
        manifest_courses.append(manifest_entry)

        # Build the full-text search index for this course.
        for module in course_data["modules"]:
            for chapter in module["chapters"]:
                plain_text = re.sub(r"<[^>]+>", " ", str(chapter.get("body", "")))
                plain_text = re.sub(r"\s+", " ", plain_text).strip()
                search_index.append(
                    {
                        "courseId": course_data["id"],
                        "courseTitle": course_data["title"],
                        "courseIcon": config.get("icon", "📚"),
                        "courseSubtitle": course_data["subtitle"],
                        "moduleTitle": module["title"],
                        "chapterNumber": chapter["number"],
                        "chapterTitle": chapter["title"],
                        "number": chapter["number"],
                        "plainText": plain_text,
                        "snippet": plain_text[:300].strip(),
                    }
                )

        out_path = OUT_COURSES / f"{config['id']}.json"
        out_path.write_text(json.dumps(course_data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Wrote {out_path}")

    # Convert all referenced PNGs to WebP.
    total_original = 0
    total_new = 0
    for src in sorted(all_image_sources):
        p = Path(src)
        if not p.exists():
            print(f"Warning: missing image {src}")
            continue
        out = OUT_IMAGES / to_webp_name(p.name)
        with Image.open(p) as img:
            img.save(out, "WEBP", quality=85, method=6, optimize=True)
        original = p.stat().st_size
        new = out.stat().st_size
        total_original += original
        total_new += new
        print(f"  {p.name} -> {out.name} ({original/1024:.1f} KB -> {new/1024:.1f} KB)")

    if all_image_sources:
        print(
            f"Converted {len(all_image_sources)} images: "
            f"{total_original/1024/1024:.1f} MB -> {total_new/1024/1024:.1f} MB"
        )

    manifest = {
        "siteTitle": "Visual Agent Course Library",
        "siteSubtitle": "A visual course collection on modern agents, MCP, A2A, RAG, and full-stack agent systems.",
        "courses": manifest_courses,
    }
    (OUT_DATA / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {OUT_DATA / 'manifest.json'}")

    search_index_path = OUT_SEARCH / "search-index.json"
    search_index_path.write_text(
        json.dumps(search_index, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"Wrote {search_index_path}")


if __name__ == "__main__":
    main()
