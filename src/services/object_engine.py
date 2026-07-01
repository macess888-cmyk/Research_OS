import json
from pathlib import Path
from typing import Any

from src.services.inspectable import Inspectable

ROOT = Path(__file__).resolve().parents[2]
OBJECTS_DIR = ROOT / "content" / "objects"


class ObjectEngine(Inspectable):
    def __init__(self):
        OBJECTS_DIR.mkdir(parents=True, exist_ok=True)

    def object_files(self):
        return sorted(OBJECTS_DIR.rglob("*.json"))

    def load_all(self):
        objects = []

        for file in self.object_files():
            try:
                with open(file, encoding="utf-8") as f:
                    data = json.load(f)

                data["_file"] = str(file.relative_to(OBJECTS_DIR))
                objects.append(data)

            except Exception as e:
                objects.append({
                    "id": file.stem,
                    "type": "error",
                    "title": file.name,
                    "error": str(e),
                    "_file": str(file.relative_to(OBJECTS_DIR)),
                })

        return objects

    def count(self):
        return len(self.load_all())

    def by_type(self):
        counts = {}

        for obj in self.load_all():
            obj_type = obj.get("type", "unknown")
            counts[obj_type] = counts.get(obj_type, 0) + 1

        return counts

    def get(self, object_id: str) -> dict[str, Any] | None:
        for obj in self.load_all():
            if obj.get("id") == object_id:
                return obj
        return None

    def search(self, query: str):
        query = query.lower().strip()

        if not query:
            return []

        results = []

        for obj in self.load_all():
            text = json.dumps(obj, ensure_ascii=False).lower()

            if query in text:
                results.append(obj)

        return results

    def related(self, object_id: str):
        obj = self.get(object_id)

        if not obj:
            return []

        related_ids = set()

        for key in [
            "projects",
            "software",
            "publications",
            "concepts",
            "collaborators",
            "repositories",
            "timeline",
            "tags",
        ]:
            values = obj.get(key, [])

            if isinstance(values, str):
                values = [values]

            for value in values:
                related_ids.add(value)

        return [
            self.get(rel_id) or {
                "id": rel_id,
                "type": "external",
                "title": str(rel_id).replace("_", " ").title(),
            }
            for rel_id in sorted(related_ids)
        ]

    def inspect(self):
        return {
            "service": "Object Engine",
            "status": "READY",
            "healthy": True,
            "objects": self.count(),
            "types": self.by_type(),
            "object_directory": str(OBJECTS_DIR),
        }