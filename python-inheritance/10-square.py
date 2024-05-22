#!/usr/bin/python3

""" Square class """

Rectangle = __import__("9-rectangle.py").Rectangle

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
        # Assign the values to private attributes
        self.__size = size

        # Validate the assigned values using the integer_validator method
        self.integer_validator("size", self.__size)

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current rectangle area.
        """
        return self.__size**2
