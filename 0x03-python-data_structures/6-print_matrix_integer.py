#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        count = 0
        for row in range(len(matrix)):
            for row_element in matrix[row]:
                row_len = len(matrix[row])
                print("{:d}".format(row_element), end="")
                if count < row_len-1:
                    print(" ", end="")
                count += 1
                if count == row_len:
                    print(end="\n")
                    count = 0
