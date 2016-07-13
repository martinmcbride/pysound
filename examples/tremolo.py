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

from pysound.wavetable import sine_wave
from pysound.wavetable import square_wave

from pysound.soundfile import write_wav

#
# Create a tremolo effect
#
amp = sine_wave(frequency=10, amplitude=0.1, offset = 0.8)
wave = square_wave(frequency=400, amplitude=amp)
write_wav(source=wave, filename='tremolo.wav')