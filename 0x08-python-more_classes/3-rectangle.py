#!/usr/bin/python3
class Rectangle:
  """Defines a rectangle, calculates area and perimeter, prints with '#'"""

  def __init__(self, width=0, height=0):
    """Initializes a Rectangle with optional width and height """
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

  def area(self):
    """Calculates and returns the area of the rectangle."""
    return self.width * self.height

  def perimeter(self):
    """Calculates and returns the perimeter of the rectangle."""
    if self.width == 0 or self.height == 0:
      return 0
    return 2 * (self.width + self.height)

  def __str__(self):
      """Returns a printable '#' representation of the rectangle."""
      if self.width == 0 or self.height == 0:
          return ""
      rectangle_str = ""
      for i in range(self.height):
          rectangle_str += "#" * self.width + "\n"
      return rectangle_str[:-1]  # Remove trailing newline

  def __repr__(self):
      """Returns a string representation that can recreate the rectangle."""
      return "Rectangle({}, {})".format(self.width, self.height)

