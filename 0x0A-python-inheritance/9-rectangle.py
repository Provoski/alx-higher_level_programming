#!/usr/bin/python3
""" 9-rectangle.py module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class that inherits from BaseGeometry class.
    BaseGeomtry class is located in 7-base_geometry.py
    module.
    with instantiation of width and height.
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator(width, self.__width)
        self.integer_validator(height, self.__height)

    def area(self):
        """returns the area of the Rectangle"""

        return self.__width*self.__height

    def __str__(self):
        """changing the default implementation of str method"""

        return("[Rectangle] {}/{}".format(self.__width, self.__height))
