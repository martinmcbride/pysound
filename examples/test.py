
import quack
from quack import buffer
from quack import soundfile
from quack import oscillators

params = buffer.BufferParams().time(2)
data = oscillators.table_wave(params, frequency=400)
file = soundfile.save(params, '/tmp/test.wav', data)
