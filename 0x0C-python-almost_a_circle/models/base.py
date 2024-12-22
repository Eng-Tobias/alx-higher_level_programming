#!/usr/bin/python3
"""
Module that contains the Base class.
"""


class Base:
    """
    Base class for managing id attribute in future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor. Initializes id attribute.

        Args:
            id (int): If not None, sets the id. Otherwise, increments
                      the __nb_objects and assigns the value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
