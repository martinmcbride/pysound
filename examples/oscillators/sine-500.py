# Author:  Martin McBride
# Created: 2021-09-12
# Copyright (C) 2021, Martin McBride
# License: MIT

from pysound.buffer import BufferParams
from pysound.oscillators import sine_wave
from pysound import soundfile
from pysound.const import Notes
from pysound.graphs import Plotter

## Create a sine wave at 500 Hz
params = BufferParams()
out = sine_wave(params, frequency=500)
soundfile.save(params, '/tmp/sine-500.wav', out)

## Plot a graph of the first part of the previous sine wave
Plotter(params, 'sine-500.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz sine wave")\
                                    .in_milliseconds()\
                                    .plot()



