#!/usr/bin/python3
"""
Reading data from one format (CSV) and converting it
into another format (JSON) using serialization techniques
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write to data.json file.

    :param csv_filename: The filename of the input CSV file
    :return: True if the conversion was successful, False otherwise
    """
    try:
        # Open and read a CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        return True

    except Exception as e:
        print("Error: {}".format(e))
        return False
