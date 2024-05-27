# <p align="center">Python - Serialization</p>
  
## Introduction:

Welcome to our exploration of marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.

### What is Marshaling?
Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.

### What is Serialization?
Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object, so it can be recreated in an identical state elsewhere. This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.

## Learning Objectives:
- Articulate the differences and similarities between marshaling and serialization.
- Implement serialization in a practical programming task.
- Understand how serialized data can be used in web applications, databases, and network communications.
- Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.

## Resources:
- Real Python Serialization
- Real Python: Working With JSON Data in Python
- Python’s pickle documentation
- Corey Schafer on Pickle
- CSV to JSON in Python
- Python XML ElementTree Guide
- Socket Programming Guide

## Files:

| Filename                   | Description                                                                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| task_00_basic_serialization.py | Python module implementing basic serialization functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python dictionary. |
| task_01_pickle.py        | Python module containing a CustomObject class with methods to serialize and deserialize instances of this class using the pickle module.                            |
| task_02_csv.py           | Python module defining a function to convert CSV data to JSON format using Python's csv and json modules.                                                    |
| task_03_xml.py           | Python module providing functions to serialize and deserialize data using XML as an alternative format to JSON, using Python's xml.etree.ElementTree module.  |
