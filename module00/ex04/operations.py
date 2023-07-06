import sys

def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def prod(a, b):
    return a * b

def quot(a, b):
    if b == 0:
        return "ERROR (division by zero)"
    return a / b

def rem(a, b):
    if b == 0:
        return "ERROR (modulo by zero)"
    return a % b

if len(sys.argv) != 3:
    if len(sys.argv) == 1:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("\tpython operations.py 10 3")
    elif len(sys.argv) == 2:
        print("AssertionError: too few arguments")
    else:
        print("AssertionError: too many arguments")
    exit()

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except:
    print("AssertionError: only integers")
    exit()

print("Sum:\t\t", sum(a, b))
print("Difference:\t", diff(a, b))
print("Product:\t", prod(a, b))
print("Quotient:\t", quot(a, b))
print("Remainder:\t", rem(a, b))