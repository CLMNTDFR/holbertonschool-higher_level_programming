#!/usr/bin/python3
"""
0-square.py

This module initializes a class called 'Square' who
contains a private instance attribute: 'size'.
"""


class Square:
    """
    The 'Square' class represents a generic square.

    Attributes:
        __size (int): The size of a square.
    """

    def __init__(self, size):
        """
        Initialize a private instance attribute: 'size'.

        Args:
            __size (int): The size of a square.
        """
        self.__size = size
