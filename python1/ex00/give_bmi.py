def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""Calculate BMI range from height and weight lists."""
	assert len(height) == 2 and len(weight) == 2, "Each list must have two elements."
	assert all(isinstance(i, (int, float)) for i in height + weight), "All elements must be int or float."