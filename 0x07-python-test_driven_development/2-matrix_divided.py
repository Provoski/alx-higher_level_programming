#!/usr/bin/python3
# 2-matrix_divided.py module supplies one function
def matrix_divided(matrix, div):
    """return a matrix whose elements has been divided by div"""
    
    data_types = (int, float)
    matrix_rows = len(matrix)
    rows_size = len(matrix[0])
    _matrix = [[None]*rows_size]*matrix_rows
    if isinstance(div, data_types) is not True:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """Collecting matrix rows"""
    for row in range(len(matrix)):
        if len(matrix[row]) != rows_size:
            raise TypeError("Each row of the matrix must have the same size")
        _matrix[row] = matrix[row].copy()
        """Div operation on rows values"""
        for val in range(len(matrix[row])):
            if isinstance(_matrix[row][val], data_types) is not True:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            _matrix[row][val] = round(_matrix[row][val]/div, 2)
    return _matrix
