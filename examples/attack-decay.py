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
from pysound.wavetable import saw_wave

from pysound.envelopes import attack_decay

#
# Create an attack/decay envelope
#

wave = saw_wave(frequency=400)
out = attack_decay(duration = 0.3, attack_time= 0.01, source=wave)
write_wav(source=out, filename='attack-decay.wav')