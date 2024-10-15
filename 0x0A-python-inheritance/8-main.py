#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)  # This should print the string representation of the rectangle
print(dir(r))  # This shows the attributes and methods of the rectangle object

try:
    print("Rectangle: {} - {}".format(r.width, r.height))  # This will raise an exception
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  # Catch and print any exceptions

try:
    r2 = Rectangle(4, True)  # This should raise a TypeError
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
