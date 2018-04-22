# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import math
from const import const, glob

def square_wave(settings=glob, frequency=const(400), amplitude=const(1),
                offset=const(0), ratio=const(0.5)):
    '''
    Generate a square wave (infinite sequence)
    rate - sample rate
    frequency - wave frequency (iterable)
    amplitude - wave amplitude (iterable)
    offset - offset of wave mean from zeor (iterable)
    ratio - ratio of high to low time (iterable)
    '''
    t = 0
    for f, a, o, r in zip(frequency, amplitude, offset, ratio):
        t += f/settings.sample_rate
        t %= 1
        yield o + a*(1 if t < r else -1)
        
def saw_wave(settings=glob, frequency=const(400), amplitude=const(1),
             offset=const(0), ratio=const(0.5)):
    '''
    Generate a saw wave (infinite sequence)
    rate - sample rate
    frequency - wave frequency (iterable)
    amplitude - wave amplitude (iterable)
    offset - offset of wave mean from zeor (iterable)
    ratio - ratio of rise to fall time (iterable)
    '''
    t = 0
    for f, a, o, r in zip(frequency, amplitude, offset, ratio):
        t += f/settings.sample_rate
        t %= 1
        if t < r:
            v = -1 + 2*t/r
        else:
            v = 1 - 2*(t-r)/(1-r)
        yield o + a*v
        
def sine_wave(settings=glob, frequency=const(400), amplitude=const(1), offset=const(0)):
    '''
    Generate a sine wave (infinite sequence)
    rate - sample rate
    frequency - wave frequency (iterable)
    amplitude - wave amplitude (iterable)
    offset - offset of wave mean from zeor (iterable)
    '''
    t = 0
    for f, a, o in zip(frequency, amplitude, offset):
        t += f/settings.sample_rate
        t %= 1
        yield o + a*math.sin(t*2*math.pi)