# Generate expected results file, and a plot, for any unit
from pysound.env_units import ADSRUnit, GenericEnvelopeUnit, EnvSection
from pysound.graph import Plotter
from pysound.math_units import AddUnit
from pysound.osc_units import SineUnit
from pysound.pysound_defs import PARAMS
from pysound.sound_file import write_text_file

PARAMS.channels = 2

def get_unit():
    a = GenericEnvelopeUnit([EnvSection(441, 0, 0.5)])
    b = SineUnit(400, 0.5)
    r = AddUnit(a, b)
    return r

DATA_FILE = "TestMathUnits_test_add.txt"

DATA_LENGTH = 441

PLOT_FILE = "test.png"
PLOT_TIME_RANGE = (0, DATA_LENGTH/PARAMS.sample_rate)

plotter = Plotter(f"../scratch/{PLOT_FILE}", get_unit()).with_time_range(*PLOT_TIME_RANGE).with_yrange(-1.2, 1.2).in_milliseconds()
plotter.plot()

write_text_file(f"expected/{DATA_FILE}", get_unit(), DATA_LENGTH)
