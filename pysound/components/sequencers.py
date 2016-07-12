# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy as np
from pysound.buffer import get_buffer

#
# sequence a set of inputs to create the output data.
# Each input consists of a tuple pair:
#  - source (SoundBuffer)
#  - start time (seconds)
# Input signals are added together to create the output, with ex#ach signal delayed acording to its start
# time. Signals can overlap. Any signals which extend beyond the sequencer duration are truncated.
#
def sequencer(rate=11025, duration=1, inputs=[]):
    samples = int(duration*rate)
    data = np.zeros(samples)
    for source, start in inputs:
        start_sample = int(start*rate)
        signal = get_buffer(source, source)
        transfer_samples = min(len(signal), samples-start_sample-1)
        for i in range(transfer_samples):
            data[i+start_sample] += signal[i]

    return data



#
# Sample the input signal initially, then resample each time the trigger signal goes from positive
# to zero or negative. In between triggers the output signal keeps the same value as the most recent sample.
#
def sample_and_hold(rate=11025, duration=1, source=1, trigger=1):
    samples = int(duration*rate)
    data = np.zeros(samples)
    d_source = get_buffer(samples, source)
    d_trigger = get_buffer(samples, trigger)
    data[0] = d_source[0]
    for i in range(1, samples):
        if d_trigger[i-1]>0 and d_trigger[i]<=0:
            data[i] = d_source[i]
        else:
            data[i] = data[i-1]
    return data

