from pysound import buffer
from pysound import soundfile
from pysound import oscillators

params = buffer.BufferParams()
data = oscillators.sine_wave(params)
soundfile.save(params, '/tmp/test.wav', data)

