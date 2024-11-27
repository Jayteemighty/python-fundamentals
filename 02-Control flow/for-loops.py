# For loops is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each item in the sequence.
# this is how a for-loop is:
# for item in sequence:
#   code to be executed for each iteraiton of items

# 1. Looping through a list
fruits = ["apples", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# output: apples, banana, cherry

# 2. Using range:
for i in range(1,6):
    print(i)

for j in range(6):
    print(j)

for k in range(1,11,2):
    print(k)


# 3. Looping through a string
for char in "Fuck you bitch ass nigga":
    print(char)

# 4. Nested For loops
colors = ["red", "green", "blue"]
shapes = ["circle", "square", "triangle"]
for color in colors:
    for shape in shapes:
        print(color, shape)

for i in range(3):
    for j in range(2):
        print(f"x = {i}, y = {j}")