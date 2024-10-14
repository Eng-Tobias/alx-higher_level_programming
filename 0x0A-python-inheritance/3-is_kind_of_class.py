#!/usr/bin/python3
"""
This module defines the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or
    an instance of a class that inherited from a_class, else False
    """
    return isinstance(obj, a_class)
