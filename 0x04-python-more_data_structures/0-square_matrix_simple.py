#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """return a square matrix"""
    matrix_rows = len(matrix)
    rows_size = len(matrix[0])
    _matrix = [[None]*rows_size]*matrix_rows
    for row in range(len(matrix)):
        _matrix[row] = matrix[row].copy()
        """squaring mateix elements"""
        for val in range(len(matrix[row])):
            _matrix[row][val] = _matrix[row][val]**2
    return _matrix

