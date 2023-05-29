from recipe import Recipe

recipe = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")

print(recipe)
print(str(recipe))

# no_name = Recipe("", 3, 60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")
# level_error = Recipe("Cake", 100, 60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")
# time_error = Recipe("Cake", 3, -60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")
# no_ingredients = Recipe("Cake", 3, 60, [], "dessert", "A delicious cake")
# error_description = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], "dessert", 42)
# empty_description = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], "dessert")
# error_type = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], 42, "A delicious cake")