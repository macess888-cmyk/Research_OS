from src.services.inspectable import Inspectable
from src.services.object_engine import ObjectEngine
from src.services.relationship_engine import RelationshipEngine
from src.graph.graph_engine import GraphEngineV2


class AnalyticsEngine(Inspectable):
    def __init__(self):
        self.objects = ObjectEngine()
        self.relationships = RelationshipEngine()
        self.graph = GraphEngineV2()

    def summary(self):
        return {
            "objects": self.objects.count(),
            "relationships": self.relationships.relationship_count(),
            "graph_nodes": self.graph.node_count(),
            "graph_edges": self.graph.edge_count(),
            "graph_density": self.graph.density(),
            "isolated_nodes": len(self.graph.isolated_nodes()),
            "object_types": self.objects.by_type(),
        }

    def quality_report(self):
        report = []

        for obj in self.objects.load_all():
            object_id = obj.get("id")
            title = obj.get("title", object_id)
            issues = []

            if not obj.get("summary"):
                issues.append("Missing summary")

            if not obj.get("tags"):
                issues.append("Missing tags")

            if obj.get("type") == "project" and not obj.get("repository"):
                issues.append("Project missing repository")

            if obj.get("type") == "publication" and not obj.get("doi"):
                issues.append("Publication missing DOI")

            completeness = self.relationships.completeness(object_id)

            report.append({
                "id": object_id,
                "title": title,
                "type": obj.get("type", "unknown"),
                "issues": issues,
                "completeness": completeness,
            })

        return report

    def issue_count(self):
        return sum(
            len(item["issues"])
            for item in self.quality_report()
        )
        
    def inspect(self):
        summary = self.summary()

        return {
            "service": "Analytics Engine",
            "status": "READY",
            "healthy": True,
            "details": summary,
        }