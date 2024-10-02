#!/usr/bin/python3
"""
Module for MagicClass that calculates area and circumference.
"""
import math

class MagicClass:
    """
    Class representing a magic circle.
    """
    def __init__(self, radius=0):
        """
        Initialize a new magic class.

        Args:
            radius (int or float, optional): The radius of the circle. Defaults to 0.
        
        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the magic circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the magic circle."""
        return 2 * math.pi * self.__radius
