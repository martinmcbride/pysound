# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

def const(value=0.0):
    '''
    Returns an infinite sequence of a constant value
    '''
    while True:
        yield(value)