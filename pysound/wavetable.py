# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Simple wave forms

import numpy as np
import math

def square_wave(params, g_frequency, g_amplitude, g_ratio, g_offset):
    '''
    Generates a square wave

    params: Sound parameters object
    frequency: wave frequency
    amplitude: wave amplitude
    ratio: on time to off time, 0.1 gives 10% on, 90% off
    '''
    buffer = np.zeros(params.size)
    t = 0

    while True:
        frequency = next(g_frequency)
        amplitude = next(g_amplitude)
        ratio = next(g_ratio)
        offset = next(g_offset)
        for i in range(params.size):
            t += frequency[i]/params.rate
            t %= 1
            buffer[i] = offset[i] + amplitude[i]*(1 if t < ratio[i] else -1)
        yield buffer

def saw_wave(params, g_frequency, g_amplitude, g_ratio, g_offset):
    '''
    Generates a sawtooth wave

    params: Sound parameters dictionary
    frequency: wave frequency
    amplitude: wave amplitude
    ratio: rise time to fall time, 0.1 gives 10% rise, 90% fall
    '''
    buffer = np.zeros(params.size)
    t = 0

    while True:
        frequency = next(g_frequency)
        amplitude = next(g_amplitude)
        ratio = next(g_ratio)
        offset = next(g_offset)
        for i in range(params.size):
            t += frequency[i]/params.rate
            t %= 1
            if t < ratio[i]:
                v = -1 + 2*t/ratio[i]
            else:
                v = 1 - 2*(t-ratio[i])/(1-ratio[i])
            buffer[i] = offset[i] + amplitude[i]*v
        yield buffer

def sine_wave(params, g_frequency, g_amplitude, g_offset):
    '''
    Generates a sine wave

    params: Sound parameters dictionary
    frequency: wave frequency
    amplitude: wave amplitude
    '''
    buffer = np.zeros(params.size)
    t = 0
    while True:
        frequency = next(g_frequency)
        amplitude = next(g_amplitude)
        offset = next(g_offset)
        for i in range(params.size):
            t += frequency[i]/params.rate
            t %= 1
            buffer[i] = offset[i] + amplitude[i]*math.sin(t*2*math.pi)
        yield buffer

