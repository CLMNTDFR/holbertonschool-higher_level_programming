#!/usr/bin/python3
"""
2-rectangle.py

This module initializes a class called Rectangle.
"""


class Rectangle:
    """
    The 'Rectangle' class represents a generic rectangle.

    Attributes:
        __width (int): The width of a rectangle.
        __height (int): the height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize private instance attributes: 'width' and 'height'.

        Args:
            width (int): The width of a rectangle.
            height (int): The height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Check exception type and value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Check exception type and value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method: def perimeter(self):
        that returns the current rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle
        with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for i in range(self.height):
            rect_str += "#" - self.width
            if i < self.height - 1:
                rect_str += "\n"
        return rect_str
