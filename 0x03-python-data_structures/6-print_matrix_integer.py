#!/usr/bin/python3
# File name:
#       6-print_matrix_integer.py
# Description:
#       Prints a matrix of integers
# Author:
#       eu-dk3-t


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
