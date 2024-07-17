#!/usr/bin/python3

'''module converting object to JSON string'''

import json


# importing the json module
def to_json_string(my_obj):
    ''' function that converts obj to JSON string '''
    return json.dumps(my_obj)
