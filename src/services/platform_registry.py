from src.services.config_service import ConfigService
from src.services.event_engine import EventEngine
from src.services.logging_service import LoggingService
from src.services.analytics_engine import AnalyticsEngine
from src.services.object_engine import ObjectEngine
from src.services.relationship_engine import RelationshipEngine
from src.services.topology_engine import TopologyEngine
from src.services.task_scheduler import TaskScheduler
from src.services.navigator_engine import NavigatorEngine
from src.geometry.structural_geometry import StructuralGeometry


class PlatformRegistry:
    """
    Self-description of Research OS.

    Services describe themselves through inspect().
    """

    def __init__(self):
        self.services_list = [
            ConfigService(),
            ObjectEngine(),
            RelationshipEngine(),
            NavigatorEngine(),
            TopologyEngine(),
            StructuralGeometry(),
            AnalyticsEngine(),
            EventEngine(),
            LoggingService(),
            TaskScheduler(),
        ]

    def services(self):
        return [
            service.inspect()
            for service in self.services_list
        ]

    def count(self):
        return len(self.services())