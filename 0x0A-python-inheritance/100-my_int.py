class MyInt(int):
    """Class that inherits from int, with inverted == and != operators."""

    def __eq__(self, other):
        """Return False if self is equal to other, True otherwise."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True if self is equal to other, False otherwise."""
        return super().__eq__(other)
