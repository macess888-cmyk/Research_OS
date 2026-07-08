from collections import defaultdict

from src.services.inspectable import Inspectable
from src.services.object_engine import ObjectEngine


class RelationshipEngine(Inspectable):
    def __init__(self):
        self.objects = ObjectEngine()

    def relationship_map(self):
        graph = defaultdict(list)

        legacy_fields = [
            "projects",
            "software",
            "concepts",
            "publications",
            "repositories",
            "collaborators",
            "timeline",
            "datasets",
        ]

        for obj in self.objects.load_all():
            source = obj.get("id")

            for relationship in obj.get("relationships", []):
                target = relationship.get("target")

                if target:
                    graph[source].append(target)

            for field in legacy_fields:
                values = obj.get(field, [])

                if isinstance(values, str):
                    values = [values]

                for value in values:
                    graph[source].append(value)

        return dict(graph)

    def related(self, object_id):
        related_objects = []
        ids = self.relationship_map().get(object_id, [])

        for rid in ids:
            obj = self.objects.get(rid)

            if obj:
                related_objects.append(obj)
            else:
                related_objects.append({
                    "id": rid,
                    "title": str(rid).replace("_", " ").title(),
                    "type": "unknown",
                })

        return related_objects

    def relationship_count(self):
        return sum(
            len(v)
            for v in self.relationship_map().values()
        )

    def orphan_objects(self):
        graph = self.relationship_map()
        incoming = set()

        for values in graph.values():
            incoming.update(values)

        orphaned = []

        for obj in self.objects.load_all():
            oid = obj["id"]
            outgoing = len(graph.get(oid, []))

            if oid not in incoming and outgoing == 0:
                orphaned.append(obj)

        return orphaned

    def completeness(self, object_id):
        obj = self.objects.get(object_id)

        if not obj:
            return None

        checks = {
            "summary": bool(obj.get("summary")),
            "status": bool(obj.get("status")),
            "tags": bool(obj.get("tags")),
            "relationships": len(self.related(object_id)) > 0,
        }

        score = sum(checks.values())
        total = len(checks)

        return {
            "score": score,
            "total": total,
            "checks": checks,
        }

    def inspect(self):
        return {
            "service": "Relationship Engine",
            "status": "READY",
            "healthy": True,
            "relationships": self.relationship_count(),
            "orphans": len(self.orphan_objects()),
        }