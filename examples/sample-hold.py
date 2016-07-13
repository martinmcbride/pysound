# Author:  Martin McBride
# Created: 2016-06-12
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound


try:
    import pysound
except ImportError:
    # if pysound is not installed append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

from pysound.sequencers import sample_and_hold
from pysound.wavetable import sine_wave
from pysound.wavetable import square_wave

from pysound.soundfile import write_wav

#
# use sample and hold to vary frequency
#

params = {'duration': 10}

lfo = sine_wave(frequency=7, offset=500, amplitude=100, **params)
trigger = square_wave(frequency=2.596, **params)
freq = sample_and_hold(source=lfo, trigger=trigger, **params)
out = sine_wave(frequency=freq, **params)
write_wav(source=out, filename='sample-hold.wav')