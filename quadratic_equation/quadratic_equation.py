import sys

if __name__ == "__main__":

	if len(sys.argv) == 4:
		a = int(sys.argv[1])
	
		if a:
			b = int(sys.argv[2])
			c = int(sys.argv[3])
			d = b**2 - 4*a*c

			if d > 0:
				x1 = int((-b + d**0.5) / 2*a)
				x2 = int((-b - d**0.5) / 2*a)
				print(x1)
				print(x2)
			elif d == 0:
				x1 = int(-b / 2*a)
				print(x1)
			else:
				print("There are no roots on the set of real numbers")

			sys.exit()

		print("'a' should not be equal to 0")
		sys.exit()

	print("usage: coefficient_a coefficient_b coefficient_c")
