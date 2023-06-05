import random

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    '''
    if not isinstance(text, str) or not isinstance(sep, str):
        yield "ERROR"
        return
    elif option is not None and option not in ["shuffle", "unique", "ordered"]:
        yield "ERROR"
        return
    else:
        words = text.split(sep)
        if option == "shuffle":
            num_words = len(words)
            for i in range(0, num_words):
                # Pick a random index from 0 to i (inclusive)
                j = random.randrange(i + 1)
                # Swap words i and j
                words[i], words[j] = words[j], words[i]    
        elif option == "unique":
            words = list(set(words))
        elif option == "ordered":
            words.sort()
        for word in words:
            yield word