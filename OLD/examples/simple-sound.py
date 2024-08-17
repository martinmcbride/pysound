from OLD.pysound import soundfile, buffer, oscillators

params = buffer.BufferParams()
data = oscillators.sine_wave(params)
soundfile.save(params, '/tmp/test.wav', data)

