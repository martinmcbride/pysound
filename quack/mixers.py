# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

from _operator import mul, add
from functools import reduce

def modulator(sources=[]):
    '''
    Multiply the source signals together
    rate - sample rate
    sources - list of sources (iterables)
    '''
    if sources:
        for values in zip(*sources):
            yield reduce(mul, values, 1)
            
def adder(sources=[]):
    '''
    Add the source signals together
    rate - sample rate
    sources - list of sources (iterables)
    '''
    if sources:
        for values in zip(*sources):
            yield reduce(add, values, 1)