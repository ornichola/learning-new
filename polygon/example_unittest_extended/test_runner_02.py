import unittest
import test_calc_unittest_03

testCases = []
testCases.append(test_calc_unittest_03.CalcBasicTests)
testCases.append(test_calc_unittest_03.CalcExtendedTests)

testLoad = unittest.TestLoader()

suites = []

for tc in testCases:
    suites.append(testLoad.loadTestsFromTestCase(tc))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)
