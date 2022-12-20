#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""it defines a Square class base on 3-square.py"""
class Square:
    """the Square class define a square with a private intance attribute called size and position.it has an Instantiation with optional size and position; def __init__(self, size=0, position = (0,0)) and instance methond def area(self) that return the current square area and the def my_print(self) that prints in stdout the square with the character #"""
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position
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
    #position property decorator
    @property

    #property getter method for position attribute
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)
    def my_print(self):
        """it prints to stdout the square with character '#' """

