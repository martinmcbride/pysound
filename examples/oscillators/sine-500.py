# Author:  Martin McBride
# Created: 2021-09-12
# Copyright (C) 2021, Martin McBride
# License: MIT

from pysound.buffer import BufferParams
from pysound.oscillators import sine_wave
from pysound import soundfile
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

## Create a sine wave at 250 Hz
params = BufferParams()
out = sine_wave(params, frequency=250)
soundfile.save(params, '/tmp/sine-250.wav', out)

## Plot a graph of the first part of the previous sine wave
Plotter(params, 'sine-250.png', out).with_timerange(0, 0.01)\
                                    .with_title("250 Hz sine wave")\
                                    .in_milliseconds()\
                                    .plot()

## Create a sine wave at 500 Hz, amplitude 0.6
params = BufferParams()
out = sine_wave(params, frequency=500, amplitude=0.6)
soundfile.save(params, '/tmp/sine-500-6.wav', out)

## Plot a graph of the first part of the previous sine wave
Plotter(params, 'sine-500-6.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz sine wave, amplitude 0.6")\
                                    .with_yrange(-1, 1)\
                                    .in_milliseconds()\
                                    .plot()

## Create a sine wave at 500 Hz, amplitude 0.3, offset .4
params = BufferParams()
out = sine_wave(params, frequency=500, amplitude=0.3, offset=0.4)
soundfile.save(params, '/tmp/sine-500-3-4.wav', out)

## Plot a graph of the first part of the previous sine wave
Plotter(params, 'sine-500-3-4.png', out).with_timerange(0, 0.01)\
                                    .with_title("500 Hz sine wave, amplitude 0.4, offset 0.4")\
                                    .with_yrange(-1, 1)\
                                    .in_milliseconds()\
                                    .plot()




