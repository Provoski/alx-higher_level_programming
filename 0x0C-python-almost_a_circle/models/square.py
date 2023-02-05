#!/usr/bin/python3
"""square.py module"""

from models.rectangle import Rectangle
"""
Square class inherinting from Reactagle class"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super(Square, self).__init__(id, height)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.size)
