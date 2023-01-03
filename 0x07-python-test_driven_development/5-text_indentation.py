#!/usr/bin/python3
def text_indentation(text):
    indentors  = ".?:"
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    for char in text:
        print("{}".format(char), end="")
        if char in indentors:
            print("\n")

