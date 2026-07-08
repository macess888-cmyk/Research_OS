from dataclasses import dataclass


@dataclass
class Relationship:
    """
    Canonical semantic relationship between two Research Objects.

    Relationships define graph topology.

    Metadata never creates relationships.
    """

    source: str

    target: str

    relation_type: str

    evidence: str | None = None

    confidence: float = 1.0