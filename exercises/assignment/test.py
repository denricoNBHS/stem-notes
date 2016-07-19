# This code tests your solutions. Please do not change it! #
import re
import unittest


class Test(unittest.TestCase):
    def test_vars(self):
        import exercise
        self.assertTrue(hasattr(exercise, "one"),
                        'You must declare a variable called "one".')
        self.assertEqual(exercise.one, 1, 'variable one\'s value seems off.')

        self.assertTrue(hasattr(exercise, "roman_one"),
                        'Did you declare the variable "roman_one"?')
        self.assertEqual(exercise.roman_one, "I",
                         'roman_one is storing the wrong value.')

        with open('exercise.py') as f:
            s = f.read()
            m = re.search('(?P<var1>one|roman_one) *== *(?P<var2>one|roman_one)', s)

            self.assertTrue(m, 'Did you test for the right equivalence?')
            self.assertNotEqual(m.group('var1'), m.group('var2'),
                                'Seeing if a variable is equivalent to itself is silly!')

if __name__ == '__main__':
    unittest.main()