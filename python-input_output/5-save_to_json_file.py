#!/usr/bin/python3

'''a module that saves object to a file using json representation'''

import json
# importing the json module


def save_to_json_file(my_obj, filename):
    '''function that saves object to text file'''
    with open(filename, 'w') as file:
        json.dump(my_obj,  file)
