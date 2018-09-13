# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import math
import numpy as np
from quack import buffer
from quack.buffer import create_buffer

SINE_TABLE = None
SINE_TABLE_SIZE = 16386

def create_sine_table():
    global SINE_TABLE
    if SINE_TABLE is None:
        args = np.linspace(0.0, 2*math.pi, num=SINE_TABLE_SIZE, endpoint=False)
        SINE_TABLE = np.sin(args)

def square_wave(params, frequency=400, amplitude=1,
                offset=0, ratio=0.5):
    '''
    Generate a square wave
    :param params: buffer parameters, controls length of signal created
    :param frequency: wave frequency (array or value)
    :param amplitude: wave amplitude (array or value)
    :param offset: offset of wave mean from zero (array or value)
    :param ratio: ratio of high to low time (array or value)
    :return: array of resulting signal
    '''
    t = 0
    frequency = create_buffer(params, frequency)
    amplitude = create_buffer(params, amplitude)
    offset = create_buffer(params, offset)
    ratio = create_buffer(params, ratio)
    phase = np.add.accumulate(frequency/params.sample_rate) % 1
    output = offset + amplitude * np.where(phase < ratio, 1, -1)
    return output
        
##def saw_wave(settings=None, frequency=const(400), amplitude=const(1),
##             offset=const(0), ratio=const(0.5)):
##    '''
##    Generate a saw wave (infinite sequence)
##    rate - sample rate
##    frequency - wave frequency (iterable)
##    amplitude - wave amplitude (iterable)
##    offset - offset of wave mean from zeor (iterable)
##    ratio - ratio of rise to fall time (iterable)
##    '''
##    settings = get_settings(settings)
##    t = 0
##    for f, a, o, r in zip(frequency, amplitude, offset, ratio):
##        t += f/settings.sample_rate
##        t %= 1
##        if t < r:
##            v = -1 + 2*t/r
##        else:
##            v = 1 - 2*(t-r)/(1-r)
##        yield o + a*v
##        
##def sine_wave(settings=None, frequency=const(400), amplitude=const(1), offset=const(0)):
##    '''
##    Generate a sine wave (infinite sequence)
##    rate - sample rate
##    frequency - wave frequency (iterable)
##    amplitude - wave amplitude (iterable)
##    offset - offset of wave mean from zeor (iterable)
##    '''
##    create_sine_table()
##    settings = get_settings(settings)
##    t = 0
##    for f, a, o in zip(frequency, amplitude, offset):
##        t += f/settings.sample_rate
##        t %= 1
##        yield o + a*SINE_TABLE[int(t*SINE_TABLE_SIZE)%SINE_TABLE_SIZE]
