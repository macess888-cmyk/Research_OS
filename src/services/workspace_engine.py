import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = ROOT / "content" / "workspace" / "repositories.json"


class WorkspaceEngine:
    def __init__(self):
        with open(WORKSPACE, encoding="utf-8") as f:
            self.data = json.load(f)

    def repositories(self):
        return self.data.get("repositories", [])

    def count(self):
        return len(self.repositories())

    def categories(self):
        counts = {}
        for repo in self.repositories():
            cat = repo.get("category", "Unknown")
            counts[cat] = counts.get(cat, 0) + 1
        return counts