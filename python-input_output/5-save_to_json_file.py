#!/usr/bin/python3


"""
function that writes an Object to a text file, using a
JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a
    JSON representation

    Args:
        my_obj: object must be written
        filename: the name of the text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dumps(my_obj, f)
