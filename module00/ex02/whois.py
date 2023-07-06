import sys

if len(sys.argv) == 1:
	print("usage: a number as argument needed")
	exit()

if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
	exit()

try:
	num = int(sys.argv[1])
except:
	num = ""

if type(num) is not int:
	print("AssertionError: argument is not an integer")
	exit()

if num == 0:
	print("I'm Zero.")
elif num % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")
