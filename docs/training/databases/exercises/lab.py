"""SQLite schema, transaction and restoration rehearsal; all databases in memory."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys=ON")
db.executescript("CREATE TABLE lessons(id INTEGER PRIMARY KEY, title TEXT NOT NULL UNIQUE); CREATE TABLE progress(lesson_id INTEGER REFERENCES lessons(id), completed INTEGER NOT NULL CHECK(completed IN (0,1)));")
with db:
    db.execute("INSERT INTO lessons VALUES(?, ?)", (1, "FilePilot"))
backup = sqlite3.connect(":memory:")
db.backup(backup)
with db:
    db.execute("ALTER TABLE lessons ADD COLUMN summary TEXT NOT NULL DEFAULT ''")
    db.execute("UPDATE lessons SET summary=? WHERE id=?", ("Safe file operations", 1))
assert db.execute("SELECT title,summary FROM lessons").fetchone() == ("FilePilot", "Safe file operations")
try:
    with db:
        db.execute("INSERT INTO progress VALUES(1,1)")
        db.execute("INSERT INTO progress VALUES(999,1)")
except sqlite3.IntegrityError:
    pass
else:
    raise AssertionError("Expected foreign-key rejection")
assert db.execute("SELECT count(*) FROM progress").fetchone()[0] == 0
restored = sqlite3.connect(":memory:")
backup.backup(restored)
assert restored.execute("SELECT * FROM lessons").fetchall() == [(1,"FilePilot")]
assert len(restored.execute("PRAGMA table_info(lessons)").fetchall()) == 2
print("PASS: compatible column addition, backfill, all-or-nothing rollback, restored pre-migration schema/data.")
for connection in (db, backup, restored): connection.close()
