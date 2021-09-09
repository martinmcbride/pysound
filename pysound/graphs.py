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

    def with_title(self, title):
        self.title = title
        return self

    def with_size(self, image_width, image_height):
        self.image_width = image_width
        self.image_height = image_height
        return self

    def plot(self):
        rcParams['figure.figsize'] = self.image_width, self.image_height
        time = np.linspace(0, self.params.get_length()/self.params.get_sample_rate(), num=self.params.get_length());
        plot.plot(time, self.waves[0])
        if self.title:
            plot.title(self.title)
        plot.xlabel('Time')
        plot.ylabel('Amplitude')
        plot.grid(True, which='both')
        plot.axhline(y=0, color='k')
        plot.savefig(self.filename)