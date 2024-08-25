# Author:  Martin McBride
# Created: 2024-08-17
# Copyright (C) 2024, Martin McBride
# License: MIT

import wave
import array

from pysound.pysound_defs import PARAMS, Connection, Unit


def writewavfile(filename: str, source: Unit, samples: int):
    '''
    Write a sequence of samples as a WAV file
    Currently a 16 bit mono file
    '''
    conn = Connection(source)
    with wave.open(filename, 'wb') as writer:
        # Set the WAV file parameters, currently default values
        writer.setnchannels(1)
        writer.setsampwidth(2)
        writer.setframerate(PARAMS.sample_rate)
        data_out = array.array('h')
        for x in conn.get(samples):
            data_out.append(int(x * 32766))
        writer.writeframes(data_out)

def writetextfile(filename: str, source: Unit, samples: int):
    '''
    Write a sequence of samples as a text file
    '''
    conn = Connection(source)
    data = conn.get(samples)
    with open(filename, 'w') as writer:
        for x in data:
            writer.write(f"{x}\n")
