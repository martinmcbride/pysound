import unittest

from pysound.osc_units import SineUnit
from pysound.pysound_defs import Connection
from pysound.soundfile import readtextfile
from test.utils import compare_buffers


class TestSineUnit(unittest.TestCase):

    def test_defaults(self):
        unit = SineUnit()
        conn = Connection(unit)
        data = conn.get(441)
        test_data = readtextfile("expected/TestSineUnit_test_defaults.txt")
        compare_buffers(data, test_data)