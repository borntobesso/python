def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the given iterable.
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
	for item in iterable:
		yield function_to_apply(item)

x = [1, 2, 3, 4, 5]
ft_map(lambda dum: dum + 1, x)