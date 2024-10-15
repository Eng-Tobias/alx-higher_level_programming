#!/usr/bin/python3
"""Module that defines a Rectangle class with area and str representation."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to represent a rectangle with area calculation and custom str."""

    def __init__(self, width, height):
        """Initialize width and height, and validate them."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
