#!/usr/bin/python3

"""
Class Student that defines a student by:
(based on 9-student.py)

Public instance attributes:
- first_name
- last_name
- age

Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary
representation of a Student instance (same as 8-class_to_json.py):

If attrs is a list of strings, only attribute names contained in this list
must be retrieved.
Otherwise, all attributes must be retrieved.

Public method def reload_from_json(self, json):
    that replaces all attributes of the Student instance:
    Assume json will always be a dictionary
"""


class Student:
    """
    A class to represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include
            in the dictionary.
            If None, all attributes will be included.

        Returns:
            dict: A dictionary containing the specified attributes
            of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with the
        corresponding values from the JSON dictionary.

        Args:
        json (dict): A dictionary containing attribute names
        as keys and their values as values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
