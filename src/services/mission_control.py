from datetime import datetime

from src.services.validation_engine import ValidationEngine
from src.services.health_engine import HealthEngine
from src.services.intelligence_engine import IntelligenceEngine
from src.graph.graph_engine import GraphEngineV2


class MissionControl:
    def __init__(self):
        self.validation = ValidationEngine()
        self.health = HealthEngine()
        self.intelligence = IntelligenceEngine()
        self.graph = GraphEngineV2()

    def platform_report(self):
        most_connected = self.graph.most_connected()

        return {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "health": self.health.report(),
            "validation": self.validation.validate(),
            "intelligence": self.intelligence.summary(),
            "graph": {
                "nodes": self.graph.node_count(),
                "edges": self.graph.edge_count(),
                "density": self.graph.density(),
                "isolated": len(self.graph.isolated_nodes()),
                "most_connected": most_connected["title"] if most_connected else "None",
            },
        }