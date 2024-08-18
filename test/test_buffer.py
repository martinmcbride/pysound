import unittest
import numpy as np
from pysound.pysound import DummyUnit


class TestDummyUnit(unittest.TestCase):

    # Test output from DummyUnit
    def test_bufferparams_default_constructor(self):
        unit = DummyUnit(10)
        data = unit.get()
        # self.assertEqual(params.get_sample_rate(), 44100)
        # self.assertEqual(params.get_length(), 44100)


if __name__ == '__main__':
    unittest.main()
