import string
import sys

def text_analyzer(text = None):
    """Count and print the numbers of characters:
    
    upper-case characters, lower-case characters, punctuation and spaces
    in a given text.
    if no text is given, the user is prompted to enter a text.
    """
    if not text:
        print("What is the text to analyse?")
        text = input(">> ")
    if type(text) is not str:
        print("AssertionError: argument is not a string")
        return
    upper = 0
    lower = 0
    punct = 0
    space = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        elif c in string.punctuation:
            punct += 1
    print("The text contains", len(text), "character(s):")
    print("-", upper, "upper letter(s)")
    print("-", lower, "lower letter(s)")
    print("-", punct, "punctuation mark(s)")
    print("-", space, "space(s)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Too many arguments.")
    elif len(sys.argv) == 1:
        text_analyzer()
    else:
        text_analyzer(sys.argv[1])