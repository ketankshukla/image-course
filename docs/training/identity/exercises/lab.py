"""Authorization model only: principals represent already-verified server identities."""
def disclose(principal, record):
    if principal is None:
        return 401, None
    if principal["organization"] != record["organization"]:
        return 403, None
    allowed = {"care": ("case_id", "transport", "clinical_note"), "transport": ("case_id", "transport")}.get(principal["role"])
    if allowed is None:
        return 403, None
    return 200, {key: record[key] for key in allowed}

record = {"organization":"demo-hospital", "case_id":"synthetic-1", "transport":"Wheelchair vehicle", "clinical_note":"Synthetic restricted note", "internal_secret":"DO_NOT_DISCLOSE"}
assert disclose(None,record)==(401,None)
assert disclose({"organization":"other", "role":"care"},record)==(403,None)
assert disclose({"organization":"demo-hospital", "role":"unknown"},record)==(403,None)
status, payload=disclose({"organization":"demo-hospital", "role":"transport"},record)
assert status==200 and set(payload)=={"case_id","transport"}
assert "clinical_note" not in payload and "internal_secret" not in payload
assert set(disclose({"organization":"demo-hospital", "role":"care"},record)[1])=={"case_id","transport","clinical_note"}
print("PASS: missing identity, cross-organization access, unknown role, and field allowlists. Authentication itself is not implemented.")
