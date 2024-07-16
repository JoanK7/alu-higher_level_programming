#!/usr/bin/python3

'''function definition'''


def read_file(filename=""):
    '''read file function'''

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
