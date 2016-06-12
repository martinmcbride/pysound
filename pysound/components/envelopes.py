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
def attack_decay(rate=11025, duration=1, source=1, attackTime=1):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    source = get_buffer(samples, source)
    for i in range(samples):
        t = i/rate
        if t < attackTime:
            data[i] = source[i]*t/attackTime
        else:
            data[i] = source[i]*(duration-t)/(duration-attackTime)
    return buffer
