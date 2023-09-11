#!/usr/bin/python3
""" Pascal Triangle """

def pascal_triangle(n):
    """ Represents a pascal triangle of size n """
    if n <= 0:
        return []

    pasc_tr = [[1]]

    while len(pasc_tr) != n:
        tri = pasc_tr[-1]
        tmp_pa = [1]
        for i in range(len(tri) - 1):
            tmp_pa += [tri[i] + tri[i + 1]]
        tmp_pa += [1]
        pasc_tr += [tmp_pa]
    return pasc_tr
