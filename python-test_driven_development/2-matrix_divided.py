#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A list of lists where each sublist contains integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if the rows of the matrix are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row size consistency
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide and round the matrix elements
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
