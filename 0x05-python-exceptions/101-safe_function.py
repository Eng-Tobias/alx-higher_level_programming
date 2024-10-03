#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)  # Call the function with provided arguments
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)  # Print the exception to stderr
        return None  # Return None if an error occurs

# Example functions to test safe_function
def print_message():
    print("This is a message.")

def my_div(a, b):
    return a / b  # Division function

def print_list(my_list, n):
    for i in range(n):
        print(my_list[i])  # Print elements of the list

# Testing safe_function with different cases
if __name__ == "__main__":
    # Test case: Calling print_message safely
    result = safe_function(print_message)
    
    # Test case: Correct division
    result = safe_function(my_div, 10, 2)
    print("Result of division:", result)

    # Test case: Division by zero
    result = safe_function(my_div, 10, 0)
    print("Result of division by zero:", result)

    # Test case: Printing list with valid n
    result = safe_function(print_list, [1, 2, 3, 4], 2)

    # Test case: Printing list with n greater than the list length
    result = safe_function(print_list, [1, 2, 3, 4], 10)
