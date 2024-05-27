#!/usr/bin/python3

"""
class Student that defines a student by:

Public instance attributes:
- first_name
- last_name
- age

Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self):
that retrieves a dictionary representation of a Student instance
(same as 8-class_to_json.py)
"""


class Student():
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

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__
