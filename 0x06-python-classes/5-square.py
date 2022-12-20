#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""it defines a Square class base on 3-square.py"""
class Square:
    """the Square class define a square with a private intance attribute called size.it has an Instantiation with optional size; def __init__(self, size=0). instance methond def area(self) that return the current square area and the def my_print(self) that prints in stdout the square with the character #"""
    def __init__(self, size=0):
        self.__size = size
    #size property decorator
    @property

    #property getter method for size
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
        """ return the square of size"""
        return (self.__size * self.__size)

    def my_print(self):
        """it prints to stdout the square with character '#' """
        if (self.__size == 0):
            print("")
        for i in range(self.__size):
            print("{}".format(self.__size*"#"))
