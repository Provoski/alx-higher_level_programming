#!/usr/bin/python3
"""0-read_file.py module"""


def read_file(filename=""):
    """a function that reads a text file and print it
    out to stdout
    """

    with open(filename, 'r', encoding='utf-8') as my_file:
        text = my_file.read()
    print("{}".format(text), end='')
