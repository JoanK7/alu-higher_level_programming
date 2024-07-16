#!/usr/bin/python3

''' a module that appends text to the end of a file'''


def append_write(filename="", text=""):
    '''function that appends tesxt to a file '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
