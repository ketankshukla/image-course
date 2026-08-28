"""Render a supported case-study collection and workspace guides with embedded assets."""
import argparse
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
HOSPITAL = DOCS / "case-studies" / "hospital"
TRAINING_EDITIONS = {
    "coding-confidence": "Coding with Confidence",
    "ci-cd": "CI/CD Workshop", "debugging": "Debugging Workshop", "testing": "Testing Workshop",
    "http-api": "HTTP/API Workshop", "git-team": "Git Team Workshop", "databases": "Database Workshop",
    "identity": "Identity Workshop", "configuration": "Configuration Workshop", "background-jobs": "Reliable Jobs Workshop",
    "observability": "Observability Workshop", "docker": "Docker Workshop", "refactoring": "Refactoring Workshop",
    "accessibility": "Interface Workshop", "performance": "Performance Workshop", "codebase": "Codebase Workshop",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collection", choices=["hospital", "filepilot", "evidence-desk", *TRAINING_EDITIONS, "all-training"], default="hospital")
    args = parser.parse_args()
    training = args.collection in TRAINING_EDITIONS or args.collection == "all-training"
    collection = DOCS / ("training" if training else "case-studies") / args.collection
    pandoc = shutil.which("pandoc")
    if not pandoc:
        candidate = Path.home() / "AppData/Local/Pandoc/pandoc.exe"
        if candidate.is_file():
            pandoc = str(candidate)
    if not pandoc:
        raise SystemExit("Install Pandoc before building document editions.")
    if args.collection == "all-training":
        documents = sorted((DOCS / "training").glob("*.md"))
        for slug in TRAINING_EDITIONS:
            documents.extend(sorted((DOCS / "training" / slug).glob("*.md")))
    else:
        documents = sorted(collection.glob("*.md")) if training else sorted(collection.rglob("*.md")) + [DOCS / "FOLDER-STRUCTURE.md", DOCS / "PUBLISHING-CASE-STUDIES.md"]
    for source in documents:
        title = source.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        edition = TRAINING_EDITIONS.get(source.parent.name, "Engineering Workshops") if training else {"filepilot": "FilePilot", "evidence-desk": "Five Layers of AI Engineering"}.get(args.collection, "HarborCare")
        subprocess.run([
            pandoc, source.name, "--from=gfm", "--to=html5", "--standalone",
            "--embed-resources", "--toc", "--toc-depth=2",
            f"--template={DOCS / 'assets/document.template.html'}",
            f"--css={DOCS / 'assets/document.css'}",
            *([f"--css={DOCS / 'assets/reading-document.css'}"] if training or args.collection in ("filepilot", "evidence-desk") else []),
            "--metadata", f"title={title}",
            "--metadata", f"edition={edition}" if source.parent != DOCS else "edition=Workspace guide",
            f"--output={source.with_suffix('.html').name}",
        ], cwd=source.parent, check=True)
        if training or args.collection == "evidence-desk":
            output = source.with_suffix('.html')
            reading = output.read_text(encoding='utf-8')
            reading = re.sub(r'href="((?!https?://)[^"#]+)\.md(#[^"]*)?"', lambda match: f'href="{match[1]}.html{match[2] or ""}"', reading)
            output.write_text(reading, encoding='utf-8')
        print(f"Rendered {source.relative_to(ROOT)}")
    print(f"Rendered {len(documents)} documents.")


if __name__ == "__main__":
    main()
