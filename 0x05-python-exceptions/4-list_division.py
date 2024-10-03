#!/usr/bin/python3

def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        result = None
    finally:
        return result
