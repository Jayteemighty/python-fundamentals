"""
LAMBDA FUNCTIONS (Anonymous Functions)
Single-expression functions defined without a name, using the 'lambda' keyword.

Key Features:
- Concise syntax for simple operations
- No return statement needed (expression is auto-returned)
- Can be used wherever function objects are required
- Limited to single expression (no multiline logic)
"""

# ==============================================================================
# 1. BASIC SYNTAX
# ==============================================================================
# Syntax: lambda arguments: expression

# Equivalent to:
# def add(a, b):
#     return a + b
add = lambda a, b: a + b
print(f"5 + 3 = {add(5, 3)}")  # Output: 5 + 3 = 8

# Immediately invoked
print((lambda x: x**2)(4))  # Output: 16

# ==============================================================================
# 2. COMMON USE CASES
# ==============================================================================
# A. Sorting with key functions
names = ["Alice", "Bob", "Charlie", "David"]
print("\nSorted by length:", sorted(names, key=lambda x: len(x)))

# B. Filtering lists
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# C. Mapping transformations
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# ==============================================================================
# 3. REAL-WORLD EXAMPLES
# ==============================================================================
# A. Data processing
data = [{"name": "John", "age": 45}, {"name": "Diana", "age": 34}]
print("\nSorted by age:", sorted(data, key=lambda x: x["age"]))

# B. Math operations
from math import pi
circle_area = lambda r: pi * r**2
print(f"Area of radius 5: {circle_area(5):.2f}")

# C. Conditional logic
grade = lambda score: "Pass" if score >= 50 else "Fail"
print("Score 65:", grade(65))

# ==============================================================================
# 4. LAMBDA VS REGULAR FUNCTIONS
# ==============================================================================
"""
Lambda Pros:
- Quick one-time use
- Cleaner for simple operations
- No namespace pollution

Regular Function Pros:
- Reusable
- Can have docstrings
- Support complex logic
- Better debugging (have names)
"""

# ==============================================================================
# 5. WHEN TO AVOID LAMBDAS
# ==============================================================================
"""
1. Complex logic (use def instead)
2. Need docstrings or annotations
3. Multi-step operations
4. When it reduces readability
"""

# ==============================================================================
# 6. ADVANCED USAGE
# ==============================================================================
# A. Multiple arguments
equation = lambda x, y, z: x**2 + y**2 + z**2
print("\nEquation result:", equation(1, 2, 3))

# B. With higher-order functions
def power_func(n):
    return lambda x: x**n

square = power_func(2)
cube = power_func(3)
print(f"Square of 4: {square(4)}")
print(f"Cube of 3: {cube(3)}")

# ==============================================================================
# 7. BEST PRACTICES
# ==============================================================================
"""
1. Keep lambda expressions short
2. Use descriptive variable names for arguments
3. Avoid nesting multiple lambdas
4. Consider readability over conciseness
"""

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Convert these to lambdas:
#    a) A function that checks if string starts with 'A'
#    b) A function that returns average of three numbers

# 2. Create a sorter that sorts strings by last character

# 3. Make a multiplier factory (like power_func but for multiplication)