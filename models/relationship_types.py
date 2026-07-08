"""
Canonical semantic relationship types for Research OS.

These define the allowed meanings of graph edges.
"""


RELATIONSHIP_TYPES = {

    "supports": "Provides evidence supporting another object.",

    "extends": "Builds upon an existing object.",

    "depends_on": "Requires another object to exist first.",

    "implements": "Represents an implementation of another object.",

    "derived_from": "Originates from another object.",

    "validated_by": "Has been validated by another object.",

    "cites": "References another object.",

    "contradicts": "Challenges or conflicts with another object.",

    "related_to": "General semantic relationship."
}