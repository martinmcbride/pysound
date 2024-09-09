import unittest

from pysound.env_units import GenericEnvelopeUnit, EnvSection, RampUnit, ADUnit, ADSRUnit
from pysound.math_units import AddUnit
from pysound.osc_units import SineUnit
from pysound.pysound_defs import Connection, PARAMS
from pysound.sound_file import read_text_file
from test.utils import compare_buffers

class TestMathUnits(unittest.TestCase):

    def test_add(self):
        a = GenericEnvelopeUnit([EnvSection(441, 0, 0.5)])
        b = SineUnit(400, 0.5)
        unit = AddUnit(a, b)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestMathUnits_test_add.txt")
        compare_buffers(data, test_data)
