#!/usr/bin/python3
def uppercase(str):
    count = 0
    for char in str:
        asc = ord(char)
        if (asc >= 97) and (asc <= 122):
            asc = asc - 32
            print(chr(asc), end='')
            count = count + 1
        else:
            print(char, end='')
            count = count + 1
        if count == len(str):
            print(end='\n')
