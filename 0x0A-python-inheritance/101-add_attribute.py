#!/usr/bin/python3
"""
Function to add a new attribute to an object if possible.
"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute to add.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
