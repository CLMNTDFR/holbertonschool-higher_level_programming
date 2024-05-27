#!/usr/bin/python3


"""
function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”

    Args:
        filename: name of the JSON file
    """
    with open(filename, "r") as file:
        json_object = json.load(file)
        return json_object
