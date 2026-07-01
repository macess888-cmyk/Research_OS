from src.services.object_engine import ObjectEngine
from src.services.relationship_engine import RelationshipEngine


class NavigatorEngine:
    def __init__(self):
        self.objects = ObjectEngine()
        self.relationships = RelationshipEngine()

    def search(self, query: str):
        """
        Search all research objects.
        """
        return self.objects.search(query)

    def explore(self, object_id: str):
        """
        Return an object together with its related objects.
        """
        obj = self.objects.get(object_id)

        if not obj:
            return None

        return {
            "object": obj,
            "related": self.relationships.related(object_id),
            "completeness": self.relationships.completeness(object_id),
        }

    def statistics(self):
        """
        Platform-wide navigation statistics.
        """
        return {
            "objects": self.objects.count(),
            "relationships": self.relationships.relationship_count(),
            "types": self.objects.by_type(),
        }