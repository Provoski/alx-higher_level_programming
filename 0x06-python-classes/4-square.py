#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""it defines a Square class base on 3-square.py"""
class Square:
    """the Square class define a square with a private intance attribute called size. it uses property getter 'def size(self)' to retrieve size and property setter 'def size(self, value)' to set it.it has an Instantiation with optional size: def __init__(self, size=0) and instance methond def area(self) that return the current square area"""
    def __init__(self, size):
        """raising exception of size is not an integer"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        """raising exception if the size is < 0"""
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size #private

    #property decorator
    @property

    #property getter method
    def size(self):
        return self.__size

    @size.setter
    #property setter method
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
