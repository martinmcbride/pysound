# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Sound file handling

import wave
import array

def write_wav(rate=11025, source=None, filename='temp.wav'):
    #Set the WAV file parameters, currently default values
    writer = wave.open(filename, 'wb');
    writer.setnchannels(1)
    writer.setsampwidth(2)
    writer.setframerate(rate)

    data_in = source.getData()
    data_out = array.array('h')
    for i in range(len(source)):
        data_out.append(int(data_in[i]*32767))
    writer.writeframes(data_out.tostring())

    writer.close()
