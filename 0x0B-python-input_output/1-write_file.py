#!/usr/bin/python3
"""1-write_file.py module"""


def write_file(filename="", text=""):
    """a function that appends a string at the end
    of a text file (UTF8) and returns the number of
    characters added
    """

    text_len = 0
    with open(filename, 'w', encoding='utf-8') as my_file:
        text_len = my_file.write(text)
    return text_len
