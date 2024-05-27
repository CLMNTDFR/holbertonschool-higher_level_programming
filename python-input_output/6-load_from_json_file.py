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
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
