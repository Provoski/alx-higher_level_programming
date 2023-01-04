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
        elif isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        if isinstance(self.__width, int) is not True:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError(" width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        if isinstance(self.__height, int) is not True:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
