# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy as np
from pysound.buffer import get_buffer


#
# Multiply the source signal by a ramp envelope.
# The envelope increases from the start value to the end value over the duration of the signal.
#
def ramp(rate=11025, duration=1, source=1, start=0, end=1):
    samples = int(duration*rate)
    data = np.zeros(samples)
    d_source = get_buffer(samples, source)
    for i in range(samples):
        t = i/samples
        data[i] = d_source[i]*(start + (end-start)*t)
    return data


#
# Multiply the source signal by an attack/decay envelope.
# The envelope increases from 0 to 1 for the attack duration, then falls
# back to zero over the remainder of the time.
#
def attack_decay(rate=11025, duration=1, source=1, attack_time=1):
    samples = int(duration*rate)
    data = np.zeros(samples)
    d_source = get_buffer(samples, source)
    for i in range(samples):
        t = i/rate
        if t < attack_time:
            data[i] = d_source[i]*t / attack_time
        else:
            data[i] = d_source[i]*(duration-t)/(duration - attack_time)
    return data
