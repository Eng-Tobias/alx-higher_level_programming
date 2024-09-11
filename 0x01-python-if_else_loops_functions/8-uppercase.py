#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Convert lowercase characters to uppercase
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()  # Print a new line after the loop
