# Generate expected results file, and a plot, for any unit
from pysound.env_units import GenericEnvelopeUnit
from pysound.graph import Plotter
from pysound.mix_units import SequencerUnit, SeqItem
from pysound.osc_units import SineUnit, SquareUnit, SawUnit
from pysound.pysound_defs import PARAMS
from pysound.sound_file import write_text_file, write_wav_file

PARAMS.channels = 2

def get_unit():
    return SineUnit((400, 200), (0.5, 0.7))

DATA_FILE = "test.txt"

DATA_LENGTH = 44100

PLOT_FILE = "test.png"
PLOT_TIME_RANGE = (0, DATA_LENGTH/PARAMS.sample_rate)

plotter = Plotter(f"../scratch/{PLOT_FILE}", get_unit()).with_time_range(*PLOT_TIME_RANGE).with_yrange(-1.2, 1.2).in_milliseconds()
plotter.plot()

write_text_file(f"expected/{DATA_FILE}", get_unit(), DATA_LENGTH)

write_wav_file(f"expected.wav", get_unit(), DATA_LENGTH)
