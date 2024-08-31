import unittest

from pysound.osc_units import SineUnit, SquareUnit, SawUnit
from pysound.pysound_defs import Connection
from pysound.soundfile import read_text_file
from test.utils import compare_buffers


class TestSineUnit(unittest.TestCase):

    def test_defaults(self):
        unit = SineUnit()
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestSineUnit_test_defaults.txt")
        compare_buffers(data, test_data)

    def test_non_defaults(self):
        unit = SineUnit(500, 0.3, 0.2, 0.5)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestSineUnit_test_non_defaults.txt")
        compare_buffers(data, test_data)
        

class TestSquareUnit(unittest.TestCase):

    def test_defaults(self):
        unit = SquareUnit()
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestSquareUnit_test_defaults.txt")
        compare_buffers(data, test_data)

    def test_non_defaults(self):
        unit = SquareUnit(500, 0.3, 0.2, 0.7, 0.5)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestSquareUnit_test_non_defaults.txt")
        compare_buffers(data, test_data)
        
        
class TestSawUnit(unittest.TestCase):

    def test_defaults(self):
        unit = SawUnit()
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestSawUnit_test_defaults.txt")
        compare_buffers(data, test_data)

    def test_non_defaults(self):
        unit = SawUnit(500, 0.3, 0.2, 0.7, 0.5)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestSawUnit_test_non_defaults.txt")
        compare_buffers(data, test_data)