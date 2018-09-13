# Author:  Martin McBride
# Created: 2018-04-22
# Copyright (C) 2018, Martin McBride
# License: MIT

# Numpy array is used to store sound data

import numpy as np

class BufferParams:
    '''
    Length and sample rate of a buffer
    '''
    
    def __init__(self, sample_rate=11025):
        '''
        Create parameters
        The length will be set equal to the sample rate, giving a 1 second sound by default
        :param sample_rate: sample rate to use, defaults to 11025
        '''
        self.length = sample_rate
        self.sample_rate = sample_rate

    def copy(self):
        '''
        Create new parameters based on self
        :return: new params object
        '''
        new = BufferParams(self.sample_rate)
        new.length = self.length
        return new

    def like(other):
        '''
        Create new parameters based on other
        :return: new params object
        '''
        new = BufferParams(other.sample_rate)
        new.length = other.length
        return new

    def time(self, time):
        '''
        Update the length of the buffer in seconds
        :param time: number of seconds
        :return: self
        '''
        self.length = int(time*self.sample_rate)
        return self
        
    def samples(self, length):
        '''
        Update the length of the buffer in samples
        :param length: number of samples
        :return: self
        '''
        self.length = length
        return self
        
    
    def t2s(self, time):
        '''
        Converts a unit of time (in seconds) to a sample count
        '''
        return int(time*self.sample_rate)

def create_buffer(params, value):
    '''
    If the value is a float, create a numpy array of the required length, filled with value
    If the value is a numpy array, check its length
    Otherwise throw a type error
    '''
    try:
        fv = float(value)
        return np.full(params.length, fv, np.float)
    except TypeError:
        if isinstance(value, np.ndarray):
            if (len(value)>=params.length):
                return value
        raise TypeError('Value must be a float or a numpy array ofthe required length')

'''
Mix an array into another at a certain point
dest - the main buffer
src - the data to be inserted
at - position (in samples) to insert the data
'''
def insert_array(dest, src, at):
    len = src.size
    dest[at:at+len] = np.add(dest[at:at+len],src) 
            
