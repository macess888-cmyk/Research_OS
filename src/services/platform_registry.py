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
    Research OS Platform Registry

    Every subsystem is responsible for describing
    itself through inspect().

    The registry simply aggregates those descriptions.
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
        """
        Collect inspection reports from every
        registered service.
        """

        reports = []

        #
        # Register the kernel separately to avoid
        # circular imports.
        #
        try:
            from src.kernel.kernel import ResearchKernel

            reports.append(
                ResearchKernel().inspect()
            )

        except Exception as e:
            reports.append(
                {
                    "service": "Research Kernel",
                    "status": "WARNING",
                    "healthy": False,
                    "error": str(e),
                }
            )

        #
        # Register every remaining service.
        #
        for service in self.services_list:

            try:
                reports.append(
                    service.inspect()
                )

            except Exception as e:
                reports.append(
                    {
                        "service": service.__class__.__name__,
                        "status": "ERROR",
                        "healthy": False,
                        "error": str(e),
                    }
                )

        return reports

    def count(self):
        return len(self.services())