import sys


def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    if len(sys.argv) == 1:
        return
    assert len(sys.argv) <= 2, "more than one argument is provided"
    assert is_intstring(sys.argv[1]), "argument is not an integer"

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
