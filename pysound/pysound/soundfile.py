# Author:  Martin McBride
# Created: 2018-04-21
# Copyright (C) 2018, Martin McBride
# License: MIT

import wave
import array

'''
Write a sequence of samples as a WAV file
Currently a 16 bit mono file
'''
class SoundFile:
    
    def __init__(self, filename='temp.wav', rate=11025):
        self.writer = wave.open(filename, 'wb');
        # Set the WAV file parameters, currently default values
        self.writer.setnchannels(1)
        self.writer.setsampwidth(2)
        self.writer.setframerate(rate)

    def write(self, source, samples=11025):
        data_out = array.array('h')
        for i, x in zip(range(samples), source):
            data_out.append(int(x * 32767))
        self.writer.writeframes(data_out.tostring())
    
    def close(self):
        self.writer.close()