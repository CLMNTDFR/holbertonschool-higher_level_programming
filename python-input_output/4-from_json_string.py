#!/usr/bin/python3


"""
function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: string we have to returns as an object JSON
    """
    return json.loads(my_str)
