import sys

if __name__ == "__main__":

	def fibonacci(number):
		a = b = 1
		for _ in range(number):
			yield a
			a, b = b, a + b

	if len(sys.argv) == 2:

		if sys.argv[1].isdecimal():
			number = int(sys.argv[1])
			num_list = [str(num) for num in fibonacci(number) if num <= number]
			print(', '.join(num_list))
			sys.exit()

	print("usage: python3 path/to/fibonacci.py number")
