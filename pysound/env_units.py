import math  # Author:  Martin McBride
# Created: 2024-08-19
# Copyright (C) 2024, Martin McBride
# License: MIT

import numpy as np
from black.brackets import dataclass

from pysound.pysound_defs import Unit, DATA_LENGTH, Connection, TABLE_SIZE, DATA_TYPE, PARAMS, BaseUnit

"""
This module contains envelope units.
"""

@dataclass
class EnvSection:
    """
    Represents a section of an envelope, used by `GenericEnvelopeUnit`. The section has a fixed `length` in samples.

    A section has a fixed `length` in samples. It can create a constant signal, a linear ramp, or an exponential ramp:

    * `EnvSection(length, start)` creates a constant section.
    * `EnvSection(length, start, end)` creates a linear ramp.
    * `EnvSection(length, start, end, exp)` creates an exponential ramp.

    Args:
        length: the length of the section, in samples.
        start: the initial value of the section.
        end: the final value of the section.
        exp: the exponential factor of the section. A positive value causes the slope to start fast and then slow down,\\
        a negative value causes the slope to start slow and then speed up, 0 is linear.
        value causes the slope to start slow and speed up, zero creates a linear section.
    """
    length: int
    start: float
    end: float = None
    exp: float = 0


class GenericEnvelopeUnit(BaseUnit):
    """
    This is a generic envelope unit that can create a wide variety of envelopes defined by a list of `EnvSection` objects.
    """

    def __init__(self, sections: list, amplitude: Unit=1):
        """
        Args:
            sections: a list of `EnvSection` objects, each defining a section of the envelope of a particular length in samples.\
            Sections are appended back to back. To create gaps, add a constant section with value 0.

            amplitude: a signal that multiplies the envelope. Defaults to 1.
        """
        super().__init__()
        self.sections = []
        for s in sections:
            end = s.start if s.end is None else s.end
            self.sections.append((s.length, s.start, end, s.exp))
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
            out = np.column_stack([seg]*PARAMS.channels)*a
        else:
            xvals = np.linspace(0, x1, num=x1, endpoint=False, dtype=DATA_TYPE) / x1
            seg = y0 + (y1 - y0) * (1 - np.exp(-factor * xvals)) / (1 - math.exp(-factor))
            out = np.column_stack([seg]*PARAMS.channels)*a

        return out


class RampUnit(BaseUnit):
    """
    Genertes a ramp signal that changes from a start value to an end value over a fixed time
    """

    def __init__(self, length, start, end, exp=0, amplitude: Unit=1):
        """
        Args:
            length: the length of the envelope, in samples.
            start: the initial value of the envelope.
            end: the final value of the envelope.
            exp: the exponential factor of the envelope. A positive value causes the slope to start fast and then slow down,\\
            a negative value causes the slope to start slow and then speed up, 0 is linear.
            amplitude: a signal that multiplies the envelope. Defaults to 1.
        """
        super().__init__()
        sections = [
            EnvSection(length, start, end, exp)
        ]
        self.envelope = GenericEnvelopeUnit(sections, amplitude)


    def get(self):
        return self.envelope.get()
