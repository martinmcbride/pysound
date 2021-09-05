from pysound import buffer
from pysound import soundfile
from pysound import oscillators
from pysound import envelopes
from pysound.const import Notes as N


params = buffer.BufferParams()
env = envelopes.attack_decay(params, attack=params.t2s(0.01))
data = oscillators.sine_wave(params, frequency=N.C4, amplitude=env)
soundfile.save(params, '/tmp/test.wav', data)
