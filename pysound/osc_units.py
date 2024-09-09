# Author:  Martin McBride
# Created: 2024-08-19
# Copyright (C) 2024, Martin McBride
# License: MIT
import math
from numbers import Number

import numpy as np

from pysound.pysound_defs import Unit, DATA_LENGTH, Connection, TABLE_SIZE, DATA_TYPE, PARAMS, BaseUnit


class SineUnit(BaseUnit):
    """
    Creates a continuous sine wave signal.
    """

    def __init__(self, frequency: Unit=400, amplitude: Unit=1, offset: Unit=0, initial_phase: float=0):
        """
        Args:
            frequency: A signal that controls the frequency of the unit, default 400 Hz.

            amplitude: A signal that controls the amplitude of the unit, default 1.

            offset: A signal that is added to the output as an offset, default 0.

            initial_phase: The initial phase of the output wave, value 0.0 to 1.0 specifies phase as a fraction of a full\
            wave. Default 0.
        """
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


class SquareUnit(BaseUnit):
    """
    Creates a continuous square wave signal.
    """

    def __init__(self, frequency: Unit=400, amplitude: Unit=1, offset: Unit=0, ratio: Unit=0.5, initial_phase: float=0):
        """
        Args:
            frequency: A signal that controls the frequency of the unit, default 400 Hz.

            amplitude: A signal that controls the amplitude of the unit, default 1.

            offset: A signal that is added to the output as an offset, default 0.

            ratio: A signal that controls the mark-space ratio of the square wave

            initial_phase: The initial phase of the output wave, value 0.0 to 1.0 specifies phase as a fraction of a full\
            wave. Default 0.
        """
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


class SawUnit(BaseUnit):
    """
    Creates a continuous saw wave signal.
    """

    def __init__(self, frequency: Unit=400, amplitude: Unit=1, offset: Unit=0, ratio: Unit=0.5, initial_phase: float=0):
        """
        Args:
            frequency: A signal that controls the frequency of the unit, default 400 Hz.

            amplitude: A signal that controls the amplitude of the unit, default 1.

            offset: A signal that is added to the output as an offset, default 0.

            ratio: A signal that controls the rise-fall ratio of the saw wave

            initial_phase: The initial phase of the output wave, value 0.0 to 1.0 specifies phase as a fraction of a full\
            wave. Default 0.
        """
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


class NoiseUnit(BaseUnit):
    """
    Creates a continuous white noise signal.
    """

    def __init__(self, amplitude: Unit=1, offset: Unit=0):
        super().__init__()
        self.data_length = DATA_LENGTH
        self.amplitude = Connection(amplitude)
        self.offset = Connection(offset)


    def get(self):
        """
        Args:
            amplitude: A signal that controls the amplitude of the unit, default 1.

            offset: A signal that is added to the output as an offset, default 0.
        """
        a = self.amplitude.get(self.data_length)
        o = self.offset.get(self.data_length)
        out = o + a * (np.random.random(DATA_LENGTH) * 2 - 1)

        return out
