"""Atomic deduplication of a database-local effect. No external side effect."""
import sqlite3
db=sqlite3.connect(":memory:")
db.executescript("CREATE TABLE receipts(task_id TEXT PRIMARY KEY); CREATE TABLE effects(task_id TEXT PRIMARY KEY, detail TEXT NOT NULL);")
def process(task_id, fail=False):
    with db:
        if db.execute("SELECT 1 FROM receipts WHERE task_id=?",(task_id,)).fetchone(): return "duplicate"
        db.execute("INSERT INTO effects VALUES(?,?)",(task_id,"synthetic indexed document"))
        if fail: raise RuntimeError("crash before receipt")
        db.execute("INSERT INTO receipts VALUES(?)",(task_id,))
    return "completed"
try: process("task-1",True)
except RuntimeError: pass
assert db.execute("SELECT count(*) FROM effects").fetchone()[0]==0
assert process("task-1")=="completed"
assert process("task-1")=="duplicate"
assert db.execute("SELECT count(*) FROM effects").fetchone()[0]==1
print("PASS: simulated crash rolled back; retry completed; duplicate delivery did not repeat the database-local effect.")
db.close()
