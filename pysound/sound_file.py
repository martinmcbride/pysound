# Author:  Martin McBride
# Created: 2024-08-17
# Copyright (C) 2024, Martin McBride
# License: MIT

import wave
import array
import numpy as np
from scipy.io import wavfile

from pysound.pysound_defs import PARAMS, Connection, Unit, DATA_TYPE, BaseUnit, DATA_LENGTH


def write_wav_file(filename: str, source: Unit, length: int):
    """
    Write a sequence of samples as a WAV file.

    Args:
        filename: Full path of file to write
        source: unit that will be used to create sound
        length: required length of file in samples

    """
    conn = Connection(source)
    with wave.open(filename, 'wb') as writer:
        # Set the WAV file parameters, currently default values
        writer.setnchannels(PARAMS.channels)
        writer.setsampwidth(2)
        writer.setframerate(PARAMS.sample_rate)
        data_out = array.array('h')
        for x in conn.get(length):
            for i in range(PARAMS.channels):
                data_out.append(int(x[i] * 32766))
        writer.writeframes(data_out)

def write_text_file(filename: str, source: Unit, samples: int):
    """
    Write a sequence of samples as a text file

        filename: Full path of file to write
        source: unit that will be used to create sound
        length: required length of file in samples

    """
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

class AudioFileInputUnit(BaseUnit):

    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
        self.first = True

    def get(self):
        # After first call, just return zeros
        if not self.first:
            return np.zeros((DATA_LENGTH, PARAMS.channels), dtype=DATA_TYPE)
        self.first = False

        samplerate, data = wavfile.read(self.filename)
        return data/32767

def check_wav_file(filename: str):
    samplerate, data = wavfile.read(filename)
    print("File: {filename}")
    print(f"Sample rate: {samplerate}")
    print(f"Number of channels: {data.shape[1]}")
    print(f"Length (samples): {data.shape[0]}")
    print(f"Length (seconds): {data.shape[0]/samplerate}")
    print(f"Data type: {data.dtype}")

def read_text_file(filename: str):
    """
    Reads sound data from a text file of numerical values.
    The file should contain one sample per line, so

    * If it is a mono file, each line should contain one numerical value
    * If it is a sterea file, each line should contain two numerical values, separated by a space.

    Args:
        filename: full path of data file to read

    Returns:
        numpy array of audio data

    """
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

