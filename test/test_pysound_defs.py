import unittest

import numpy as np

from pysound.osc_units import SineUnit
from pysound.pysound_defs import DummyUnit, Connection, BufferUnit, DATA_LENGTH, BufferReaderUnit
from test.utils import compare_buffers


class TestDummyUnit(unittest.TestCase):

    # Test output from DummyUnit. Tested here because it is needed to test connection
    def test_dummyunit(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(10)
        self.assertSequenceEqual(data.tolist(), [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]])


class TestConnection(unittest.TestCase):

    # Test output from DummyUnit. Tested here because it is needed to test connection
    def test_connection_exact_length(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(10)
        self.assertSequenceEqual(data.tolist(), [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]])

    def test_connection_short(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(5)
        self.assertSequenceEqual(data.tolist(), [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])
        data = conn.get(5)
        self.assertSequenceEqual(data.tolist(), [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]])

    def test_connection_veryshort(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(3)
        self.assertSequenceEqual(data.tolist(), [[0, 0], [1, 1], [2, 2]])
        data = conn.get(3)
        self.assertSequenceEqual(data.tolist(), [[3, 3], [4, 4], [5, 5]])
        data = conn.get(3)
        self.assertSequenceEqual(data.tolist(), [[6, 6], [7, 7], [8, 8]])

    def test_connection_long(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(15)
        self.assertSequenceEqual(data.tolist(), [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])

    def test_connection_verylong(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(25)
        self.assertSequenceEqual(data.tolist(), [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])

    def test_connection_split(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(15)
        self.assertSequenceEqual(data.tolist(), [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])
        data = conn.get(15)
        self.assertSequenceEqual(data.tolist(), [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]])

    def test_connection_constant(self):
        conn = Connection([5, 5])
        data = conn.get(10)
        self.assertSequenceEqual(data.tolist(), [[5, 5]]*10)


class TestBufferUnit(unittest.TestCase):

    # def test_bufferunit_1_connection(self):
    #     unit = SineUnit(frequency=101)
    #     buffer = BufferUnit(unit)
    #     reader = BufferReaderUnit(buffer)
    #     conn0 = Connection(reader)
    #     data = conn0.get(DATA_LENGTH*3)
    #
    #     unit = SineUnit(101)
    #     conn =  Connection(unit)
    #     expected = conn.get(DATA_LENGTH*3)
    #     compare_buffers(data, expected)
    #
    # def test_bufferunit_3_connection(self):
    #     unit = SineUnit(frequency=101)
    #     buffer = BufferUnit(unit)
    #     reader1 = BufferReaderUnit(buffer)
    #     conn0 = Connection(reader1)
    #     data0 = conn0.get(DATA_LENGTH*3)
    #     reader2 = BufferReaderUnit(buffer)
    #     conn1 = Connection(reader2)
    #     data1 = conn1.get(DATA_LENGTH*3)
    #     reader3 = BufferReaderUnit(buffer)
    #     conn2 = Connection(reader3)
    #     data2 = conn2.get(DATA_LENGTH*3)
    #
    #     unit = SineUnit(101)
    #     conn =  Connection(unit)
    #     expected = conn.get(DATA_LENGTH*3)
    #     compare_buffers(data0, expected)
    #     compare_buffers(data1, expected)
    #     compare_buffers(data2, expected)

    def test_bufferunit_diff_length(self):
        unit = SineUnit(frequency=101)
        buffer = BufferUnit(unit)
        reader1 = BufferReaderUnit(buffer)
        conn0 = Connection(reader1)
        reader2 = BufferReaderUnit(buffer)
        conn1 = Connection(reader2)
        reader3 = BufferReaderUnit(buffer)
        conn2 = Connection(reader3)
        data0a = conn0.get(DATA_LENGTH + 1)
        data1a = conn1.get(DATA_LENGTH-1)
        data2a = conn2.get(512)
        data0b = conn0.get(DATA_LENGTH + 1)
        data1b = conn1.get(DATA_LENGTH-1)
        data2b = conn2.get(DATA_LENGTH*2)
        data0c = conn0.get(DATA_LENGTH - 2)
        data1c = conn1.get(DATA_LENGTH+2)
        data2c = conn2.get(512)

        unit = SineUnit(101)
        conn =  Connection(unit)
        expected = conn.get(DATA_LENGTH*3)
        compare_buffers(np.concatenate((data0a, data0b, data0c)), expected)
        compare_buffers(np.concatenate((data1a, data1b, data1c)), expected)
        compare_buffers(np.concatenate((data2a, data2b, data2c)), expected)



if __name__ == '__main__':
    unittest.main()
