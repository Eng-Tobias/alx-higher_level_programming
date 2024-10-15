#!/usr/bin/python3
"""
MyInt is a rebel. MyInt inherits from int
and has the == and != operators inverted.
"""


class MyInt(int):
    """
    Inherits from int and overrides equality operators.
    """


    def __eq__(self, other):
        """
        Invert the behavior of the equality operator.
        """
        return super().__ne__(other)


    def __ne__(self, other):
        """
        Invert the behavior of the non-equality operator.
        """
        return super().__eq__(other)
