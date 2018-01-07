#!/usr/bin/python3
"""
Matrix Module
"""
def matrix_divided(matrix, div):
    """
        Matrix divided
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list) and not isinstance(matrix[1], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) is not len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    for x in matrix[0] + matrix[1]:
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    matrix = [matrix[0], matrix[1]]
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in x]for x in matrix]
