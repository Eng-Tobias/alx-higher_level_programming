#!/usr/bin/python3
safe_print_string = __import__('6-raise_exception').safe_print_string

value = "Hello, World!"
if safe_print_string(value):
    print("Success")
else:
    print("Failed")
