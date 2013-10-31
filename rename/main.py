import sys
try:
	path = sys.argv[1]
	print(path)
except IndexError:
	print("No path given")
