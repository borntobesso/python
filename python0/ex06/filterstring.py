import sys
from ft_filter import ft_filter


def main():
    """
    Output a list of words from S that have a length greater than N
    """
    if len(sys.argv) != 3:
        raise AssertionError("Exactly two arguments are required.")
    try:
        text = sys.argv[1]
        assert isinstance(text, str), "The first argument must be a string."
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("The second argument must be an integer.")

    result = list(ft_filter(lambda x: len(x) > n, text.split()))

    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
