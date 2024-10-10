#!/usr/bin/python3
import sys

def print_solution(board):
    """Prints the board in the required format."""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)

def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row][col] without being attacked."""
    for i in range(row):
        # Check if any queen is in the same column or in the diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """Uses backtracking to solve the N Queens problem."""
    board = [-1] * N  # Initialize the board with -1 (no queens placed)
    
    def backtrack(row):
        """Backtracks through the board and tries placing queens."""
        if row == N:  # If all queens are placed, print the solution
            print_solution(board)
            return
        
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col  # Place the queen
                backtrack(row + 1)  # Move to the next row
                board[row] = -1  # Backtrack (remove the queen)

    backtrack(0)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(N)
