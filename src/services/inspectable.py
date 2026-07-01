class Inspectable:
    """
    Base interface for all inspectable Research OS services.

    Every service is responsible for describing
    its own observable state.
    """

    def inspect(self):
        raise NotImplementedError(
            "Inspectable services must implement inspect()."
        )