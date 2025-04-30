"""
LIST COMPREHENSIONS
A concise way to create lists by iterating over sequences with optional conditions.
"""

# ==============================================================================
# 1. BASIC LIST COMPREHENSION
# ==============================================================================
# Syntax: [expression for item in iterable]
# ----------------------------------------
squares = [x**2 for x in range(5)]  # Squares of 0-4
print(squares)  # Output: [0, 1, 4, 9, 16]

# Equivalent loop:
# squares = []
# for x in range(5):
#     squares.append(x**2)


# ==============================================================================
# 2. LIST COMPREHENSION WITH CONDITIONS
# ==============================================================================
# Syntax: [expression for item in iterable if condition]
# ------------------------------------------------------
evens = [x for x in range(10) if x % 2 == 0]  # Even numbers 0-8
print(evens)  # Output: [0, 2, 4, 6, 8]

# Filtering strings:
fruits = ["apple", "banana", "cherry", "date"]
a_fruits = [fruit for fruit in fruits if fruit.startswith("a")]
print(a_fruits)  # Output: ["apple"]


# ==============================================================================
# 3. IF-ELSE IN LIST COMPREHENSION
# ==============================================================================
# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]
# -------------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
parity = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(parity)  # Output: ["odd", "even", "odd", "even", "odd"]


# ==============================================================================
# 4. NESTED LOOPS IN LIST COMPREHENSION
# ==============================================================================
# Syntax: [expression for outer_item in outer_iterable for inner_item in inner_iterable]
# -------------------------------------------------------------------------------------
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4]

# Cartesian product:
colors = ["red", "green"]
sizes = ["S", "M"]
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)  # Output: [('red', 'S'), ('red', 'M'), ('green', 'S'), ('green', 'M')]


# ==============================================================================
# 5. ADVANCED EXAMPLES
# ==============================================================================
# Dictionary from list comprehension:
keys = ["name", "age", "job"]
values = ["Alice", 25, "Engineer"]
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'job': 'Engineer'}

# Set comprehension (unique values):
numbers = [1, 2, 2, 3, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # Output: {16, 1, 9, 4}


# ==============================================================================
# 6. WHEN TO AVOID LIST COMPREHENSIONS
# ==============================================================================
# - Avoid overly complex logic (reduce readability)
# - When you need side effects (e.g., printing during iteration)
# - For large data transformations (generators may be better)