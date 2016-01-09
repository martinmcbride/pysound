# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Square wave example


try:
    import pysound
except ImportError:
    # if pysound is not installed append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import numpy as np
from pysound.params import Params
from pysound.soundfile import write_wav
from pysound.constant import constant
from pysound.wavetable import square_wave

params = Params()

wave = square_wave(params, constant(params, 400), constant(params, 1), constant(params, 0.5), constant(params, 0))
write_wav(params, wave, 'test.wav')