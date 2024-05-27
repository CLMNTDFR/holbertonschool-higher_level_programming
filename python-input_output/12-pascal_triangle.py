#!/usr/bin/python3

"""
Pascal's Triangle Function
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle of n.

    Args:
        n (int): The number of rows to generate in
        the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.

    """
    # Initialize the result list to store the Pascal's triangle
    pascal_result = []

    # Check if n is less than or equal to zero
    if n <= 0:
        return pascal_result

    # Generate each row of the Pascal's triangle
    current_line = [1]
    for _ in range(n):
        # Add the current line to the result
        pascal_result.append(current_line)

        # Generate the next line
        new_line = [1]
        for i in range(len(current_line) - 1):
            new_line.append(current_line[i] + current_line[i + 1])
        new_line.append(1)

        # Update the current line for the next iteration
        current_line = new_line

    return pascal_result
