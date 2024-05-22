#!/usr/bin/python3

"""
Class that inherits from list
"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """
        prints list in ascending sort
        """
        sort_list = super().copy()
        sort_list.sort()
        print(sort_list)
