#!/usr/bin/python3
"""
Test the add_attribute function.
"""


class MyClass():
    """
    A sample class for testing.
    """
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)  # Should print: John


a = "My String"
try:
    add_attribute(a, "name", "Bob")
    print(a.name)  # This line should not be reached
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  # Should print: [TypeError] can't add new attribute
