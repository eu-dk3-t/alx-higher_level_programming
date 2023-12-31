#!/usr/bin/python3
""" Module containing the ``Rectangle`` class """


class Rectangle:
    """ Rectangle Class  """

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """ 
        Function name:
            __init__
        Description:
            Initializes an instance of ``Rectangle``

        Args:
            width (int, optional): The width of the ``Rectangle`` instance.
            height (int, optional): The height of the ``Rectangle`` instance.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """
            FUnction name:
                __str__
            Description:
                Returns a string representation of ``Rectangle`` instance using '#'
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (('#' * self.width + '\n') * (self.height - 1) +
                    '#' * self.width)

    def __repr__(self):
        """
            Returns a string representation of ``Rectangle`` that works with
            eval()
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """ Prints a message when a ``Rectangle`` instance is deleted """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """ Returns width of instance. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns height of instance """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the ``Rectangle`` instance. """
        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter of the ``Rectangle`` instance. """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)
