import unittest

from pysound.pysound_defs import DummyUnit, Connection


class TestDummyUnit(unittest.TestCase):

    # Test output from DummyUnit. Tested here because it is needed to test connection
    def test_dummyunit(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(10)
        self.assertSequenceEqual(data.tolist(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


class TestConnection(unittest.TestCase):

    # Test output from DummyUnit. Tested here because it is needed to test connection
    def test_connection_exact_length(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(10)
        self.assertSequenceEqual(data.tolist(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_connection_short(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(5)
        self.assertSequenceEqual(data.tolist(), [0, 1, 2, 3, 4])
        data = conn.get(5)
        self.assertSequenceEqual(data.tolist(), [5, 6, 7, 8, 9])

    def test_connection_veryshort(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(3)
        self.assertSequenceEqual(data.tolist(), [0, 1, 2])
        data = conn.get(3)
        self.assertSequenceEqual(data.tolist(), [3, 4, 5])
        data = conn.get(3)
        self.assertSequenceEqual(data.tolist(), [6, 7, 8])

    def test_connection_long(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(15)
        self.assertSequenceEqual(data.tolist(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4])

    def test_connection_verylong(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(25)
        self.assertSequenceEqual(data.tolist(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4])

    def test_connection_split(self):
        unit = DummyUnit(10)
        conn = Connection(unit)
        data = conn.get(15)
        self.assertSequenceEqual(data.tolist(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4])
        data = conn.get(15)
        self.assertSequenceEqual(data.tolist(), [5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_connection_constant(self):
        conn = Connection([5, 5])
        data = conn.get(10)
        self.assertSequenceEqual(data.tolist(), [5, 5]*10)



if __name__ == '__main__':
    unittest.main()
