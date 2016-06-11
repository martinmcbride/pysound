# Author:  Martin McBride
# Created: 2016-06-11
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy

def get_buffer(samples, value):
    if type(value)==numpy.ndarray:
        return value
    else:
        buffer = numpy.zeros(samples)
        buffer.fill(value)
        return buffer

