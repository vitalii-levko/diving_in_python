import sys

if __name__ == "__main__":

	if len(sys.argv) == 2:
		digit_string = sys.argv[1]

		if digit_string.isdecimal():
			digit_sum = 0

			for digit in digit_string:
				digit_sum += int(digit)

			print(digit_sum)
			sys.exit()

	print("usage: python3 path/to/solution.py digit_string")
