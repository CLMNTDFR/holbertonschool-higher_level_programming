#!/usr/bin/python3

"""
Script that converts an object's attributes to a dictionary
suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing the attributes of obj.
    """
    # vars() returns an attributes's dictionnary of an object
    json_obj = vars(obj)
    return json_obj
