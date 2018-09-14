# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import numpy as np

def linseg(params, start=0, end=1):
    '''
    Signal starts at start value, ramps linearly up to end value
    :param params: buffer parameters, controls length of signal created
    :param start: start value (number)
    :param end: end value (number)
    :return: array of resulting signal
    '''
    return np.linspace(start, end, num=params.length, endpoint=True)

def attack_decay(params, attack, start=0, peak=1):
    '''
    Signal starts at min value, ramps linearly up to max value during the
    attack time, than ramps back down to min value over remaining time
    :param params: buffer parameters, controls length of signal created
    :param attack: attack time, in samples
    :param start: start value (number)
    :param peak: peak value (number)
    :return:
    '''
    if attack >= params.length:
        # Envelope is attack only
        return np.linspace(start, peak*params.length/attack, num=params.length, endpoint=True, dtype=np.float)
    # Envelope is attack-decay
    attack_signal = np.linspace(start, peak, num=attack, endpoint=False, dtype=np.float)
    decay_signal = np.linspace(peak, start, num=params.length-attack, endpoint=True, dtype=np.float)
    return np.concatenate((attack_signal, decay_signal))


class GenericEnvelope:

    def __init__(self, params):
        self.params = params
        self.data = np.zeros(params.length, dtype=np.float)
        self.latest = 0
        self.pos = 0

    def set(self, value, samples=0):
        if self.params.length > self.pos and samples > 0:
            len = min(samples, self.params.length-self.pos)
            self.data[self.pos:self.pos+len] = np.full(len, value, dtype=np.float)
            self.pos += len
        self.latest = value
        return self

    def linseg(self, value, samples):
        if self.params.length > self.pos and samples > 0:
            len = min(samples, self.params.length - self.pos)
            end = value if len == samples else self.latest + (value - self.latest)*len/samples
            self.data[self.pos:self.pos + len] = np.linspace(self.latest, end, num=len, endpoint=False, dtype=np.float)
            self.pos += len
        self.latest = value
        return self

    def build(self):
        return self.data