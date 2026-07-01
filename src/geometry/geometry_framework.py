class GeometryInspector:
    """
    Base class for all Research OS geometry inspectors.

    Geometry inspectors observe structure.
    They do not decide, execute, or assign authority.
    """

    name = "Geometry"

    def inspect(self):
        raise NotImplementedError(
            "Geometry inspectors must implement inspect()."
        )