import math
from dataclasses import dataclass

import numpy as np

from pysound.pysound_defs import Connection, TABLE_SIZE, PARAMS, BaseUnit, DATA_TYPE, Unit


@dataclass
class SeqItem:
    start_time: int
    duration: int
    unit: Unit


class SequencerUnit(BaseUnit):

    def __init__(self, signals: list, duration: int):
        super().__init__()
        self.signals = signals
        self.duration = duration

    def get(self):
        out = np.zeros((self.duration, PARAMS.channels), dtype=DATA_TYPE)

        for item in self.signals:
            if item.start_time >= self.duration:
                break
            duration = item.duration
            if item.start_time + duration >= self.duration:
                duration = self.duration - item.start_time
            conn = Connection(item.unit)
            content = conn.get(duration)
            out[item.start_time:item.start_time+duration] += content

        return out


