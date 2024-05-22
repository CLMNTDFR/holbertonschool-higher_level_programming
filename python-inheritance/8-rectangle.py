#!/usr/bin/python3


"""
8-base_geometry.py

This module initializes a class called BaseGeometry.
"""


class BaseGeometry:
    """
    The 'BaseGeometry' class.
    """

    def __init__(self):
        """Initialize the class (even if empty)."""
        pass

    def area(self):
        """
        Public instance method: def area(self):
        raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value:
        raise a TypeError if value is not an int
        raise a ValueError if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    The subclass 'Rectangle'.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        width and height must be validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
