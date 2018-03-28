from matrix import Matrix

def run():

	A = Matrix(1,2,3,4)
	print("Macierz A:")
	print(A)

	B = Matrix(5,6,7,8)
	print("Macierz B:")
	print(B)

	print("Macierz M = A + 1:")
	M = A + 1
	print(M)

	print("Macierz M = 1 + A:")
	M = 1 + A
	print(M)

	print("Macierz M = B + A:")
	M = B + A
	print(M)

	print("Macierz M = A * 2:")
	M = A * 2
	print(M)

	print("Macierz M = 2 * A:")
	M = 2 * A
	print(M)

	print("Macierz M = B * A:")
	M = B * A
	print(M)

if __name__ == "__main__":
	run()