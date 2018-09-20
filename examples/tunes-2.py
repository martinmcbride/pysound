from quack import buffer
from quack import soundfile
from quack import oscillators
from quack import sequencers
from quack.const import Notes as N

params = buffer.BufferParams().set_time(1)
notes = [N.C4, N.D4, N.E4, N.F4, N.G4, N.A4, N.B4, N.C5]
buffers = [oscillators.sine_wave(params, frequency=f) for f in notes]
data = sequencers.join(buffers)
soundfile.save(params, '/tmp/test.wav', data)
