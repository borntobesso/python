def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
		Args:
			function_to_apply: a function taking an iterable.
		    iterable: an iterable object (list, tuple, iterator).
		Return:
			An iterable.
		    None if the iterable can not be used by the function.
	"""
	if not callable(function_to_apply):
	    raise TypeError("First argument must be a callable function.")
	elif not hasattr(iterable, '__iter__'):
	    raise TypeError("Second argument must be an iterable.")
	else:
		for item in iterable:
			if isinstance(function_to_apply(item), bool):
			    if function_to_apply(item):
				    yield item
			else:
			    raise TypeError("Filter function must return a boolean value.")
                
x = [1, 2, 3, 4, 5]

print(ft_filter(lambda dum: not (dum % 2), x))