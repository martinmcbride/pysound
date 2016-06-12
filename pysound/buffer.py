# Author:  Martin McBride
# Created: 2016-06-11
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound

import numpy as np

#
# Soundbuffer holds a data array of sound samples
#
class SoundBuffer:
    def __init__(self, samples):
        self.data = np.zeros(samples)

    def getData(self):
        return self.data;

    def __len__(self):
        return self.data.size

#
# Helper function. If value is a SoundBuffer return its data.
# If value is a number, return a data array filled with that number.
#
def get_buffer(samples, value):
    if type(value)==SoundBuffer:
        return value.getData()
    else:
        data = np.zeros(samples)
        data.fill(value)
        return data

