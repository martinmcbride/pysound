import unittest

from pysound.env_units import GenericEnvelopeUnit, EnvSection, RampUnit, ADUnit, ADSRUnit
from pysound.pysound_defs import Connection, PARAMS
from pysound.sound_file import read_text_file
from test.utils import compare_buffers


class TestGenericEnvelopeUnit(unittest.TestCase):
    pass

    def test_const(self):
        unit = GenericEnvelopeUnit([EnvSection(441, 0.5)])
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestGenericEnvelopeUnit_test_const.txt")
        compare_buffers(data, test_data)

    def test_ramp(self):
        unit = GenericEnvelopeUnit([EnvSection(441, 0.7, -0.4)])
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestGenericEnvelopeUnit_test_ramp.txt")
        compare_buffers(data, test_data)

    def test_exp(self):
        unit = GenericEnvelopeUnit([EnvSection(441, 0.5, -0.6, 5)])
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestGenericEnvelopeUnit_test_exp.txt")
        compare_buffers(data, test_data)

    def test_negexp(self):
        unit = GenericEnvelopeUnit([EnvSection(441, 0.5, -0.6, -5)])
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestGenericEnvelopeUnit_test_negexp.txt")
        compare_buffers(data, test_data)

    def test_ramp_mono(self):
        PARAMS.channels = 1
        unit = GenericEnvelopeUnit([EnvSection(441, 0.7, -0.4)])
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestGenericEnvelopeUnit_test_ramp_mono.txt")
        compare_buffers(data, test_data)
        PARAMS.channels = 2

class TestRampUnit(unittest.TestCase):

    def test_default(self):
        unit = RampUnit(441, 0, 1)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestRampUnit_test_defaults.txt")
        compare_buffers(data, test_data)

    def test_exp(self):
        unit = RampUnit(441, 0, 1, 4)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestRampUnit_test_exp.txt")
        compare_buffers(data, test_data)


class TestADUnit(unittest.TestCase):

    def test_default(self):
        unit = ADUnit(441, 100, 1)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestADUnit_test_defaults.txt")
        compare_buffers(data, test_data)

    def test_exp(self):
        unit = ADUnit(441, 300, 0.5, 4)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestADUnit_test_exp.txt")
        compare_buffers(data, test_data)

class TestADSRUnit(unittest.TestCase):

    def test_default(self):
        unit = ADSRUnit(441, 50, 50, 50, 1, 0.5)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestADSRUnit_test_defaults.txt")
        compare_buffers(data, test_data)

    def test_exp(self):
        unit = ADSRUnit(441, 50, 100, 25, 0.5, 0.2, 4)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestADSRUnit_test_exp.txt")
        compare_buffers(data, test_data)
