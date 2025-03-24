ECHO is on.
import unittest
from my_awesome_lib.data_utils import convert_to_int

class TestDataUtils(unittest.TestCase):
    def test_valid_conversion(self):
        self.assertEqual(convert_to_int("10"), 10)
        self.assertEqual(convert_to_int("0"), 0)

    def test_invalid_conversion(self):
        self.assertIsNone(convert_to_int("abc"))
        self.assertIsNone(convert_to_int("12.3"))

    def test_none_input(self):
        self.assertIsNone(convert_to_int(None))

if __name__ == '__main__':
    unittest.main()
