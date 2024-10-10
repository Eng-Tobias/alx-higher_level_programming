#!/usr/bin/python3
import sys

def print_usage():
    print("Usage: nqueens N")
    sys.exit(1)

def is_valid_input(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def solve_nqueens(n):
    def can_place(queens, row, col):
        for r, c in queens:
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def place_queen(queens, row):
        if row == n:
            solutions.append(queens.copy())
            return
        for col in range(n):
            if can_place(queens, row, col):
                queens.append((row, col))
                place_queen(queens, row + 1)
                queens.pop()

    solutions = []
    place_queen([], 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    N = is_valid_input(sys.argv[1])
    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)
