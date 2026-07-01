import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT_FILE = ROOT / "content" / "projects" / "projects.json"


class ProjectEngine:
    def __init__(self):
        with open(PROJECT_FILE, encoding="utf-8") as f:
            self.data = json.load(f)

    def projects(self):
        return self.data.get("projects", [])

    def count(self):
        return len(self.projects())

    def get(self, project_id):
        for project in self.projects():
            if project["id"] == project_id:
                return project
        return None