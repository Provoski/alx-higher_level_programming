#!/usr/bin/python
"""7-base_geometry.py module"""


class BaseGeometry:
    """defines a public instance methods; area, integer_validator"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is not True:
            raise TypeError(name+" "+"must be an integer")
        if value <= 0:
            raise ValueError(name+" "+"must be greater than 0")
