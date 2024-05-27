#!/usr/bin/python3

"""
create objects from a JSON file
"""
import json


def load_from_json_file(filename):
    """function for create object from a JSON file

    Args:
        filename: the name of the file
    Returns:
        all json object in file .json
    """
    with open(filename, "r") as file:
        json_object = json.load(file)
        return json_object
