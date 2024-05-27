#!/usr/bin/python3
import json

"""
function that returns the JSON representation of an
object(string)
"""


def to_json_string(my_obj):
    """
     function that returns the JSON representation of
     an object (string)

    Args:
        my_obj: object we have to returns with JSON format
    """
    return json.dumps(my_obj)
