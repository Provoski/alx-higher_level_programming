#!/usr/bin/python3
""" 100-my_int module """


class MyInt(int):
    """ inverted == and != int class """

    def __eq__(self, other):
        """ inverting  equal to """

        return super().__ne__(other)

    def __ne__(self, other):
        """ inverting not equal to """

        return super().__eq__(other)
