#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)
print(r)  # This should print [Rectangle] 3/5
print("Area:", r.area())  # This should print Area: 15
