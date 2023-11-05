import unittest

from main import SynchronizingTables


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(SynchronizingTables(3, [15, 11, 19], [1000, 2000, 3000]), [2000, 1000, 3000])

    def test_something_1(self):
        self.assertEqual(SynchronizingTables(3, [50, 1, 1024], [20000, 100000, 90000]), [90000, 20000, 100000])


if __name__ == '__main__':
    unittest.main()
