
import quack
from quack import buffer
from quack import soundfile
from quack import oscillators

params = buffer.BufferParams().time(2)
ratio = oscillators.saw_wave(params, frequency=10, amplitude=0.4, offset=0.5)
data = oscillators.saw_wave(params, frequency=400, ratio=ratio)
file = soundfile.save(params, '/tmp/test.wav', data)
