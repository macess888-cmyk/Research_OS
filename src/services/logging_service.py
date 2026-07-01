from pathlib import Path
from datetime import datetime

from src.services.inspectable import Inspectable

ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "research_os.log"


class LoggingService(Inspectable):
    def __init__(self):
        LOG_DIR.mkdir(exist_ok=True)

    def write(self, level, source, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = (
            f"[{timestamp}] "
            f"[{level}] "
            f"[{source}] "
            f"{message}\n"
        )

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)

    def info(self, source, message):
        self.write("INFO", source, message)

    def warning(self, source, message):
        self.write("WARNING", source, message)

    def error(self, source, message):
        self.write("ERROR", source, message)

    def read(self):
        if not LOG_FILE.exists():
            return []

        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return f.readlines()

    def inspect(self):
        return {
            "service": "Logging Service",
            "status": "READY",
            "healthy": True,
            "entries": len(self.read()),
            "log_file": str(LOG_FILE),
        }