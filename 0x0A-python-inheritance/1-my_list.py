#!/usr/bin/python3
"""A class that inherits form the list class."""


class MyList(list):
    def print_sorted(self):
        """return sorted list in ascending order"""

        my_list = self.copy()
        print(sorted(my_list))
