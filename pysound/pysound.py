# Author:  Martin McBride
# Created: 2024-08-17
# Copyright (C) 2024, Martin McBride
# License: MIT

import numpy as np

DATA_LENGTH = 256
DATA_TYPE = np.double


class Connection:

    def __init__(self, unit):
        self.unit = unit
        self.data = []

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


class Unit:

    def __init__(self):
        pass

    def get(self):
        pass
    

class DummyUnit(Unit):
    """
    Unit that return fixed length buffers constaining [0.0, 1.0, 2.0...]

    Length is set in constructor. Mainly intended for testing purposes
    """

    def __init__(self, length):
        super().__init__()
        self.length = length

    def get(self):
        a = np.arange(5, dtype = np.double)
        return np.arange(self.length, dtype=DATA_TYPE)
