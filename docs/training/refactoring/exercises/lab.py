"""Characterization tests preserve existing output during a small refactor."""
def legacy(items):
    out=[]
    for item in items:
        if item["active"]:
            out.append({"id":item["id"],"label":item["title"].strip()})
    return sorted(out,key=lambda x:x["id"])
def is_visible(item): return item["active"]
def to_card(item): return {"id":item["id"],"label":item["title"].strip()}
def refactored(items): return sorted((to_card(x) for x in items if is_visible(x)),key=lambda x:x["id"])
cases=[[],[{"id":2,"title":" B ","active":True},{"id":1,"title":" A ","active":False}], [{"id":2,"title":" B ","active":True},{"id":1,"title":" A ","active":True}]]
expected=[[],[{"id":2,"label":"B"}],[{"id":1,"label":"A"},{"id":2,"label":"B"}]]
for data,want in zip(cases,expected):
    assert legacy(data)==want
    assert refactored(data)==want
print("PASS: three explicit characterization cases match before and after responsibility extraction.")
