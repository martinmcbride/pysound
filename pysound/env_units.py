 # Author:  Martin McBride
# Created: 2024-08-19
# Copyright (C) 2024, Martin McBride
# License: MIT

import numpy as np

from pysound_defs import Unit, DATA_LENGTH, Connection, TABLE_SIZE, DATA_TYPE, PARAMS, BaseUnit



class GenericEnvelopeUnit(BaseUnit):

    def __init__(self, sections: list, amplitude: Unit=1):
        super().__init__()
        self.sections = sections
        self.amplitude = Connection(amplitude)
        self.current_section = 0


    def get(self):
        a = self.amplitude.get(self.data_length)
        out = None

        return out
