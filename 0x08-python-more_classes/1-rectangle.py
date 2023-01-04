#!/usr/bin/python3
"""1-rectangle module, it contains one class"""


class Rectangle:
    """
    it defines a rectangle with a private insatance
    width and height
    """

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, int) is not True:
            raise ValueError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
