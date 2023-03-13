#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    args_no = len(argv)
    add = 0
    add = int(add)
    for i in range(1, args_no):
        add = add + int(argv[i])
    print("{}".format(add))
