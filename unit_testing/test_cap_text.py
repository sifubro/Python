import unittest
import cap_text

import matplotlib.pyplot as plt

'''
run it as 
python test_cap_text.py
'''

class TestCapText(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = cap_text.capitalize_text(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = cap_text.capitalize_text(text)
        self.assertEqual(result, "Monty Python")

if __name__ == '__main__':
    unittest.main()

