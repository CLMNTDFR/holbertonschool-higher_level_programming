#!/usr/bin/python3
"""
This module provides a function add_integer that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if they are floats.

    Args:
        a: The first number, which must be an integer or float.
        b: The second number, which must be an integer or float. Default is 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        The sum of the two numbers as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
