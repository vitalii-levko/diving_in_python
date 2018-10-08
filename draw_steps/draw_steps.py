import sys

if __name__ == "__main__":

	if len(sys.argv) == 2:

		if sys.argv[1].isdecimal():
			num_steps = int(sys.argv[1])
			step = "#"

			for i in range(1, num_steps+1):
				print('{0:>{width}}'.format(step*i, width=num_steps))

			sys.exit()

	print("usage: python3 path/to/draw_steps.py num_steps")