def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    	function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
    	A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("First argument must be a function")
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Second argument must be an iterable")
    iterator = iter(iterable)
    try:
        initializer = next(iterator)
        result = initializer
    except StopIteration:
        raise TypeError("Reduce of empty sequence with no initial value")
    for item in iterator:
        result = function_to_apply(result, item)
    return result
    
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
