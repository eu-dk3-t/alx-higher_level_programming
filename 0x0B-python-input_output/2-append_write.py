#!/usr/bin/python3
""" Appends a string at the end of a file """


def append_write(filename="", text=""):
    """ Appends onto a utf-8 encoded text file. """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
