
import quack
from quack import buffer
from quack import soundfile
from quack import oscillators
from quack import envelopes
from quack import mixers

params = buffer.BufferParams().time(2)
ramp = envelopes.linseg(params, 100, 400)
env = envelopes.attack_decay(params, params.t2s(1), 0, 1)
data = oscillators.table_wave(params, frequency=ramp)
data2 = oscillators.table_wave(params, frequency=ramp+5)
data3 = oscillators.table_wave(params, frequency=ramp+8)
data4 = oscillators.table_wave(params, frequency=ramp+11)
sum = mixers.adder([data, data2, data3, data4])
mod = mixers.modulator([env, sum])
data = envelopes.GenericEnvelope(params).linseg(1, params.t2s(1)).linseg(0, params.t2s(2)).build()

file = soundfile.save(params, '/tmp/test.wav', data)
