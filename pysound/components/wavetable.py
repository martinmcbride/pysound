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
    d_frequency = get_buffer(samples, frequency)
    d_amplitude = get_buffer(samples, amplitude)
    d_ratio = get_buffer(samples, ratio)
    d_offset = get_buffer(samples, offset)
    for i in range(samples):
        t += d_frequency[i]/rate
        t %= 1
        data[i] = d_offset[i] + d_amplitude[i]*(1 if t < d_ratio[i] else -1)
    return buffer


def saw_wave(rate=11025, duration=1, frequency=400, amplitude=1, ratio=0.5, offset=0):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    t = 0
    d_frequency = get_buffer(samples, frequency)
    d_amplitude = get_buffer(samples, amplitude)
    d_ratio = get_buffer(samples, ratio)
    d_offset = get_buffer(samples, offset)
    for i in range(samples):
        t += d_frequency[i]/rate
        t %= 1
        if t < d_ratio[i]:
            v = -1 + 2*t/d_ratio[i]
        else:
            v = 1 - 2*(t-d_ratio[i])/(1-d_ratio[i])
        data[i] = d_offset[i] + d_amplitude[i]*v
    return buffer


def sine_wave(rate=11025, duration=1, frequency=400, amplitude=1, ratio=0.5, offset=0):
    samples = int(duration*rate)
    buffer = SoundBuffer(samples)
    data = buffer.getData()
    t = 0
    d_frequency = get_buffer(samples, frequency)
    d_amplitude = get_buffer(samples, amplitude)
    d_offset = get_buffer(samples, offset)
    for i in range(samples):
        t += d_frequency[i]/rate
        t %= 1
        data[i] = d_offset[i] + d_amplitude[i]*math.sin(t*2*math.pi)
    return buffer

