# Author:  Martin McBride
# Created: 2021-09-05
# Copyright (C) 2021, Martin McBride
# License: MIT

import numpy as np
import matplotlib.pyplot as plot
from pylab import rcParams

class Plotter:

    def __init__(self, params, filename, *waves):
        self.params = params
        self.filename = filename
        self.waves = waves
        self.title = ''
        self.image_width = 10
        self.image_height = 4
        self.xrange = None
        self.yrange = None
        self.enable_milliseconds = False

    def with_title(self, title):
        self.title = title
        return self

    def with_size(self, image_width, image_height):
        self.image_width = image_width
        self.image_height = image_height
        return self

    def with_xrange(self, x0, x1):
        self.xrange = (x0, x1)
        return self

    def with_timerange(self, t0, t1):
        x0 = self.params.t2s(t0)
        x1 = self.params.t2s(t1)
        self.xrange = (x0, x1)
        return self

    def with_yrange(self, y0, y1):
        self.yrange = (y0, y1)
        return self

    def in_milliseconds(self, enable_milliseconds=True):
        self.enable_milliseconds = enable_milliseconds;
        return self

    def plot(self):
        rcParams['figure.figsize'] = self.image_width, self.image_height
        plot.figure()

        time_scale = 1000 if self.enable_milliseconds else 1
        time = np.linspace(0, self.params.get_length()*time_scale/self.params.get_sample_rate(),
                           num=self.params.get_length())

        if self.xrange:
            plot.xlim(self.xrange[0]*time_scale/self.params.get_sample_rate(),
                      self.xrange[1]*time_scale/self.params.get_sample_rate())

        if self.yrange:
            plot.ylim(*self.yrange)

        for wave in self.waves:
            plot.plot(time, wave)

        if self.title:
            plot.title(self.title)
        time_units = '(ms)' if self.enable_milliseconds else '(s)'
        plot.xlabel('Time ' + time_units)
        plot.ylabel('Amplitude')
        plot.grid(True, which='both')
        plot.axhline(y=0, color='k')
        plot.savefig(self.filename)
