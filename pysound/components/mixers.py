# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

from pysound.buffer import SoundBuffer, get_buffer

#
# Multiply the source signals together
#
def modulator(rate=11025, duration=1, sources=[]):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    signals = []
    for source in sources:
        signals.append(get_buffer(samples, source))
    for i in range(samples):
        val = 1
        for signal in signals:
            val *= signal[i]
        data[i] = val
    return buffer
