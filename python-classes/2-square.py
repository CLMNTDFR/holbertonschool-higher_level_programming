#!/usr/bin/python3
"""
2-square.py

This module initializes a class called 'Square' who
contains a private instance attribute: 'size'.
"""


class Square:
    """
    The 'Square' class represents a generic square.

    Attributes:
        __size (int): The size of a square.
    """

    def __init__(self, size=0):
        """
        Initialize a private instance attribute: 'size'.

        Args:
            __size (int): The size of a square.

        Raises:
            TypeError: The size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
