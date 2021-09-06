# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import numpy as np
from functools import reduce

def modulator(sources=None):
    '''
    Multiply all sources
    :param sources: list of arrays, must all be same length
    :return:
    '''
    if not sources:
        return np.zeros(0)
    return reduce(np.multiply, sources)
            
def adder(sources=None):
    '''
    Multiply all sources
    :param sources: list of arrays, must all be same length
    :return:
    '''
    if not sources:
        return np.zeros(0)
    return reduce(np.add, sources)

def sequencer(params, source_specs):
    '''
    Add a sequence of sounds to a buffer
    :param params: buffer parameters, controls length of signal created
    :param source_spec: list of tuples containing (source, position). The source is added into the output buffer
    at the sample position given by the second element in the tuple
    :return:
    '''
    output = np.zeros(params.get_length(), dtype=np.float)
    for source, pos in source_specs:
        if pos >= 0:
            length = min(source.size, params.get_length() - pos)
            if length > 0:
                output[pos:pos+length] += source[:length]
    return output
