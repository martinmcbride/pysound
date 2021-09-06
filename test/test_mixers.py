import unittest
import numpy as np
from pysound.buffer import BufferParams
from pysound.mixers import modulator, adder, sequencer


class TestBuffer(unittest.TestCase):

    def test_modulator_0_sources(self):
        params = BufferParams(length=10)
        result = modulator()
        expected = np.array([], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_modulator_1_source(self):
        params = BufferParams(length=10)
        source0 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        result = modulator([source0])
        expected = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_modulator_2_sources(self):
        params = BufferParams(length=10)
        source0 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        source1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], np.float)
        result = modulator([source0, source1])
        expected = np.array([10.0, 40.0, 90.0, 160.0, 250.0, 360.0, 490.0, 640.0, 810.0, 1000.0], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_modulator_3_sources(self):
        params = BufferParams(length=10)
        source0 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        source1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], np.float)
        source1 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], np.float)
        result = modulator([source0, source1])
        expected = np.array([20.0, 80.0, 180.0, 320.0, 500.0, 720.0, 980.0, 1280.0, 1620.0, 2000.0], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_adder_0_sources(self):
        params = BufferParams(length=10)
        result = adder()
        expected = np.array([], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_adder_1_source(self):
        params = BufferParams(length=10)
        source0 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        result = adder([source0])
        expected = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_adder_2_sources(self):
        params = BufferParams(length=10)
        source0 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        source1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], np.float)
        result = adder([source0, source1])
        expected = np.array([11.0, 22.0, 33.0, 44.0, 55.0, 66.0, 77.0, 88.0, 99.0, 110.0], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_adder_3_sources(self):
        params = BufferParams(length=10)
        source0 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], np.float)
        source1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], np.float)
        source1 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], np.float)
        result = adder([source0, source1])
        expected = np.array([12.0, 24.0, 36.0, 48.0, 60.0, 72.0, 84.0, 96.0, 108.0, 120.0], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_sequencer_0_sources(self):
        params = BufferParams(length=10)
        result = sequencer(params, [])
        expected = np.array([0]*10, np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_sequencer_1_source(self):
        params = BufferParams(length=10)
        source0 = np.array([1]*3, np.float)
        result = sequencer(params, [(source0, 2)])
        expected = np.array([0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_sequencer_2_sources(self):
        params = BufferParams(length=10)
        source0 = np.array([1]*3, np.float)
        source1 = np.array([2]*4, np.float)
        result = sequencer(params, [(source0, 2), (source1, 6)])
        expected = np.array([0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 2.0, 2.0, 2.0, 2.0], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

    def test_sequencer_3_sources(self):
        params = BufferParams(length=10)
        source0 = np.array([1]*3, np.float)
        source1 = np.array([2]*4, np.float)
        source2 = np.array([3]*5, np.float)
        result = sequencer(params, [(source0, 2), (source1, 6), (source2, 0)])
        expected = np.array([3.0, 3.0, 4.0, 4.0, 4.0, 0.0, 2.0, 2.0, 2.0, 2.0], np.float)
        self.assertTrue(np.array_equal(result, expected), "Buffer not expected shape and content")

