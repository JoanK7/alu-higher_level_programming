#!/usr/bin/python3

'''module that returns a dictionary description with a simple
data structure'''


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    """
    return obj.__dict__
