# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Simple wave forms

import numpy as np
import math
from pysound.buffer import SoundBuffer, get_buffer

def square_wave(rate=11025, duration=1, frequency=400, amplitude=1, ratio=0.5, offset=0):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    t = 0
    frequency = get_buffer(samples, frequency)
    amplitude = get_buffer(samples, amplitude)
    ratio = get_buffer(samples, ratio)
    offset = get_buffer(samples, offset)
    for i in range(samples):
        t += frequency[i]/rate
        t %= 1
        data[i] = offset[i] + amplitude[i]*(1 if t < ratio[i] else -1)
    return buffer

def saw_wave(rate=11025, duration=1, frequency=400, amplitude=1, ratio=0.5, offset=0):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    t = 0
    frequency = get_buffer(samples, frequency)
    amplitude = get_buffer(samples, amplitude)
    ratio = get_buffer(samples, ratio)
    offset = get_buffer(samples, offset)
    for i in range(samples):
        t += frequency[i]/rate
        t %= 1
        if t < ratio[i]:
            v = -1 + 2*t/ratio[i]
        else:
            v = 1 - 2*(t-ratio[i])/(1-ratio[i])
        data[i] = offset[i] + amplitude[i]*v
    return buffer

def sine_wave(rate=11025, duration=1, frequency=400, amplitude=1, ratio=0.5, offset=0):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    t = 0
    frequency = get_buffer(samples, frequency)
    amplitude = get_buffer(samples, amplitude)
    offset = get_buffer(samples, offset)
    for i in range(samples):
        t += frequency[i]/rate
        t %= 1
        data[i] = offset[i] + amplitude[i]*math.sin(t*2*math.pi)
    return buffer

