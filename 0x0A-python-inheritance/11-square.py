#!/usr/bin/python3
""" 11-square.py module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class that inherits from Square class.
    Square  class is located in 9-rectangle.py
    module.
    """

    def __init__(self, size):
        self.__size = sizesuper().__init__(size, size)
        self.integer_validator("size", self.__size)
        self.__width = self.__size
        self.__height = self.__size

    def area(self):
        """returns the area of the Square"""

        return self.__width*self.__height

    def __str__(self):
        """changing the default implementation of str mmethod"""

        return("[Square] {}/{}".format(self.__width, self.__height))
