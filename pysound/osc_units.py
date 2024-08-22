# Author:  Martin McBride
# Created: 2024-08-19
# Copyright (C) 2024, Martin McBride
# License: MIT
import math
from numbers import Number

import numpy as np

from pysound.pysound import Unit, DATA_LENGTH, Connection, TABLE_SIZE, DATA_TYPE, PARAMS, RawUnit


class SineUnit(RawUnit):

    def __init__(self, frequency: Unit=400, amplitude: Unit=1, offset: Unit=0, phase: float=0):
        super().__init__()
        self.data_length = DATA_LENGTH
        self.frequency = Connection(frequency)
        self.amplitude = Connection(amplitude)
        self.offset = Connection(offset)
        self.phase = Connection(phase)
        self.previous_index = 0

        args = np.linspace(0.0, 2 * math.pi, num=TABLE_SIZE, endpoint=False)
        self.table = np.sin(args)


    def get(self):
        f = self.frequency.get(self.data_length)
        a = self.amplitude.get(self.data_length)
        o = self.offset.get(self.data_length)
        p = self.phase.get(self.data_length)
        index_accumulator = np.add.accumulate(f / PARAMS.sample_rate) % 1
        index = np.floor(((p + self.previous_index + index_accumulator) % 1) * TABLE_SIZE).astype(int)
        out = o + a * self.table[index]
        self.previous_index += index_accumulator[-1]

        return out
