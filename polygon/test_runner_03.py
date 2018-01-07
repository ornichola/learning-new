import unittest
import test_calc_unittest_03

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(test_calc_unittest_03)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suites)
