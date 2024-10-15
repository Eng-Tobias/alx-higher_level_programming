#!/usr/bin/python3
"""
10-main.py
Test the Rectangle class.
"""

Rectangle = __import__('9-rectangle').Rectangle

# Create instances of Rectangle
r1 = Rectangle(4, 6)
r2 = Rectangle(2, 8)

# Print string representation and area of the rectangles
print(r1)          # Expected output: [Rectangle] 4/6
print(r1.area())   # Expected output: 24

print(r2)          # Expected output: [Rectangle] 2/8
print(r2.area())   # Expected output: 16

# Attempt to create rectangles with invalid dimensions
try:
    r3 = Rectangle(0, 5)  # This should raise a ValueError
except Exception as e:
    print(e)              # Expected: width must be greater than 0

try:
    r4 = Rectangle(4, -3)  # This should raise a ValueError
except Exception as e:
    print(e)               # Expected: height must be greater than 0

try:
    r5 = Rectangle("3", 5)  # This should raise a TypeError
except Exception as e:
    print(e)               # Expected: width must be an integer
