#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class to represent a square, which is a special rectangle."""

    def __init__(self, size):
        """Initialize the square by validating the size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
