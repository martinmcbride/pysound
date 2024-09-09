# Author:  Martin McBride
# Created: 2024-08-17
# Copyright (C) 2024, Martin McBride
# License: MIT

from dataclasses import dataclass
from typing import Type, Union

import numpy as np

DATA_LENGTH = 1024
"""Default data length. Buffers can be any length, but if there are no special requirements this is a reasonable value to use."""

DATA_TYPE = np.double

TABLE_SIZE = 65536
"""Default table size for wave tables and similar"""

@dataclass
class Params():
    """
    Class holding global parameters for audio generation
    """
    sample_rate: int = 44100
    """Sample rate in samples per second"""

    channels: int = 2
    """Number of channels - 1 for mono, 2 for stereo, or more for other systems"""

PARAMS = Params()

def t2s(time):
    return int(time*PARAMS.sample_rate)

class BaseUnit:
    """
    Base class for all audio units
    """

    def __init__(self):
        pass

    def get(self):
        """
        Get some data from the unit. The unit will return a data buffer containing 1 or more samples. Use the shape of the
        buffer to determine the length and number of channels.
        """
        pass

Unit = BaseUnit | float

class Connection:
    """
    Accepts data from a unit and sends it to another unit.

    A unit can request data buffers of any convenient size, and it can return data buffers of any convenient size. This often
    simplifies the design of individual units. The buffer sizes often won't match. For example the supplying unit might return
    buffers of length 256 samples, but the receiving unit might request buffers of length 400 samples.

    The `Connection` acts a buffer between units so each can do its own thing.
    """

    def __init__(self, unit: Unit):
        """
        Args:
            unit: the supplying unit.
        """
        self.unit = unit
        self.data = np.zeros((0, PARAMS.channels), DATA_TYPE)

    def get(self, length=DATA_LENGTH):
        if isinstance(self.unit, (int, float)):
            return np.full((length, PARAMS.channels), self.unit)
        if isinstance(self.unit, (list, tuple)):
            if len(self.unit) != PARAMS.channels:
                raise ValueError(f"Connection list value has length {len(self.unit)} but number of channels is {PARAMS.channels}")
            return np.full((length, PARAMS.channels), self.unit)
        else:
            while len(self.data) < length:
                extra = self.unit.get()
                self.data = np.concatenate((self.data, extra))
            value = self.data[:length]
            self.data = self.data[length:]
            return value



class DummyUnit(BaseUnit):
    """
    Unit that returns a repeating pattern of [0.0, 1.0, 2.0 ... length-1] on all channels

    Length is set in constructor. Mainly intended for testing purposes.
    """

    def __init__(self, length: int):
        """
        Args:
            length: Length of repeat pattern.
        """
        super().__init__()
        self.length = length

    def get(self):
        a = np.arange(self.length, dtype=DATA_TYPE)
        return np.tile(a, (PARAMS.channels, 1)).transpose(1, 0)
