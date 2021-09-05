from pysound import buffer
from pysound import soundfile
from pysound import oscillators
from pysound import sequencers
from pysound.const import Notes as N

params = buffer.BufferParams()
data1 = oscillators.sine_wave(params, frequency=N.C4)
data2 = oscillators.sine_wave(params, frequency=N.D4)
data3 = oscillators.sine_wave(params, frequency=N.E4)
data4 = oscillators.sine_wave(params, frequency=N.F4)
data5 = oscillators.sine_wave(params, frequency=N.G4)
data6 = oscillators.sine_wave(params, frequency=N.A4)
data7 = oscillators.sine_wave(params, frequency=N.B4)
data8 = oscillators.sine_wave(params, frequency=N.C5)
data = sequencers.join((data1, data2, data3, data4, data5, data6, data7, data8))
soundfile.save(params, '/tmp/test.wav', data)
