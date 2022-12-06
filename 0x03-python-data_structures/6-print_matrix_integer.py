#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	count = 0
	for row in range(len(matrix)):
		for row_element in matrix[row]:
			row_len = len(matrix[row])
			print("{} ".format(row_element), end="")
			count = count + 1
			if count == row_len:
				print(end="\n")
				count = 0
