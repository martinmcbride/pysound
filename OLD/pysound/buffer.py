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
    
    def __init__(self, length=44100, sample_rate=44100):
        '''
        Create a BufferParams
        :param length: Length of buffer in samples
        :param sample_rate: Number of samples per second
        '''
        self._sample_rate = sample_rate
        self._length = length

    def with_duration(self, time):
        '''
        Factory method, create a new BufferParams with different duration
        :param length:
        :return:
        '''
        return BufferParams(self.t2s(time), self._sample_rate)

    def with_length(self, length):
        '''
        Factory method, create a new BufferParams with different length
        :param length:
        :return:
        '''
        return BufferParams(length, self._sample_rate)

    def with_sample_rate(self, sample_rate):
        '''
        Factory method, create a new BufferParams with different sample_rate
        :param sample_rate:
        :return:
        '''
        return BufferParams(self._length, sample_rate)

    def t2s(self, time):
        '''
        Converts a unit of time (in seconds) to a sample count
        '''
        return int(time*self._sample_rate)

    def get_length(self):
        return self._length

    def get_sample_rate(self):
        return self._sample_rate


def create_buffer(params, value=0.0):
    '''
    If the value is a float, create a numpy array of the required length, filled with value
    If the value is a numpy array, copy it up to the maximum size.
    Otherwise throw a type error
    '''
    if isinstance(value, np.ndarray):
        buffer = np.full(params.get_length(), 0.0, np.float)
        if params.get_length() <= value.shape[0]:
            buffer[:] = value[:params.get_length()]
        else:
            buffer[:value.shape[0]] = value[:]
        return buffer
    try:
        fv = float(value)
        return np.full(params.get_length(), fv, np.float)
    except TypeError:
        raise TypeError('Value must be a float or a numpy array')

def mix_buffer(dest, src, at):
    '''
    Mix an array into another at a certain point
    dest - the main buffer
    src - the data to be inserted
    at - position (in samples) to insert the data
    '''
    destlen = dest.size
    srclen = src.size
    if at < 0:          #Before start
        raise IndexError("Source buffer position less than 0")
    if at + src.size > destlen:             #After end
        raise IndexError("Source buffer extends beyond destination buffer")
    length = srclen
    if at + srclen > destlen:
        length -= at + srclen - destlen
    if length <= 0:
        return
    dest[at:at+srclen] = np.add(dest[at:at+srclen], src[:])
            
