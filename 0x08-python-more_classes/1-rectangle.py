#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle with private width and height attributes"""

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle with optional width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the private width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the private width attribute with validation """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the private height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the private height attribute with validation """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

