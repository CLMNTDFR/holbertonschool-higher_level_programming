#!/usr/bin/python3

""" MyInt class """


class MyInt(int):
    """
    Rebel Classe MyInt
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
