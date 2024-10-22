#!/usr/bin/python3
"""
Module that contains the Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x coordinate.
            y (int): y coordinate.
            id (int): id of the object (optional).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
