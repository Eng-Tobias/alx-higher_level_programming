#!/usr/bin/python3
""" Rectangle module that inherits from Base """
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    Represents a rectangle with attributes for width, height, x, and y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle (optional).
            y (int): The y-coordinate of the rectangle (optional).
            id (int): The id of the rectangle (optional).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Return the area of the rectangle.
        Area = width * height
        """
        return self.width * self.height

    def display(self):
        """
        Print the rectangle with the character # using the x and y attributes.
        """
        # Print y spaces first
        for _ in range(self.y):
            print()
        
        # Print rectangle
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Return the string representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    # Add additional validation methods here if needed.
