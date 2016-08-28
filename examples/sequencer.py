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

from pysound.sequencers import sequencer
from pysound.wavetable import square_wave
from pysound.music import Notes

from pysound.soundfile import write_wav

#
# Create a sequence
#
w1 = square_wave(frequency=Notes.A4, duration=1, amplitude=0.5)
w2 = square_wave(frequency=Notes.C4, duration=1, amplitude=0.5)
w3 = square_wave(frequency=Notes.E4, duration=1, amplitude=0.5)

seq = [
    (w1, 0),
    (w2, 1),
    (w3, 1.5),
    (w1, 2)
]

wave = sequencer(inputs=seq)
write_wav(source=wave, filename='sequencer.wav')