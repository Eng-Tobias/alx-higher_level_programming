#!/usr/bin/python3
"""Divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with the results.

    Raises:
        TypeError: If matrix is not a matrix of integers/floats,
                    or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
