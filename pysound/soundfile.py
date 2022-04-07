# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

from scipy.io.wavfile import read, write
from pysound.buffer import BufferParams

def save(params, filename, source):
    '''
    Write a sequence of samples as a WAV file
    '''
    write(filename, params.get_sample_rate(), source)

def load_with_params(filename, channel=0):
    '''
    Read a sequence of samples from a WAV file
    Return the buffer params and data
    '''
    rate, data = read(filename)
    params = BufferParams(data.shape[0], rate)

    # If the data is mono, return it
    if data.ndim == 1:
        return params, data

    # Otherwise return requested channel
    return params, data[channel]

def load(filename, channel=0):
    '''
    Read a sequence of samples from a WAV file
    Return the data
    '''
    _, data = load_with_params(filename, channel)
    return data

