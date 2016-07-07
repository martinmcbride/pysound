# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

from pysound.buffer import SoundBuffer, get_buffer


#
# Sample the input signal initially, then resample each time the trigger signal goes from positive
# to zero or negative. In between triggers the output signal keeps the same value as the most recent sample.
#
def sample_and_hold(rate=11025, duration=1, source=1, trigger=1):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    d_source = get_buffer(samples, source)
    d_trigger = get_buffer(samples, trigger)
    data[0] = d_source[0]
    for i in range(1, samples):
        if d_trigger[i-1]>0 and d_trigger[i]<=0:
            data[i] = d_source[i]
        else:
            data[i] = data[i-1]
    return buffer

