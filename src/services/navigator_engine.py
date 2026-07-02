from src.services.inspectable import Inspectable
from src.services.object_engine import ObjectEngine
from src.services.relationship_engine import RelationshipEngine


class NavigatorEngine(Inspectable):
    def __init__(self):
        self.objects = ObjectEngine()
        self.relationships = RelationshipEngine()

    def search(self, query: str):
        return self.objects.search(query)

    def explore(self, object_id: str):
        obj = self.objects.get(object_id)

        if not obj:
            return None

        return {
            "object": obj,
            "related": self.relationships.related(object_id),
            "completeness": self.relationships.completeness(object_id),
        }

    def statistics(self):
        return {
            "objects": self.objects.count(),
            "relationships": self.relationships.relationship_count(),
            "types": self.objects.by_type(),
        }

    def inspect(self):
        stats = self.statistics()

        return {
            "service": "Navigator Engine",
            "status": "READY",
            "healthy": True,
            "details": stats,
        }