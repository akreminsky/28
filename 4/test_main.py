import unittest

from main import *


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual([0], MadMax(1, [0]))

    def test_one_one(self):
        self.assertEqual([1, 3, 2], MadMax(3, [1, 2, 3]))

    def test_massive(self):
        self.assertEqual([1, 3, 4, 5, 10, 9, 8, 7, 6], MadMax(9, [1, 3, 5, 4, 7, 6, 10, 9, 8]))

    def test_massive_2(self):
        self.assertEqual([1, 2, 3, 7, 6, 5, 4], MadMax(7, [1, 2, 3, 4, 5, 6, 7]))

    def test_massive_shaffle(self):
        self.assertEqual([2, 3, 4, 5, 10, 9, 8, 7, 6], MadMax(9, [10, 9, 8, 7, 6, 5, 4, 3, 2]))


if __name__ == '__main__':
    unittest.main()
