from collections import defaultdict

from src.services.object_engine import ObjectEngine
from src.services.relationship_engine import RelationshipEngine


class GraphEngineV2:
    def __init__(self):
        self.objects = ObjectEngine()
        self.relationships = RelationshipEngine()
        self.nodes = self.objects.load_all()
        self.edges = self._build_edges()

    def _build_edges(self):
        edges = []

        relationship_map = self.relationships.relationship_map()

        for source, targets in relationship_map.items():
            for target in targets:
                edges.append(
                    {
                        "source": source,
                        "target": target,
                    }
                )

        return edges

    def node_count(self):
        return len(self.nodes)

    def edge_count(self):
        return len(self.edges)

    def node_lookup(self):
        return {
            node.get("id"): node
            for node in self.nodes
            if node.get("id")
        }

    def degree_map(self):
        degrees = defaultdict(int)

        for edge in self.edges:
            degrees[edge["source"]] += 1
            degrees[edge["target"]] += 1

        return dict(degrees)

    def most_connected(self):
        degrees = self.degree_map()

        if not degrees:
            return None

        node_id = max(degrees, key=degrees.get)
        node = self.node_lookup().get(node_id)

        return {
            "id": node_id,
            "title": node.get("title", node_id) if node else node_id,
            "degree": degrees[node_id],
        }

    def isolated_nodes(self):
        degrees = self.degree_map()
        isolated = []

        for node in self.nodes:
            node_id = node.get("id")

            if node_id and degrees.get(node_id, 0) == 0:
                isolated.append(node)

        return isolated

    def density(self):
        n = self.node_count()

        if n <= 1:
            return 0

        possible_edges = n * (n - 1)

        return round(self.edge_count() / possible_edges, 3)