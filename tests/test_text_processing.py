ECHO is on.
import unittest
from my_awesome_lib.text_processing import count_words

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("Python is awesome"), 3)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

if __name__ == '__main__':
    unittest.main()
