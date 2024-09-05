# Author:  Martin McBride
# Created: 2024-08-19
# Copyright (C) 2024, Martin McBride
# License: MIT

import numpy as np
import matplotlib.pyplot as plot
from pylab import rcParams

from pysound.pysound_defs import PARAMS, Connection


class Plotter:

    def __init__(self, filename: str, wave):
        self.filename = filename
        self.wave = Connection(wave)
        self.title = ''
        self.image_width = 10
        self.image_height = 4
        self.xrange = (0, 44100)
        self.yrange = None
        self.enable_milliseconds = False

    def with_title(self, title: str):
        self.title = title
        return self

    def with_size(self, image_width: int | float, image_height: int | float):
        self.image_width = image_width
        self.image_height = image_height
        return self

    def with_xrange(self, x0: int, x1: int):
        self.xrange = (x0, x1)
        return self

    def with_time_range(self, t0: float, t1: float):
        self.xrange = (t0*PARAMS.sample_rate, int(t1*PARAMS.sample_rate))
        return self

    def with_yrange(self, y0: int | float, y1: int | float):
        self.yrange = (y0, y1)
        return self

    def in_milliseconds(self, enable_milliseconds=True):
        self.enable_milliseconds = enable_milliseconds
        return self

    def plot(self):
        data = self.wave.get(self.xrange[1])
        rcParams['figure.figsize'] = self.image_width, self.image_height
        plot.figure()

        time_scale = 1000 if self.enable_milliseconds else 1
        time = np.linspace(0, self.xrange[1]*time_scale/PARAMS.sample_rate,
                           num=self.xrange[1])

        if self.xrange is not None:
            plot.xlim(self.xrange[0]*time_scale/PARAMS.sample_rate,
                      self.xrange[1]*time_scale/PARAMS.sample_rate)

        if self.yrange is not None:
            plot.ylim(*self.yrange)

        plot.plot(time, data)

        if self.title:
            plot.title(self.title)
        time_units = '(ms)' if self.enable_milliseconds else '(s)'
        plot.xlabel('Time ' + time_units)
        plot.ylabel('Amplitude')
        plot.grid(True, which='both')
        plot.axhline(y=0, color='k')
        plot.savefig(self.filename)