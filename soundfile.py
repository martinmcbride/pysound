# Author:  Martin McBride
# Created: 2024-08-17
# Copyright (C) 2024, Martin McBride
# License: MIT

import wave
import array

from pysound.pysound import PARAMS, Connection


def writewavfile(filename, source, samples):
    '''
    Write a sequence of samples as a WAV file
    Currently a 16 bit mono file
    '''
    conn = Connection(source)
    writer = wave.open(filename, 'wb');
    # Set the WAV file parameters, currently default values
    writer.setnchannels(1)
    writer.setsampwidth(2)
    writer.setframerate(PARAMS.sample_rate)
    data_out = array.array('h')
    for x in conn.get(samples):
        data_out.append(int(x * 32766))
    writer.writeframes(data_out)
    writer.close()