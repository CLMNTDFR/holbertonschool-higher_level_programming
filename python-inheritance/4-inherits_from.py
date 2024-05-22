#!/usr/bin/python3
"""
Module that defines if the object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class;
        otherwise False.
    """
    # Check if the type of obj is a subclass of a_class and ensure obj is not an instance of a_class
    return issubclass(type(obj), a_class) and type(obj) is not a_class
