#!/usr/bin/python3
"""
Basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON file to
recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): A Python dictionary with data.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes the data to recreate a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with deserialized JSON data from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
