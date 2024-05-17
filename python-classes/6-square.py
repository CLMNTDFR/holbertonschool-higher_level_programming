#!/usr/bin/python3
"""
6-square.py - This module initializes a class called 'Square'.
"""


class Square:
    """
    The 'Square' class represents a generic square.

    Attributes:
        __size (int): The size of a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize two privates instance attributes: 'size' & 'position'.

        Args:
            __size (int): The size of a square
            Defaults to 0.
            __position (tuple, int): The position of the square
            Defaults to 0.

        Raises:
            TypeError: The size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Check exception type and value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        """Return the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

        for i in range(self.__position[1]):
            print()

        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
