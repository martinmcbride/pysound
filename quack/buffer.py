# Author:  Martin McBride
# Created: 2018-04-22
# Copyright (C) 2018, Martin McBride
# License: MIT

# Numpy array is used to store sound data

import numpy as np
from const import SETTINGS

'''
Create a zero numpy array
'''
def create_empty_array(samples):
    return np.zeros(samples)

'''
Create a numpy array from an iterator and a size in samples
'''
def create_array_from_iterator(it, samples):
    return np.fromiter(it, np.float, samples)

'''
Mix an array into another at a certain point
dest - the main buffer
src - the data to be inserted
at - position (in samples) to insert the data
'''
def insert_array(dest, src, at):
    len = src.size
    dest[at:at+len] = np.add(dest[at:at+len],src) 
            