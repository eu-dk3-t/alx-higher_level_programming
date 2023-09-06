#!/usr/bin/python3
""" Module containing the ``Rectangle`` class """


class Rectangle:
    """ Rectangle Class  """

    number_of_instances = 0
    print_symbol = '#'

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
            return ((str(self.print_symbol) * self.width + '\n') *
                    (self.height - 1) + str(self.print_symbol) * self.width)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ 
        Function name:
            bigger_or_equal
        Description:
            Static method to determine which rectangle is bigger
        Args:
            rect_1 (:obj:`Rectangle`): A `Rectangle` instance.
            rect_2 (:obj:`Rectangle`): A `Rectangle` instance.

        Returns:
            The `Rectangle` instance with the largest area, or rect_1 if both
            are equal in area.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ 
        Function name:
            square
        Description:
            Class method that produces a square using the `Rectangle` class
        Args:
            size (int, optional): The sides of the square.
        Returns:
            A `Rectangle` instance where height == width == size
        """
        return cls(size, size)
