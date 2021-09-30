# Author:  Martin McBride
# Created: 2021-09-30
# Copyright (C) 2021, Martin McBride
# License: MIT

from pysound.buffer import BufferParams
from pysound.oscillators import square_wave
from pysound import soundfile
from pysound.graphs import Plotter

## Create a square wave at 500 Hz
params = BufferParams()
out = square_wave(params, frequency=500)
soundfile.save(params, '/tmp/square-500.wav', out)

## Plot a graph of the first part of the previous square wave
Plotter(params, 'square-500.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz square wave")\
                                    .in_milliseconds()\
                                    .plot()

## Create a square wave at 500 Hz
params = BufferParams()
out = square_wave(params, frequency=500, ratio=0.2)
soundfile.save(params, '/tmp/pulse-500.wav', out)

## Plot a graph of the first part of the previous square wave
Plotter(params, 'pulse-500.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz pulse wave")\
                                    .in_milliseconds()\
                                    .plot()



