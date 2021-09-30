# Author:  Martin McBride
# Created: 2021-09-30
# Copyright (C) 2021, Martin McBride
# License: MIT

from pysound.buffer import BufferParams
from pysound.oscillators import saw_wave
from pysound import soundfile
from pysound.graphs import Plotter

## Create a triangle wave at 500 Hz
params = BufferParams()
out = saw_wave(params, frequency=500)
soundfile.save(params, '/tmp/triangle-500.wav', out)

## Plot a graph of the first part of the previous saw wave
Plotter(params, 'triangle-500.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz triangle wave")\
                                    .in_milliseconds()\
                                    .plot()

## Create an unequal triangle wave at 500 Hz
params = BufferParams()
out = saw_wave(params, frequency=500, ratio=0.3)
soundfile.save(params, '/tmp/triangle-unequal-500.wav', out)

## Plot a graph of the first part of the previous saw wave
Plotter(params, 'triangle-unequal-500.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz unequal triangle wave")\
                                    .in_milliseconds()\
                                    .plot()

## Create a saw wave at 500 Hz
params = BufferParams()
out = saw_wave(params, frequency=500, ratio=0)
soundfile.save(params, '/tmp/saw-500.wav', out)

## Plot a graph of the first part of the previous saw wave
Plotter(params, 'saw-500.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz saw wave")\
                                    .in_milliseconds()\
                                    .plot()



