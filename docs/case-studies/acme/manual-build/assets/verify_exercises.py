"""Execute the workbooks' small pure-Python lessons; not application integration tests."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent

def lesson_function(filename, name):
    text = (ROOT / filename).read_text(encoding='utf-8')
    for code in re.findall(r'```python\n(.*?)```', text, re.S):
        if f'def {name}(' in code:
            namespace = {}
            exec(compile(code, filename, 'exec'), namespace)
            return namespace[name]
    raise AssertionError(name)

def rejects(fn, args, error):
    try:
        fn(*args)
    except error:
        return
    raise AssertionError((fn.__name__, args))

money = lesson_function('01-FOUNDATIONS.md', 'remaining_charge')
assert money(12000, 7500) == 4500
for args in [(-1, 0), (100, -1), (100, 101)]:
    rejects(money, args, ValueError)
rejects(money, (100, True), TypeError)
credit = lesson_function('02-MCP-GATEWAY.md', 'validate_credit_amount')
assert credit(7500, 12000) is None
for args in [(0, 100), (-1, 100), (101, 100)]:
    rejects(credit, args, ValueError)
rejects(credit, (True, 100), TypeError)
chunk = lesson_function('03-RAG-WORKBENCH.md', 'chunk_text')
assert chunk('') == []
assert chunk('one two three four five', 3, 1) == ['one two three', 'three four five']
assert chunk('one two three', 3, 1) == ['one two three']
rejects(chunk, ('abc', 3, 3), ValueError)
finance = lesson_function('04-A2A-SPECIALISTS.md', 'calculate_credit')
assert finance(12000, 7500, True) == 7500
assert finance(12000, 7500, False) == 0
assert finance(5000, 7500, True) == 5000
rejects(finance, (-1, 100, True), ValueError)
rejects(finance, (100, 100, 'yes'), TypeError)
transition = lesson_function('05-DURABLE-WORKFLOW.md', 'transition')
assert transition('RECEIVED', 'start') == 'GATHERING'
assert transition('EXECUTING', 'response_unknown') == 'RECONCILING'
assert transition('RECONCILING', 'receipt_found') == 'COMPLETED'
rejects(transition, ('RECEIVED', 'receipt_found'), ValueError)
for svg in (ROOT / 'assets').glob('*.svg'):
    ET.parse(svg)
print('PASS: five pure-Python lessons (23 checks) and three SVG XML documents. Full application not built or tested.')
