import json
from pathlib import Path
from datetime import datetime

from src.services.inspectable import Inspectable

ROOT = Path(__file__).resolve().parents[2]
EVENT_DIR = ROOT / "content" / "events"
EVENT_FILE = EVENT_DIR / "events.json"


class EventEngine(Inspectable):
    def __init__(self):
        EVENT_DIR.mkdir(parents=True, exist_ok=True)

        if not EVENT_FILE.exists():
            EVENT_FILE.write_text("[]", encoding="utf-8")

    def publish(self, category, action, status="INFO", details=None):
        events = self.all_events()

        event = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "category": category,
            "action": action,
            "status": status,
            "details": details or {},
        }

        events.insert(0, event)

        EVENT_FILE.write_text(
            json.dumps(events, indent=2),
            encoding="utf-8",
        )

        return event

    def all_events(self):
        try:
            return json.loads(EVENT_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []

    def recent(self, limit=10):
        return self.all_events()[:limit]

    def count(self):
        return len(self.all_events())

    def inspect(self):
        return {
            "service": "Event Engine",
            "status": "READY",
            "healthy": True,
            "events": self.count(),
            "event_file": str(EVENT_FILE),
        }