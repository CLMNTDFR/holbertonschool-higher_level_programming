#!/usr/bin/python3
"""
Module that defines a function to check the type of an object.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is an instance of a_class or a subclass of a_class.
        False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
