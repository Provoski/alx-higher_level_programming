#!/usr/bin/python3
"""7-base_geometry.py module"""


class BaseGeometry:
    """defines a public instance methods; area, integer_validator"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an interger".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
