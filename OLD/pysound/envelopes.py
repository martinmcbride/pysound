# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import numpy as np
import math

def linseg(params, start=0, end=1):
    '''
    Signal starts at start value, ramps linearly up to end value
    :param params: buffer parameters, controls length of signal created
    :param start: start value (number)
    :param end: end value (number)
    :return: array of resulting signal
    '''
    return np.linspace(start, end, num=params.get_length(), endpoint=True)


class GenericEnvelope:
    '''
    Generic envelope builder
    '''

    def __init__(self, params):
        self.params = params
        self.data = np.zeros(params.get_length(), dtype=np.float)
        self.latest = 0
        self.pos = 0

    def set(self, value, samples=0):
        '''
        Set the current value and optionally maintain it for a period
        :param value: New current value
        :param samples: Add current value for this number of samples (if not zero)
        :return:
        '''
        if self.params.get_length() > self.pos and samples > 0:
            l = min(samples, self.params.get_length()-self.pos)
            self.data[self.pos:self.pos+l] = np.full(l, value, dtype=np.float)
            self.pos += l
        self.latest = value
        return self

    def hold(self, samples):
        '''
        Hold the previous value for a period
        :param samples: Add previous value for this number of samples
        :return:
        '''
        if self.params.get_length() > self.pos and samples > 0:
            l = min(samples, self.params.get_length()-self.pos)
            self.data[self.pos:self.pos+l] = np.full(l, self.latest, dtype=np.float)
            self.pos += l
        return self

    def linseg(self, value, samples):
        '''
        Create a linear section moving from current value to new value over a certain number of
        samples.
        :param value: New value
        :param samples: Length of segment in samples
        :return:
        '''
        if self.params.get_length() > self.pos and samples > 0:
            len = min(samples, self.params.get_length() - self.pos)
            end = value if len == samples else self.latest + (value - self.latest)*len/samples
            self.data[self.pos:self.pos + len] = np.linspace(self.latest, end, num=len, endpoint=False, dtype=np.float)
            self.pos += len
        self.latest = value
        return self

    def expseg(self, value, samples, factor=5):
        '''
        Create an exponential section moving from current value to new value over a certain number of
        samples.
        :param value: New value
        :param samples: Length of segment in samples
        :param factor: exponential factor
        :return:
        '''
        sample_rate = self.params.get_sample_rate()
        factor = -factor
        if self.params.get_length() > self.pos and samples > 0:
            len = min(samples, self.params.get_length() - self.pos)
            x0 = 0
            x1 = len
            y0 = self.latest
            y1 = value
            xvals = np.linspace(0, len, num=len, endpoint=False, dtype=np.float)/x1
            self.data[self.pos:self.pos + len] = y0 + (y1-y0)*(1-np.exp(factor*xvals))/(1-math.exp(factor))
            self.pos += len
        self.latest = value
        return self

    def build(self):
        if self.params.get_length() > self.pos:
            l = self.params.get_length()-self.pos
            self.data[self.pos:self.pos+l] = np.full(l, self.latest, dtype=np.float)
        return self.data


def attack_decay(params, attack, start=0, peak=1, factor=5):
    '''
    Signal starts at min value, ramps linearly up to max value during the
    attack time, than ramps back down to min value over remaining time
    :param params: buffer parameters, controls length of signal created
    :param attack: attack time, in samples
    :param start: start value (number)
    :param peak: peak value (number)
    :param factor: exponential factor
    :return:
    '''
    builder = GenericEnvelope(params)
    builder.set(start)
    builder.expseg(peak, attack, factor)
    if attack < params.get_length():
        builder.expseg(start, params.get_length() - attack, factor)
    return builder.build()

