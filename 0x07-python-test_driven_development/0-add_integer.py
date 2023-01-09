#!/usr/bin/python3

"""0-add_integer module that supplies one function."""


def add_integer(a, b=98):
    """Returns the addition of two values"""

    data_types = (int, float)
    if isinstance(a, data_types) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, data_types) is False:
        raise TypeError("b must be an integer")
    val_1 = int(a)
    val_2 = int(b)
    return (val_1 + val_2)
