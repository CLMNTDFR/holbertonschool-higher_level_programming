#!/usr/bin/python3
"""
Check if  the object is exactly an instance of the specified class
"""

def is_same_class(obj, a_class):
    """
    Return True if the object is an instance of a class,
    else, return False
    """
    return type(obj) == a_class
