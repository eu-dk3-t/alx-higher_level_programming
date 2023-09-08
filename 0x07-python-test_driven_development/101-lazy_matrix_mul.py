#!/usr/bin/python3
""" Defines a matrix multiplication function using numpy. """
import numpy as nm


def lazy_matrix_mul(m_a, m_b):
    """
    Function name:
        lazy_matrix_mul
    Description:
        Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    return (nm.matmul(m_a, m_b))
