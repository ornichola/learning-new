import unittest
import test_calc_unittest

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_calc_unittest.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
