"""Trace reconstruction and log minimization with synthetic events."""
events=[]
def emit(request_id, service, outcome, **fields):
    allowed={key:fields[key] for key in ("duration_ms","error_code") if key in fields}
    events.append({"request_id":request_id,"service":service,"outcome":outcome,**allowed})
emit("req-A","web","started",query="SYNTHETIC_PRIVATE_QUERY",token="SYNTHETIC_SECRET")
emit("req-B","web","ok",duration_ms=10)
emit("req-A","api","error",error_code="INDEX_TIMEOUT",duration_ms=250)
emit("req-A","web","error",error_code="UPSTREAM_FAILED",duration_ms=270)
chain=[e for e in events if e["request_id"]=="req-A"]
assert [e["service"] for e in chain]==["web","api","web"]
assert chain[1]["error_code"]=="INDEX_TIMEOUT"
assert all("query" not in e and "token" not in e for e in events)
requests=[e for e in events if e["service"]=="web" and e["outcome"]!="started"]
errors=sum(e["outcome"]=="error" for e in requests)
assert (errors,len(requests))==(1,2)
print("PASS: linked failure chain, allowlisted logging fields, 1 failed request out of 2 synthetic completed requests.")
print("This is a teaching log model, not an installed telemetry collector.")
