from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"

def load_md(relative_path: str) -> str:
    file_path = CONTENT / relative_path
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    return f"Missing file: {relative_path}"