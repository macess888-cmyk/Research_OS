from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECTS = ROOT / "content" / "software" / "projects"

def list_projects():
    return sorted(PROJECTS.glob("*.md"))