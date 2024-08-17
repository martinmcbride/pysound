from OLD.pysound import soundfile, buffer, oscillators
from OLD.pysound import envelopes
from OLD.pysound.const import Notes as N


params = buffer.BufferParams()
env = envelopes.attack_decay(params, attack=params.t2s(0.01))
data = oscillators.sine_wave(params, frequency=N.C4, amplitude=env)
soundfile.save(params, '/tmp/test.wav', data)
