import unittest
from matrix import Matrix

#weronka341 - tested code creator

class MatrixTest(unittest.TestCase):
	def setUp(self):
		self.test_instance = Matrix(1, 5, 2, 1)

	def checkIfNotSquareMatrix():
		self.assertRaises(IncorrectValuePassed, Matrix(1, 2, 3))

	def checkIncorrectSizeAddition():
		self.assertRaises(IncorrectValuePassed, self.test_instance + Matrix(1, 2))
