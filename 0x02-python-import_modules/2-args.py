#!/usr/bin/python3
from sys import argv
if __name__  == "__main__":
	args_no = len(argv)
	if args_no == 1:
		print("{0} arguments.".format(0))
	elif args_no == 2:
		print("{0} argument:".format(1))
		for i in range(1, args_no):
			print("{0}: {1}".format(i, argv[i]))
	else:
		print("{0} arguments:".format(args_no - 1))
		for i in range(1, args_no):
			print("{0}: {1}".format(i, argv[i]))

	
