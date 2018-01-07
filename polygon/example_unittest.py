import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

# this should be included for running unittests from module
# and then script should be launched as:
# $ python3 modulename.py
if __name__ == '__main__':
    unittest.main()

# or we can exclude last idiom and launch test using command:
# $ python3 -m unittest -v modulename.py
