#!/usr/bin/python3
"""A class that inherits form the list class."""


class MyList(list):
    """ this class is a subclass of list objrct """

    def print_sorted(self):
        """return sorted list in ascending order"""

        print(sorted(self))
