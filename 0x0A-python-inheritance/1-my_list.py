#!/usr/bin/python3
"""
Module for MyList class that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        """
        print(sorted(self))
