#!/usr/bin/python3
""" Reads a file """


def read_file(filename=""):
    """ Reads a file """
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end='')
