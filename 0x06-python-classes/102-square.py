#!/usr/bin/python3
"""
Module for Square class with comparison methods.
"""

class Square:
    """
    Class representing a square.
    """
    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size to set.
        
        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __lt__(self, other):
        """Return True if the square is smaller than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if the square is less than or equal to the other."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Return True if the square is equal to the other."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the square is not equal to the other."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Return True if the square is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if the square is greater than or equal to the other."""
        return self.area() >= other.area()
