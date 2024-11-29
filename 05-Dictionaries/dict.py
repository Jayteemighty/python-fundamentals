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

popped = student.pop["popped"]  # Removes and returns the value of a key

student.clear() # Removes all items from the dictionary

print(student)