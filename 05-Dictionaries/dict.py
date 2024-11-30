#A dictionary is an unordered, mutable collection of key-value pairs. It allows you to store and access data using unique keys instead of numerical indices.

# 1. Creating a Dictionary
dict_name = {"key1": "value1", "key2": "value2", "key3": "value3"}

empty_dict = {} # Empty Dictionary

students = {"Kareema": 13, "Abiola": 15, "Idowu": 10}   # Dictionary with data

mixed_dict = {"name": "Omowereyy", "scores": [90, 100, 99, 78], "age": 24, "graduated": True} # Dict with mixed data

# 2. Accessing Dictionary Elements
student = {"name": "Joshua", "age": 24, "wealthy": True, "Happy": True}
print(student["name"]) # Output: Joshua
print(student["wealthy"]) # Output: True

# we could use .get() it help avoid errors incase the key does not exist
print(student.get("Happy"))
print(student.get("age"))

# 3. Adding, Updating and Deleting Items
student = {"name": "Joshua", "age": 23, "wealthy": True, "deleted": "Yep", "popped": "Yeppy"}

student["Happy"] = True  # Adding a new key-value pair

student["age"] = 24  # Updating an existing key-value pair

del student["deleted"]  # Delete a key-value pair

popped = student.pop("popped")  # Removes and returns the value of a key

student.clear() # Removes all items from the dictionary

print(student)

# 4. Dictionary Methods
student = {"name": "Alice", "age": 20, "grade": "A"}

#dict.keys()    # Returns a view of all keys in the dictionary
print(student.keys())

#dict.values()  # Returns a view of all values in the dictionary
print(student.values())

#dict.items()   # Returns a view of all key-value pairs as tuples
print(student.items())

#dict.update()  # Updates the dictionary with key-value pairs from another dictionary
student.update({"graduated": True, "grade": "A+"})
print(student)

#dict.copy()    # Creates a shallow copy of the dictionary
student_copy = student.copy()
print(student_copy)


# 5. Iterating over a Dictionary
student = {"name": "Alicia Keys", "age": 20, "grade": "A"}

for key in student:
    print(key)         # Iterating over keys

for value in student.values():
    print(value)       # Iterating over keys

for key, value in student.items():
    print(f"{key}: {value}")  # Iterating over key-value pairs


# 6. Dictionary Comprehensions
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(even_squares) # Output: {2: 4, 4: 16}


# 7. Nesting Dictionaries
student = {
    "Joshua": {"age": 24, "school": "UI"},
    "Akala": {"age": 33, "school": "OAU PG"}
}

print(student["Joshua"]["school"])