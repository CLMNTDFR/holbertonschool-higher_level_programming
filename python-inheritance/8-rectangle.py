#!/usr/bin/python3


"""
8-base_geometry.py

This module initializes a subclass Rectangle
(inherite from BaseGeometry)
"""


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


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
