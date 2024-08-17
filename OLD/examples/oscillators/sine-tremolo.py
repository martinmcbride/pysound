# Author:  Martin McBride
# Created: 2021-09-12
# Copyright (C) 2021, Martin McBride
# License: MIT

from OLD.pysound.buffer import BufferParams
from OLD.pysound.oscillators import sine_wave
from OLD.pysound import soundfile
from OLD.pysound.const import Notes
from OLD.pysound.graphs import Plotter

params = BufferParams()

## Create a 10 Hz sine wave with an amplitude between 0.6 and 1.0
amp = sine_wave(params, frequency=10, amplitude=0.2, offset=0.8)

## Create a sine wave C3 with
out = sine_wave(params, frequency=Notes.C3, amplitude=amp)
soundfile.save(params, '/tmp/sine-tremolo.wav', out)

## Plot a graph of the first part of the amplitide sine wave
Plotter(params, 'sine-tremolo-amplitude.png', amp).with_timerange(0, 0.2).plot()

## Plot a graph of the first part of the tremolo sine wave
Plotter(params, 'sine-tremolo.png', out).with_timerange(0, 0.2).plot()



