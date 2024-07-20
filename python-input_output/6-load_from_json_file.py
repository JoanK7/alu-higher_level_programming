#!/usr/bin/python3

'''a module that creates an object from json file '''

import json
# importing the json module


def load_from_json_file(filename):
    ''' a function that creates an objet from a json file '''
    with open(filename, 'r') as file:
        my_obj = json.load(file)
        return my_obj
