from generator import generator

text = "Le Lorem Ipsum est simplement du faux texte."

for word in generator(text, sep=" "):
    print(word)

print("\n")

for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("\n")

for word in generator(text, sep=" ", option="ordered"):
    print(word)

print("\n")

text = "Lorem Ipsum Lorem Ipsum"

for word in generator(text, sep=" ", option="unique"):
    print(word)

print("\n")

# Error tests

for word in generator(text, sep=" ", option="unknown"):
    print(word)

print("\n")

for word in generator(text, sep=" ", option=1):
    print(word) 

print("\n")

for word in generator(text, sep=1):
    print(word)

print("\n")

text = 1.0
for word in generator(text, sep="."):
    print(word)

print("\n")