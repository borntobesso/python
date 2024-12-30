import sys


def main():
    """Takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characthers,
    digits and spaces."""
    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        assert False, "only one argument is required"

    upper = 0
    lower = 0
    punct = 0
    digit = 0
    space = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        else:
            punct += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, KeyboardInterrupt, EOFError) as e:
        match e.__class__.__name__:
            case "KeyboardInterrupt":
                print("\nKeyboardInterrupt")
            case "EOFError":
                print("\nEOFError")
            case _:
                print(f"AssertionError: {e}")
