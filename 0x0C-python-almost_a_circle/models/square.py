#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherinting from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ modifying defaul __str__ method """
        txt = "[Square] ({}) {}/{} - {}"
        return txt.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        method: public method - update
        use: assign an arguments to each attribute
        class attribute
        """

        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.size = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.size = args[1]
            self.__y = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.size = args[1]
            self.__y = args[2]
            self.__x = args[3]

        """
        mapping arguments to class attributes
        """
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.size = value
            if key == "x":
                self.__x = value
            if key == "y":
                self.__y = value

    def to_dictionary(self):

        """
        method: to_dictionary
        function: return the dictionary representation
        of square
        """

        square_dict = {
                "id": self.id,
                "size": self.height,
                "x": self.x,
                "y": self.y
                }
        return square_dict
