# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import numpy as np
from functools import reduce

def modulator(sources=[]):
    '''
    Multiply all sources
    :param sources: list of arrays, must all be same length
    :return:
    '''
    return reduce(np.multiply, sources)
            
def adder(sources=[]):
    '''
    Multiply all sources
    :param sources: list of arrays, must all be same length
    :return:
    '''
    return reduce(np.add, sources)
