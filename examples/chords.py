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
from pysound.mixers import adder
from pysound.music import Notes

from pysound.soundfile import write_wav

#
# Simple instrument
#
def instrument(freq1, freq2, freq3):
    wave = adder(sources=[
                    sine_wave(frequency=freq1, duration=2, amplitude=0.3),
                    sine_wave(frequency=freq2, duration=2, amplitude=0.3),
                    sine_wave(frequency=freq3, duration=2, amplitude=0.3),
                    ],
                duration=2)
    return wave;


#
# Create a sequence
#
seq = [
    (instrument(Notes.C4, Notes.E4, Notes.G4), 0),
    (instrument(Notes.A3, Notes.C4, Notes.E4), 2),
    (instrument(Notes.F3, Notes.A3, Notes.C4), 4),
    (instrument(Notes.D4, Notes.F4, Notes.A4), 6),
]

wave = sequencer(inputs=seq)
write_wav(source=wave, filename='chords.wav')