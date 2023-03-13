#!/usr/bin/python3
from sys import argv


if __name__  == "__main__":
    args_no = len(argv)
    if args_no == 1:
        print("{} arguments.".format(0))
    elif args_no == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments:".format(args_no - 1))
        for i in range(1, args_no):                     print("{}: {}".format(i, argv[i]))

	
