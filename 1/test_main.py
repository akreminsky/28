import unittest

from main import squirrel

class FactTests(unittest.TestCase):
    def test_fact_first_num(self):
        self.assertEqual(1,  squirrel(5))
        self.assertEqual(3,  squirrel(10))
        self.assertEqual(8, squirrel(14))

    def test_zero_one(self):
        self.assertEqual(1, squirrel(0))
        self.assertEqual(1, squirrel(1))

    def test_minus(self):
        try:
            squirrel(-1)
        except Exception as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()