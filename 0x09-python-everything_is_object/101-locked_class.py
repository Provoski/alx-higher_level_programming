#!/usr/bin/python3
# module 101-locked_class has one class
class LockedClass:
    """has no class or object.
    It prevent the user from dynamically
    creating new instance attribute except first_name attribute"""

    __slots___ = ['first_name']
