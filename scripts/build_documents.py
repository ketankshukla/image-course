"""Render a supported case-study collection and workspace guides with embedded assets."""
import argparse
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
HOSPITAL = DOCS / "case-studies" / "hospital"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collection", choices=["hospital", "filepilot"], default="hospital")
    args = parser.parse_args()
    collection = DOCS / "case-studies" / args.collection
    pandoc = shutil.which("pandoc")
    if not pandoc:
        candidate = Path.home() / "AppData/Local/Pandoc/pandoc.exe"
        if candidate.is_file():
            pandoc = str(candidate)
    if not pandoc:
        raise SystemExit("Install Pandoc before building document editions.")
    documents = sorted(collection.rglob("*.md")) + [DOCS / "FOLDER-STRUCTURE.md", DOCS / "PUBLISHING-CASE-STUDIES.md"]
    for source in documents:
        title = source.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        subprocess.run([
            pandoc, source.name, "--from=gfm", "--to=html5", "--standalone",
            "--embed-resources", "--toc", "--toc-depth=2",
            f"--template={DOCS / 'assets/document.template.html'}",
            f"--css={DOCS / 'assets/document.css'}",
            *([f"--css={DOCS / 'assets/reading-document.css'}"] if args.collection == "filepilot" else []),
            "--metadata", f"title={title}",
            "--metadata", ("edition=FilePilot" if args.collection == "filepilot" else "edition=HarborCare") if source.parent != DOCS else "edition=Workspace guide",
            f"--output={source.with_suffix('.html').name}",
        ], cwd=source.parent, check=True)
        print(f"Rendered {source.relative_to(ROOT)}")
    print(f"Rendered {len(documents)} documents.")


if __name__ == "__main__":
    main()
