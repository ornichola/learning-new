import unittest
import test_calc_unittest_03

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(test_calc_unittest_03)

testResult = unittest.TestResult()

runner = unittest.TextTestRunner(verbosity=1)
testResult = runner.run(suites)
print('errors')
print(len(testResult.errors))
print('failures')
print(len(testResult.failures))
print('skipped')
print(len(testResult.skipped))
print('testsRun')
print(testResult.testsRun)
