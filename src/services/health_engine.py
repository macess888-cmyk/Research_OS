from src.services.registry_engine import RegistryEngine
from src.services.graph_engine import GraphEngine


class HealthEngine:

    def __init__(self):
        self.registry = RegistryEngine()
        self.graph = GraphEngine()

    def report(self):

        return {
            "Sections": len(self.registry.all_sections()),
            "Content Files": sum(self.registry.summary().values()),
            "Graph Nodes": self.graph.node_count(),
            "Relationships": self.graph.edge_count(),
            "Node Types": len(self.graph.node_types()),
        }