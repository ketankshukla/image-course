"""Parse synthetic configuration without reading or printing real environment variables."""
from urllib.parse import urlparse
def load(values):
    mode=values.get("APP_ENV","development")
    if mode not in {"development","staging","production"}: raise ValueError("APP_ENV")
    raw=values.get("DEBUG","false").lower()
    if raw not in {"true","false"}: raise ValueError("DEBUG")
    debug=raw=="true"
    endpoint=values.get("API_URL", "http://127.0.0.1:4175")
    parsed=urlparse(endpoint)
    if parsed.scheme not in {"http","https"} or not parsed.hostname: raise ValueError("API_URL")
    if mode=="production" and (debug or parsed.scheme!="https"): raise ValueError("unsafe production configuration")
    return {"mode":mode,"debug":debug,"endpoint":endpoint}
assert load({"DEBUG":"false"})["debug"] is False
assert load({"APP_ENV":"production","API_URL":"https://example.invalid"})["mode"]=="production"
for invalid in ({"DEBUG":"yes"},{"APP_ENV":"prodution"},{"APP_ENV":"production"},{"APP_ENV":"production","API_URL":"https://example.invalid","DEBUG":"true"}):
    try: load(invalid)
    except ValueError: pass
    else: raise AssertionError(invalid)
print("PASS: explicit booleans, environment allowlist, valid endpoint, fail-closed production settings.")
