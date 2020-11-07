import sys
import os
import unittest

sys.path.append(os.getcwd())

from utils.flatten import flatten_list


class FlattenListTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list_filled = [1, 2, [3, 4, [5, 6], 7], 8]
        self.input_list_empty = []

    def test_flatten_list_filled(self):
        response_flatten_list = flatten_list(self.input_list_filled, [])
        self.assertListEqual(response_flatten_list, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(type(response_flatten_list), list)
        self.assertEqual(sum(response_flatten_list), 36)

    def test_flatten_list_empty(self):
        response_flatten_list = flatten_list(self.input_list_empty, [])
        self.assertListEqual(response_flatten_list, [])
        self.assertEqual(type(response_flatten_list), list)
        self.assertEqual(sum(response_flatten_list), 0)


if __name__ == "__main__":
    unittest.main()
