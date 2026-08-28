"""Disposable local Git history. Never operates on the user's repository."""
import os
from pathlib import Path
import subprocess
import tempfile

with tempfile.TemporaryDirectory(prefix="git-team-lab-") as folder:
    root = Path(folder)
    env = dict(os.environ, GIT_AUTHOR_NAME="Training User", GIT_AUTHOR_EMAIL="training@example.invalid", GIT_COMMITTER_NAME="Training User", GIT_COMMITTER_EMAIL="training@example.invalid", GIT_CONFIG_NOSYSTEM="1")
    def git(*args, expected=0):
        result = subprocess.run(["git", "-c", "commit.gpgsign=false", "-c", "core.hooksPath=" + str(root / "no-hooks"), *args], cwd=root, env=env, text=True, capture_output=True)
        assert result.returncode == expected, result.stdout + result.stderr
        return result.stdout
    page = root / "policy.txt"
    git("init", "-b", "main")
    page.write_text("Review: optional\n", encoding="utf-8")
    git("add", "policy.txt"); git("commit", "-m", "baseline")
    git("switch", "-c", "feature/reviewer")
    page.write_text("Review: one colleague\n", encoding="utf-8")
    git("commit", "-am", "require colleague")
    git("switch", "main")
    page.write_text("Review: test evidence\n", encoding="utf-8")
    git("commit", "-am", "require evidence")
    git("merge", "feature/reviewer", expected=1)
    assert "<<<<<<<" in page.read_text(encoding="utf-8")
    page.write_text("Review: one colleague plus test evidence\n", encoding="utf-8")
    git("add", "policy.txt"); git("commit", "-m", "combine both requirements")
    assert len(git("rev-list", "--parents", "-n", "1", "HEAD").split()) == 3
    page.write_text("Review: unnecessary\n", encoding="utf-8")
    git("commit", "-am", "deliberately bad change")
    git("revert", "--no-edit", "HEAD")
    assert page.read_text(encoding="utf-8") == "Review: one colleague plus test evidence\n"
    print(git("log", "--oneline", "--graph", "--all"))
    print("PASS: real conflict, two-parent resolution, and history-preserving revert. Temporary repo removed on exit.")
