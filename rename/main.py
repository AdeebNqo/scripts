import sys
from string import ascii_lowercase

lc = list(ascii_lowercase)
letters = [0,1,2,3,4,5,6,7,8,9]+lc

def getname():
	print('name given')
try:
	path = sys.argv[1]
	print(path)
except IndexError:
	print("No path given")
