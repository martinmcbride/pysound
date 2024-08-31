import unittest

from pysound.osc_units import SineUnit, SquareUnit
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

    def test_non_defaults(self):
        unit = SineUnit(500, 0.3, 0.2, 0.5)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = readtextfile("expected/TestSineUnit_test_non_defaults.txt")
        compare_buffers(data, test_data)
        

class TestSquareUnit(unittest.TestCase):

    def test_defaults(self):
        unit = SquareUnit()
        conn = Connection(unit)
        data = conn.get(441)
        test_data = readtextfile("expected/TestSquareUnit_test_defaults.txt")
        compare_buffers(data, test_data)

    def test_non_defaults(self):
        unit = SquareUnit(500, 0.3, 0.2, 0.7, 0.5)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = readtextfile("expected/TestSquareUnit_test_non_defaults.txt")
        compare_buffers(data, test_data)