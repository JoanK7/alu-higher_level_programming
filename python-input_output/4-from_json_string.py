#!/usr/bin/python3

'''module that converts json string to object: deserilization'''

import json
# import the json module


def from_json_string(my_str):
    '''function that does deserilization'''
    return json.loads(my_str)
