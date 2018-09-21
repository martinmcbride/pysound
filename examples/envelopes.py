from quack import buffer
from quack import soundfile
from quack import oscillators
from quack import envelopes


params = buffer.BufferParams().set_time(1)
env = envelopes.attack_decay(params, attack=params.t2s(0.01))
data = oscillators.sine_wave(params, frequency=500, amplitude=env)
soundfile.save(params, '/tmp/test.wav', data)
