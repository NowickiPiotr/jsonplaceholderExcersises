import unittest
import TestCreatingMethods
import TestDeleteMethods
import TestGetMethods
import TestUpdateMethods

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TestCreatingMethods))
suite.addTests(loader.loadTestsFromModule(TestDeleteMethods))
suite.addTests(loader.loadTestsFromModule(TestGetMethods))
suite.addTests(loader.loadTestsFromModule(TestUpdateMethods))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)