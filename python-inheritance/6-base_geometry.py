#!/usr/bin/python3

''' creating a class '''


class BaseGeometry:
    ''' instance method'''
    def __init__(self):
        '''initialize class '''
        pass

    def area(self):
        '''raises an exception'''
        raise Exception('area() is not implemented')
