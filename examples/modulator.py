# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound


try:
    import pysound
except ImportError:
    # if pysound is not installed append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

from pysound.soundfile import write_wav
from pysound.wavetable import sine_wave

from pysound.mixers import modulator

#
# Mix the signals
#
wave1 = sine_wave(frequency=400)
wave2 = sine_wave(frequency=10)
wave = modulator(sources=[wave1, wave2])
write_wav(source=wave, filename='modulator.wav')