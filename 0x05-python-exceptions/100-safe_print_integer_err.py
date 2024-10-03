#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False

# Test cases
if __name__ == "__main__":
    values = [89, -89, "89", '89', 89.9, 0, None, [89]]
    for v in values:
        has_been_print = safe_print_integer_err(v)
