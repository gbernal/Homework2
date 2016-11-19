# Showing a unites

import unittest


class OutcomesTest(unittest.TestCase):
	
	def test(self):
		self.assertTrue(True)
	
	def test_fail(self):
		self.assertTrue(False)

	def test_error(self):
		self.RuntimeError('Test error!')

# if this file is run directly, run the tests
if __name__ == '__main__':
    unittest.main()


