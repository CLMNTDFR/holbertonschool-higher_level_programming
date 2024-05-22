#!/usr/bin/python3
"""
Check if  the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the specified class.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj is an instance of a_class, False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
