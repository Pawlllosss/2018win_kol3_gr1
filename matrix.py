from math import sqrt

class IncorrectValuePassed(Exception):
	pass


class Matrix:

	def __init__ (self, *args):
		n = sqrt(len(args))
		if not n.is_integer():
			raise IncorrectValuePassed('Incorrect number of values for square matrix')
		else:
			self._size = int(n)
			self._elements = self._size * self._size
			self._values = [args[i * self._size : (i + 1) * self._size ] for i in range(self._size)]


	def __str__ (self):
		output = '\n' + ('\n'.join(['  '.join(['{:{}}'.format(item, self._size) for item in row]) for row in self._values]))
		return output + '\n'


	def __add__ (self, other):
		if isinstance(other, int):
			result = [x + other for rows in self._values for x in rows]
			return Matrix(*result)

		if other._size != self._size:
			raise IncorrectValuePassed("Wrong dimension of matrix you want to add. Should be {}".format(self._size))
		
		if isinstance(other, Matrix):
			result = []
			for i in range(self._size):
				for j in range(self._size):
					result.append(self._values[i][j] + other._values[i][j])
			return Matrix(*result)


	def __radd__ (self, other):
		return self.__add__(other)


	def __sub__ (self, other):
		if isinstance(other, int):
			result = [x - other for rows in self._values for x in rows]
			return Matrix(*result)

		if other._size != self._size:
			raise IncorrectValuePassed("Wrong dimension of matrix you want to subtract. Should be {}".format(self._size))
		
		if isinstance(other, Matrix):
			result = []
			for i in range(self._size):
				for j in range(self._size):
					result.append(self._values[i][j] - other._values[i][j])
			return Matrix(*result)


	def __rsub__ (self, other):
		return self.__sub__(other)


	def __mul__ (self, other):
		if isinstance(other, int):
			result = []
			for i in range(self._size):
				for j in range(self._size):
					result.append(self._values[i][j] * other)
			return Matrix(*result)

		if self._size != other._size:
			raise IncorrectValuePassed("Wrong dimension of matrix you want to multiply. Should be {}".format(self._size))

		if isinstance(other, Matrix):
			result = []
			for i in range(self._size):
				for j in range(self._size):
					s = 0
					for k in range(self._size):
						s += self._values[i][k] * self._values[k][j]
					result.append(s)
			return Matrix(*result)

	def __rmul__ (self, other):
		return self.__mul__(other)



