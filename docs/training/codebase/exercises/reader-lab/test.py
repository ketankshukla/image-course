from service import visible_titles
assert visible_titles("")==["MCP basics"]
assert visible_titles("mCp")==["MCP basics"]
assert visible_titles("Unfinished")==[]
print("PASS: baseline published-only filtering. Whitespace query behavior is the learner's next change.")
