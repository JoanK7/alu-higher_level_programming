#!/usr/bin/python3
"""
Square Module
This module defines the Square class.

"""


class Square:
    """
    Square Class

    This represents a square with a size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the Square with an optional size.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.size = size  # Calls the setter method

    @property
    def size(self):
        """
        Getter method for size attribute.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the Square object.

        Returns:
            str: Informal string representation of the Square object.

        """
        return f"Square with size: {self.__size}"
