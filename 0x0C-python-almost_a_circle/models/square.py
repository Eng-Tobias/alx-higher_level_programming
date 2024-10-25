#!/usr/bin/python3
""" Square module that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Represents a square with attributes for size, x, and y.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square (optional).
            y (int): The y-coordinate of the square (optional).
            id (int): The id of the square (optional).
        """
        # Validate the size parameter as it serves as both width and height
        self.validate_size(size)
        
        # Call the super class constructor with size for width and height
        super().__init__(size, size, x, y, id)

    @staticmethod
    def validate_size(size):
        """Validate size as an integer greater than 0."""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be greater than 0")

    def __str__(self):
        """
        Return the string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
