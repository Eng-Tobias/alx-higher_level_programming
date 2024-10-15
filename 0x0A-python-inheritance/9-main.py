#!/usr/bin/python3
"""Test for Rectangle class."""

Rectangle = __import__('8-rectangle').Rectangle

def main():
    # Create a Rectangle instance
    r = Rectangle(5, 3)

    # Print the area of the rectangle
    print("Area:", r.area())

    # Print the string representation of the rectangle
    print(r)

if __name__ == "__main__":
    main()
