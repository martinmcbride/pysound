# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy as np
from pysound.buffer import get_buffer, is_buffer_signal, get_signal_length


#
# sequence a set of inputs to create the output data.
# Each input consists of a tuple pair:
#  - source (SoundBuffer)
#  - start time (seconds)
# Input signals are added together to create the output, with each signal delayed according to its start
# time. Signals can overlap.
#
# The output signal will be extended to fit all the supplied input signals
#
def sequencer(rate=11025, duration=1, inputs=[]):
    # Calculate the total number of output samples. This will be *at least* duration*rate,
    # but may be more if any input signals extend beyond that.
    samples = int(duration * rate)
    for source, start in inputs:
        if is_buffer_signal(source):
            end = int(start * rate) + get_signal_length(source)
            if end > samples:
                samples = end;
        else:
            raise TypeError('sequencer sources cannot be constants')

    data = np.zeros(samples)
    for source, start in inputs:
        start_sample = int(start * rate)
        transfer_samples = get_signal_length(source)
        signal = get_buffer(transfer_samples, source)
        for i in range(transfer_samples):
            data[i + start_sample] += signal[i]

    return data


#
# Sample the input signal initially, then resample each time the trigger signal goes from positive
# to zero or negative. In between triggers the output signal keeps the same value as the most recent sample.
#
def sample_and_hold(rate=11025, duration=1, source=1, trigger=1):
    samples = int(duration * rate)
    data = np.zeros(samples)
    d_source = get_buffer(samples, source)
    d_trigger = get_buffer(samples, trigger)
    data[0] = d_source[0]
    for i in range(1, samples):
        if d_trigger[i - 1] > 0 and d_trigger[i] <= 0:
            data[i] = d_source[i]
        else:
            data[i] = data[i - 1]
    return data
