# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

def ramp(rate=11025, duration=1, start=0, end=1):
    '''
    Signal starts at start value, ramps linearly up to end value
    rate - sample rate
    duration - sound duration in seconds
    start - initial value of signal
    end - final value of signal
    '''
    samples = int(duration*rate)
    for i in range(samples):
        t = i/samples
        yield start + (end-start)*t

def attack_decay(rate=11025, duration=1, attack_time=0.5, min=0, max=1):
    '''
    Signal starts at min value, ramps linearly up to max value during the
    attack time, than ramps back down to min value over remaining time 
    rate - sample rate
    duration - sound duration in seconds
    start - initial value of signal
    end - final value of signal
    '''
    samples = int(duration*rate)
    for i in range(samples):
        t = i/samples
        if t < attack_time:
            yield min + (max-min)*t / attack_time
        else:
            yield min + (max-min)*(duration-t)/(duration - attack_time)
