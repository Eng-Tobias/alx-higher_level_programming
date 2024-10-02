#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
    size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
        size (int): The size of the square. Default is 0.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2
