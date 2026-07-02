from src.graph.graph_engine import GraphEngineV2
from src.services.inspectable import Inspectable


class TopologyEngine(Inspectable):
    def __init__(self):
        self.graph = GraphEngineV2()

    def summary(self):
        degrees = self.graph.degree_map()

        if degrees:
            avg_degree = round(sum(degrees.values()) / len(degrees), 2)
        else:
            avg_degree = 0

        return {
            "nodes": self.graph.node_count(),
            "edges": self.graph.edge_count(),
            "density": self.graph.density(),
            "average_degree": avg_degree,
            "isolated_nodes": len(self.graph.isolated_nodes()),
            "most_connected": self.graph.most_connected(),
        }

    def boundary_report(self):
        isolated = self.graph.isolated_nodes()
        most = self.graph.most_connected()

        return {
            "isolated": isolated,
            "central": most,
        }

    def inspect(self):
        summary = self.summary()

        return {
            "service": "Topology Engine",
            "status": "READY",
            "healthy": True,
            "details": summary,
        }