# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

from pysound.buffer import SoundBuffer, get_buffer

#
# Multiply the source signal by an attack/decay envelope.
# The envelope increases from 0 to 1 for the attack duration, then falls
# back to zero over the remainder of the time.
#
def sample_and_hold(rate=11025, duration=1, source=1, trigger=1):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    source = get_buffer(samples, source)
    trigger = get_buffer(samples, trigger)
    data[0] = source[0]
    for i in range(1, samples):
        if trigger[i-1]>0 and trigger[i]<0:
            data[i] = source[i]
        else:
            data[i] = data[i-1]
    return buffer
