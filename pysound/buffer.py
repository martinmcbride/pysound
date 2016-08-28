# Author:  Martin McBride
# Created: 2016-06-11
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy as np

def is_buffer_signal(value):
    return type(value) == np.ndarray

# Get length of signal
#  - If the signal is an array, it is the length of the array
#  - If the signal is a value, it is 0

def get_signal_length(value):
    if is_buffer_signal(value):
        return value.size
    else:
        return 0


#
# Helper function. Convert an input value to a numpy array.
#  - If the input is an array of length >= samples, the entire array will be returned
#  - If the input is an array of length < samples, the array will be padded with zeroes to be and returned.
#  - If the input is a number, an array of length samples will be created and returned.

def get_buffer(samples, value):
    if is_buffer_signal(value):
        if value.size >= samples:
            return value
        else:
            data = np.zeros(samples)
            data[0:value.shape[0]] = value
            return data
    else:
        data = np.zeros(samples)
        data.fill(value)
        return data
