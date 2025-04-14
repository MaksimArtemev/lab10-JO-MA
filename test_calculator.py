import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(1, 1), 1)
        self.assertEqual(mul(1, 9), 9)
        self.assertEqual(mul(9, 9), 81)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(9, 81), (1 / 9))
        self.assertEqual(div(5, 5), 1)
        self.assertAlmostEqual(div(1, 3), 0.33333333333333333)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(2, 2), math.sqrt(8))
        self.assertEqual(hypotenuse(2, 3), math.sqrt(13))
        self.assertEqual(hypotenuse(10, 10), math.sqrt(200))

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()