import calc
import unittest

class CalcTest(unittest.TestCase):
    '''Calc tests'''

    @classmethod
    def setUpClass(cls):
        '''Set up for class'''
        print('setUpClass')
        print('==========\n')

    @classmethod
    def tearDownClass(cls):
        '''Tear down for class'''
        print('\n==========')
        print('tearDownClass')

    def setUp(self):
        '''Set up for test'''
        print('Set up for [' + self.shortDescription() + ']')

    def tearDown(self):
        '''Tear down for test'''
        print('Tear down for [' + self.shortDescription() + ']')
        print("")

    def test_add(self):
        '''Add operation test'''
        print('id: ' + self.id())
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        '''Sub operation test'''
        print('id: ' + self.id())
        self.assertEqual(calc.sub(4, 3), 1)

    def test_mul(self):
        '''Mul operation test'''
        print('id: ' + self.id())
        self.assertEqual(calc.mul(5, 6), 30)

    def test_div(self):
        '''Div operation test'''
        print('id: ' + self.id())
        self.assertEqual(calc.div(8, 4), 2)

if __name__ == '__main__':
    unittest.main()
