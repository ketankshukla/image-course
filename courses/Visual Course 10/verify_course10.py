from pathlib import Path
import re

root = Path(__file__).resolve().parent / "diagram-docs"
required = [
    r"##\s+At a glance",
    r"##\s+What the diagram teaches",
    r"##\s+Case study",
    r"##\s+Composition",
    r"##\s+Element by element",
    r"##\s+Colour and flow semantics",
    r"##\s+How to present it",
    r"##\s+Lab and checkpoint",
    r"##\s+Glossary",
    r"##\s+Sources",
]
optional = [
    r"###\s+The Next\.js surface",
    r"###\s+The Python surface",
    r"###\s+Analogy",
]

failures = 0
for f in sorted(root.glob("*.md")):
    text = f.read_text(encoding="utf-8")
    words = len(re.findall(r"\b\w+\b", text))
    missing = [sec for sec in required if not re.search(sec, text, re.I)]
    present_optional = [sec for sec in optional if re.search(sec, text, re.I)]
    ok = words >= 2500 and not missing
    if not ok:
        failures += 1
    print(f"{f.name}: {words} words, required missing={missing or 'none'}, optional={present_optional}, ok={ok}")

print(f"\nFailures: {failures}")
