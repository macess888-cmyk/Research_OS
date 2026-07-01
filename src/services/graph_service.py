import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "content" / "graph" / "graph.json"


def load_graph():
    with open(GRAPH, encoding="utf-8") as f:
        return json.load(f)