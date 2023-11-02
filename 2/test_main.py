import unittest

from main import odometer


class FactTests(unittest.TestCase):
    def test_odometer_nums(self):
        self.assertEqual(800, odometer([10, 20, 30, 40]))
        self.assertEqual(30, odometer([10, 1, 20, 2]))

    def test_odometer_long_ints(self):
        self.assertEqual(5930, odometer([10, 1, 20, 2, 100, 3, 400, 5, 1000, 10]))
