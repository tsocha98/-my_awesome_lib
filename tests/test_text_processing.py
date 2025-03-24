import unittest
from my_awesome_lib.text_processing import reverse_text

class TestTextProcessing(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")
        self.assertEqual(reverse_text("Python"), "nohtyP")

    def test_reverse_text_with_spaces(self):
        self.assertEqual(reverse_text("hello world"), "dlrow olleh")

    def test_reverse_text_empty_string(self):
        self.assertEqual(reverse_text(""), "")

    def test_reverse_text_special_characters(self):
        self.assertEqual(reverse_text("123!@#"), "#@!321")

if __name__ == '__main__':
    unittest.main()

