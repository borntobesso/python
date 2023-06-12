import sys
import string

argc = len(sys.argv)

if argc != 3:
	print("ERROR")
	exit()
str = sys.argv[1]
try:
	n = int(sys.argv[2])
except ValueError:
	print("ERROR")
	exit()
if n < 0 or len(str) == 0:
	print("ERROR")
	exit()
	
str = str.split()
str_without_punctuation = [s.translate(s.maketrans("", "", string.punctuation)) for s in str]
str = [s for s in str_without_punctuation if len(s) > n]

print(str)