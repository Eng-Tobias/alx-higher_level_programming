#!/usr/bin/python3
"""
Test the MyInt class.
"""
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)          # Should print: 3
print(my_i == 3)    # Should print: False
print(my_i != 3)    # Should print: True
