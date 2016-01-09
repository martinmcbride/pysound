# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Sound file handling

import wave
import array

def write_wav(params, sound, filename):
    #Set the WAV file parameters, currently default values
    writer = wave.open(filename, 'wb');
    writer.setnchannels(1)
    writer.setsampwidth(2)
    writer.setframerate(params.rate)

    #Loop over all frames. For each frame, get the buffer (an np array) and
    #scale it to an array of ints, then write it out.
    for frame in range(int(params.time*params.rate)//params.size):
        data = array.array('h')
        v = next(sound)
        for i in range(params.size):
            data.append(int(v[i]*32767))
        writer.writeframes(data.tostring())

    writer.close()
