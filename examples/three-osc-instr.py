from pysound import buffer
from pysound import soundfile
from pysound import oscillators
from pysound import envelopes
from pysound import mixers
from pysound import const

def three_osc_instr(params, frequency, detune1, detune2):
    tone1 = oscillators.saw_wave(params, frequency=frequency)
    tone2 = oscillators.saw_wave(params, frequency=frequency*(1-detune1))
    tone3 = oscillators.saw_wave(params, frequency=frequency*(1+detune2))
    return (tone1 + tone2 + tone3) / 3


params = buffer.BufferParams().set_time(4).set_tempo(120)
detune1 = envelopes.linseg(params, 0.001, 0.007)
detune2 = envelopes.linseg(params, 0.005, 0.002)
data = three_osc_instr(params, frequency=400, detune1=detune1, detune2=detune2)
soundfile.save(params, '/tmp/test.wav', data)
