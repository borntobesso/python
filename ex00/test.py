from recipe import Recipe
from book import Book

cake_recipe = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")
print("Cake recipe:")
print(cake_recipe)
print("Cake recipe using str():\n" + str(cake_recipe))\

# no_name = Recipe("", 3, 60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")
# level_error = Recipe("Cake", 100, 60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")
# time_error = Recipe("Cake", 3, -60, ["eggs", "flour", "sugar"], "dessert", "A delicious cake")
# no_ingredients = Recipe("Cake", 3, 60, [], "dessert", "A delicious cake")
# error_description = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], "dessert", 42)
# empty_description = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], "dessert")
# error_type = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], 42, "A delicious cake")

sandwich_recipe = Recipe("Sandwich", 1, 5, ["ham", "bread", "cheese", "tomatoes"], "lunch", "A fresh sandwich")
salad_recipe = Recipe("Salad", 2, 15, ["avocado", "arugula", "tomatoes", "spinach"], "starter", "")
pizza_recipe = Recipe("Pizza", 4, 30, ["tomatoes", "cheese", "ham", "mushrooms"], "lunch")

book = Book("My recipe book")
print("Book name : " + book.name)
print("Book last update : ", end="")
print(book.last_update)
print("Book creation date : ", end="")
print(book.creation_date)

print()
print("Adding recipes to book")
book.add_recipe(cake_recipe)
book.add_recipe(sandwich_recipe)
book.add_recipe(salad_recipe)
book.add_recipe(pizza_recipe)

# print()
# print("Adding recipe with wrong type")
# book.add_recipe("wrong type")

print("Book last update : ", end="")
print(book.last_update)
print("Book recipes : ")
for key in book.recipes_list:
    print(f"{key} : ", end="")
    for recipe in book.recipes_list[key]:
        print(recipe.name, end="")
        if recipe != book.recipes_list[key][-1]:
            print(", ", end="")
    print()
print()

print("Getting recipe by name")
book.get_recipe_by_name("Cake")
book.get_recipe_by_name("Salad")
print("Gettitng recipe by wrong name")
# book.get_recipe_by_name("")
book.get_recipe_by_name("wrong name")
print()

print("Getting recipes by type")
starters = book.get_recipes_by_types("starter")
for recipe in starters:
    print(recipe.name)
    if recipe is not starters[-1]:
        print(", ", end="")
    print()
lunches = book.get_recipes_by_types("lunch")
for recipe in lunches:
    print(recipe.name)
    if recipe is not lunches[-1]:
        print(", ", end="")
print("Getting recipes by wrong type")
book.get_recipes_by_types("")
book.get_recipes_by_types("wrong type")
book.get_recipes_by_types(42)
print()
