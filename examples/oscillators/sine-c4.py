# Author:  Martin McBride
# Created: 2021-09-12
# Copyright (C) 2021, Martin McBride
# License: MIT

from pysound.buffer import BufferParams
from pysound.oscillators import sine_wave
from pysound import soundfile
from pysound.const import Notes
from pysound.graphs import Plotter

## Create a sine wave middle C
params = BufferParams()
out = sine_wave(params, frequency=Notes.C4)
soundfile.save(params, '/tmp/sine-c4.wav', out)

## Plot a graph of the first part of the previous sine wave
Plotter(params, 'sine-c4.png', out).with_timerange(0, 0.1).plot()



