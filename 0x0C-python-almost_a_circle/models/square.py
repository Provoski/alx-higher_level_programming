#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherinting from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(size, size, x, y, id)
        self._size = size

    @property
    def size(self):
        """ size property gette"""
        return self._size

    @size.setter
    def size(self, size):
        """ size property setter """
        self._size = size

    def __str__(self):
        """ modifying defaul __str__ method """
        txt = "[Square] ({}) {}/{} - {}"
        return txt.format(self.id, self.x, self.y, self.width)
