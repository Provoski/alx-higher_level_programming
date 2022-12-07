#!/usr/bin/python3
from calculator_1 import sub, mul, div, add
a = 10
b = 5
if __name__ == "__main__":
	print("{0} + {1} = {2}".format(a, b, add(a, b)))
	print("{0} - {1} = {2}".format(a, b, sub(a, b)))
	print("{0} * {1} = {2}".format(a, b, mul(a, b)))
	print("{0} / {1} = {2}".format(a, b, div(a, b)))	
