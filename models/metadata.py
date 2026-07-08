from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Metadata:
    """
    Descriptive metadata for a Research Object.

    Metadata supports discovery, inspection and reporting.

    Metadata does NOT define graph topology.
    """

    tags: List[str] = field(default_factory=list)

    summary: str = ""

    status: str = "draft"

    source: Optional[str] = None

    author: Optional[str] = None

    created: datetime = field(default_factory=datetime.utcnow)

    modified: datetime = field(default_factory=datetime.utcnow)