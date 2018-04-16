import unittest
import matrix


# weronka341 - tested code creator

class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.test_instance = matrix.Matrix(1, 5, 2, 1)

    def test_notsquarematrix(self):
        self.assertRaises(matrix.IncorrectValuePassed, matrix.Matrix, 1, 2, 3)
        self.assertRaises(matrix.IncorrectValuePassed, matrix.Matrix, 1, 2, 3, 43, 12)
        self.assertRaises(matrix.IncorrectValuePassed, matrix.Matrix, 23, 12, 654, 23123, 43)

    def test_creatingemptymatrix(self):
        self.assertRaises(matrix.IncorrectValuePassed, matrix.Matrix)

    def test_wronginputtype(self):
        self.assertRaises(matrix.IncorrectValuePassed, matrix.Matrix, '12', '32', '3', '7')
        self.assertRaises(matrix.IncorrectValuePassed, matrix.Matrix, "I don't have idea what I'm doing")

    def test_zeromatrixmultiplication(self):
        zero_matrix = matrix.Matrix(*[0] * 9)
        second_matrix = matrix.Matrix(*range(1,10))
        result_matrix1 = zero_matrix * second_matrix
        result_matrix2 = second_matrix * zero_matrix
        self.assertEqual(zero_matrix._values, result_matrix1._values)
        self.assertEqual(zero_matrix._values, result_matrix2._values)

    def test_identitymatrixmultiplication(self):
        identity_matrix = matrix.Matrix(1, 0, 0, 0, 1, 0, 0, 0, 1)
        second_matrix = matrix.Matrix(2, 3, 1, 5, 3, 12, 54, 32, 12)
        result_matrix1 = identity_matrix * second_matrix
        result_matrix2 = second_matrix * identity_matrix
        self.assertEqual(second_matrix._values, result_matrix1._values)
        self.assertEqual(second_matrix._values, result_matrix2._values)

    def test_addition(self):
        first_matrix = matrix.Matrix(*range(1,10))
        second_matrix = matrix.Matrix(*range(1,19, 2))
        result1 = first_matrix + second_matrix
        result2 = second_matrix + first_matrix
        self.assertEqual([(2, 5, 8), (11, 14, 17), (20, 23, 26)], result1._values)
        self.assertEqual([(2, 5, 8), (11, 14, 17), (20, 23, 26)], result2._values)

    def test_incorrectsizeaddition(self):
        with self.assertRaises(matrix.IncorrectValuePassed):
            self.test_instance + matrix.Matrix(1, 2, 4, 5, 1, 5, 3, 2, 65)
            matrix.Matrix(1, 2, 4, 5, 1, 5, 3, 2, 65) + self.test_instance

    def test_substraction(self):
        first_matrix = matrix.Matrix(12, 34, 21, 5)
        second_matrix = matrix.Matrix(5, 13, 12, 32)
        result1 = first_matrix - second_matrix
        result2 = second_matrix - first_matrix
        self.assertEqual([(7, 21), (9, -27)], result1._values)
        self.assertEqual([(-7, -21), (-9, 27)], result2._values)

    def test_matrixconversionwrongtype(self):
        with self.assertRaises(matrix.IncorrectValuePassed):
            self.test_instance + '2'
            '34' + self.test_instance
            self.test_instance + "string"
            "anotherstring" + self.test_instance

    def test_incorrectsizesubstraction(self):
        with self.assertRaises(matrix.IncorrectValuePassed):
            self.test_instance - matrix.Matrix(1, 2, 4, 5, 1, 5, 3, 2, 65)
            matrix.Matrix(1, 2, 4, 5, 1, 5, 3, 2, 65) - self.test_instance


if __name__ == "__main__":
    unittest.main()
