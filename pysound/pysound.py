# Author:  Martin McBride
# Created: 2024-08-17
# Copyright (C) 2024, Martin McBride
# License: MIT

from dataclasses import dataclass
from typing import Type, Union

import numpy as np

DATA_LENGTH = 16
DATA_TYPE = np.double
TABLE_SIZE = 65536

@dataclass
class Params():
    sample_rate: int = 44100

PARAMS = Params()


class RawUnit:

    def __init__(self):
        pass

    def get(self):
        pass

Unit = RawUnit | int | float

class Connection:

    def __init__(self, unit: Unit):
        self.unit = unit
        self.data = np.zeros(0, DATA_TYPE)

    def get(self, length=DATA_LENGTH):
        if isinstance(self.unit, (int, float)):
            return np.full(length, self.unit)
        else:
            while len(self.data) < length:
                extra = self.unit.get()
                self.data = np.concatenate((self.data, extra))
            value = self.data[:length]
            self.data = self.data[length:]
            return value



class DummyUnit(RawUnit):
    """
    Unit that return fixed length buffers constaining [0.0, 1.0, 2.0...]

    Length is set in constructor. Mainly intended for testing purposes
    """

    def __init__(self, length: int):
        super().__init__()
        self.length = length

    def get(self):
        a = np.arange(5, dtype = np.double)
        return np.arange(self.length, dtype=DATA_TYPE)
