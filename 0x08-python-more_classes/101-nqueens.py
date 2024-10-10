#!/usr/bin/python3
import sys


def print_usage():
    """Print usage information."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_input(n):
    """Check if the input is a valid integer greater than or equal to 4."""
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def solve_nqueens(n):
    """Solve the N queens puzzle."""
    # Your implementation here


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    N = is_valid_input(sys.argv[1])
    solve_nqueens(N)
