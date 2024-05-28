#!/usr/bin/python3
"""
Explore serialization and deserialization using
XML as an alternative format to JSON.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize the dictionary into XML format and save it to the given filename.

    :param dictionary: The Python dictionary to serialize
    :type dictionary: dict
    :param filename: The filename to save the serialized XML data
    :type filename: str
    """
    # Create root element
    root = ET.Element('data')

    # Add dictionary items as child elements to the root
    for key, value in dictionary.items():
        child = ET.Element(key)
        # Convert value to string if necessary
        child.text = str(value)
        root.append(child)

    # Create XML tree from root element
    tree = ET.ElementTree(root)

    # Write XML tree to file
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename into a Python dictionary.

    :param filename: The filename containing the serialized XML data
    :type filename: str
    :return: The deserialized data as a Python dictionary
    :rtype: dict
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Create an empty dictionary to store deserialized data
        deserialized_data = {}

        # Iterate over child elements of the root
        for child in root:
            # Add key-value pairs to the dictionary
            deserialized_data[child.tag] = child.text

        return deserialized_data

    except Exception as e:
        print("Error: {}".format(e))
        return None
