from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]

def count_files(pattern):
    return len(list(ROOT.rglob(pattern)))

def count_git_commits():
    try:
        result = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception:
        return "N/A"

def get_dashboard_stats():
    return {
        "Markdown Files": count_files("*.md"),
        "Python Files": count_files("*.py"),
        "Images": count_files("*.jpg") + count_files("*.jpeg") + count_files("*.png"),
        "Git Commits": count_git_commits(),
    }