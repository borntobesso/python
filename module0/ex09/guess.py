import random
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print()
random_number = random.randint(1, 99)
count = 0

while True:
	count += 1
	print("What's your guess between 1 and 99?")
	user_input = input(">> ")
	if user_input == "exit":
		print("Goodbye!")
		exit()
	try:
		guess = int(user_input)
	except ValueError:
		print("That's not a number.")
		continue
	if guess == random_number:
		if random_number == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if count == 1:
			print("Congratulations! You got it on your first try!")
		else:
			print("Congratulations, you've got it!")
			print(f"You won in {count} attempts!")
		break
	elif guess > random_number:
		print("Too high!")
	else:
		print("Too low!")