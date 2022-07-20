#!/usr/bin/python3

"""this is a continuity of the Square class
now every square objet must have a size
"""


class Square():
    """ the class Square create objet square
    with size entered by the operator
    the size is supposed to be an integer of float
    any other numeric number
    """

    def __init__(self, size):
        """this method initialise the objet square
        by his size entersd in parameter.
        size is private
        """
        self.__size = size


if __name__ == "__main__":
    # not required, this code is just to test my class
    square = Square(3)
    print(square)
