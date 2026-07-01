from datetime import datetime

from src.services.validation_engine import ValidationEngine
from src.services.health_engine import HealthEngine
from src.services.intelligence_engine import IntelligenceEngine


class MissionControl:

    def __init__(self):
        self.validation = ValidationEngine()
        self.health = HealthEngine()
        self.intelligence = IntelligenceEngine()

    def platform_report(self):
        return {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "health": self.health.report(),
            "validation": self.validation.validate(),
            "intelligence": self.intelligence.summary(),
        }