#!/usr/bin/python3
"""Module to indent text"""

def text_indentation(text):
    """Prints text with 2 new lines after ., ?, or :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    lines = [line.strip() for line in text.split("\n")]
    print("\n".join(lines))
