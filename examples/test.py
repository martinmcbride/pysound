from const import const
from oscillators import sine_wave, saw_wave, square_wave
from soundfile import SoundFile


freq = sine_wave(offset=const(400), frequency=const(10), amplitude=const(100))
ratio = sine_wave(offset=const(0.5), frequency=const(1), amplitude=const(0.4))
sound = square_wave(frequency=freq, ratio=ratio)

file = SoundFile()
file.write(sound)
file.close()
    