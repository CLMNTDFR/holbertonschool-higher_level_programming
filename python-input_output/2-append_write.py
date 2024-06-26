#!/usr/bin/python3

"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
        text (str): the text to write in file
    """
    with open(filename, "a", encoding="utf-8") as f:
        """
        returns the number of characters written
        """
        return f.write(text)
