#!/usr/bin/python3
"""
5-square.py - This module initializes a class called 'Square'.
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
            __size (int): The size of a square
            Defaults to 0.

        Raises:
            TypeError: The size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Check execption type and value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current square area.
        """
        return self.__size**2

    def my_print(self):
        """
        Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
