cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
		'prep_time': 10
	},
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
		'prep_time': 60
	},
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
		'prep_time': 15
	}
}

def all_recipes():
    print("All recipe names:")
    for key in cookbook.keys():
        print(key)
        
def print_recipe(recipe):
	if recipe in cookbook:
		print("Recipe for " + recipe + ":")
		print("\tIngredients list:", cookbook[recipe]['ingredients'])
		print("\tTo be eaten for " + cookbook[recipe]['meal'] + ".")
		print("\tTakes", cookbook[recipe]['prep_time'], "minutes of cooking.")
	else:
		print("This recipe doesn't exist.")
		
def delete_recipe(recipe):
	if recipe in cookbook:
		del cookbook[recipe]
		print("Recipe for " + recipe + " deleted.")
	else:
		print("This recipe doesn't exist.")
		
def add_recipe(recipe, ingredients, meal, prep_time):
	if recipe in cookbook:
		print("This recipe already exists. Would you like to overwrite it? (y/n)")
		choice = input()
		if (choice == 'n' or choice == 'N'):
			print("Recipe not modified.")
			return
	cookbook[recipe] = {
		'ingredients': ingredients,
		'meal': meal,
		'prep_time': prep_time
	}
	print("Recipe for " + recipe + " added.")
	
def main():
	print(">> Welcome to the Python Cookbook !")
	print(">> List of available options:")
	print("\t1: Add a recipe")
	print("\t2: Delete a recipe")
	print("\t3: Print a recipe")
	print("\t4: Print the cookbook")
	print("\t5: Quit")
	while True:
		print("\n>> Please select an option.")
		choice = input(">> ")
		if (choice == '1'):
			print("\n>> Please enter the recipe's name to add:")
			recipe = input(">> ")
			print("\n>> Please enter the recipe's ingredients line by line:")
			ingredients = []
			while True:
				ingredient = input(">> ")
				if (ingredient == ''):
					break
				ingredients.append(ingredient)
			print("\n>> Please enter the recipe's meal type:")
			meal = input(">> ")
			print("\n>> Please enter the recipe's preparation time in minutes:")
			prep_time = input(">> ")
			add_recipe(recipe, ingredients, meal, prep_time)
		elif (choice == '2'):
			print("\n>> Please enter the recipe's name to delete:")
			recipe = input(">> ")
			delete_recipe(recipe)
		elif (choice == '3'):
			print("\n>> Please enter the recipe's name to get its details:")
			recipe = input(">> ")
			print_recipe(recipe)
		elif (choice == '4'):
			all_recipes()
		elif (choice == '5'):
			print("\nCookbook closed. Goodbye !")
			return
		else:
			print("\nSorry, this option does not exist.")
			print("List of available options:")
			print("\t1: Add a recipe")
			print("\t2: Delete a recipe")
			print("\t3: Print a recipe")
			print("\t4: Print the cookbook")
			print("\t5: Quit")
			continue
		
main()