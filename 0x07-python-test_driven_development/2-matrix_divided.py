#!/usr/bin/python3
"""
Divide a matrix module
"""


def matrix_divided(matrix=None, div=None, *args):
    """
    matrix_divided - a function that divides all elements of a matrix.
    
    Returns a new matrix
    """
    """ validate that more than 2 arguments were not passed"""
    if len(args) > 0:
        raise TypeError("matrix_divided() expects 2 required"
                        " positional arguments, but ... were given")

    if matrix is None or div is None:
        raise TypeError("matrix_divided() missing 2 required positional arguments")
    
    """ Validate div argument"""
    if not isinstance(div, (int, float)) and div is not None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    _list = []
    
    """ validate that each rows of the matrix is of equal length"""
    for i in range(len(matrix)):
        """ check that matrix is a list of list"""
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    """ Function main code"""
    for rows in matrix:
        row = []
        for item in rows:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            n = round(item / div, 2)
            row.append(n)

        _list.append(row)
    return _list
