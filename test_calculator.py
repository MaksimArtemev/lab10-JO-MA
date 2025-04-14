import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2

    def test_add(self):  # 3 assertions

        self.assertEqual(add(2, 5), 7)

        self.assertEqual(add(1, 3), 4)

        self.assertEqual(add(10, 10), 20)

    def test_subtract(self):  # 3 assertions

        self.assertEqual(subtract(5, 2), 3)

        self.assertEqual(subtract(10, 10), 0)

        self.assertEqual(subtract(5, 4), 1)

    ######## Partner 2

    def test_divide_by_zero(self):  # 1 assertion

        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions

        self.assertEqual(logarithm(100, 10), 2)

        self.assertEqual(logarithm(1, 5), 0)

        self.assertEqual(logarithm(8, 2), 3)

    def test_log_invalid_base(self):  # 1 assertion

        with self.assertRaises(ValueError):
            logarithm(-1, 1)

    def test_multiply(self):  # 3 assertions

        self.assertEqual(mul(1, 1), 1)

        self.assertEqual(mul(1, 9), 9)

        self.assertEqual(mul(9, 9), 81)

    def test_divide(self):  # 3 assertions

        self.assertEqual(div(9, 81), (1 / 9))

        self.assertEqual(div(5, 5), 1)

        self.assertAlmostEqual(div(1, 3), 0.33333333333333333)

    def test_log_invalid_argument(self):  # 1 assertion

        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions

        self.assertEqual(hypotenuse(2, 2), math.sqrt(8))

        self.assertEqual(hypotenuse(2, 3), math.sqrt(13))

        self.assertEqual(hypotenuse(10, 10), math.sqrt(200))

    def test_sqrt(self):  # 3 assertions

        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(1), 1)

        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()