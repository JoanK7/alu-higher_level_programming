#!/usr/bin/python3

'''Add all args to a python list and save them to a file'''

import sys
import os.path


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    # Check if the file exists, and load the data if it does
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add all arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)
