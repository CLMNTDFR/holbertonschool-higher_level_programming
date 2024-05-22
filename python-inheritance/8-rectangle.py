#!/usr/bin/python3

""" Rectangle class """


BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""
This module defines the Rectangle class which inherits from BaseGeometry.
It is used to represent a rectangle with a specific width and height.
"""


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.
    Attributes:
    __width (int): The width of the rectangle, a private instance attribute.
    __height (int): The height of the rectangle, a private instance attribute.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
