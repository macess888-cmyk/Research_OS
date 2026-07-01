from src.services.health_engine import HealthEngine
from src.services.validation_engine import ValidationEngine
from src.services.registry_engine import RegistryEngine
from src.services.graph_engine import GraphEngine
from src.services.workspace_engine import WorkspaceEngine
from src.services.repository_engine import RepositoryEngine
from src.services.intelligence_engine import IntelligenceEngine


class ResearchKernel:

    def __init__(self):

        self.health = HealthEngine()

        self.validation = ValidationEngine()

        self.registry = RegistryEngine()

        self.graph = GraphEngine()

        self.workspace = WorkspaceEngine()

        self.repositories = RepositoryEngine()

        self.intelligence = IntelligenceEngine()