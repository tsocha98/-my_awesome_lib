ECHO is on.
import unittest
from my_awesome_lib.math_tools import add

class TestMathTools(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

if __name__ == '__main__':
    unittest.main()
