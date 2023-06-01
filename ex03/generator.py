def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    '''
    if not isinstance(text, str):
        return "ERROR"
    if option is not None and option not in ["suffle", "unique", "ordered"]:
        return "ERROR"
    
    