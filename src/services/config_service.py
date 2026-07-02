import json
from pathlib import Path

from src.services.inspectable import Inspectable


ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "config" / "settings.json"


class ConfigService(Inspectable):
    def __init__(self):
        with open(CONFIG, "r", encoding="utf-8") as f:
            self.settings = json.load(f)

    def get(self, *keys, default=None):
        value = self.settings

        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return default

        return value if value is not None else default

    @property
    def app_name(self):
        return self.get("application", "name")

    @property
    def version(self):
        return self.get("application", "version")

    @property
    def author(self):
        return self.get("application", "author")

    def inspect(self):
        return {
            "service": "Configuration Service",
            "status": "READY",
            "healthy": True,
            "application": self.app_name,
            "version": self.version,
            "author": self.author,
            "config_file": str(CONFIG),
        }