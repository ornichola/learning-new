import unittest
import test_calc_unittest_03

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_calc_unittest_03.CalcBasicTests))
calcTestSuite.addTest(unittest.makeSuite(test_calc_unittest_03.CalcExtendedTests))
print("count of test: " + str(calcTestSuite.countTestCases()) + '\n')

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
