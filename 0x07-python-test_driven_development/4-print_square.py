#!/usr/bin/python3
def print_square(size):
    """ print a square with '#' of lenght 'size'"""
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("{:s}".format("#"*size))
