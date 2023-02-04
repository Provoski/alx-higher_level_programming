#!/usr/bin/python3
""" base class """

class Base:
    __nb_object = 0

    """Base class Constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
