import math  # Author:  Martin McBride
# Created: 2024-08-19
# Copyright (C) 2024, Martin McBride
# License: MIT

import numpy as np

from pysound.pysound_defs import Unit, DATA_LENGTH, Connection, TABLE_SIZE, DATA_TYPE, PARAMS, BaseUnit



class GenericEnvelopeUnit(BaseUnit):

    def __init__(self, sections: list, amplitude: Unit=1):
        """
        sections is a list of envelope sections. Each section is a tuple:

        (l, a) creates a constant level a for l samples
        (l, a, b) creates a linear ramp from a to b over l samples
        (l, a, b, f) creates an exponential ramp from a to b with curve factor f over l samples
        """
        super().__init__()
        self.sections = []
        for s in sections:
            if len(s) == 2:
                self.sections.append((s[0], s[1], s[1], 0))
            elif len(s) == 3:
                self.sections.append((s[0], s[1], s[2], 0))
            elif len(s) == 4:
                self.sections.append(tuple(s))
            else:
                ValueError("Each section must be a sequence of 2, 3, or 4 values")
        self.amplitude = Connection(amplitude)
        self.current_section = 0


    def get(self):
        if self.current_section >= len(self.sections):
            return np.zeros((DATA_LENGTH, PARAMS.channels), dtype=DATA_TYPE)

        section = self.sections[self.current_section]
        self.current_section += 1
        x0 = 0
        x1, y0, y1, factor = section

        a = self.amplitude.get(x1)

        if abs(factor) < 0.00001:
            seg = np.linspace(y0, y1, num=x1, endpoint=False, dtype=DATA_TYPE)
            out = np.column_stack((seg, seg))*a
        else:
            xvals = np.linspace(0, x1, num=x1, endpoint=False, dtype=DATA_TYPE) / x1
            seg = y0 + (y1 - y0) * (1 - np.exp(-factor * xvals)) / (1 - math.exp(-factor))
            out = np.column_stack((seg, seg))*a

        return out
