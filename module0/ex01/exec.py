import sys

arguments = sys.argv[1:]
arg = ""

def swap_case(s):
	new_s = ""
	for c in s:
		if c.islower():
			new_s += c.upper()
		elif c.isupper():
			new_s += c.lower()
		else:
			new_s += c
	return new_s

if len(arguments) > 1:
	arg = " ".join(arguments)
elif len(arguments) == 1:
	arg = arguments[0]
else:
	print("usage: one or more arguments needed")
	exit()

rev_arg = arg[::-1]
print(swap_case(rev_arg))
