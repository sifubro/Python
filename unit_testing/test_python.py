import unittest
import cap_text
import arithmetic

import matplotlib.pyplot as plt

'''
run it as 
python test_cap_text.py
'''

class TestAddInt(unittest.TestCase):

    def test_one(self):
        '''
        You can add multiple checks in 1 test!
        '''

        x, y = (1,2)
        result = arithmetic.add(x,y)
        self.assertEqual(result, 3)

        x, y = (3,-5)
        result = arithmetic.add(x,y)
        self.assertEqual(result, -2)

        x, y = (-8,8)
        result = arithmetic.add(x,y)
        self.assertEqual(result, 0)

        # you can even test exceptions
        x, y = (-8,0)
        #self.assertRaises(ValueError, arithmetic.divide, x, y)
        with self.assertRaises(ValueError):
            arithmetic.divide(x,y)


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

