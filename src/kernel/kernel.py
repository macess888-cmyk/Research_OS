from src.services.object_engine import ObjectEngine
from src.services.relationship_engine import RelationshipEngine
from src.services.navigator_engine import NavigatorEngine
from src.services.analytics_engine import AnalyticsEngine
from src.services.platform_registry import PlatformRegistry
from src.graph.graph_engine import GraphEngineV2


class ResearchKernel:
    """
    Central orchestration layer for Research OS.

    Pages should interact with the kernel instead of
    directly coordinating multiple services.
    """

    def __init__(self):
        self.objects = ObjectEngine()
        self.relationships = RelationshipEngine()
        self.navigator = NavigatorEngine()
        self.analytics = AnalyticsEngine()
        self.graph = GraphEngineV2()
        self.registry = PlatformRegistry()

    def status(self):
        return {
            "kernel": "READY",
            "version": "1.4.0",
            "objects": self.objects.count(),
            "relationships": self.relationships.relationship_count(),
            "nodes": self.graph.node_count(),
            "edges": self.graph.edge_count(),
            "density": self.graph.density(),
            "services": len(self.registry.services()),
        }

    def search(self, query):
        return self.navigator.search(query)

    def explore(self, object_id):
        return self.navigator.explore(object_id)

    def analytics_summary(self):
        return self.analytics.summary()

    def services(self):
        return self.registry.services()