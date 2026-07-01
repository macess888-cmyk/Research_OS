import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "content" / "graph" / "graph.json"


class GraphEngine:

    def __init__(self):
        with open(GRAPH, encoding="utf-8") as f:
            self.graph = json.load(f)

        self.nodes = self.graph["nodes"]
        self.edges = self.graph["edges"]

        self.lookup = {
            node["id"]: node
            for node in self.nodes
        }

    def node_count(self):
        return len(self.nodes)

    def edge_count(self):
        return len(self.edges)

    def node_types(self):
        counts = {}

        for node in self.nodes:
            t = node["type"]
            counts[t] = counts.get(t, 0) + 1

        return counts

    def neighbors(self, node_id):
        result = []

        for edge in self.edges:
            if edge["from"] == node_id:
                result.append(self.lookup[edge["to"]])

            elif edge["to"] == node_id:
                result.append(self.lookup[edge["from"]])

        return result

    def relationships(self, node_id):
        rels = []

        for edge in self.edges:
            if edge["from"] == node_id:
                rels.append(edge)

            elif edge["to"] == node_id:
                rels.append(edge)

        return rels