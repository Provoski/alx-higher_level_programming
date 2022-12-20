#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""it defines a Square class base on 1-square.py"""
class Square:
    """the Square class define a square with a private intance attribute called size and an optional size in def __init__(self, size=0)"""
    def __init__(self, size=0):
        """raising exception of size is not an integer"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        """raising exception if the size is < 0"""
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size #private
