# Author:  Martin McBride
# Created: 2021-09-12
# Copyright (C) 2021, Martin McBride
# License: MIT

from pysound.buffer import BufferParams
from pysound.oscillators import sine_wave
from pysound import soundfile
from pysound.envelopes import linseg
from pysound.graphs import Plotter

## Create a sine wave 40Hz
params = BufferParams()
out = sine_wave(params, frequency=40)
soundfile.save(params, '/tmp/sine-40.wav', out)

## Plot a graph of the he previous sine wave
Plotter(params, 'sine-40.png', out).plot()

## Create a sine wave 20 to 60Hz
freq = linseg(params, start=20, end=60)
out = sine_wave(params, frequency=freq)
soundfile.save(params, '/tmp/sine-rising.wav', out)

## Plot a graph of the he previous sine wave
Plotter(params, 'sine-rising.png', out).plot()



