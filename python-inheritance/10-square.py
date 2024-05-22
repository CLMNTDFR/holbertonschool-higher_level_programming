#!/usr/bin/python3

""" Square class """

Rectangle = __import__("9-rectangle").Rectangle

"""
This module defines the Square class which inherits from Rectangle,
itself which inherits from BaseGeometry.
It is used to represent a square with a specific size.
"""


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from Rectangle.
    Attributes:
    __size (int): The size of the square, a private instance attribute.
    """

    def __init__(self, size):
        """Initialize a new Square instance.
        Args:
            size (int): The size of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current rectangle area.
        """
        return super().area()
