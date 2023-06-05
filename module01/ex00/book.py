import datetime as dt
from recipe import Recipe

class Book:
	def __init__(self, name):
		if not isinstance(name, str) or len(name) == 0:
			raise ValueError("Name must be a non-empty string")
		self.name = name
		self.last_update = dt.datetime.now()
		self.creation_date = dt.datetime.now()
		self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
		
	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		if not isinstance(name, str) or len(name) == 0:
			raise ValueError("Name must be a non-empty string")
		for recipe_type in self.recipes_list:
			for recipe in self.recipes_list[recipe_type]:
				if recipe.name == name:
					print(recipe)
					return recipe
		print(f"Recipe {name} not found")
		return None
	
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if not isinstance(recipe_type, str) or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
			raise ValueError("Recipe type must be a string and must be 'starter', 'lunch' or 'dessert'")
		return self.recipes_list[recipe_type]
	
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if not isinstance(recipe, Recipe):
			raise ValueError("Recipe must be a Recipe instance")
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = dt.datetime.now()