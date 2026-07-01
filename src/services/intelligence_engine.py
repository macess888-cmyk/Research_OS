from src.services.registry_engine import RegistryEngine
from src.services.graph_engine import GraphEngine


class IntelligenceEngine:

    def __init__(self):
        self.registry = RegistryEngine()
        self.graph = GraphEngine()

    def summary(self):

        registry = self.registry.summary()

        return {
            "sections": len(registry),
            "files": sum(registry.values()),
            "graph_nodes": self.graph.node_count(),
            "graph_edges": self.graph.edge_count(),
            "graph_types": len(self.graph.node_types())
        }

    def orphan_nodes(self):

        orphaned = []

        for node in self.graph.nodes:
            if not self.graph.relationships(node["id"]):
                orphaned.append(node)

        return orphaned

    def graph_density(self):

        n = self.graph.node_count()

        if n <= 1:
            return 0

        return round(
            self.graph.edge_count() / n,
            2
        )