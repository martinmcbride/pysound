from quack import buffer
from quack import soundfile
from quack import oscillators

params = buffer.BufferParams().set_time(2)
data = oscillators.sine_wave(params, frequency=600, amplitude=0.5)
soundfile.save(params, '/tmp/test.wav', data)

