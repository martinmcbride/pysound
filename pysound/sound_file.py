# Author:  Martin McBride
# Created: 2024-08-17
# Copyright (C) 2024, Martin McBride
# License: MIT

import wave
import array
import numpy as np

from pysound.pysound_defs import PARAMS, Connection, Unit, DATA_TYPE


def write_wav_file(filename: str, source: Unit, samples: int):
    '''
    Write a sequence of samples as a WAV file
    Currently a 16 bit mono file
    '''
    conn = Connection(source)
    with wave.open(filename, 'wb') as writer:
        # Set the WAV file parameters, currently default values
        writer.setnchannels(PARAMS.channels)
        writer.setsampwidth(2)
        writer.setframerate(PARAMS.sample_rate)
        data_out = array.array('h')
        for x in conn.get(samples):
            data_out.append(int(x[0] * 32766))
            data_out.append(int(x[1] * 32766))
        writer.writeframes(data_out)

def write_text_file(filename: str, source: Unit, samples: int):
    '''
    Write a sequence of samples as a text file
    '''
    conn = Connection(source)
    data = conn.get(samples)
    with open(filename, 'w') as writer:
        for x in data:
            for i in range(PARAMS.channels):
                writer.write(f"{x[i]:.8f} ")
            writer.write(f"\n")

def read_text_file(filename: str):
    '''
    Read a sequence of samples from a text file, stored one per line in format:

    -0.30598718268393843
    -0.47033054373828387
    0.41079667568696454
    ...
    '''
    data = []
    with open(filename, 'r') as reader:
        for line in reader.readlines():
            line = line.strip()
            values = line.split(" ")
            if len(values) != PARAMS.channels:
                raise Exception(f"Expected {PARAMS.channels} values per line, got {len(values)}")
            x = [float(v) for v in values]
            data.append(x)

    return np.array(data, dtype=DATA_TYPE)

