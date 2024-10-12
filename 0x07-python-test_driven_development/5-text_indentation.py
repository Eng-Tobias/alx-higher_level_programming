#!/usr/bin/python3
"""Function to print text with indentation."""

def text_indentation(text):
    """Print text with 2 new lines after ., ?, and :.

    Args:
        text: The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char in {'.', '?', ':'}:
            print("\n")
