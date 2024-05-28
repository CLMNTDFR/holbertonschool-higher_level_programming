#!/usr/bin/python3
"""
Serialize and deserialize custom Python objects using the pickle module.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        :param filename: The filename to save the serialized object
        :type filename: str
        """
        try:
            # 'wb' = write + binary
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Serialization error: {}".format(e))
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        :param filename: The filename to load the serialized object from
        :type filename: str
        :return: An instance of CustomObject or None if an error occurs
        :rtype: CustomObject or None
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Deserialization error: {}".format(e))
            return None
