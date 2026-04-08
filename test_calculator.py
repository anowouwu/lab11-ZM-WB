# https://github.com/anowouwu/lab11-ZM-WB
# Partner 1: Will Benson
# Partner 2: Zachary Miller
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(-2,3) == 1
        assert add(0,0) == 0
        assert add(0, 1) == 1

    def test_subtract(self): # 3 assertions
        assert subtract(5,3) == 2
        assert subtract(-2, 2) == -4
        assert subtract(0, -2) == 2

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert mul(-2, 4) == -8

    def test_divide(self): # 3 assertions
        assert div(4, 4) == 1

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        assert logarithm(8,2) == 3
        assert logarithm(100, 10) == 2
        assert logarithm(27,3) == 3

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(8,0)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(3, 4) == 5
        assert hypotenuse(5, 12) == 13
        assert hypotenuse(6, 8) == 10

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        assert square_root(4) == 2

# Do not touch this
if __name__ == "__main__":
    unittest.main()