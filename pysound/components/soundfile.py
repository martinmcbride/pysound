# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Sound file handling

import wave
import array

def write_wav(rate=11025, samples=11025, source=[], filename='temp.wav'):
    #Set the WAV file parameters, currently default values
    writer = wave.open(filename, 'wb');
    writer.setnchannels(1)
    writer.setsampwidth(2)
    writer.setframerate(rate)

    data = array.array('h')
    for i in range(samples):
        data.append(int(source[i]*32767))
    writer.writeframes(data.tostring())

    writer.close()
