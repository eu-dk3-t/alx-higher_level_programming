#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Class, square"""
    def __init__(self, size=0):
        """
        FUnction name:
            __init__
        Description:
            Initialization
            Error checks
        Attributes:
            size (:obj:`int`, optional): The size of the square.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        """
        Function name:
            size
        Description:
            getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Function name:
            size
        Description:
            setter
            Raises error messages
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Function name:
            area
        Description:
            Returns the area

        """
        return self.__size ** 2

    def my_print(self):
        """
        FUnction name:
            my_print
        Description:
            Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return None

        for i in range(1, self.area() + 1):
            print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()
