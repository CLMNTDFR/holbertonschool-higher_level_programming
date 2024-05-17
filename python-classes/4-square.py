#!/usr/bin/python3
"""
4-square.py - This module initializes a class called 'Square'.
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
        @property
        def size(self):
            return self.__size
        
        @size.setter
        def size(self, value):
        
            if not isinstance(size, int):
                raise TypeError("size must be an integer")

            if size < 0:
                raise ValueError("size must be >= 0")

                self.__size = size

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current square area.
        """
        return self.__size**2
