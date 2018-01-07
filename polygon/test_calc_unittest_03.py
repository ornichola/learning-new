import calc
import unittest

class CalcBasicTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(4, 3), 1)

    def test_mul(self):
        self.assertEqual(calc.mul(5, 6), 30)

    def test_div(self):
        self.assertEqual(calc.div(8, 4), 2)


class CalcExtendedTests(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(calc.sqrt(25), 5)

    def test_pow(self):
        self.assertEqual(calc.pow(2, 6), 64)


if __name__ == '__main__':
    unittest.main()
