#!/usr/bin/python3

'''
instantiating a class
'''


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes
    ----------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.
    number_of_instances : int
        The number of Rectangle instances.
    print_symbol : any
        The symbol used for string representation of the rectangle.

    Methods
    -------
    __init__(width=0, height=0):
        Initializes the rectangle with optional width and height.
    width:
        Gets the width of the rectangle.
    width(value):
        Sets the width of the rectangle with validation.
    height:
        Gets the height of the rectangle.
    height(value):
        Sets the height of the rectangle with validation.
    area():
        Returns the area of the rectangle.
    perimeter():
        Returns the perimeter of the rectangle.
    __str__():
        Returns the string representation of the rectangle.
    __repr__():
        Returns the string representation to recreate a new instance.
    __del__():
        Prints a message when an instance is deleted.
    bigger_or_equal(rect_1, rect_2):
        Returns the biggest rectangle based on the area.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object.

        Parameters
        ----------
            width : int, optional
                The width of the rectangle (default is 0).
            height : int, optional
                The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Returns the string representation to recreate a new instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.

        Parameters
        ----------
            rect_1 : Rectangle
                The first rectangle.
            rect_2 : Rectangle
                The second rectangle.

        Raises
        ------
            TypeError
                If rect_1 is not an instance of Rectangle.
                If rect_2 is not an instance of Rectangle.

        Returns
        -------
            Rectangle
                The rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
