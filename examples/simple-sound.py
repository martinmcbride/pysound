from quack import buffer
from quack import soundfile
from quack import oscillators

params = buffer.BufferParams()
data = oscillators.sine_wave(params)
soundfile.save(params, '/tmp/test.wav', data)

