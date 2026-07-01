from pathlib import Path

from src.services.registry_engine import RegistryEngine
from src.services.graph_engine import GraphEngine


class ValidationEngine:

    def __init__(self):
        self.registry = RegistryEngine()
        self.graph = GraphEngine()

    def validate(self):

        report = []

        # Registry
        sections = self.registry.all_sections()

        if sections:
            report.append(("PASS", "Content registry loaded"))
        else:
            report.append(("FAIL", "No content sections found"))

        # Content
        files = sum(self.registry.summary().values())

        if files > 0:
            report.append(("PASS", f"{files} content files discovered"))
        else:
            report.append(("FAIL", "No content files found"))

        # Graph
        if self.graph.node_count() > 0:
            report.append(("PASS", f"{self.graph.node_count()} graph nodes"))
        else:
            report.append(("FAIL", "Knowledge graph is empty"))

        if self.graph.edge_count() > 0:
            report.append(("PASS", f"{self.graph.edge_count()} graph relationships"))
        else:
            report.append(("WARNING", "No graph relationships"))

        # Repository
        root = Path.cwd()

        if (root / ".git").exists():
            report.append(("PASS", "Git repository detected"))
        else:
            report.append(("WARNING", "Git repository not detected"))

        return report