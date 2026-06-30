from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"

def search_content(query: str):
    query = query.strip().lower()
    results = []

    if not query:
        return results

    for path in CONTENT.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()

        if query in lower:
            lines = text.splitlines()
            matches = []

            for i, line in enumerate(lines, start=1):
                if query in line.lower():
                    matches.append((i, line.strip()))

            results.append({
                "path": path.relative_to(CONTENT),
                "matches": matches[:5],
            })

    return results