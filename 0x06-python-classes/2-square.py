#!/usr/bin/python3


class Square:
    """ class square with attribute size    """
    def __init__(self, size=0):
        """
        Function name:
            __init__
        Description:
            Initialization
            Checks for common errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
