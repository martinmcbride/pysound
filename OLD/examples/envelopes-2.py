from OLD.pysound import soundfile, buffer, oscillators, sequencers
from OLD.pysound import envelopes
from OLD.pysound.const import Notes as N

def simple_instr(params, frequency):
    env = envelopes.attack_decay(params, attack=params.t2s(0.01))
    data = oscillators.sine_wave(params, frequency=frequency, amplitude=env)
    return data


params = buffer.BufferParams()
notes = [N.C4, N.D4, N.E4, N.F4, N.G4, N.A4, N.B4, N.C5]
buffers = [simple_instr(params, frequency=f) for f in notes]
data = sequencers.join(buffers)
soundfile.save(params, '/tmp/test.wav', data)
