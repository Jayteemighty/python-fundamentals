# Variables: are used to store data which can be used later
# data types include:
# 1. Strings
# 2. Integers
# 3. Booleans
# 4. Floats
# 5. Lists
# 6. Tuples
# 7. Dictionaries

# 1. Strings
name = "Joshua"
country = "United States"

print(name) # Output: Joshua
print(country) # Output: United States


# 2. Integers
age = 200
no_of_apples = 25

print(age) # Output: 200
print(no_of_apples) # Output: 25


# 3. Booleans
is_adult = True
is_boy = False
print(is_adult) # Output: True
print(is_boy) # Output: False


# 4. Floats
age = 24.1
no_of_apples = 25.99
print(age) # Output: 24.1
print(no_of_apples) # Output: 25.99

# 5. Lists are ordered collections that can store multiple items,they are mutable.
list_example = ['joshua', 39, 48.2, True]
fruits = ["banana", "apple", "cashew"]
print(list_example) # Output: ['joshua', 39, 48.2, True]
print(fruits) # Output: ['banana', 'apple', 'cashew']

# 6. Tuples are similar to lists, but they are immutable (cannot be changed after creation).
list_example = ('joshua', 39, 48.2, True)
fruits = ("banana", "apple", "cashew")
print(list_example) # Output: ['joshua', 39, 48.2, True]
print(fruits) # Output: ['banana', 'apple', 'cashew']

# 7. Dictionaries are unordered collections of key-value pairs.
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(person["name"])  # Output: John


# 8. Type Casting: You can also convert between different data types using casting.
x = 5       # int
y = 2.5     # float

# Casting to float and int
x_to_float = float(x)  # Convert int to float
y_to_int = int(y)     # Convert float to int

print(x_to_float)  # Output: 5.0
print(y_to_int)    # Output: 2
