#!/usr/bin/python3
""" This Script defines a subclass from the subclass
Rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ The Class Defines a Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ The Constructor
            Initializes a new square
        """
        super().__init__(size, size, x, y, id)

    # Str Method
    def __str__(self):
        """ Returns a string rep of a square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    # Getter and Setter Methods
    @property
    def size(self):
        """ Returns the size """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets size to value """
        self.width = value
        self.height = value

    # Update Method
    def update(self, *args, **kwargs):
        """ Updates the class Square """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # To dict Method
    def to_dictionary(self):
        """ Returns a dict rep of a square """
        return {'id' : self.id, 'size' : self.size, 'x' : self.x, 'y' : self.y}
