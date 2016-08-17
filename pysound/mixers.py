# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy as np
from pysound.buffer import get_buffer


#
# Multiply the source signals together
#
def modulator(rate=11025, duration=1, sources=[]):
    samples = int(duration*rate)
    data = np.zeros(samples)
    signals = [get_buffer(samples, source) for source in sources]
    for i in range(samples):
        val = 1
        for signal in signals:
            val *= signal[i]
        data[i] = val
    return data

#
# Add the source signals together
#
def adder(rate=11025, duration=1, sources=[]):
    samples = int(duration*rate)
    data = np.zeros(samples)
    signals = [get_buffer(samples, source) for source in sources]
    for i in range(samples):
        val = 0
        for signal in signals:
            val += signal[i]
        data[i] = val
    return data
