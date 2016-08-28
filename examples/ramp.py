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

from pysound.soundfile import write_wav
from pysound.wavetable import sine_wave

from pysound.envelopes import ramp
from pysound.music import Notes

#
# Create a ramp envelope and a ramp frequency
#

freq = ramp(start=Notes.A4, end=Notes.A3)
wave = sine_wave(frequency=freq)
out = ramp(source=wave)
write_wav(source=out, filename='ramp.wav')