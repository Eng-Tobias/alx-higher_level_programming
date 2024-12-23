#!/usr/bin/python3
"""Function to print a name."""

def say_my_name(first_name, last_name=""):
    """Print My name is <first_name> <last_name>.

    Args:
        first_name: The first name.
        last_name: The last name (default is empty).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
