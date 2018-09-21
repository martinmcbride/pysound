from pysound import buffer
from pysound import soundfile
from pysound import oscillators
from pysound import envelopes


params = buffer.BufferParams().set_time(1)
env = envelopes.attack_decay(params, attack=params.t2s(0.01))
data = oscillators.sine_wave(params, frequency=500, amplitude=env)
soundfile.save(params, '/tmp/test.wav', data)
