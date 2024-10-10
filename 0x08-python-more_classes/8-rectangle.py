#!/usr/bin/python3
"""
This module defines a Rectangle class.
The Rectangle class provides functionalities to calculate the area,
perimeter, and string representation of a rectangle.
It also tracks the number of instances and allows comparison between
rectangles.
"""


class Rectangle:
    """
    Represents a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    # ...

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the rectangle with the larger area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        Returns:
            The rectangle with the larger area, or rect_1 if they are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
