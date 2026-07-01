from src.services.config_service import ConfigService
from src.services.event_engine import EventEngine
from src.services.logging_service import LoggingService
from src.services.analytics_engine import AnalyticsEngine
from src.services.object_engine import ObjectEngine
from src.services.relationship_engine import RelationshipEngine
from src.services.topology_engine import TopologyEngine
from src.geometry.structural_geometry import StructuralGeometry


class PlatformRegistry:
    """
    Self-description of Research OS.

    Every subsystem should be able to describe
    itself through this registry.
    """

    def __init__(self):
        self.config = ConfigService()
        self.events = EventEngine()
        self.logs = LoggingService()
        self.analytics = AnalyticsEngine()
        self.objects = ObjectEngine()
        self.relationships = RelationshipEngine()
        self.topology = TopologyEngine()
        self.geometry = StructuralGeometry()

    def services(self):
        topo = self.topology.summary()

        return [
            {
                "name": "Configuration",
                "status": "READY",
                "details": {
                    "Version": self.config.version,
                    "Author": self.config.author,
                },
            },
            {
                "name": "Object Engine",
                "status": "READY",
                "details": {
                    "Objects": self.objects.count(),
                },
            },
            {
                "name": "Relationship Engine",
                "status": "READY",
                "details": {
                    "Relationships": self.relationships.relationship_count(),
                },
            },
            {
                "name": "Topology Engine",
                "status": "READY",
                "details": {
                    "Nodes": topo["nodes"],
                    "Edges": topo["edges"],
                    "Density": topo["density"],
                },
            },
            {
                "name": "Geometry Framework",
                "status": "READY",
                "details": self.geometry.inspect(),
            },
            {
                "name": "Analytics Engine",
                "status": "READY",
                "details": self.analytics.summary(),
            },
            {
                "name": "Event Engine",
                "status": "READY",
                "details": {
                    "Events": self.events.count(),
                },
            },
            {
                "name": "Logging Service",
                "status": "READY",
                "details": {},
            },
        ]