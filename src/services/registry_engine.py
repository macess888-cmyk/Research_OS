from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"


class RegistryEngine:

    def __init__(self):
        self.content = CONTENT

    def files(self, section):
        folder = self.content / section

        if not folder.exists():
            return []

        return sorted(folder.rglob("*.md"))

    def count(self, section):
        return len(self.files(section))

    def all_sections(self):
        return sorted(
            [
                p.name
                for p in self.content.iterdir()
                if p.is_dir()
            ]
        )

    def summary(self):
        return {
            section: self.count(section)
            for section in self.all_sections()
        }