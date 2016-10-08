# Author:  Martin McBride
# Created: 2016-10-08
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
from pysound.wavetable import sine_wave
from pysound.envelopes import attack_decay
from pysound.music import Notes

from pysound.soundfile import write_wav

#
# Simple instrument
#
def instrument(freq):
    wave = sine_wave(frequency=freq, duration=0.5, amplitude=0.5);
    return wave;


#
# Create a sequence
#
seq = [
    (instrument(Notes.C4), 0),
    (instrument(Notes.D4), 0.5),
    (instrument(Notes.E4), 1.0),
    (instrument(Notes.F4), 1.5),
    (instrument(Notes.G4), 2.0),
    (instrument(Notes.A4), 2.5),
    (instrument(Notes.B4), 3.0),
    (instrument(Notes.C5), 3.5),
]

wave = sequencer(inputs=seq)
write_wav(source=wave, filename='scale.wav')