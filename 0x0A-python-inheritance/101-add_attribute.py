#!/usr/bin/python3
""" 101-add_attribute module """


def add_attribute(obj, name, value):
    """ add attribute to an object """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
