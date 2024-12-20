ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Modify list value
ft_list[1] = "World!"

# Create new tuple
ft_tuple = ("Hello", "France!")

# Modify set value
ft_set.remove("tutu!")
ft_set.add("Paris!")

# Modify dict value
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)