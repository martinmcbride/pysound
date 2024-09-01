import unittest

from pysound.mix_units import SequencerUnit, SeqItem
from pysound.pysound_defs import Connection
from pysound.sound_file import read_text_file
from test.utils import compare_buffers


class TestSequencerUnit(unittest.TestCase):

    def test_single(self):
        unit = SequencerUnit([SeqItem(100, 50, 0.5)], 441)
        conn = Connection(unit)
        data = conn.get(441)
        test_data = read_text_file("expected/TestSequencerUnit_test_single.txt")
        compare_buffers(data, test_data)
