#!/usr/bin/python3

# Import the add function from add_0 module
from add_0 import add

# Assign values to variables a and b
a = 1
b = 2

# Use the print function with string formatting to display the result
print("{} + {} = {}".format(a, b, add(a, b)))
