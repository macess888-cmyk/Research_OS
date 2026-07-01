from src.geometry.geometry_framework import GeometryInspector
from src.graph.graph_engine import GraphEngineV2
from src.services.inspectable import Inspectable


class StructuralGeometry(GeometryInspector, Inspectable):
    name = "Structural Geometry"

    def __init__(self):
        self.graph = GraphEngineV2()

    def inspect(self):
        most_connected = self.graph.most_connected()

        return {
            "service": self.name,
            "status": "FOUNDATION",
            "healthy": True,
            "nodes": self.graph.node_count(),
            "edges": self.graph.edge_count(),
            "density": self.graph.density(),
            "isolated": len(self.graph.isolated_nodes()),
            "most_connected": most_connected["title"] if most_connected else "None",
            "geometry": "UNKNOWN → HOLD",
        }