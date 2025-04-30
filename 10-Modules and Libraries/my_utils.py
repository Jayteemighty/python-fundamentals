"""
MODULES AND LIBRARIES

Definitions:
1. MODULE: A single Python file (.py) containing reusable code (functions, classes, variables)
   - Example: 'math.py' is a built-in module for mathematical operations

2. LIBRARY: A collection of modules/packages that provide specific functionality
   - Example: 'requests' library for HTTP operations (made of multiple .py files)

3. PACKAGE: A directory containing multiple modules and an __init__.py file
   - Example: 'urllib' package (contains request.py, response.py, etc.)

4. PYPI: Python Package Index - repository of third-party libraries (pip installs from here)
"""

# ==============================================================================
# my_utils.py CONTENT (custom module example)
# ==============================================================================
"""
\"\"\"
MY_UTILS.PY - Custom utility module
Contains frequently used functions
\"\"\"
import math

def greet(name):
    \"\"\"Return a personalized greeting\"\"\"
    return f"Hello, {name}!"

def calculate_circle_area(radius):
    \"\"\"Calculate area of circle given radius\"\"\"
    return math.pi * radius ** 2

def is_prime(n):
    \"\"\"Check if number is prime\"\"\"
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(limit):
    \"\"\"Generate Fibonacci sequence up to limit\"\"\"
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
"""

# ==============================================================================
# 1. USING OUR CUSTOM MODULE
# ==============================================================================
import my_utils

print(my_utils.greet("Developer"))  # Hello, Developer!
print(f"Area: {my_utils.calculate_circle_area(5):.2f}")  # Area: 78.54

# Prime check
print(f"Is 17 prime? {my_utils.is_prime(17)}")  # True

# Fibonacci sequence
print("Fibonacci:", list(my_utils.fibonacci(50)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ==============================================================================
# [Previous sections 2-10 remain unchanged...]
# ==============================================================================