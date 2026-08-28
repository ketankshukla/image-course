"""Measured local query example: prints observed timings, never a promised speedup."""
import sqlite3
import time
import statistics
db=sqlite3.connect(":memory:")
db.execute("CREATE TABLE lessons(id INTEGER PRIMARY KEY, category TEXT, title TEXT)")
db.executemany("INSERT INTO lessons VALUES(?,?,?)",((i,"rare" if i%100==0 else "common",f"Lesson {i}") for i in range(10000)))
query="SELECT id,title FROM lessons WHERE category=?"
def measure():
    samples=[]
    for _ in range(21):
        start=time.perf_counter()
        rows=db.execute(query,("rare",)).fetchall()
        samples.append((time.perf_counter()-start)*1000)
    assert len(rows)==100
    return rows,statistics.median(samples[1:])
before,ms_before=measure()
plan_before=db.execute("EXPLAIN QUERY PLAN "+query,("rare",)).fetchall()
db.execute("CREATE INDEX lessons_category ON lessons(category)")
after,ms_after=measure()
plan_after=db.execute("EXPLAIN QUERY PLAN "+query,("rare",)).fetchall()
assert sorted(before)==sorted(after)
assert any("lessons_category" in row[3] for row in plan_after)
print("Before plan:",plan_before)
print("After plan:",plan_after)
print(f"Observed median milliseconds: before={ms_before:.4f}, after={ms_after:.4f}")
print("PASS: result equivalence and intended index usage. Timing ratio is not asserted or guaranteed.")
db.close()
