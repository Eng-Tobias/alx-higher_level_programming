#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
if safe_print_integer(value):
    print("Success")
else:
    print("Failed")

value = "Hello"
if safe_print_integer(value):
    print("Success")
else:
    print("Failed")
