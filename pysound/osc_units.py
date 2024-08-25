# Author:  Martin McBride
# Created: 2024-08-19
# Copyright (C) 2024, Martin McBride
# License: MIT
import math
from numbers import Number

import numpy as np

from pysound.pysound_defs import Unit, DATA_LENGTH, Connection, TABLE_SIZE, DATA_TYPE, PARAMS, RawUnit


class SineUnit(RawUnit):

    def __init__(self, frequency: Unit=400, amplitude: Unit=1, offset: Unit=0, initial_phase: float=0):
        super().__init__()
        self.data_length = DATA_LENGTH
        self.frequency = Connection(frequency)
        self.amplitude = Connection(amplitude)
        self.offset = Connection(offset)
        self.initial_phase = Connection(initial_phase)
        self.previous_phase = 0

        args = np.linspace(0.0, 2 * math.pi, num=TABLE_SIZE, endpoint=False)
        self.table = np.sin(args)


    def get(self):
        f = self.frequency.get(self.data_length)
        a = self.amplitude.get(self.data_length)
        o = self.offset.get(self.data_length)
        p = self.initial_phase.get(self.data_length)
        phase_accumulator = np.add.accumulate(f / PARAMS.sample_rate) % 1
        index = np.floor(((p + self.previous_phase + phase_accumulator) % 1) * TABLE_SIZE).astype(int)
        out = o + a * self.table[index]
        self.previous_phase += phase_accumulator[-1]

        return out


class SquareUnit(RawUnit):

    def __init__(self, frequency: Unit=400, amplitude: Unit=1, offset: Unit=0, ratio: Unit=0.5, initial_phase: float=0):
        super().__init__()
        self.data_length = DATA_LENGTH
        self.frequency = Connection(frequency)
        self.amplitude = Connection(amplitude)
        self.offset = Connection(offset)
        self.ratio = Connection(ratio)
        self.initial_phase = Connection(initial_phase)
        self.previous_phase = 0


    def get(self):
        f = self.frequency.get(self.data_length)
        a = self.amplitude.get(self.data_length)
        o = self.offset.get(self.data_length)
        r = self.ratio.get(self.data_length)
        p = self.initial_phase.get(self.data_length)
        phase_accumulator = np.add.accumulate(f / PARAMS.sample_rate) % 1
        phase = (p + self.previous_phase + phase_accumulator) % 1
        out = o + a * np.where(phase < r, 1, -1)
        self.previous_phase += phase_accumulator[-1]

        return out


class SawUnit(RawUnit):

    def __init__(self, frequency: Unit=400, amplitude: Unit=1, offset: Unit=0, ratio: Unit=0.5, initial_phase: float=0):
        super().__init__()
        self.data_length = DATA_LENGTH
        self.frequency = Connection(frequency)
        self.amplitude = Connection(amplitude)
        self.offset = Connection(offset)
        self.ratio = Connection(ratio)
        self.initial_phase = Connection(initial_phase)
        self.previous_phase = 0


    def get(self):
        f = self.frequency.get(self.data_length)
        a = self.amplitude.get(self.data_length)
        o = self.offset.get(self.data_length)
        r = self.ratio.get(self.data_length)
        p = self.initial_phase.get(self.data_length)
        phase_accumulator = np.add.accumulate(f / PARAMS.sample_rate) % 1
        phase = (p + self.previous_phase + phase_accumulator) % 1
        out = o + a * np.where(phase < r, -1 + 2 * phase / r, 1 - 2 * (phase - r) / (1 - r))
        self.previous_phase += phase_accumulator[-1]

        return out


class NoiseUnit(RawUnit):

    def __init__(self, amplitude: Unit=1, offset: Unit=0):
        super().__init__()
        self.data_length = DATA_LENGTH
        self.amplitude = Connection(amplitude)
        self.offset = Connection(offset)


    def get(self):
        a = self.amplitude.get(self.data_length)
        o = self.offset.get(self.data_length)
        out = o + a * (np.random.random(DATA_LENGTH) * 2 - 1)

        return out
