# Author:  Martin McBride
# Created: 2016-06-11
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy as np

#
# Helper function. If value is a numpy arrays return it.
# If value is a number, return a numpy array filled with that number.
#
def get_buffer(samples, value):
    if type(value)==np.ndarray:
        return value
    else:
        data = np.zeros(samples)
        data.fill(value)
        return data

