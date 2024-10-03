#!/usr/bin/python3

def safe_print_string(value):
    try:
        print(value)
        return True
    except Exception:
        return False
