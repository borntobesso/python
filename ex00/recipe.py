class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
		if len(name) == 0 or not isinstance(name, str):
			raise ValueError("Name must be a non-empty string")
		self.name = name
		if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
			raise ValueError("Cooking level must be an integer between 1 and 5")
		self.cooking_lvl = cooking_lvl
		if not isinstance(cooking_time, int) or cooking_time < 0:
			raise ValueError("Cooking time must be a positive integer")
		self.cooking_time = cooking_time
		if not isinstance(ingredients, list) or len(ingredients) == 0:
			raise ValueError("Ingredients must be a non-empty list")
		self.ingredients = ingredients
		if not isinstance(recipe_type, str) or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
			raise ValueError("Recipe type must be a string and must be 'starter', 'lunch' or 'dessert'")
		self.recipe_type = recipe_type
		if description is None:
			description = ""
		elif not isinstance(description, str):
			raise ValueError("Description must be a string")
		self.description = description

    
	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = ""
		txt += f"Recipe name: {self.name}\n"
		txt += f"Cooking level: {self.cooking_lvl}\n"
		txt += f"Cooking time: {self.cooking_time}\n"
		txt += "Ingredients: "
		txt += self.ingredients[0]
		for i in range(1, len(self.ingredients)):
			txt += f", {self.ingredients[i]}"
		txt += "\n"
		txt += f"Description: {self.description}\n"
		txt += f"Recipe type: {self.recipe_type}\n"
		return txt