#!/usr/bin/python3
# File name:
#       0-square_matrix_simple.py
# Description:
#       Squares all ints in a matrix
# Author:
#       eu-dk3-t


def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x*x, row)) for row in matrix]
