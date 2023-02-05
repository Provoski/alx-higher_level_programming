#!/usr/bin/python3
"""
rectagle.py module. this model defines a Rectagle class
which inherit from the base class.
it alsonhave different methods and attributs.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class. it  inheriting from Base class
    which is the parent class.
    """

    def __init__(self, width, height,  x=0, y=0, id=None):
        """
        initiallizing class attributes and validating
        """

        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if isinstance(x, int) is not True:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if isinstance(y, int) is not True:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """property getter for width"""

        return self.__width

    @width.setter
    def width(self, width):
        """property setter for width"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """property getter for height"""

        return self.__height

    @height.setter
    def height(self, height):
        """property setter for height"""

        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """property getter for x"""

        return self.__x

    @x.setter
    def x(self, x):
        """property setter for x"""

        if isinstance(x, int) is not True:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """property getter for y"""

        return self.__y

    @y.setter
    def y(self, y):
        """property setter for y"""

        if isinstance(y, int) is not True:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        method: area
        use: returns the area value of a rectangle
        logic: width * height
        """

        return self.__width*self.__height

    def display(self):
        """
        method: display
        use: prints in stdout the Rectangle instance
        with the character
        """

        for i in range(self.__height):
            print("{}".format("#"*self.__width))

    def __str__(self):
        """overriding default __str__ content"""

        t = "[Rectangle] ({}) {}/{} - {}/{}"
        o = t.format(self.id, self.__x, self.__y, self.__width, self.__height)
        return o
    """
    def update(self, *args, **kwargs):
        method: public method - update
        use: assign an arguments to each attribute
        class attribute

        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        if len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
            mapping arguments to class attributes
        for key, value in kwargs.items():
            if key == "id" and key is not None:
                self.id = value
            if key == "width" and key is not None:
                self.width = value
            if key == "height" and key is not None:
                self.height = value
            if key == "x" and key is not None:
                self.x = value
            if key == "y" and key is not None:
                self.y = value
        """
