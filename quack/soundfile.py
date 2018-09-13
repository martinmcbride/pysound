# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import wave
import array
from const import get_settings

'''
Write a sequence of samples as a WAV file
Currently a 16 bit mono file
'''
class SoundFile:
    
    def __init__(self, filename='temp.wav', settings=None):
        self.writer = wave.open(filename, 'wb');
        self.settings = get_settings(settings)
        # Set the WAV file parameters, currently default values
        self.writer.setnchannels(1)
        self.writer.setsampwidth(2)
        self.writer.setframerate(self.settings.sample_rate)

    def write(self, source):
        data_out = array.array('h')
        for x in source:
            data_out.append(int(x * 16384))
        self.writer.writeframes(data_out.tostring())
    
    def close(self):
        self.writer.close()