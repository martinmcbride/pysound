import unittest
import numpy as np
from pysound.buffer import BufferParams, create_buffer, mix_buffer


class TestBuffer(unittest.TestCase):

    # Create default buffer params
    def test_bufferparams_default_constructor(self):
        params = BufferParams()
        self.assertEqual(params.get_sample_rate(), 44100)
        self.assertEqual(params.get_length(), 44100)

    # Create non-default buffer params
    def test_bufferparams_non_default_constructor(self):
        params = BufferParams(length=1000, sample_rate=3000)
        self.assertEqual(params.get_sample_rate(), 3000)
        self.assertEqual(params.get_length(), 1000)

    # Change length
    def test_bufferparams_with_length(self):
        params = BufferParams()
        params = params.with_length(2000)
        self.assertEqual(params.get_sample_rate(), 44100)
        self.assertEqual(params.get_length(), 2000)

    # Change duration
    def test_bufferparams_with_duration(self):
        params = BufferParams()
        params = params.with_duration(1.5)
        self.assertEqual(params.get_sample_rate(), 44100)
        self.assertEqual(params.get_length(), 66150)

    # Change sample_rate
    def test_bufferparams_with_sample_rate(self):
        params = BufferParams()
        params = params.with_sample_rate(8000)
        self.assertEqual(params.get_sample_rate(), 8000)
        self.assertEqual(params.get_length(), 44100)

    # Test time to samples
    def test_t2s(self):
        params = BufferParams(sample_rate=1000)
        self.assertEqual(params.t2s(2.5), 2500)

    # Create zero buffer
    def test_create_zero_buffer(self):
        params = BufferParams(length=10)
        buffer = create_buffer(params)
        expected = np.array([0.0]*10, np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

    # Create filled buffer
    def test_create_filled_buffer(self):
        params = BufferParams(length=9)
        buffer = create_buffer(params, 1.1)
        expected = np.array([1.1]*9, np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

    # Create copied buffer with source length equal to buffer length
    def test_create_copied_buffer_src_length_eq_dest_length(self):
        params = BufferParams(length=7)
        src = np.array([2, 4, 6, 8, 10, 12, 14], np.float)
        buffer = create_buffer(params, src)
        expected = np.array([2, 4, 6, 8, 10, 12, 14], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

    # Create copied buffer with source length less than buffer length
    def test_create_copied_buffer_src_length_lt_dest_length(self):
        params = BufferParams(length=10)
        src = np.array([2, 4, 6, 8, 10, 12, 14], np.float)
        buffer = create_buffer(params, src)
        expected = np.array([2, 4, 6, 8, 10, 12, 14, 0, 0, 0], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

    # Create copied buffer with source length greater than buffer length
    def test_create_copied_buffer_src_length_gt_dest_length(self):
        params = BufferParams(length=5)
        src = np.array([2, 4, 6, 8, 10, 12, 14], np.float)
        buffer = create_buffer(params, src)
        expected = np.array([2, 4, 6, 8, 10], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

    # Create copied buffer with source length of 1
    def test_create_copied_buffer_src_length_1(self):
        params = BufferParams(length=5)
        src = np.array([2], np.float)
        buffer = create_buffer(params, src)
        expected = np.array([2, 0, 0, 0, 0], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

    # Mix data into a buffer
    def test_insert_array_at_0(self):
        # Same length
        params = BufferParams(length=5)
        buffer = create_buffer(params, 1)
        data = np.array([2, 4, 6, 8, 10], np.float)
        mix_buffer(buffer, data, 0)
        expected = np.array([3, 5, 7, 9, 11], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

        # Data shorter than buffer
        params = BufferParams(length=5)
        buffer = create_buffer(params, 1)
        data = np.array([2, 4, 6, 8], np.float)
        mix_buffer(buffer, data, 0)
        expected = np.array([3, 5, 7, 9, 1], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

    def test_insert_array_at_2(self):
        # Data exactly fills buffer
        params = BufferParams(length=5)
        buffer = create_buffer(params, 1)
        data = np.array([2, 4, 6], np.float)
        mix_buffer(buffer, data, 2)
        expected = np.array([1, 1, 3, 5, 7], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

        # Data shorter than buffer
        params = BufferParams(length=5)
        buffer = create_buffer(params, 1)
        data = np.array([2, 4], np.float)
        mix_buffer(buffer, data, 2)
        expected = np.array([1, 1, 3, 5, 1], np.float)
        self.assertTrue(np.array_equal(buffer, expected), "Buffer not expected shape and content")

if __name__ == '__main__':
    unittest.main()
