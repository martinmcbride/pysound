# Generate expected results file, and a plot, for any unit

from pysound.graph import Plotter
from pysound.osc_units import SineUnit, SquareUnit
from pysound.pysound_defs import PARAMS
from pysound.soundfile import writetextfile


def get_unit():
    return SquareUnit()

DATA_FILE = "TestSquareUnit_test_defaults.txt"

DATA_LENGTH = 441

PLOT_FILE = "test.png"
PLOT_TIME_RANGE = (0, DATA_LENGTH/PARAMS.sample_rate)

plotter = Plotter(f"../scratch/{PLOT_FILE}", get_unit()).with_time_range(*PLOT_TIME_RANGE).with_yrange(-1.2, 1.2).in_milliseconds()
plotter.plot()

writetextfile(f"expected/{DATA_FILE}", get_unit(), DATA_LENGTH)
