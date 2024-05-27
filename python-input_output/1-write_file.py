#!/usr/bin/python3

"""writes a file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to read. Defaults to an
        empty string.
        text (str): the text to write in file
    """
    with open(filename, "w", encoding="utf-8") as f:
        """
        returns the number of characters written
        """
        return f.write(text)
