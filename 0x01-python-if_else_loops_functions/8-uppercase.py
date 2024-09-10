#!/usr/bin/python3

def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:  # Check if the character is a lowercase letter
            # Convert lowercase to uppercase
            char = chr(ascii_val - 32)
        print(char, end='')  # Print the character without a newline
    print()  # Print a newline at the end
